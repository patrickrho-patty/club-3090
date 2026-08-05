#!/usr/bin/env python3
"""Quantize the SFT merged Qwen3.6-35B-A3B model to W4A16 AutoRound on 3x3090.

Run on patricks-mint:
    cd /data/projects/club-3090
    source .venv-quant/bin/activate
    python3 scripts/quantize_sft_llmcompressor_gpu.py
"""

import argparse
import os

import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer

from llmcompressor import oneshot
from llmcompressor.modifiers.autoround import AutoRoundModifier, fix_batch_if_needed
from llmcompressor.utils.dev import load_context


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model_id",
        default="patrick-patty/qwen36-35b-a3b-sft-curated-v2-52k-merged",
    )
    parser.add_argument(
        "--dataset_repo",
        default="patrick-patty/rho-sft-curated-v2-v1",
    )
    parser.add_argument(
        "--dataset_file",
        default="runs/sft-curated-v2-52k/axolotl_train/sft_dataset.jsonl",
    )
    parser.add_argument(
        "--output_dir",
        default="/data/projects/club-3090/models-cache/qwen36-35b-a3b-sft-w4a16-autoround",
    )
    parser.add_argument("--num_calibration_samples", type=int, default=128)
    parser.add_argument("--max_seq_length", type=int, default=2048)
    parser.add_argument("--iters", type=int, default=200)
    parser.add_argument("--upload_repo", default=None)
    return parser.parse_args()


def main():
    args = parse_args()

    print(f"CUDA available: {torch.cuda.is_available()}")
    print(f"GPU count: {torch.cuda.device_count()}")
    for i in range(torch.cuda.device_count()):
        print(f"  GPU {i}: {torch.cuda.get_device_name(i)}")

    # Use all 3x3090s with llmcompressor's load_context for MoE linearization + offloading.
    max_memory = {0: "22GiB", 1: "22GiB", 2: "22GiB", "cpu": "200GiB"}
    print(f"Loading model {args.model_id} with load_context and max_memory={max_memory}...")
    with load_context(AutoModelForCausalLM):
        model = AutoModelForCausalLM.from_pretrained(
            args.model_id,
            torch_dtype=torch.bfloat16,
            trust_remote_code=True,
            device_map="auto",
            max_memory=max_memory,
        )
    tokenizer = AutoTokenizer.from_pretrained(
        args.model_id,
        trust_remote_code=True,
    )

    print(f"Loading calibration dataset {args.dataset_repo}/{args.dataset_file}...")
    dataset = load_dataset(args.dataset_repo, data_files=args.dataset_file, split="train")
    dataset = dataset.shuffle(seed=42).select(range(args.num_calibration_samples))

    def preprocess(example):
        messages = example.get("messages", [])
        return {
            "text": tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=False,
            )
        }

    def tokenize(sample):
        return tokenizer(
            sample["text"],
            padding="max_length",
            max_length=args.max_seq_length,
            truncation=True,
            add_special_tokens=False,
            return_attention_mask=True,
        )

    dataset = dataset.map(preprocess)
    dataset = dataset.map(tokenize, remove_columns=dataset.column_names)
    dataset = dataset.map(fix_batch_if_needed)

    recipe = AutoRoundModifier(
        targets="Linear",
        scheme="W4A16",
        ignore=["lm_head"],
        iters=args.iters,
    )

    print("Starting AutoRound W4A16 quantization on GPU...")
    oneshot(
        model=model,
        dataset=dataset,
        recipe=recipe,
        max_seq_length=args.max_seq_length,
        num_calibration_samples=args.num_calibration_samples,
    )

    print(f"Saving quantized model to {args.output_dir}")
    os.makedirs(args.output_dir, exist_ok=True)
    model.save_pretrained(args.output_dir, save_compressed=True)
    tokenizer.save_pretrained(args.output_dir)

    if args.upload_repo:
        from huggingface_hub import HfApi
        api = HfApi()
        api.create_repo(args.upload_repo, private=True, exist_ok=True)
        api.upload_folder(
            folder_path=args.output_dir,
            repo_id=args.upload_repo,
            repo_type="model",
        )
        print(f"Uploaded to {args.upload_repo}")

    print("Done.")


if __name__ == "__main__":
    main()

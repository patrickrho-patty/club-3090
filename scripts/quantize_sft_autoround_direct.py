#!/usr/bin/env python3
"""Quantize the SFT merged Qwen3.6-35B-A3B model to W4A16 using AutoRound directly.

Bypasses llm-compressor entirely. AutoRound handles multi-GPU natively via
its `device_map` and `low_gpu_mem_usage` parameters.

Run on patricks-mint:
    cd /data/projects/club-3090
    source .venv-quant/bin/activate
    python3 scripts/quantize_sft_autoround_direct.py
"""

import argparse
import os

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from auto_round import AutoRound


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model_id",
        default="patrick-patty/qwen36-35b-a3b-sft-curated-v2-52k-merged",
    )
    parser.add_argument(
        "--output_dir",
        default="/data/projects/club-3090/models-cache/qwen36-35b-a3b-sft-w4a16-autoround",
    )
    parser.add_argument("--iters", type=int, default=200)
    parser.add_argument("--nsamples", type=int, default=128)
    parser.add_argument("--seqlen", type=int, default=2048)
    parser.add_argument("--batch_size", type=int, default=4)
    parser.add_argument("--upload_repo", default=None)
    return parser.parse_args()


def main():
    args = parse_args()

    print(f"CUDA available: {torch.cuda.is_available()}")
    print(f"GPU count: {torch.cuda.device_count()}")
    for i in range(torch.cuda.device_count()):
        print(f"  GPU {i}: {torch.cuda.get_device_name(i)}")

    # AutoRound handles multi-GPU and block-by-block loading natively.
    # No device_map or low_gpu_mem_usage needed — those cause slowdowns.
    print(f"Creating AutoRound for {args.model_id}...")

    tokenizer = AutoTokenizer.from_pretrained(args.model_id, trust_remote_code=True)

    ar = AutoRound(
        model=args.model_id,
        tokenizer=tokenizer,
        platform="hf",
        scheme="W4A16",
        iters=args.iters,
        nsamples=args.nsamples,
        seqlen=args.seqlen,
        batch_size=args.batch_size,
        seed=42,
        model_dtype="bfloat16",
        trust_remote_code=True,
        # torch_compile is enabled by default in recent auto-round
        enable_torch_compile=True,
    )

    # Run quantization
    print("Starting AutoRound W4A16 quantization...")
    ar.quantize()

    # Save
    print(f"Saving quantized model to {args.output_dir}")
    os.makedirs(args.output_dir, exist_ok=True)
    ar.save_quantized(
        output_dir=args.output_dir,
        inplace=True,
        pack_qkv=True,
    )
    tokenizer.save_pretrained(args.output_dir)

    # Upload to HF
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

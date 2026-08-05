#!/usr/bin/env python3
"""Test how transformers distributes the Qwen3.6 MoE model across GPUs."""

import torch
from transformers import AutoModelForCausalLM

MODEL_ID = "patrick-patty/qwen36-35b-a3b-sft-curated-v2-52k-merged"


def print_mem(label):
    print(f"\n{label}")
    for i in range(torch.cuda.device_count()):
        alloc = torch.cuda.memory_allocated(i) / 1e9
        reserved = torch.cuda.memory_reserved(i) / 1e9
        print(f"  GPU {i}: allocated={alloc:.2f} GB, reserved={reserved:.2f} GB")


def main():
    max_memory = {0: "22GiB", 1: "22GiB", 2: "22GiB", "cpu": "200GiB"}
    print(f"Loading with max_memory={max_memory}")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        device_map="auto",
        max_memory=max_memory,
    )
    print_mem("After load")
    print(f"\nDevices in model:")
    for name, param in model.named_parameters():
        if param.device.type == "meta":
            print(f"  META: {name}")
        break
    print(f"  ... (first param on {next(model.parameters()).device})")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Quick smoke test: can the merged SFT Qwen3.6-35B-A3B model load across the 3x3090s?"""

import os
import sys

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_ID = "patrick-patty/qwen36-35b-a3b-sft-curated-v2-52k-merged"


def main():
    print(f"torch: {torch.__version__}")
    print(f"cuda available: {torch.cuda.is_available()}")
    print(f"gpu count: {torch.cuda.device_count()}")
    for i in range(torch.cuda.device_count()):
        print(f"  GPU {i}: {torch.cuda.get_device_name(i)}")
        print(f"    free: {torch.cuda.mem_get_info(i)[0] / 1e9:.2f} GB")
        print(f"    total: {torch.cuda.mem_get_info(i)[1] / 1e9:.2f} GB")

    if not torch.cuda.is_available():
        print("No CUDA available; abort.")
        sys.exit(1)

    print(f"\nLoading {MODEL_ID} with device_map='auto' ...")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        torch_dtype="auto",
        trust_remote_code=True,
        device_map="auto",
    )
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True)

    print("\nLoaded. Memory per GPU after load:")
    for i in range(torch.cuda.device_count()):
        alloc = torch.cuda.memory_allocated(i) / 1e9
        reserved = torch.cuda.memory_reserved(i) / 1e9
        print(f"  GPU {i}: allocated={alloc:.2f} GB, reserved={reserved:.2f} GB")

    print("\nSmoke forward pass ...")
    inputs = tokenizer("Hello, world!", return_tensors="pt").to(model.device)
    with torch.no_grad():
        out = model(**inputs)
    print(f"logits shape: {out.logits.shape}")
    print("GPU load test PASSED")


if __name__ == "__main__":
    main()

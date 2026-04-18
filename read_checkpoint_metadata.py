"""
Read metadata from YOLO checkpoint (safe mode).

This script loads checkpoint in default (safe) mode
and prints training arguments if available.

Useful when full model loading is restricted.
"""

import torch

ckpt = torch.load("models/best.pt", map_location="cpu")

if isinstance(ckpt, dict):
    print(ckpt.get('train_args', {}))
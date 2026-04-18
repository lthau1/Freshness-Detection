"""
Inspect YOLO checkpoint file.

This script safely loads a YOLO .pt model file and prints:
- Ultralytics version used for training
- Training arguments
- Git metadata (if available)

Useful for debugging version mismatch issues during deployment.
"""

import torch
from ultralytics.nn.tasks import DetectionModel

# Allow custom class from Ultralytics when loading checkpoint
torch.serialization.add_safe_globals([DetectionModel])

ckpt = torch.load(
    "models/best.pt",
    map_location="cpu",
    weights_only=False
)

print("VERSION:", ckpt.get("version"))
print("TRAIN_ARGS:", ckpt.get("train_args"))
print("GIT:", ckpt.get("git"))
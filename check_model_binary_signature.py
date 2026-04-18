"""
Check raw binary content of YOLO model.

This script scans the .pt file to detect specific strings
(e.g., 'TorchVision') that may cause deserialization errors.

Useful for diagnosing pickle-related issues.
"""

with open("models/best.pt", "rb") as f:
    data = f.read()

print(b"TorchVision" in data)
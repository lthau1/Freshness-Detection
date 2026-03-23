import torch

model_path = "models/best.pt"

ckpt = torch.load(model_path, map_location="cpu", weights_only=False)

print(type(ckpt))

if isinstance(ckpt, dict):
    print("\n=== KEYS ===")
    print(ckpt.keys())

    for k, v in ckpt.items():
        print(f"{k}: {type(v)}")
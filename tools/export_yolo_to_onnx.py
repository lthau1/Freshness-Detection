from ultralytics import YOLO

# Load the trained YOLO .pt model
model = YOLO('models/best.pt')

# Export the PyTorch .pt model to ONNX format
# This conversion is used to reduce model size and make inference faster and more efficient
# ONNX models are lighter and more suitable for deployment compared to .pt files
path = model.export(format="onnx", simplify=True)

print(f"ONNX model has been saved at: {path}")
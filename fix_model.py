from ultralytics import YOLO

# Initialize and load the trained YOLO model from the checkpoint file
# "best.pt" is typically the best-performing weights saved during training
model = YOLO("models/best.pt")

# Save the model again as a "clean" version
# This step is often used to re-export or standardize the model file,
# ensuring compatibility or removing unnecessary training artifacts
model.save("models/best_clean.pt")

# Notify user that the process has completed successfully
print("Done! Saved best_clean.pt")
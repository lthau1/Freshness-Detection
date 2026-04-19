# =========================
# SYSTEM CONFIG
# =========================
import os

# Disable YOLO auto-install to avoid unexpected dependency installation
os.environ["YOLO_AUTOINSTALL"] = "False"

# =========================
# CORE LIBRARIES
# =========================
import streamlit as st
import torch
import torch.nn as nn
import numpy as np
import pandas as pd
from PIL import Image
import cv2

# =========================
# DEEP LEARNING
# =========================
from torchvision import models, transforms
from ultralytics import YOLO

# =========================
# HUGGING FACE DOWNLOAD
# =========================
from huggingface_hub import hf_hub_download

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="AI-based Fruit & Vegetable Freshness Detection",
    layout="wide"
)

# =========================
# ENV VARIABLES
# =========================
HF_TOKEN = os.getenv("HF_TOKEN")  # optional (only needed for private repo)

# =========================
# FILE SYSTEM SETUP
# =========================
MODEL_DIR = "models"
os.makedirs(MODEL_DIR, exist_ok=True)

# =========================
# MODEL DOWNLOAD FUNCTION
# =========================
def download_model(repo_id, filename, local_dir=MODEL_DIR):
    file_path = os.path.join(local_dir, filename)

    if not os.path.exists(file_path):
        hf_hub_download(
            repo_id=repo_id,
            filename=filename,
            local_dir=local_dir,
            token=HF_TOKEN if HF_TOKEN else None
        )

    return file_path

# Download models from Hugging Face (public and reliable source)
best_model_path = download_model(
    repo_id="lthau1/Freshness-Detection",
    filename="best.pt"
)

resnet_model_path = download_model(
    repo_id="lthau1/Freshness-Detection",
    filename="resnet_fresh_rotten_best.pth"
)

# --- FUNCTION TO LOAD YOLO MODEL ---
@st.cache_resource
def load_yolo_model():
    return YOLO('models/best.pt')

# --- FUNCTION TO LOAD RESNET50 MODEL ---
@st.cache_resource # Prevents reloading the model on every user interaction
def load_resnet_model(model_path):
    # Initialize ResNet50 model architecture
    model = models.resnet50(weights=None)
    num_ftrs = model.fc.in_features
    # Adjust final output layer to match your classification classes
    model.fc = nn.Linear(num_ftrs, 2) 
    
    # Load weights from .pth file
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    checkpoint = torch.load(model_path, map_location=device)
    
    # Check if checkpoint is a dictionary (common when saving via state_dict)
    if isinstance(checkpoint, dict) and 'state_dict' in checkpoint:
        model.load_state_dict(checkpoint['state_dict'])
    else:
        model.load_state_dict(checkpoint)
        
    model.to(device)
    model.eval()
    return model, device

# --- CLASS LABELS (Ensure order matches your data.yaml) ---
class_names = ['Fresh', 'Rotten']

# Function to load external CSS
def load_css(file_name):
    with open(file_name, encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("assets/style.css")

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("Navigation")
    app_mode = st.radio("", ["1. Introduction", "2. System Demo"])
    

# ---------------------------------------------------------
# SECTION 1: INTRODUCTION
# ---------------------------------------------------------
if app_mode == "1. Introduction":
    st.header("🍎 Scientific Research Introduction")
    
    st.write("""
    ### Research Objectives:
    Build an AI model using Deep Learning techniques to classify and evaluate the freshness of agricultural products, aiming to minimize food waste and improve production efficiency.
    
    ### Research Objects: 
    9 types of fruits and vegetables (Apple, Banana, Bitter Gourd, Bell Pepper, Cucumber, Okra, Orange, Potato, Tomato).
    
    ### Technologies Used:
    * **YOLO v11:** For object detection and localization.
    * **ResNet50:** For detailed classification of fresh/withered status.
    """)
    
# ---------------------------------------------------------
# SECTION 2: SYSTEM DEMO - ROBUST GLOBAL ANALYSIS
# ---------------------------------------------------------
elif "2. System Demo" in app_mode:
    st.header("🔍 Quality Analysis System")
    
    uploaded_file = st.file_uploader("Upload vegetable image...", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        img_pil = Image.open(uploaded_file).convert('RGB')
        col_left, col_right = st.columns([1.2, 1]) 
        
        with col_left:
            st.image(img_pil, caption="🖼️ Original Image")

        with col_right:
            st.write("### **Identification & Evaluation Results**")
            try:
                # Load models
                yolo_model = load_yolo_model() 
                resnet_model, device = load_resnet_model('models/resnet_fresh_rotten_best.pth')
                
                # Run inference
                results = yolo_model(img_pil)
                
                if len(results[0].boxes) > 0:
                    # Select the object with highest confidence as representative
                    best_box = results[0].boxes[0] 
                    ten_loai = yolo_model.names[int(best_box.cls[0])]
                    conf_yolo = float(best_box.conf[0])
                    
                    # Crop the best region for status analysis
                    x1, y1, x2, y2 = map(int, best_box.xyxy[0])
                    crop_img = img_pil.crop((x1, y1, x2, y2))
                    
                    # Image preprocessing pipeline
                    preprocess = transforms.Compose([
                        transforms.Resize((224, 224)),
                        transforms.ToTensor(),
                        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
                    ])
                    input_tensor = preprocess(crop_img).unsqueeze(0).to(device)
                    
                    # ResNet Status Classification
                    with torch.no_grad():
                        outputs = resnet_model(input_tensor)
                        probs = torch.nn.functional.softmax(outputs, dim=1)
                        conf_res, pred_idx = torch.max(probs, 1)
                    
                    trang_thai = class_names[pred_idx.item()]
                    is_fresh = "fresh" in trang_thai.lower() or "tươi" in trang_thai.lower()

                    # --- DISPLAY CONSOLIDATED RESULT ---
                    st.markdown(f"### Product Type: **{ten_loai}**")
                    
                    if is_fresh:
                        st.success(f"🌿 Freshness Status: **{trang_thai}**")
                    else:
                        st.error(f"🍂 Freshness Status: **{trang_thai}**")
                    
                    # Display 4 technical metrics
                    st.write("---")
                    st.write(f"Detection Confidence (YOLO): **{conf_yolo*100:.2f}%**")
                    st.write(f"Classification Confidence (ResNet): **{conf_res.item()*100:.2f}%**")
                    
                    
                else:
                    st.warning("⚠️ System could not identify any objects in the image.")

            except Exception as e:
                st.error(f"❌ Processing Error: {e}")

# ---------------------------------------------------------

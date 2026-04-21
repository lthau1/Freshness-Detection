# =========================
# SYSTEM CONFIG
# =========================
import os
os.environ["YOLO_AUTOINSTALL"] = "False"

# =========================
# CORE LIBRARIES
# =========================
import streamlit as st
import torch
import torch.nn as nn
from PIL import Image

# =========================
# DEEP LEARNING
# =========================
from torchvision import models, transforms
from ultralytics import YOLO

# =========================
# HUGGING FACE
# =========================
from huggingface_hub import hf_hub_download

# =========================
# IMPORT LANGUAGE FILE
# =========================
from lang import TEXT, LABEL_MAP, STATUS_MAP

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Freshness Detection",
    layout="centered"
)

# =========================
# MODEL DIR
# =========================
MODEL_DIR = "models"
os.makedirs(MODEL_DIR, exist_ok=True)

# =========================
# DOWNLOAD MODEL
# =========================
def download_model(repo_id, filename):
    path = os.path.join(MODEL_DIR, filename)
    if not os.path.exists(path):
        hf_hub_download(
            repo_id=repo_id,
            filename=filename,
            local_dir=MODEL_DIR
        )
    return path

YOLO_PATH = download_model("lthau1/Freshness-Detection", "best.pt")
RESNET_PATH = download_model("lthau1/Freshness-Detection", "resnet_fresh_rotten_best.pth")

# =========================
# LOAD MODELS
# =========================
@st.cache_resource
def load_yolo_model(path):
    return YOLO(path)

@st.cache_resource
def load_resnet_model(path):
    model = models.resnet50(weights=None)
    model.fc = nn.Linear(model.fc.in_features, 2)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    checkpoint = torch.load(path, map_location=device)

    if isinstance(checkpoint, dict) and 'state_dict' in checkpoint:
        model.load_state_dict(checkpoint['state_dict'])
    else:
        model.load_state_dict(checkpoint)

    model.to(device)
    model.eval()
    return model, device

class_names = ['Fresh', 'Rotten']

# =========================
# LOAD CSS
# =========================
def load_css(file_name):
    with open(file_name, encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("assets/style.css")


# =========================
# TRANSLATE FUNCTIONS
# =========================
def translate_label(label_en):
    return LABEL_MAP.get(label_en.lower(), {}).get(lang, label_en)

def translate_status(status_en):
    return STATUS_MAP.get(status_en, {}).get(lang, status_en)

# =========================
# UI HEADER
# =========================
# LANGUAGE SELECT (first)
col_title, col_lang = st.columns([4, 1])

with col_lang:
    st.markdown('<div style="padding-top: 10px;"></div>', unsafe_allow_html=True)
    lang_choice = st.selectbox(
        "🌐",
        ["Tiếng Việt", "English"],
        label_visibility="collapsed"
    )

lang = "vi" if lang_choice == "Tiếng Việt" else "en"
t = TEXT[lang]

with col_title:
    st.markdown(f"""
    <div class="app-header">
        <h2 class="app-title">{t['title']}</h2>
        <p class="app-subtitle">{t['subtitle']}</p>
        <p class="app-note">{t['note']}</p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# UPLOAD
# =========================
uploaded_file = st.file_uploader(t["upload"], type=["jpg", "png", "jpeg"])

# =========================
# PROCESS
# =========================
if uploaded_file:
    img_pil = Image.open(uploaded_file).convert('RGB')

    col_left, col_right = st.columns([1.2, 1])

    with col_left:
        st.image(img_pil, caption="🖼️")

    with col_right:
        st.write(f"### **{t['result']}**")

        try:
            # =========================
            # YOLO
            # =========================
            yolo_model = load_yolo_model(YOLO_PATH)

            with st.spinner(t["running"]):
                results = yolo_model(img_pil)

            if len(results[0].boxes) == 0:
                st.warning(t["no_object"])
                st.stop()

            best_box = results[0].boxes[0]

            label_en = results[0].names[int(best_box.cls[0])]
            label = translate_label(label_en)

            conf_yolo = float(best_box.conf[0])

            x1, y1, x2, y2 = map(int, best_box.xyxy[0])
            crop_img = img_pil.crop((x1, y1, x2, y2))

            # =========================
            # RESNET
            # =========================
            resnet_model, device = load_resnet_model(RESNET_PATH)

            preprocess = transforms.Compose([
                transforms.Resize((224, 224)),
                transforms.ToTensor(),
                transforms.Normalize(
                    [0.485, 0.456, 0.406],
                    [0.229, 0.224, 0.225]
                )
            ])

            input_tensor = preprocess(crop_img).unsqueeze(0).to(device)

            with torch.no_grad():
                outputs = resnet_model(input_tensor)
                probs = torch.softmax(outputs, dim=1)
                conf_res, pred_idx = torch.max(probs, 1)

            status_en = class_names[pred_idx.item()]
            status = translate_status(status_en)

            # =========================
            # DISPLAY
            # =========================
            st.markdown(f"### {t['product']}: **{label}**")

            if status_en.lower() == "fresh":
                st.success(status)
            else:
                st.error(status)

            st.write("---")
            st.write(f"{t['yolo_conf']}: {conf_yolo*100:.2f}%")
            st.write(f"{t['resnet_conf']}: {conf_res.item()*100:.2f}%")

        except Exception as e:
            st.error(f"{t['error']}: {e}")
🚀 **Live Demo (Render):** https://freshness-detection-ieyu.onrender.com
⚡ **Alternative Demo (Streamlit):** https://freshness-detection-lthau1.streamlit.app/

---

# 🥦 Freshness Detection System for Agricultural Products

An AI-powered web application that detects fruit/vegetable types and evaluates their freshness status (**Fresh vs. Rotten**) using a hybrid deep learning pipeline.

---

## 🧠 Model Architecture

This system combines two deep learning models:

* **Object Detection:** YOLOv11 (Ultralytics)
* **Classification:** ResNet50 (PyTorch)
* **Frontend:** Streamlit

### 🔄 Pipeline

1. Upload an image
2. YOLO detects the object (fruit/vegetable)
3. The detected region is cropped
4. ResNet50 classifies freshness (Fresh / Rotten)
5. Final result is displayed with confidence scores

---

## 🎯 Objectives

* **Waste Reduction:** Detect spoiled products early to prevent contamination
* **Automation:** Replace manual inspection in supply chains
* **Accuracy:** Combine detection + classification for better performance

---

## 📂 Project Structure

```text
freshness_detection/
├── app.py
├── Dockerfile
├── requirements.txt
├── data.yaml
├── README.md

├── assets/
│   └── style.css

├── models/              # model files (NOT included)
│   └── .gitkeep

├── tools/               # debugging utilities
│   ├── inspect_yolo_checkpoint.py
│   ├── check_model_binary_signature.py
│   ├── read_checkpoint_metadata.py
│   └── fix_model_checkpoint.py

├── .gitignore
├── .dockerignore
```

---

## 📥 Model Weights (Required)

Due to GitHub file size limits, download model weights manually:

* **YOLOv11 weights:**
  https://drive.google.com/drive/folders/1GFRhN_P7ZmQSskmxo9Hy82dkUOUuE40R

* **ResNet50 weights:**
  https://drive.google.com/drive/folders/1JFwuHVZDLHgZ7rziAOyuc5ERii73CU7b

Place them inside:

```text
models/
```

---

## ⚙️ Installation (Local)

### 1. Clone the repository

```bash
git clone https://github.com/lthau1/Freshness-Detection.git
cd Freshness-Detection
```

---

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate:

* Windows:

```bash
venv\Scripts\activate
```

* macOS/Linux:

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Open browser:

```text
http://localhost:8501
```

---

## 🐳 Run with Docker

```bash
docker build -t freshness-app .
docker run -p 8501:8501 freshness-app
```

---

## 🧪 Tools (Debugging Utilities)

Located in the `tools/` folder:

* `inspect_yolo_checkpoint.py`
  → Inspect model metadata (version, training args)

* `check_model_binary_signature.py`
  → Check raw binary for problematic strings (e.g., TorchVision)

* `read_checkpoint_metadata.py`
  → Safely read checkpoint metadata

* `fix_model_checkpoint.py`
  → Re-save YOLO model to fix serialization issues

---

## ⚠️ Notes

* Model files are not included in the repository
* Ensure correct Ultralytics version to avoid loading errors
* First run may take time due to model download
* Docker builds may require additional system libraries for OpenCV

---

## 📸 Demo

*(Add screenshot here for better presentation)*

```text
assets/demo.png
```

---

## 📌 Author

Developed by **lthau1**
GitHub: https://github.com/lthau1

## 📄 License

This project is for academic and research purposes.

🚀 Live Demo: https://freshness-detection-snzgh2u9zrtnujh9xmgby2.streamlit.app/

# Freshness Detection System for Agricultural Products 

This project is an AI-powered web application designed to identify 9 types of fruits/vegetables and evaluate their freshness status (Fresh vs. Rotten) using a Hybrid Deep Learning approach (YOLOv11 + ResNet50).

## 📌 Research Objectives
* **Waste Reduction:** Early detection of spoiled products to prevent cross-contamination in storage.
* **Production Efficiency:** Automating the quality inspection process in the supply chain.
* **Accuracy:** Combining the localization power of YOLO with the high-precision classification of ResNet50.

## 📂 Project Structure
```text
freshness_detection/
├── app.py              # Main Streamlit application
├── requirements.txt    # List of required Python libraries
├── data.yaml           # YOLO configuration (labels info)
├── models/             # Pre-trained models
│   ├── best.pt         # YOLOv11 weights (Detection)
│   └── resnet_fresh_rotten_best.pth   # ResNet50 weights (Classification)
├── assets/             # UI styling
│   └── style.css       # Custom CSS for the web interface
└── README.md           # Project documentation\


## 📥 Model Weights Download (REQUIRED)
Due to GitHub's file size limits, please download BOTH weight files and place them in the `/models` folder:

* **YOLOv11 (best.pt):https://drive.google.com/drive/folders/1GFRhN_P7ZmQSskmxo9Hy82dkUOUuE40R
* **ResNet50 (resnet_...pth):https://drive.google.com/drive/folders/1JFwuHVZDLHgZ7rziAOyuc5ERii73CU7b

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/lthau1/Freshness-Detection.git](https://github.com/lthau1/Freshness-Detection.git)
  


🚀 Setup & Installation
1. Prerequisites
Python 3.11.9 

Download: https://www.python.org/downloads/release/python-3119/

2. Installation Steps
Open your terminal in the project directory and run:

# Create a virtual environment
py -3.11 -m venv venv

# Unlock permission to run scripts
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Activate the virtual environment
.\venv\Scripts\activate

# Update pip
python -m pip install --upgrade pip

# Install required libraries
python -m pip install -r requirements.txt

3. Running the Application
Once the installation is complete, start the web interface:

streamlit run app.py


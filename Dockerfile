FROM python:3.11.9

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install \
    streamlit==1.32.0 \
    torch==2.0.1 \
    torchvision==0.15.2 \
    ultralytics==8.0.20 \
    opencv-python-headless \
    pillow \
    numpy \
    pandas \
    gdown

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
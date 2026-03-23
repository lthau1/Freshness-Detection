FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y libgl1

RUN pip install \
    streamlit==1.32.0 \
    torch==2.0.1 \
    torchvision==0.15.2 \
    ultralytics==8.0.130 \
    opencv-python-headless==4.8.1.78 \
    numpy==1.26.4 \
    pandas \
    pillow \
    gdown

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
FROM python:3.10-slim

# tránh lỗi input khi apt install
ENV DEBIAN_FRONTEND=noninteractive

# cài system libs cho opencv
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# tạo thư mục app
WORKDIR /app

# copy requirements trước (tối ưu build)
COPY requirements.txt .

# cài python libs
RUN pip install --no-cache-dir -r requirements.txt

# copy toàn bộ code
COPY . .

# mở port
EXPOSE 8501

# chạy streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
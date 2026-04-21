# =========================
# LANGUAGE CONFIG
# =========================

TEXT = {
    "vi": {
        "title": "Nhận diện và phân loại độ tươi nông sản",
        "subtitle": "Tải ảnh lên để hệ thống xác định loại nông sản và phân loại tình trạng (Tươi / Hư).",
        "note": "Áp dụng cho 9 loại: Táo, Chuối, Mướp đắng, Ớt chuông, Dưa leo, Đậu bắp, Cam, Khoai tây, Cà chua.",
        "upload": "Tải ảnh lên (jpg, png)",
        "result": "Kết quả nhận diện & đánh giá",
        "product": "Sản phẩm",
        "fresh": "Tươi",
        "rotten": "Hư",
        "no_object": "Không phát hiện đối tượng",
        "running": "Đang xử lý...",
        "yolo_conf": "Độ tin cậy YOLO",
        "resnet_conf": "Độ tin cậy ResNet",
        "error": "Lỗi"
    },
    "en": {
        "title": "Fruit & Vegetable Freshness Detection",
        "subtitle": "Upload an image to identify the product type and classify its freshness (Fresh / Rotten).",
        "note": "Supports 9 types: Apple, Banana, Bitter Gourd, Bell Pepper, Cucumber, Okra, Orange, Potato, Tomato.",
        "upload": "Upload image (jpg, png)",
        "result": "Detection & Evaluation Results",
        "product": "Product",
        "fresh": "Fresh",
        "rotten": "Rotten",
        "no_object": "No object detected",
        "running": "Processing...",
        "yolo_conf": "YOLO Confidence",
        "resnet_conf": "ResNet Confidence",
        "error": "Error"
    }
}

# Label mapping
LABEL_MAP = {
    "apple": {"vi": "Táo", "en": "Apple"},
    "banana": {"vi": "Chuối", "en": "Banana"},
    "bittergourd": {"vi": "Mướp đắng", "en": "Bitter Gourd"},
    "capsicum": {"vi": "Ớt chuông", "en": "Bell Pepper"},
    "cucumber": {"vi": "Dưa leo", "en": "Cucumber"},
    "okra": {"vi": "Đậu bắp", "en": "Okra"},
    "orange": {"vi": "Cam", "en": "Orange"},
    "potato": {"vi": "Khoai tây", "en": "Potato"},
    "tomato": {"vi": "Cà chua", "en": "Tomato"},
}

STATUS_MAP = {
    "Fresh": {"vi": "Tươi", "en": "Fresh"},
    "Rotten": {"vi": "Hư", "en": "Rotten"}
}
---
name: image-computer-vision
description: "Xử lý hình ảnh và nhận diện ký tự (OCR) bằng OpenCV, Pillow và EasyOCR không đòi hỏi quyền Admin."
---

# Image & Computer Vision (Portable & Non-Admin)

Kỹ năng này hướng dẫn trợ lý AI (Anti Gravity) viết mã nguồn xử lý hình ảnh, cắt ghép, lọc nhiễu đồ họa và nhận diện ký tự viết (OCR) trên Windows dạng Portable, chạy ở quyền người dùng thông thường và không cần cài đặt các ứng dụng hệ thống lớn.

## 1. Cài đặt thư viện Python cục bộ (Không cần Admin)

```powershell
.venv\Scripts\pip install opencv-python pillow easyocr
```

*Lưu ý:* Chọn **EasyOCR** thay vì Tesseract OCR bởi vì EasyOCR chạy hoàn toàn trên nền tảng PyTorch của Python, tự động tải các file model trí tuệ nhân tạo (model weights) về thư mục lưu trữ cục bộ, không yêu cầu cài đặt phần mềm Tesseract `.exe` vào ổ C hệ thống (nơi yêu cầu quyền Admin).

## 2. Mã nguồn Xử lý ảnh cơ bản với OpenCV & Pillow (Mẫu)

```python
import cv2
from PIL import Image

def process_image(input_path, output_path):
    # Đọc ảnh bằng OpenCV
    img = cv2.imread(input_path)
    
    # 1. Chuyển sang ảnh xám (Grayscale) để chuẩn bị cho OCR hoặc nhận diện
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 2. Lọc nhiễu (Gaussian Blur)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # 3. Phân ngưỡng ảnh (Binarization) để làm rõ chữ viết
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Lưu ảnh đã xử lý bằng OpenCV
    cv2.imwrite(output_path, thresh)

def crop_and_resize(input_path, output_path, crop_box, size):
    # Sử dụng Pillow để cắt ghép ảnh nhẹ nhàng
    with Image.open(input_path) as im:
        # crop_box dạng (left, upper, right, lower)
        cropped = im.crop(crop_box)
        resized = cropped.resize(size)
        resized.save(output_path)
```

## 3. Nhận diện ký tự (OCR) Portable bằng EasyOCR

EasyOCR sẽ tự động tải mô hình ngôn ngữ ở lần chạy đầu tiên. Ta cấu hình thư mục lưu trữ model ngay trong dự án để đảm bảo tính di động (Portable):

```python
import os
import easyocr

# Thiết lập thư mục lưu trữ model cục bộ của EasyOCR
project_dir = os.path.dirname(os.path.abspath(__file__))
model_storage_dir = os.path.join(project_dir, "bin", "easyocr_models")
os.makedirs(model_storage_dir, exist_ok=True)

def perform_ocr(image_path, lang_list=['vi', 'en']):
    # Khởi tạo Reader với đường dẫn lưu model cục bộ
    reader = easyocr.Reader(lang_list, model_storage_dir=model_storage_dir, gpu=False)
    
    # Đọc chữ từ ảnh
    result = reader.readtext(image_path)
    
    # Trả về chuỗi văn bản nhận diện được
    text_results = [detection[1] for detection in result]
    return " ".join(text_results)
```

## 4. Nguyên tắc Đóng gói
Khi đóng gói ứng dụng bằng PyInstaller, hãy đảm bảo bao gồm thư mục lưu trữ model `bin/easyocr_models` để người dùng máy khác chạy được ngay ngoại tuyến (offline) mà không cần tải lại model qua internet:
```powershell
.venv\Scripts\pyinstaller --onefile --add-data "bin/easyocr_models;bin/easyocr_models" main.py
```

---
name: pdf-data-extractor
description: "Trích xuất dữ liệu bảng biểu từ tệp PDF dạng văn bản hoặc dạng scan ảnh."
---

# PDF Data Extractor (Portable & Non-Admin)

Kỹ năng này hướng dẫn trợ lý AI (Anti Gravity) viết mã nguồn đọc tài liệu PDF, tự động nhận dạng cấu trúc bảng biểu, và chuyển đổi chúng sang định dạng Excel/CSV.

## 1. Điều kiện tiên quyết và Thư viện Portable

Chúng ta sử dụng **`pdfplumber`** để trích xuất cấu trúc bảng từ các tệp PDF dạng văn bản (text-based PDF). Đối với PDF dạng hình ảnh quét (scanned PDF), chúng ta sẽ kết hợp với **`EasyOCR`** (từ skill `image-computer-vision`).

### Cài đặt thư viện:
```powershell
.venv\Scripts\pip install pdfplumber
```

## 2. Trích xuất bảng từ PDF dạng Văn bản (Text-based PDF)

`pdfplumber` cung cấp các thuật toán trích xuất bảng (table extraction) thông minh bằng cách phát hiện các nét vẽ đường viền (lines) hoặc phân khoảng cách văn bản.

### Mã nguồn Python mẫu:
```python
import pdfplumber
import pandas as pd

def extract_tables_from_pdf(pdf_path, output_excel_path):
    all_dfs = []
    
    with pdfplumber.open(pdf_path) as pdf:
        # Lặp qua từng trang của tệp PDF
        for page_idx, page in enumerate(pdf.pages):
            tables = page.extract_tables()
            
            for table_idx, table in enumerate(tables):
                # Chuyển bảng dạng danh sách (list of lists) thành DataFrame
                if len(table) > 1:
                    headers = table[0]
                    # Thay thế tiêu đề trống bằng tên mặc định
                    headers = [f"Col_{i}" if not h else h for i, h in enumerate(headers)]
                    
                    df = pd.DataFrame(table[1:], columns=headers)
                    df['pdf_page'] = page_idx + 1
                    all_dfs.append(df)
                    
    # Lưu toàn bộ các bảng tìm thấy vào các sheet Excel tương ứng
    if all_dfs:
        with pd.ExcelWriter(output_excel_path) as writer:
            for idx, df in enumerate(all_dfs):
                df.to_excel(writer, sheet_name=f"Table_Page_{df['pdf_page'].iloc[0]}_{idx}", index=False)
        print(f"Trích xuất thành công {len(all_dfs)} bảng sang Excel.")
    else:
        print("Không tìm thấy bảng biểu có cấu trúc trong tệp PDF.")
```

## 3. Trích xuất dữ liệu từ PDF dạng Ảnh quét (Scanned PDF)

Đối với tài liệu scan không thể bôi đen văn bản, chúng ta phải chuyển đổi các trang PDF thành ảnh rồi gọi bộ nhận diện ký tự quang học (OCR).

### Cài đặt thư viện chuyển đổi PDF sang ảnh (Không cần Admin):
Thư viện `pdf2image` yêu cầu phần mềm Poppler. Để đảm bảo Portable và không cần cài đặt phần mềm ngoài, chúng ta sử dụng thư viện **`fitz` (PyMuPDF)** - một thư viện Python độc lập tự chứa mọi tài nguyên:
```powershell
.venv\Scripts\pip install PyMuPDF easyocr
```

### Mã nguồn Python mẫu:
```python
import fitz  # PyMuPDF
import os
import easyocr
import pandas as pd

def extract_scanned_pdf_ocr(pdf_path, output_txt_path):
    # Khởi tạo EasyOCR Reader (sử dụng cấu hình model cục bộ)
    project_dir = os.path.dirname(os.path.abspath(__file__))
    model_storage_dir = os.path.join(project_dir, "bin", "easyocr_models")
    reader = easyocr.Reader(['vi', 'en'], model_storage_dir=model_storage_dir, gpu=False)
    
    # Mở tài liệu PDF bằng PyMuPDF
    doc = fitz.open(pdf_path)
    full_text = []
    
    for page_idx in range(len(doc)):
        page = doc.load_page(page_idx)
        # Chuyển trang PDF thành đối tượng Pixmap (hình ảnh)
        pix = page.get_pixmap(dpi=150)
        
        # Chuyển đổi Pixmap sang định dạng byte PNG để EasyOCR xử lý trực tiếp trong RAM
        img_bytes = pix.tobytes("png")
        
        # Nhận diện chữ
        result = reader.readtext(img_bytes)
        page_text = " ".join([detection[1] for detection in result])
        
        full_text.append(f"--- TRANG {page_idx + 1} ---\n{page_text}\n")
        
    # Lưu nội dung văn bản trích xuất được
    with open(output_txt_path, "w", encoding="utf-8") as f:
        f.write("\n".join(full_text))
```

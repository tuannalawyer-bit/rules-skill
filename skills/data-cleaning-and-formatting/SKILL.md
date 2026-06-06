---
name: data-cleaning-and-formatting
description: "Chuẩn hóa định dạng, làm sạch dữ liệu thô và xử lý giá trị trống (Null/NaN) sử dụng pandas."
---

# Data Cleaning & Formatting (Portable & Non-Admin)

Kỹ năng này hướng dẫn trợ lý AI (Anti Gravity) viết mã nguồn chuẩn hóa dữ liệu thô, loại bỏ các lỗi nhập liệu, làm sạch các giá trị trống và định dạng đúng các kiểu dữ liệu trước khi thực hiện phân tích hoặc chạy mô hình.

## 1. Loại bỏ dữ liệu trùng lặp và khoảng trắng thừa

Dữ liệu thu thập từ Web hoặc kết xuất từ SAP thường bị thừa các khoảng trắng ẩn hoặc bị lặp lại do lỗi tải dữ liệu.

### Mã nguồn Python mẫu:
```python
import pandas as pd

def clean_whitespace_and_duplicates(df):
    cleaned_df = df.copy()
    
    # 1. Loại bỏ khoảng trắng thừa đầu và cuối ở tất cả các cột dạng chuỗi (string)
    for col in cleaned_df.select_dtypes(include=['object']):
        cleaned_df[col] = cleaned_df[col].astype(str).str.strip()
        
    # 2. Loại bỏ các dòng trùng lặp hoàn toàn
    cleaned_df = cleaned_df.drop_duplicates()
    return cleaned_df
```

## 2. Chuẩn hóa Định dạng Ngày tháng (Datetime) và Số (Numeric)

Ngày tháng trong Excel/SAP có thể hiển thị dưới nhiều dạng khác nhau (`DD/MM/YYYY`, `MM-DD-YYYY`, `YYYY.MM.DD`). Chuyển đổi toàn bộ về định dạng chuẩn của Pandas.

### Mã nguồn Python mẫu:
```python
import pandas as pd

def standardize_data_types(df, datetime_cols, numeric_cols):
    standardized_df = df.copy()
    
    # 1. Chuẩn hóa cột Ngày tháng
    for col in datetime_cols:
        # errors='coerce' sẽ chuyển các giá trị lỗi hoặc sai định dạng thành NaT (Not a Time)
        standardized_df[col] = pd.to_datetime(standardized_df[col], errors='coerce')
        
    # 2. Chuẩn hóa cột Số (loại bỏ ký tự phân tách hàng nghìn như dấu phẩy hoặc dấu chấm)
    for col in numeric_cols:
        # Nếu cột ở dạng string chứa dấu phân tách hàng nghìn (ví dụ "1,000,000" hoặc "1.000.000")
        if standardized_df[col].dtype == 'object':
            # Loại bỏ ký tự không phải số
            standardized_df[col] = standardized_df[col].astype(str).str.replace(r'[^\d.-]', '', regex=True)
            
        standardized_df[col] = pd.to_numeric(standardized_df[col], errors='coerce')
        
    return standardized_df
```

## 3. Xử lý giá trị trống (Null / NaN)

### Mã nguồn Python mẫu:
```python
def handle_missing_values(df, strategy_dict):
    """
    strategy_dict: Từ điển chỉ định phương pháp xử lý cho từng cột.
    Ví dụ: {'salary': 'median', 'name': 'fill_unknown', 'score': 'drop'}
    """
    result_df = df.copy()
    
    for col, strategy in strategy_dict.items():
        if col not in result_df.columns:
            continue
            
        if strategy == 'median':
            result_df[col] = result_df[col].fillna(result_df[col].median())
        elif strategy == 'mean':
            result_df[col] = result_df[col].fillna(result_df[col].mean())
        elif strategy == 'fill_unknown':
            result_df[col] = result_df[col].fillna("Unknown")
        elif strategy == 'drop':
            result_df = result_df.dropna(subset=[col])
            
    return result_df
```

## 4. Giải quyết lỗi Mã hóa Tiếng Việt (Encoding)
Khi mở các tệp CSV xuất ra từ hệ thống SAP GUI trên máy Windows, tiếng Việt thường bị lỗi font do sai mã hóa (Encoding).
* Luôn thử mở tệp với các mã hóa sau để tự động phát hiện mã hóa đúng: `utf-8`, `utf-8-sig` (đặc biệt hữu ích cho CSV từ Excel), `latin1`, `cp1258` (mã hóa Windows Vietnamese), hoặc `utf-16` (dữ liệu kết xuất từ một số phiên bản SAP).
* Đoạn code đọc file an toàn:
  ```python
  def read_csv_safe(file_path):
      encodings = ['utf-8-sig', 'utf-8', 'cp1258', 'latin1']
      for enc in encodings:
          try:
              df = pd.read_csv(file_path, encoding=enc)
              print(f"Đọc tệp thành công với mã hóa: {enc}")
              return df
          except UnicodeDecodeError:
              continue
      raise Exception("Không thể tự động giải mã tệp CSV bằng các bảng mã thông dụng.")
  ```

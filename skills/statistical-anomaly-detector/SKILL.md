---
name: statistical-anomaly-detector
description: "Phân tích bất thường đơn biến bằng thống kê Z-Score và IQR sử dụng pandas và numpy."
---

# Statistical Anomaly Detector (Z-Score & IQR)

Kỹ năng này hướng dẫn trợ lý AI (Anti Gravity) viết mã nguồn phát hiện các điểm bất thường (outliers/anomalies) trong từng cột dữ liệu số bằng các phương pháp thống kê truyền thống Z-Score và IQR.

## 1. Phương pháp Z-Score (Dành cho dữ liệu Phân phối chuẩn)

Z-Score đo lường số lần độ lệch chuẩn ($\sigma$) mà một điểm dữ liệu lệch khỏi giá trị trung bình ($\mu$). Thông thường, các điểm có Z-Score tuyệt đối lớn hơn $3$ ($|Z| > 3$) được coi là bất thường.

### Mã nguồn Python mẫu:
```python
import numpy as np
import pandas as pd

def detect_anomalies_zscore(df, column, threshold=3):
    data = df[column]
    mean = np.mean(data)
    std = np.std(data)
    
    if std == 0:
        return pd.DataFrame() # Tránh chia cho 0
        
    z_scores = (data - mean) / std
    
    # Gắn nhãn và lọc các hàng có điểm bất thường
    df_outliers = df[np.abs(z_scores) > threshold].copy()
    df_outliers['z_score'] = z_scores[np.abs(z_scores) > threshold]
    return df_outliers
```

## 2. Phương pháp IQR (Dành cho dữ liệu bất kỳ / Lệch nhiều)

IQR (Interquartile Range) là hiệu số giữa phân vị thứ 75 ($Q3$) và phân vị thứ 25 ($Q1$). Điểm bất thường được định nghĩa là nằm ngoài khoảng:
$[Q1 - 1.5 \times IQR, \quad Q3 + 1.5 \times IQR]$

### Mã nguồn Python mẫu:
```python
import pandas as pd

def detect_anomalies_iqr(df, column):
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    # Lọc các điểm dữ liệu nằm ngoài biên độ
    outliers_mask = (df[column] < lower_bound) | (df[column] > upper_bound)
    df_outliers = df[outliers_mask].copy()
    
    df_outliers['bound_violation'] = df[column].apply(
        lambda x: 'Quá thấp' if x < lower_bound else ('Quá cao' if x > upper_bound else 'Bình thường')
    )
    return df_outliers
```

## 3. Lựa chọn Phương pháp phù hợp

* **Chọn Z-Score khi:** Dữ liệu có hình chuông đối xứng (phân phối chuẩn), ví dụ: chiều cao, cân nặng, điểm số kiểm tra.
* **Chọn IQR khi:** Dữ liệu có độ lệch lớn (skewed), có nhiều giá trị cực trị tự nhiên, ví dụ: doanh thu, thu nhập, số lượng hàng tồn kho, lượng truy cập. IQR không bị ảnh hưởng bởi chính các giá trị cực trị đó khi tính toán biên độ.

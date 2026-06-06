---
name: time-series-anomaly-detector
description: "Phát hiện bất thường theo chuỗi thời gian sử dụng Rolling Statistics và thư viện ADTK."
---

# Time Series Anomaly Detector (Rolling Stats & ADTK)

Kỹ năng này hướng dẫn trợ lý AI (Anti Gravity) viết mã nguồn phát hiện các điểm bất thường trong chuỗi dữ liệu thời gian liên tục (time series), tính đến yếu tố xu hướng (trend) và tính chu kỳ (seasonality).

## 1. Phương pháp Thống kê Trượt (Rolling Statistics)

Phương pháp này tạo ra một biên độ động chạy dọc theo chuỗi thời gian bằng cách tính toán giá trị trung bình trượt (Moving Average) và độ lệch chuẩn trượt (Rolling Standard Deviation) trên một cửa sổ thời gian xác định (ví dụ: cửa sổ 7 ngày hoặc 30 ngày).

### Mã nguồn Python mẫu:
```python
import pandas as pd

def detect_anomalies_rolling(df, time_column, value_column, window=7, num_std=2):
    # Sắp xếp và đặt index theo cột thời gian
    df_sorted = df.sort_values(by=time_column).copy()
    df_sorted = df_sorted.set_index(time_column)
    
    # Tính toán trung bình trượt và độ lệch chuẩn trượt
    rolling_mean = df_sorted[value_column].rolling(window=window, min_periods=1).mean()
    rolling_std = df_sorted[value_column].rolling(window=window, min_periods=1).std().fillna(0)
    
    # Thiết lập ngưỡng trên và ngưỡng dưới động
    upper_bound = rolling_mean + (num_std * rolling_std)
    lower_bound = rolling_mean - (num_std * rolling_std)
    
    # Gắn cờ các dòng vượt quá ngưỡng
    df_sorted['rolling_mean'] = rolling_mean
    df_sorted['upper_bound'] = upper_bound
    df_sorted['lower_bound'] = lower_bound
    df_sorted['is_anomaly'] = (df_sorted[value_column] > upper_bound) | (df_sorted[value_column] < lower_bound)
    
    # Trả về kết quả chứa các điểm bất thường và biên độ để vẽ biểu đồ
    return df_sorted.reset_index()
```

## 2. Sử dụng thư viện ADTK (Anomaly Detection Toolkit)

Thư viện ADTK thiết kế chuyên sâu cho dữ liệu chuỗi thời gian, cung cấp các bộ phát hiện mức độ biến động đột ngột hoặc các thay đổi về xu hướng.

### Cài đặt thư viện:
```powershell
.venv\Scripts\pip install adtk
```

### Mã nguồn Python mẫu:
```python
import pandas as pd
from adtk.data import validate_to_datetime
from adtk.detector import ThresholdAD, VolatilityShiftAD

def detect_anomalies_adtk(df, time_column, value_column, low_threshold=None, high_threshold=None):
    # Validate định dạng thời gian và đặt làm index
    df_adtk = df.copy()
    df_adtk[time_column] = pd.to_datetime(df_adtk[time_column])
    df_adtk = df_adtk.set_index(time_column)
    df_adtk = validate_to_datetime(df_adtk)
    
    # 1. Phát hiện vượt ngưỡng cố định (ThresholdAD)
    if low_threshold is not None or high_threshold is not None:
        threshold_detector = ThresholdAD(low=low_threshold, high=high_threshold)
        anomalies = threshold_detector.detect(df_adtk[value_column])
        df_adtk['is_anomaly'] = anomalies
        return df_adtk.reset_index()
        
    # 2. Phát hiện thay đổi mức độ biến động đột ngột (VolatilityShiftAD)
    volatility_detector = VolatilityShiftAD(c=3.0, side="both")
    anomalies = volatility_detector.fit_detect(df_adtk[value_column])
    df_adtk['is_anomaly'] = anomalies.fillna(False)
    
    return df_adtk.reset_index()
```

## 3. Lưu ý đối với dữ liệu chuỗi thời gian
* **Đầy đủ dữ liệu:** Chuỗi thời gian yêu cầu không được mất mát dòng hoặc gián đoạn lớn. Hãy sử dụng kỹ năng `data-cleaning-and-formatting` để nội suy các giá trị thời gian bị thiếu trước khi phân tích.
* **Tần suất dữ liệu:** Đảm bảo cột mốc thời gian được phân chia đều (ví dụ: theo từng ngày, từng giờ hoặc từng phút).

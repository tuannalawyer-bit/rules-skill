---
name: ml-anomaly-detector
description: "Phát hiện bất thường đa biến bằng thuật toán học máy Isolation Forest và LOF sử dụng scikit-learn."
---

# ML Anomaly Detector (Isolation Forest & LOF)

Kỹ năng này hướng dẫn trợ lý AI (Anti Gravity) viết mã nguồn phát hiện các điểm bất thường phức tạp dựa trên sự kết hợp đồng thời của nhiều cột thuộc tính (đa biến) bằng các mô hình học máy nhẹ của Scikit-learn.

## 1. Phương pháp Isolation Forest (Rừng cô lập)

Isolation Forest hoạt động bằng cách xây dựng một loạt cây quyết định ngẫu nhiên để cô lập các điểm dữ liệu. Điểm bất thường (outliers) dễ bị cô lập hơn và sẽ nằm ở các nhánh nông gần gốc cây, trong khi các điểm bình thường cần nhiều lát cắt sâu hơn.

### Mã nguồn Python mẫu:
```python
import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies_isolation_forest(df, feature_columns, contamination=0.05):
    """
    contamination: tỷ lệ dự đoán điểm bất thường trong tập dữ liệu (mặc định 5%)
    """
    # Chuẩn bị dữ liệu đầu vào (chỉ lấy các cột số được chỉ định)
    X = df[feature_columns].fillna(df[feature_columns].median())
    
    # Khởi tạo và huấn luyện mô hình
    model = IsolationForest(contamination=contamination, random_state=42)
    model.fit(X)
    
    # Dự đoán: 1 là bình thường, -1 là bất thường
    predictions = model.predict(X)
    anomaly_scores = model.decision_function(X) # Điểm số bất thường (càng thấp càng bất thường)
    
    # Thêm nhãn vào DataFrame gốc
    df_result = df.copy()
    df_result['is_anomaly'] = predictions == -1
    df_result['anomaly_score'] = anomaly_scores
    
    # Chỉ trả về các hàng được dự đoán là bất thường
    return df_result[df_result['is_anomaly']]
```

## 2. Phương pháp Local Outlier Factor (LOF)

LOF phát hiện các bất thường dựa trên mật độ dữ liệu cục bộ. Nó so sánh mật độ của một điểm dữ liệu với mật độ của các điểm lân cận xung quanh. Một điểm có mật độ thấp hơn đáng kể so với lân cận sẽ bị coi là bất thường.

### Mã nguồn Python mẫu:
```python
import pandas as pd
from sklearn.neighbors import LocalOutlierFactor

def detect_anomalies_lof(df, feature_columns, n_neighbors=20, contamination=0.05):
    X = df[feature_columns].fillna(df[feature_columns].median())
    
    # Khởi tạo mô hình LOF
    model = LocalOutlierFactor(n_neighbors=n_neighbors, contamination=contamination)
    predictions = model.fit_predict(X) # 1 là bình thường, -1 là bất thường
    
    df_result = df.copy()
    df_result['is_anomaly'] = predictions == -1
    return df_result[df_result['is_anomaly']]
```

## 3. Quy trình Tiền xử lý dữ liệu Học máy
Để các mô hình học máy chạy chính xác, dữ liệu cần được chuẩn bị:
1. **Xử lý giá trị trống (Missing Values):** Điền giá trị trung vị (`median`) hoặc loại bỏ dòng trống.
2. **Chuẩn hóa thang đo (Scaling):** Nếu các cột số có thang đo quá lệch nhau (ví dụ: cột Tuổi có giá trị từ 1-100, cột Thu nhập từ 1 triệu - 100 triệu), hãy chuẩn hóa dữ liệu trước bằng `StandardScaler` hoặc `MinMaxScaler` để tránh mô hình bị lệch trọng số:
   ```python
   from sklearn.preprocessing import StandardScaler
   scaler = StandardScaler()
   X_scaled = scaler.fit_transform(X)
   ```

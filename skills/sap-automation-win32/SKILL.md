---
name: sap-automation-win32
description: "Tự động hóa phần mềm SAP GUI & SAP Analysis trong Excel bằng win32com.client và openpyxl."
---

# SAP Automation Win32 (SAP GUI & SAP Analysis)

Kỹ năng này hướng dẫn trợ lý AI (Anti Gravity) tự động hóa SAP GUI và Excel SAP Analysis trên hệ điều hành Windows ở quyền người dùng thông thường bằng cách sử dụng giao tiếp COM thông qua Python.

## 1. Điều kiện tiên quyết trên Windows

1. **Bật tính năng SAP GUI Scripting:**
   Trong SAP GUI, đi tới **Options > Accessibility & Scripting > Scripting** và tích chọn **Enable scripting**. Bỏ tích các tùy chọn thông báo (Notification) để tránh các cửa sổ cảnh báo bật lên ngắt quãng quá trình chạy code.
2. **Cài đặt thư viện pywin32 và openpyxl cục bộ:**
   ```powershell
   .venv\Scripts\pip install pywin32 openpyxl
   ```

## 2. Kết nối và Điều khiển SAP GUI bằng Python

Không sử dụng các công cụ click chuột theo tọa độ (như PyAutoGUI), luôn sử dụng đối tượng COM để điều khiển trực tiếp các phần tử UI của SAP nhằm đảm bảo độ tin cậy tuyệt đối.

```python
import win32com.client
import time

def connect_to_sap():
    try:
        # Truy cập Engine Scripting của SAP GUI đang chạy
        sap_gui_auto = win32com.client.GetObject("SAPGUI")
        application = sap_gui_auto.GetScriptingEngine
        
        # Lấy kết nối và phiên hoạt động đầu tiên
        connection = application.Children(0)
        session = connection.Children(0)
        return session
    except Exception as e:
        print(f"Không thể kết nối tới SAP GUI: {e}")
        return None

def run_sap_transaction(session, transaction_code):
    if not session:
        return
    
    # Điều hướng tới Transaction Code (ví dụ: /nVA01)
    session.findById("wnd[0]/tbar[0]/okcd").text = transaction_code
    session.findById("wnd[0]").sendVKey(0) # Phím Enter
    time.sleep(1)
    
    # Ví dụ: Nhập liệu vào một textbox dựa trên ID phần tử
    # Luôn ghi lại ID phần tử bằng chức năng "Script Recording and Playback" của SAP GUI
    # session.findById("wnd[0]/usr/txtXYZ").text = "Dữ liệu nhập"
```

## 3. Tự động hóa SAP Analysis trong Excel

Để tự động cập nhật (Refresh) các báo cáo SAP Analysis được liên kết trong file Excel:

```python
import win32com.client

def refresh_sap_analysis(excel_file_path):
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = True # Hoặc False để chạy ngầm
    
    try:
        # Mở file Excel báo cáo SAP
        workbook = excel.Workbooks.Open(excel_file_path)
        
        # Gọi Add-in SAP Analysis for Office để refresh dữ liệu
        # Add-in SAP Analysis thường đăng ký lệnh thông qua Application.Run
        excel.Application.Run("SAPExecuteCommand", "Refresh")
        
        # Lưu và đóng
        workbook.Save()
        workbook.Close()
    except Exception as e:
        print(f"Lỗi khi refresh SAP Analysis: {e}")
    finally:
        excel.Quit()
```

## 4. Nguyên tắc An toàn & Portable
* **Không lưu thông tin đăng nhập trong code:** Luôn yêu cầu thông tin đăng nhập từ file cấu hình ngoài (như JSON) được mã hóa hoặc nhập trực tiếp từ bàn phím.
* **Thời gian trễ (Sleep):** SAP phản hồi chậm hơn script chạy rất nhiều. Luôn chèn `time.sleep()` hợp lý hoặc viết hàm chờ phần tử UI xuất hiện trước khi tương tác.

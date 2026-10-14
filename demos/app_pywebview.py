"""
WinCommerce Desktop Application Launcher (pywebview)
Chạy ứng dụng Desktop độc lập 100% bằng Python và Windows WebView2.

Cài đặt thư viện:
    pip install pywebview

Chạy ứng dụng:
    python demos/app_pywebview.py
"""

import os
import sys

def run_app():
    try:
        import webview
    except ImportError:
        print("[!] Thư viện 'pywebview' chưa được cài đặt.")
        print("[i] Vui lòng chạy lệnh: pip install pywebview")
        return

    # Đường dẫn tệp giao diện standalone
    base_dir = os.path.dirname(os.path.abspath(__file__))
    html_file = os.path.join(base_dir, "wincommerce_desktop_standalone.html")

    # API Cầu nối (Python Bridge) cho phép Javascript từ giao diện gọi ngược về Python
    class RetailApi:
        def get_stores_count(self):
            return 3856

        def query_ai_forecast(self, prompt):
            return f"Phản hồi từ Python Backend: Đã xử lý '{prompt}' thành công với thuật toán tối ưu tồn kho!"

    api = RetailApi()

    # Khởi tạo cửa sổ Desktop chuẩn Native
    window = webview.create_window(
        title="WinCommerce Management OS",
        url=f"file:///{html_file.replace(os.sep, '/')}",
        js_api=api,
        width=1440,
        height=900,
        resizable=True,
        min_size=(1024, 700),
        frameless=False,  # Để True nếu muốn ẩn toàn bộ viền hệ điều hành để dùng titlebar tùy biến
        easy_drag=True
    )

    webview.start(debug=False)

if __name__ == "__main__":
    run_app()

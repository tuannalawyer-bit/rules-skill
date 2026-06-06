---
name: web-scraping-headless
description: "Duyệt web động và cào dữ liệu dạng portable, không yêu cầu quyền Admin bằng Playwright (chromium) và BeautifulSoup."
---

# Web Scraping Headless (Portable & Non-Admin)

Kỹ năng này hướng dẫn trợ lý AI (Anti Gravity) viết mã nguồn thu thập dữ liệu (scraping) và tự động hóa trình duyệt trên Windows đảm bảo tính di động (Portable), chạy ở quyền người dùng thông thường và không đòi hỏi quyền quản trị viên (Admin).

## 1. Thiết lập Môi trường Portable cho Playwright

Playwright mặc định lưu trình duyệt Chromium vào thư mục AppData của hệ thống (yêu cầu quyền ghi hệ thống hoặc có thể bị khóa). Để đảm bảo ứng dụng hoàn toàn Portable:

1. **Thiết lập thư mục tải browser cục bộ:**
   Chỉ định biến môi trường `PLAYWRIGHT_BROWSERS_PATH` trỏ vào một thư mục con ngay trong thư mục dự án (ví dụ: `bin/ms-playwright`).
   
   Cú pháp thiết lập trong mã nguồn Python:
   ```python
   import os
   # Đặt đường dẫn tải browser cục bộ trong thư mục dự án
   project_dir = os.path.dirname(os.path.abspath(__file__))
   os.environ["PLAYWRIGHT_BROWSERS_PATH"] = os.path.join(project_dir, "bin", "ms-playwright")
   ```

2. **Cài đặt thư viện và Tải trình duyệt (Không cần Admin):**
   ```powershell
   # Cài đặt thư viện Playwright cục bộ vào virtual environment (.venv)
   .venv\Scripts\pip install playwright
   
   # Tải chromium về thư mục cục bộ đã cấu hình ở trên
   $env:PLAYWRIGHT_BROWSERS_PATH = ".\bin\ms-playwright"
   .venv\Scripts\playwright install chromium
   ```

## 2. Mã nguồn Tự động hóa & Scraping Web Động (Mẫu)

```python
import os
import sys

# 1. Cấu hình biến môi trường trước khi import playwright
project_dir = os.path.dirname(os.path.abspath(__file__))
os.environ["PLAYWRIGHT_BROWSERS_PATH"] = os.path.join(project_dir, "bin", "ms-playwright")

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def scrape_dynamic_site(url):
    with sync_playwright() as p:
        # Khởi chạy trình duyệt headless từ thư mục cục bộ
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Thiết lập thời gian chờ tối đa
        page.set_default_timeout(15000)
        
        # Điều hướng trang web
        page.goto(url)
        
        # Chờ phần tử động được render hoàn toàn
        page.wait_for_selector("body")
        
        # Lấy nội dung trang
        html_content = page.content()
        browser.close()
        
        # Phân tích nội dung bằng BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")
        return soup
```

## 3. Đóng gói Portable (Sử dụng PyInstaller)

Để chuyển ứng dụng thành một tệp `.exe` duy nhất có thể chạy trên máy khác:

1. Đóng gói mã nguồn kèm theo các tệp nhị phân của trình duyệt Chromium:
   ```powershell
   .venv\Scripts\pip install pyinstaller
   
   # Đóng gói và copy thư mục trình duyệt cục bộ đi kèm
   .venv\Scripts\pyinstaller --onefile --add-data "bin/ms-playwright;bin/ms-playwright" main.py
   ```
2. Đảm bảo ứng dụng chạy trong vùng quyền User thường (Default UAC). Không chỉnh sửa manifest yêu cầu quyền Administrator (`requireAdministrator`).

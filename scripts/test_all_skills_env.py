# -*- coding: utf-8 -*-
"""
Kịch bản kiểm thử toàn diện môi trường và thư viện phục vụ 18 kỹ năng tùy chỉnh.
Thực thi kiểm tra theo nguyên tắc Run-Before-Deliver của General Rules v2.3.0.
"""

import sys
import os

def test_suite():
    results = {}
    print("=" * 60)
    print("[*] BẮT ĐẦU CHẠY BỘ KIỂM THỬ TOÀN DIỆN 18 KỸ NĂNG TÙY CHỈNH")
    print("=" * 60)

    # 1. Kiểm tra Imports lõi
    try:
        import pandas as pd
        import numpy as np
        import openpyxl
        import scipy
        import sklearn
        from sklearn.ensemble import IsolationForest
        import adtk
        from bs4 import BeautifulSoup
        import lxml
        import requests
        import win32com.client
        import cv2
        from PIL import Image
        import moviepy
        import pdfplumber
        import pypdf
        from playwright.sync_api import sync_playwright
        results["1. Core Imports"] = "PASS (17/17 packages)"
        print("[+] Ca 1: Nhập thư viện lõi -> ĐẠT")
    except Exception as e:
        results["1. Core Imports"] = f"FAIL ({e})"
        print(f"[-] Ca 1: Nhập thư viện lõi -> THẤT BẠI: {e}")

    # 2. Kiểm tra Xử lý Dữ liệu & Học máy (Skills 2, 9, 16, 17)
    try:
        import pandas as pd
        import numpy as np
        from sklearn.ensemble import IsolationForest
        
        # Tạo dữ liệu chuỗi thời gian & ma trận số liệu
        dates = pd.date_range(start="2026-01-01", periods=20, freq="D")
        vals = [10, 12, 11, 13, 12, 11, 14, 13, 100, 12, 11, 13, 12, 14, 11, 12, 13, 11, 12, 10]
        df = pd.DataFrame({"Date": dates, "Value": vals}).set_index("Date")
        
        # Test Rolling Mean & Z-score
        rolling_mean = df["Value"].rolling(window=3).mean()
        
        # Test Isolation Forest Anomaly Detection
        model = IsolationForest(contamination=0.1, random_state=42)
        df["Anomaly"] = model.fit_predict(df[["Value"]])
        
        # Test Excel Export
        excel_path = "test_data_output.xlsx"
        df.to_excel(excel_path, engine="openpyxl")
        if os.path.exists(excel_path):
            os.remove(excel_path)
            
        results["2. Data Cleaning & Anomaly ML"] = "PASS"
        print("[+] Ca 2: Xử lý dữ liệu, Rolling Stats & Isolation Forest ML -> ĐẠT")
    except Exception as e:
        results["2. Data Cleaning & Anomaly ML"] = f"FAIL ({e})"
        print(f"[-] Ca 2: Xử lý dữ liệu -> THẤT BẠI: {e}")

    # 3. Kiểm tra Tự động hóa Windows / COM (Skill 14)
    try:
        import win32com.client
        fso = win32com.client.Dispatch("Scripting.FileSystemObject")
        temp_folder = fso.GetSpecialFolder(2).Path
        assert len(temp_folder) > 0
        results["3. Win32 COM & SAP Automation Ready"] = "PASS"
        print("[+] Ca 3: Khởi tạo COM Dispatcher (Sẵn sàng cho SAP GUI & Excel) -> ĐẠT")
    except Exception as e:
        results["3. Win32 COM & SAP Automation Ready"] = f"FAIL ({e})"
        print(f"[-] Ca 3: COM Dispatcher -> THẤT BẠI: {e}")

    # 4. Kiểm tra Thị giác máy tính & Xử lý Ảnh (Skill 8)
    try:
        import cv2
        import numpy as np
        from PIL import Image
        
        # Tạo ảnh giả lập và xử lý OpenCV
        img_pil = Image.new("RGB", (100, 100), color=(255, 255, 255))
        img_np = np.array(img_pil)
        gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)
        assert thresh.shape == (100, 100)
        results["4. Computer Vision (OpenCV & PIL)"] = "PASS"
        print("[+] Ca 4: Xử lý hình ảnh OpenCV & Pillow -> ĐẠT")
    except Exception as e:
        results["4. Computer Vision (OpenCV & PIL)"] = f"FAIL ({e})"
        print(f"[-] Ca 4: Computer Vision -> THẤT BẠI: {e}")

    # 5. Kiểm tra Trích xuất PDF (Skill 10)
    try:
        import pypdf
        writer = pypdf.PdfWriter()
        writer.add_blank_page(width=100, height=100)
        pdf_test_path = "test_sample.pdf"
        with open(pdf_test_path, "wb") as f:
            writer.write(f)
            
        reader = pypdf.PdfReader(pdf_test_path)
        assert len(reader.pages) == 1
        if os.path.exists(pdf_test_path):
            os.remove(pdf_test_path)
        results["5. PDF Extraction & Creation"] = "PASS"
        print("[+] Ca 5: Đọc và tạo PDF (pypdf/pdfplumber) -> ĐẠT")
    except Exception as e:
        results["5. PDF Extraction & Creation"] = f"FAIL ({e})"
        print(f"[-] Ca 5: PDF Processing -> THẤT BẠI: {e}")

    # 6. Kiểm tra Playwright Headless Scraping (Skill 18)
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.set_content("<html><body><div id='content'>Antigravity Web Scraping OK</div></body></html>")
            text = page.locator("#content").inner_text()
            browser.close()
            assert text == "Antigravity Web Scraping OK"
        results["6. Headless Browser Scraping (Playwright)"] = "PASS"
        print("[+] Ca 6: Trình duyệt Headless Chromium Playwright -> ĐẠT")
    except Exception as e:
        results["6. Headless Browser Scraping (Playwright)"] = f"FAIL ({e})"
        print(f"[-] Ca 6: Playwright Headless -> THẤT BẠI: {e}")

    # 7. Kiểm tra Biên tập Video MoviePy (Skill 1)
    try:
        import moviepy
        import imageio_ffmpeg
        ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
        assert os.path.exists(ffmpeg_exe)
        results["7. AI Video Filmmaking (MoviePy & Portable FFmpeg)"] = f"PASS ({os.path.basename(ffmpeg_exe)})"
        print(f"[+] Ca 7: MoviePy & FFmpeg Portable ({os.path.basename(ffmpeg_exe)}) -> ĐẠT")
    except Exception as e:
        results["7. AI Video Filmmaking (MoviePy & Portable FFmpeg)"] = f"FAIL ({e})"
        print(f"[-] Ca 7: MoviePy -> THẤT BẠI: {e}")

    print("=" * 60)
    print("KẾT QUẢ TỔNG HỢP KIỂM THỬ:")
    all_passed = True
    for test_name, status in results.items():
        print(f" - {test_name}: {status}")
        if not status.startswith("PASS"):
            all_passed = False
    print("=" * 60)
    
    if all_passed:
        print("[SUCCESS] 100% CÁC CA KIỂM THỬ ĐÃ VƯỢT QUA! TẤT CẢ TÀI NGUYÊN ĐÃ SẴN SÀNG!")
        return 0
    else:
        print("[ERROR] CÓ CA KIỂM THỬ KHÔNG ĐẠT!")
        return 1

if __name__ == "__main__":
    sys.exit(test_suite())

# Quy tắc & Kỹ năng tùy chỉnh cho Google Antigravity

Repository này lưu trữ các nguyên tắc hoạt động toàn cục và 11 kỹ năng tùy chỉnh của trợ lý AI (Anti Gravity) phục vụ các công việc tự động hóa, cào dữ liệu, xử lý ảnh, dựng phim và QA dữ liệu trên Windows.

---

## 1. Cấu trúc Kho lưu trữ

*   **`rules/general_rules.md`**: Bản nguyên tắc hoạt động toàn cục (chỉ code khi xác nhận, tự động sao lưu, kiểm thử QA tự động sửa lỗi, không yêu cầu quyền Admin, chạy ứng dụng portable khởi động < 2s).
*   **`projects/Dự án AI/development_log.csv`**: Tệp nhật ký phát triển ghi nhận lịch sử thay đổi phiên bản.
*   **`skills/`**: Danh sách 11 kỹ năng tùy chỉnh:
    *   `web-scraping-headless`: Cào web động không admin bằng Playwright.
    *   `sap-automation-win32`: Tự động hóa SAP GUI và Excel Analysis qua COM API.
    *   `image-computer-vision`: Xử lý hình ảnh và EasyOCR.
    *   `ai-video-filmmaking`: Biên tập video tự động bằng MoviePy và FFmpeg portable.
    *   `reasoning-critic-qa`: Kỹ năng tự phản biện ngược và QA vá lỗi tự động.
    *   `statistical-anomaly-detector`: Tìm điểm bất thường bằng Z-Score và IQR.
    *   `ml-anomaly-detector`: Tìm bất thường đa biến bằng Isolation Forest và LOF.
    *   `time-series-anomaly-detector`: Tìm bất thường chuỗi thời gian bằng Rolling Stats và ADTK.
    *   `data-cleaning-and-formatting`: Dọn dẹp dữ liệu thô và sửa lỗi font tiếng Việt.
    *   `excel-report-generator`: Định dạng báo cáo Excel chuyên nghiệp, tô màu cảnh báo.
    *   `pdf-data-extractor`: Trích xuất bảng dữ liệu từ tệp PDF/PDF Scan.

---

## 2. Hướng dẫn Đồng bộ ngược về máy tính mới (Windows)

Để đồng bộ và sử dụng toàn bộ các kỹ năng và quy tắc này trên một máy tính khác của bạn:

### Bước 1: Clone kho lưu trữ này về máy
Mở Terminal/PowerShell trên máy tính mới và chạy lệnh:
```powershell
git clone https://github.com/tuannalawyer-bit/rules-skill.git
cd rules-skill
```

### Bước 2: Đồng bộ Nguyên tắc hoạt động toàn cục (Global Rules)
Sao chép tệp `general_rules.md` vào thư mục cấu hình ẩn của Antigravity trên máy mới:
```powershell
# Tạo thư mục đích nếu chưa có
New-Item -ItemType Directory -Path "$HOME\.gemini\antigravity\knowledge\global_directives" -Force

# Sao chép tệp nguyên tắc
Copy-Item -Path "rules\general_rules.md" -Destination "$HOME\.gemini\antigravity\knowledge\global_directives\" -Force
```

### Bước 3: Đồng bộ các Kỹ năng tùy chỉnh (Global Skills)
Sao chép thư mục `skills` vào thư mục cấu hình skill toàn cục của máy mới:
```powershell
# Tạo thư mục đích nếu chưa có
New-Item -ItemType Directory -Path "$HOME\.gemini\config\skills" -Force

# Sao chép toàn bộ các kỹ năng con
Copy-Item -Path "skills\*" -Destination "$HOME\.gemini\config\skills\" -Recurse -Force
```

Khởi động lại phiên làm việc của Anti Gravity trên máy tính mới. Hệ thống sẽ tự động tải các nguyên tắc toàn cục và nhận diện toàn bộ 11 kỹ năng mới để sẵn sàng phục vụ bạn!

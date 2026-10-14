# Quy tắc & Kỹ năng tùy chỉnh cho ChatGPT/Codex và Google Antigravity

Repository này lưu trữ các nguyên tắc hoạt động dùng chung và 22 kỹ năng tùy chỉnh cho ChatGPT/Codex và Google Antigravity/Gemini, phục vụ các công việc tự động hóa, cào dữ liệu, xử lý ảnh, dựng phim, QA và chẩn đoán lỗi dữ liệu trên Windows.

---

## 1. Cấu trúc Kho lưu trữ

*   **`rules/general_rules.md`**: Bản nguyên tắc hoạt động toàn cục (chỉ code khi xác nhận, tương thích Tiếng Việt Telex, tự động sao lưu, kiểm thử QA tự động sửa lỗi, không yêu cầu quyền Admin, chạy ứng dụng portable khởi động < 2s).
*   **`projects/Dự án AI/development_log.csv`**: Tệp nhật ký phát triển ghi nhận lịch sử thay đổi phiên bản.
*   **`skills/`**: Danh sách 22 kỹ năng tùy chỉnh:
    *   **Nhóm năng suất & QA:**
        *   `ai-bug-triage`: Phân loại, gom cụm lỗi, đánh giá mức độ nghiêm trọng (P0-P3) và lập báo cáo lỗi (Bug Report) chi tiết chuẩn công nghiệp.
        *   `code-review-and-qa`: Rà soát mã nguồn và kiểm định chất lượng sản phẩm đa trục (Tính đúng đắn, bảo mật, xử lý lỗi biên và chất lượng kiểm thử).
        *   `diagnose`: Chẩn đoán lỗi phần mềm từng bước khoa học.
        *   `exploratory-testing`: Kiểm thử thăm dò sản phẩm (Exploratory Testing), rà soát hành vi bất thường, kịch bản phá bĩnh và phát hiện lỗi tiềm ẩn.
        *   `git-commit-helper`: Tự động hóa phân tích git diff, sinh commit Semantic, quản lý phiên bản SemVer và ghi nhật ký phát triển development_log.csv.
        *   `grill-me`: Phỏng vấn sâu chất vấn giải pháp để đồng bộ lên GitHub.
        *   `handoff`: Bàn giao ngữ cảnh phiên làm việc giữa các máy tính.
        *   `prototype`: Xây dựng nhanh phiên bản thô chạy thử (MVP) của phần mềm.
        *   `reasoning-critic-qa`: Phản biện giải pháp, phân tích rủi ro, kiểm thử (QA) và tự động sửa lỗi trong các ứng dụng di động & portable.
        *   `skill-documenter`: Tự động quét thư mục skills/, đọc YAML frontmatter của từng kỹ năng và đồng bộ bảng danh sách kỹ năng vào tệp README.md chính.
    *   **Nhóm cào dữ liệu & Tự động hóa:**
        *   `sap-automation-win32`: Tự động hóa phần mềm SAP GUI & SAP Analysis trong Excel bằng win32com.client và openpyxl.
        *   `web-scraping-headless`: Duyệt web động và cào dữ liệu dạng portable, không yêu cầu quyền Admin bằng Playwright (chromium) và BeautifulSoup.
    *   **Nhóm xử lý đa phương tiện:**
        *   `ai-video-filmmaking`: Làm phim AI bằng API và biên tập video tự động bằng MoviePy & FFmpeg portable.
        *   `image-computer-vision`: Xử lý hình ảnh và nhận diện ký tự (OCR) bằng OpenCV, Pillow và EasyOCR không đòi hỏi quyền Admin.
        *   `premium-ui-assets`: Cung cấp thư viện mã CSS/HTML mẫu chuẩn premium (gradient, glassmorphism, dark mode, micro-animations, màu HSL) để thiết kế giao diện cao cấp.
        *   `wincommerce-luminous-liquid-glass`: >-
    *   **Nhóm xử lý dữ liệu nâng cao:**
        *   `data-cleaning-and-formatting`: Chuẩn hóa định dạng, làm sạch dữ liệu thô và xử lý giá trị trống (Null/NaN) sử dụng pandas.
        *   `excel-report-generator`: Tạo báo cáo Excel cao cấp, tô màu có điều kiện (Conditional Formatting) và tạo biểu đồ bằng openpyxl.
        *   `ml-anomaly-detector`: Phát hiện bất thường đa biến bằng thuật toán học máy Isolation Forest và LOF sử dụng scikit-learn.
        *   `pdf-data-extractor`: Trích xuất dữ liệu bảng biểu từ tệp PDF dạng văn bản hoặc dạng scan ảnh.
        *   `statistical-anomaly-detector`: Phân tích bất thường đơn biến bằng thống kê Z-Score và IQR sử dụng pandas và numpy.
        *   `time-series-anomaly-detector`: Phát hiện bất thường theo chuỗi thời gian sử dụng Rolling Statistics và thư viện ADTK.

---

## 2. Hướng dẫn Đồng bộ ngược về máy tính mới (Windows)

Để đồng bộ và sử dụng toàn bộ các kỹ năng và quy tắc này trên một máy tính khác của bạn:

### Bước 1: Clone kho lưu trữ này về máy
Mở Terminal/PowerShell trên máy tính mới và chạy lệnh:
```powershell
git clone https://github.com/tuannalawyer-bit/rules-skill.git
cd rules-skill
```

### Bước 2: Đồng bộ nguyên tắc cho nền tảng đang dùng

#### ChatGPT/Codex

Đặt `AGENTS.md` tại thư mục gốc của repository cần làm việc. Nếu dự án đã có `AGENTS.md`, hãy hợp nhất nội dung thay vì ghi đè để giữ các quy ước riêng của dự án.

#### Google Antigravity/Gemini

Sao chép tệp `general_rules.md` vào thư mục cấu hình ẩn của Antigravity trên máy mới:
```powershell
# Tạo thư mục đích nếu chưa có
New-Item -ItemType Directory -Path "$HOME\.gemini\antigravity\knowledge\global_directives" -Force

# Sao chép tệp nguyên tắc
Copy-Item -Path "rules\general_rules.md" -Destination "$HOME\.gemini\antigravity\knowledge\global_directives\" -Force
```

### Bước 3: Đồng bộ các kỹ năng tùy chỉnh

Với Codex, sao chép các thư mục kỹ năng vào thư mục kỹ năng cá nhân `$HOME\.codex\skills`. Với Antigravity, sử dụng `$HOME\.gemini\config\skills` như dưới đây. Hãy kiểm duyệt nội dung trước khi cài và không ghi đè kỹ năng đã tùy chỉnh nếu chưa sao lưu.

```powershell
# Codex
New-Item -ItemType Directory -Path "$HOME\.codex\skills" -Force
Copy-Item -Path "skills\*" -Destination "$HOME\.codex\skills\" -Recurse -Force

# Antigravity/Gemini
# Tạo thư mục đích nếu chưa có
New-Item -ItemType Directory -Path "$HOME\.gemini\config\skills" -Force

# Sao chép toàn bộ các kỹ năng con
Copy-Item -Path "skills\*" -Destination "$HOME\.gemini\config\skills\" -Recurse -Force
```

Khởi động một phiên làm việc mới trên nền tảng tương ứng để hệ thống nạp lại nguyên tắc và nhận diện các kỹ năng.

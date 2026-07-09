---
name: skill-documenter
description: "Tự động quét thư mục skills/, đọc YAML frontmatter của từng kỹ năng và đồng bộ bảng danh sách kỹ năng vào tệp README.md chính."
---

# Skill Documenter

Kỹ năng này hướng dẫn trợ lý AI quét hệ thống kỹ năng hiện tại của dự án và tự động cập nhật, đồng bộ hóa thông tin trong tệp tài liệu `README.md` chính của kho lưu trữ.

## Quy trình Thực hiện

Khi người dùng yêu cầu cập nhật tài liệu hoặc đồng bộ danh sách kỹ năng, tôi phải thực hiện các bước sau:

### Bước 1: Quét hệ thống kỹ năng
1. Duyệt qua thư mục `skills/` cục bộ để lấy danh sách tất cả các kỹ năng hiện có (các thư mục con chứa tệp `SKILL.md`).
2. Với mỗi kỹ năng, đọc nội dung tệp `SKILL.md` và phân tích phần YAML frontmatter ở đầu tệp để lấy ra:
   - `name`: Tên định danh của kỹ năng.
   - `description`: Mô tả ngắn gọn về tính năng của kỹ năng.

### Bước 2: Phân loại kỹ năng
Phân loại các kỹ năng tìm thấy thành các nhóm chính tương ứng trong cấu trúc `README.md`:
*   **Nhóm năng suất & QA:** các kỹ năng như `reasoning-critic-qa`, `diagnose`, `grill-me`, `handoff`, `prototype`, `git-commit-helper`, `skill-documenter`.
*   **Nhóm cào dữ liệu & Tự động hóa:** các kỹ năng như `web-scraping-headless`, `sap-automation-win32`.
*   **Nhóm xử lý đa phương tiện:** các kỹ năng như `image-computer-vision`, `ai-video-filmmaking`.
*   **Nhóm xử lý dữ liệu nâng cao:** các kỹ năng như `statistical-anomaly-detector`, `ml-anomaly-detector`, `time-series-anomaly-detector`, `data-cleaning-and-formatting`, `excel-report-generator`, `pdf-data-extractor`.

### Bước 3: Đồng bộ vào README.md
1. Đọc tệp `README.md` chính tại gốc dự án.
2. Tìm vùng danh sách kỹ năng dưới mục `## 1. Cấu trúc Kho lưu trữ` -> `* **skills/**: Danh sách kỹ năng tùy chỉnh:`.
3. Tái cấu trúc và tạo lại danh sách kỹ năng theo đúng tên và mô tả trích xuất được từ bước 1 & 2.
4. Ghi đè tệp `README.md` với danh sách kỹ năng mới đã cập nhật đầy đủ, đảm bảo định dạng Markdown chính xác và sạch đẹp.

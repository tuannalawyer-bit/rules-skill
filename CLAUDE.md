# Hướng dẫn Phát triển Kho lưu trữ Rules & Skills

Tệp này quy định quy trình phát triển, kiểm thử và đóng góp dành riêng cho dự án quản lý các quy tắc (`rules/`) và kỹ năng tùy chỉnh (`skills/`).

## Quy trình làm việc với Skills & Rules

1. **Khi tạo mới hoặc cập nhật một Kỹ năng:**
   - Tạo thư mục mới trong `skills/<tên-kỹ-năng>/` và tệp `SKILL.md` bên trong.
   - Bắt buộc phải khai báo YAML frontmatter ở đầu tệp `SKILL.md` chứa hai trường `name` và `description` (tên kỹ năng viết thường không dấu, ngăn cách bằng dấu gạch ngang).
   - Tách biệt các phần tài liệu tham khảo dài, code mẫu nặng sang thư mục `skills/<tên-kỹ-năng>/references/` hoặc `skills/<tên-kỹ-năng>/examples/` để tối ưu hóa context window (phân lớp thông tin - Progressive Disclosure).

2. **Chạy kiểm thử trước khi bàn giao (Run-Before-Deliver):**
   - Chạy script kiểm duyệt định dạng các kỹ năng: `python scripts/validate_skills.py` (hoặc đường dẫn tương ứng với python cục bộ).
   - Tất cả các tệp `SKILL.md` phải vượt qua bước kiểm duyệt này mà không có bất kỳ lỗi frontmatter nào.

3. **Cập nhật Nhật ký phát triển (Development Log):**
   - Cập nhật dòng log tương ứng vào tệp `projects/Dự án AI/development_log.csv` theo định dạng **UTF-8 có BOM (`utf-8-sig`)**.
   - Định dạng phiên bản SemVer (ví dụ: tăng Patch cho sửa lỗi nhỏ; Minor cho tính năng/kỹ năng mới; Major cho thay đổi lớn).
   - Định dạng cột bắt buộc: `Yêu cầu sửa đổi,Giải pháp thực hiện,Tên phiên bản,Thời gian xây dựng` (với thời gian theo định dạng `dd-mm-yyyy HH:mm:ss`).

## Các lệnh PowerShell thường dùng
- Kiểm tra tính hợp lệ của Skills:
  `python scripts/validate_skills.py` (hoặc `python_portable\python.exe scripts\validate_skills.py` nếu sử dụng môi trường portable).
- Sao chép toàn bộ Skills sang cấu hình hệ thống Antigravity:
  `Copy-Item -Path "skills\*" -Destination "$HOME\.gemini\config\skills\" -Recurse -Force`
- Sao chép Rules sang cấu hình hệ thống Antigravity:
  `Copy-Item -Path "rules\general_rules.md" -Destination "$HOME\.gemini\antigravity\knowledge\global_directives\" -Force`

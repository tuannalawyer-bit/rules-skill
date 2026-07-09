---
name: git-commit-helper
description: "Tự động hóa phân tích git diff, sinh commit Semantic, quản lý phiên bản SemVer và ghi nhật ký phát triển development_log.csv."
---

# Git Commit & Development Log Helper

Kỹ năng này hướng dẫn trợ lý AI tự động hóa và đồng bộ luồng công việc kiểm soát phiên bản (Git) và ghi nhật ký phát triển (`development_log.csv`) một cách an toàn, chính xác và nhất quán.

## Quy trình Thực hiện

Khi người dùng yêu cầu commit hoặc hoàn tất một công việc phát triển, tôi phải thực hiện các bước sau:

### Bước 1: Phân tích các thay đổi (Git Diff)
1. Sử dụng lệnh `git status` và `git diff` để kiểm tra các tệp tin đã bị sửa đổi hoặc thêm mới trong không gian làm việc.
2. Xác định phạm vi (scope) và mục tiêu cốt lõi của các thay đổi vừa thực hiện (ví dụ: cập nhật rules, tạo skill mới, sửa lỗi script).

### Bước 2: Xác định phiên bản và viết Nhật ký
1. Đọc tệp nhật ký `projects/Dự án AI/development_log.csv` để xác định phiên bản hiện tại (ví dụ: `v2.0.0`).
2. Xác định mã phiên bản tiếp theo dựa trên quy tắc SemVer:
   - **PATCH** (Ví dụ: `2.0.0` -> `2.0.1`): Nếu chỉ sửa các lỗi nhỏ, cập nhật câu từ trong quy tắc hoặc sửa lỗi script nhỏ.
   - **MINOR** (Ví dụ: `2.0.0` -> `2.1.0`): Nếu bổ sung thêm kỹ năng mới hoặc cấu hình mới không làm thay đổi luồng hoạt động cũ.
   - **MAJOR** (Ví dụ: `2.0.0` -> `3.0.0`): Nếu tái cấu trúc hệ thống hoặc có những thay đổi lớn gây ảnh hưởng đến tính tương thích.
3. Tạo dòng thông tin nhật ký mới với định dạng:
   `Yêu cầu sửa đổi,Giải pháp thực hiện,Tên phiên bản,Thời gian xây dựng`
   - *Thời gian xây dựng* phải lấy theo định dạng: `dd-mm-yyyy HH:mm:ss`.
   - Lưu ý bọc các trường trong dấu ngoặc kép kép `""...""` nếu nội dung chứa dấu phẩy.
   - Ghi nội dung này vào tệp `projects/Dự án AI/development_log.csv` đảm bảo lưu với mã hóa **UTF-8 có BOM (`utf-8-sig`)**.

### Bước 3: Đề xuất Lệnh Commit Semantic
1. Tạo thông điệp commit theo chuẩn Conventional Commits:
   `type(scope): description`
   - *type* bao gồm: `feat` (tính năng/kỹ năng mới), `fix` (sửa lỗi), `docs` (tài liệu/quy tắc), `refactor` (tái cấu trúc).
   - *scope* là phạm vi sửa đổi (ví dụ: `skills`, `rules`, `scripts`).
   - *description* là mô tả ngắn gọn bằng Tiếng Việt hoặc Tiếng Anh không dấu/có dấu (ví dụ: `feat(skills): add git-commit-helper skill`).
2. Đề xuất lệnh commit hoàn chỉnh trên khung chat để người dùng phê duyệt trước khi thực thi:
   `git add . ; git commit -m "feat(skills): add git-commit-helper skill"`

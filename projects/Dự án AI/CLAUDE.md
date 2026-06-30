# Dự án: Dự án AI
Các ứng dụng nhỏ, di động (Portable), chạy ở quyền người dùng thông thường (không đòi Admin) trên hệ điều hành Windows.

---

## 1. Lệnh hệ thống (Commands)
*   **Môi trường ảo Python:** `.venv`
*   **Lệnh chạy chương trình:** `.venv\Scripts\python main.py`
*   **Lệnh cài đặt thư viện:** `.venv\Scripts\pip install [tên_gói]`
*   **Lệnh chạy kiểm thử:** `.venv\Scripts\pytest`

---

## 2. Tiêu chuẩn viết code (Coding Guidelines)
*   **Giao tiếp & Phê duyệt (Pre-coding):**
    *   Nêu rõ giả định, trình bày đánh đổi và làm rõ mơ hồ trước khi viết code.
    *   Chỉ phân tích trên chat, chỉ chỉnh sửa tệp tin hoặc chạy lệnh hệ thống khi có sự đồng ý rõ ràng từ người dùng.
*   **Quy trình sao lưu & Nhật ký (Safe Coding):**
    *   Bắt buộc tạo bản sao lưu `.bak_YYYYMMDD_HHMMSS` trước khi chỉnh sửa bất kỳ tệp tin nguồn hay tài liệu nào.
    *   Ghi nhận nhật ký vào `development_log.csv` (lưu bằng `utf-8-sig`) ngay sau khi sửa thành công. Định dạng cột thời gian bắt buộc là **`dd-mm-yyyy HH:mm:ss`** (ví dụ: `30-06-2026 21:30:00`).
*   **Hành vi lập trình tinh gọn (Simplicity & Surgical Changes):**
    *   Chỉ sửa đổi đúng tệp tin và dòng code bắt buộc, không refactor bừa bãi.
    *   Viết lượng code tối thiểu cần thiết để giải quyết vấn đề, cấm vẽ thêm logic dự phòng. Tinh chỉnh và làm sạch code trước khi bàn giao.
*   **Tương thích Tiếng Việt (Telex/Unicode) & Xử lý đường dẫn:**
    *   Ghi rõ `encoding='utf-8'` khi đọc/ghi tệp văn bản Tiếng Việt (`encoding='utf-8-sig'` đối với CSV).
    *   Bọc đường dẫn có chứa khoảng trắng hoặc ký tự có dấu trong dấu ngoặc kép đôi `"..."` khi gọi qua dòng lệnh Shell.
*   **Đóng gói Portable & Không Admin:**
    *   Ứng dụng hoạt động trong không gian quyền người dùng (User space), tuyệt đối không đòi quyền Admin.
    *   Thiết kế dạng Portable, tối ưu hóa tốc độ khởi động phần mềm dưới **2 giây**.

---

## 3. Nhật ký sửa sai (Lessons Learned / Do Not Repeat)
*(Vùng ghi nhận các lỗi đã mắc phải và giải pháp xử lý bắt buộc để tránh lặp lại lỗi)*

*   **LỖI 1: Lỗi font chữ Tiếng Việt khi xuất file CSV từ Python mở bằng Excel.**
    *   *SỬA:* Sử dụng mã hóa `encoding='utf-8-sig'` thay vì `utf-8` khi lưu file CSV.
*   **LỖI 2: Lỗi Shell không tìm thấy tệp/thư mục khi đường dẫn chứa ký tự Tiếng Việt có dấu.**
    *   *SỬA:* Luôn bọc đường dẫn trong dấu ngoặc kép đôi `"..."` khi truyền tham số cho các tiến trình con hoặc CLI (như git, python, ffmpeg).
*   **LỖI 3: Thư viện Playwright bị chặn hoặc đòi quyền admin khi cài đặt trình duyệt mặc định.**
    *   *SỬA:* Luôn cấu hình biến môi trường `PLAYWRIGHT_BROWSERS_PATH` trỏ cục bộ về thư mục dự án để tải trình duyệt Chromium di động về đó.

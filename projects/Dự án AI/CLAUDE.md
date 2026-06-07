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
*   **Tương thích Tiếng Việt (Telex/Unicode):**
    *   Luôn ghi rõ tham số `encoding='utf-8'` khi đọc/ghi tệp tin văn bản chứa Tiếng Việt.
    *   Sử dụng mã hóa `encoding='utf-8-sig'` khi kết xuất tệp CSV để tương thích tốt với phần mềm Excel trên Windows.
*   **Xử lý đường dẫn tương thích:**
    *   Bắt buộc bọc mọi đường dẫn tệp/thư mục có chứa khoảng trắng hoặc chữ Tiếng Việt có dấu (như `"C:\...\Dự án AI\"`) trong dấu ngoặc kép đôi `"..."` khi gọi lệnh qua dòng lệnh Shell (CMD/PowerShell).
    *   Luôn sử dụng thư viện `pathlib` hoặc `os.path` để quản lý đường dẫn một cách an toàn.
*   **Đóng gói Portable & Không Admin:**
    *   Ứng dụng phải được thiết kế chạy hoàn toàn trong không gian quyền người dùng (User space), không đòi hỏi hoặc yêu cầu quyền Administrator.
    *   Tối ưu hóa mã nguồn (sử dụng lazy load) để đảm bảo tốc độ khởi động của phần mềm dưới **2 giây**.

---

## 3. Nhật ký sửa sai (Lessons Learned / Do Not Repeat)
*(Vùng ghi nhận các lỗi đã mắc phải và giải pháp xử lý bắt buộc để tránh lặp lại lỗi)*

*   **LỖI 1: Lỗi font chữ Tiếng Việt khi xuất file CSV từ Python mở bằng Excel.**
    *   *SỬA:* Sử dụng mã hóa `encoding='utf-8-sig'` thay vì `utf-8` khi lưu file CSV.
*   **LỖI 2: Lỗi Shell không tìm thấy tệp/thư mục khi đường dẫn chứa ký tự Tiếng Việt có dấu.**
    *   *SỬA:* Luôn bọc đường dẫn trong dấu ngoặc kép đôi `"..."` khi truyền tham số cho các tiến trình con hoặc CLI (như git, python, ffmpeg).
*   **LỖI 3: Thư viện Playwright bị chặn hoặc đòi quyền admin khi cài đặt trình duyệt mặc định.**
    *   *SỬA:* Luôn cấu hình biến môi trường `PLAYWRIGHT_BROWSERS_PATH` trỏ cục bộ về thư mục dự án để tải trình duyệt Chromium di động về đó.

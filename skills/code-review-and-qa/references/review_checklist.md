# Detailed Code Review & QA Checklist

Tài liệu tham khảo chi tiết về bảng kiểm định mã nguồn và kiểm thử chất lượng trước khi bàn giao.

---

## 1. Danh mục Kiểm tra Chi tiết (Comprehensive Checklist)

### 1.1 Tính Đúng đắn & Logic
* [ ] Tất cả các nhánh rẽ (`if / else / switch / match`) đều có nhánh xử lý mặc định an toàn.
* [ ] Không xảy ra lỗi Off-by-one trong các vòng lặp hoặc cắt mảng (slice).
* [ ] Kiểm tra kiểu dữ liệu và giá trị `None` / `null` trước khi truy cập thuộc tính hoặc gọi phương thức.
* [ ] Các hàm bất đồng bộ (`async / await`) được await đúng chỗ, không tạo ra unhandled promise rejections.

### 1.2 Hiệu năng & Tài nguyên
* [ ] Tránh các truy vấn lồng nhau (N+1 queries) hoặc vòng lặp xử lý I/O nặng nề.
* [ ] Sử dụng các cấu trúc dữ liệu tối ưu (`set` thay vì `list` khi tra cứu membership `O(1)` vs `O(n)`).
* [ ] Sử dụng cơ chế nạp chậm (lazy loading) cho các thư viện nặng để giữ thời gian khởi động ứng dụng dưới 2 giây.

### 1.3 Quy chuẩn Kiểm thử (Testing Standards)
* [ ] Mỗi hàm logic cốt lõi đều có unit test tương ứng.
* [ ] Test cases bao phủ cả giá trị hợp lệ, giá trị biên và giá trị không hợp lệ.
* [ ] Không hardcode môi trường cụ thể (đường dẫn tuyệt đối máy cá nhân, cổng cố định) trong file test.

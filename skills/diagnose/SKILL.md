---
name: diagnose
description: "Chẩn đoán lỗi phần mềm từng bước khoa học."
---

# Diagnose Skill (Chẩn đoán lỗi phần mềm khoa học)

Kỹ năng này hướng dẫn trợ lý AI (Anti Gravity) thực hiện chẩn đoán lỗi phần mềm một cách kỷ luật, khoa học theo từng bước rõ ràng, thay vì đoán mò và sửa đổi code ngẫu nhiên (vibe coding).

## 1. Quy trình Chẩn đoán 4 Bước

Khi phát hiện lỗi (lỗi chương trình bị sập, lỗi logic, hoặc log ghi nhận exception):

### Bước 1: Thu thập thông tin lỗi (Information Gathering)
*   Đọc kỹ log lỗi (stack trace).
*   Xác định chính xác tệp tin, lớp, hoặc dòng code gây ra lỗi.
*   Hiểu rõ hành vi mong muốn ban đầu so với lỗi thực tế xảy ra.

### Bước 2: Đặt giả định (Hypothesis Generation)
*   Trước khi sửa bất kỳ dòng code nào, tôi bắt buộc phải viết ra ít nhất **2 đến 3 nguyên nhân tiềm ẩn** (giả định) có thể gây ra lỗi này.
*   *Ví dụ giả định:*
    *   *Giả định A:* Thư viện `win32com.client` không thể kết nối SAP GUI do phần mềm SAP chưa mở.
    *   *Giả định B:* Đường dẫn thư mục `Dự án AI` bị lỗi mã hóa Unicode tiếng Việt trên shell Windows khiến tệp tin không tồn tại.

### Bước 3: Điều tra & Xác minh (Investigation & Verification)
*   Chạy các lệnh kiểm tra nhỏ hoặc thêm code in debug tạm thời để chứng minh/bác bỏ từng giả định một.
*   Không được sửa code chính thức ở bước này. Chỉ tập trung tìm xem giả định nào là đúng.

### Bước 4: Khắc phục & Chạy thử lại (Resolution & Retesting)
*   Sau khi xác minh được nguyên nhân chính xác, tiến hành sửa đổi code (chỉ sửa đúng chỗ gây lỗi).
*   Chạy thử nghiệm lại sản phẩm ngay lập tức để xác nhận lỗi đã biến mất hoàn toàn.
*   Tự động cập nhật tệp `development_log.csv` về sửa đổi này.

## 2. Các Quy tắc an toàn khi sửa lỗi
*   **Không sửa nhiều lỗi cùng lúc:** Giải quyết từng lỗi một. Sửa một lỗi, chạy thử thành công, rồi mới chuyển sang lỗi tiếp theo.
*   **Bảo toàn log gốc:** Luôn chụp lại hoặc lưu trữ lại thông báo lỗi ban đầu để so sánh sau khi sửa.
*   **Tối giản hóa code sửa:** Phương án sửa lỗi tốt nhất là phương án thay đổi ít dòng code nhất mà vẫn giải quyết triệt để vấn đề.

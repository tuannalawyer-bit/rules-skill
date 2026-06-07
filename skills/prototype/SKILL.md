---
name: prototype
description: "Xây dựng nhanh phiên bản thô chạy thử (MVP) của phần mềm."
---

# Prototype Skill (Xây dựng bản mẫu nhanh)

Kỹ năng này hướng dẫn trợ lý AI (Anti Gravity) xây dựng nhanh một phiên bản chạy thử thô (Minimum Viable Product - MVP) để kiểm tra tính khả thi của ý tưởng lập trình trước khi đi sâu vào viết toàn bộ dự án phức tạp.

## 1. Mục tiêu của Prototype
*   **Chứng minh tính khả thi:** Trả lời câu hỏi *"Ý tưởng này có thể chạy được thực tế không?"*.
*   **Không cầu kỳ về kiến trúc:** Tập trung vào chức năng cốt lõi (Core functionality), bỏ qua giao diện cầu kỳ (UI), tối ưu hiệu năng hay xử lý lỗi quá phức tạp.
*   **Tốc độ:** Xây dựng nhanh trong thời gian ngắn nhất có thể.

## 2. Quy trình viết Prototype

Khi bắt đầu viết một bản mẫu (ví dụ: một tool cào dữ liệu từ trang web mới hoặc tool tự động hóa một form SAP mới):

1.  **Xác định tính năng cốt lõi duy nhất:**
    *   Ví dụ: Đối với cào web, tính năng cốt lõi là tải được trang và lấy được thẻ HTML chứa dữ liệu. Bỏ qua việc lưu database hay xử lý đa luồng.
    *   Ví dụ: Đối với SAP GUI, tính năng cốt lõi là kết nối thành công và điền thử được 1 trường dữ liệu.
2.  **Viết một tệp script đơn lẻ (`prototype_main.py`):**
    *   Chứa toàn bộ code trong một file để dễ chạy và kiểm thử nhanh.
    *   Sử dụng thư viện tối giản nhất có thể.
3.  **Chạy thử nghiệm và xác minh:**
    *   Chạy script để kiểm tra xem tính năng cốt lõi hoạt động đúng không.
    *   Nếu thành công, trình bày kết quả cho người dùng để xin ý kiến nâng cấp lên dự án chính thức.
    *   Nếu thất bại, sử dụng kỹ năng `diagnose` để phân tích nguyên nhân và điều chỉnh nhanh.

## 3. Chuyển đổi từ Prototype lên Bản chính thức (Production)
Khi bản mẫu hoạt động tốt và được bạn phê duyệt nâng cấp lên bản chính thức:
*   Tái cấu trúc mã nguồn sạch đẹp (sử dụng kỹ năng `data-cleaning-and-formatting` và `reasoning-critic-qa`).
*   Bổ sung cơ chế xử lý lỗi nâng cao, ghi log thời gian thực.
*   Đóng gói thành phiên bản Portable và không yêu cầu quyền Admin theo đúng nguyên tắc hoạt động toàn cục.

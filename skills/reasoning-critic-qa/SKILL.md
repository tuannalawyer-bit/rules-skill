---
name: reasoning-critic-qa
description: "Phản biện giải pháp, phân tích rủi ro, kiểm thử (QA) và tự động sửa lỗi trong các ứng dụng di động & portable."
---

# Reasoning, Critique & QA (Portable Systems)

Kỹ năng này hướng dẫn trợ lý AI (Anti Gravity) áp dụng tư duy phản biện hệ thống, tự đánh giá tính khả thi, phân tích rủi ro và thực hiện quy trình kiểm soát chất lượng (QA) nghiêm ngặt trước khi đề xuất hoặc triển khai mã nguồn.

## 1. Quy trình Phản biện Độc lập (Self-Critique Workflow)

Trước khi đề xuất giải pháp viết code cho người dùng, tôi phải tự chạy bộ câu hỏi thẩm định sau:

1. **Ranh giới Phân quyền (No Admin Rule):**
   - *Câu hỏi:* Giải pháp này có đòi hỏi quyền quản trị viên (Administrator / UAC) khi cài đặt hoặc vận hành không?
   - *Yêu cầu:* Nếu có, tôi phải thiết kế lại giải pháp chạy trong User Space (thư mục User Profile, Local AppData hoặc thư mục dự án cục bộ).
2. **Tính di động (Portability Check):**
   - *Câu hỏi:* Ứng dụng này có phụ thuộc vào bất kỳ tài nguyên hệ thống toàn cục nào không (ví dụ: biến môi trường PATH, registry cụ thể, các phần mềm cài cứng trên ổ C)?
   - *Yêu cầu:* Chuyển đổi mọi tài nguyên thành dạng cục bộ trong thư mục ứng dụng (đường dẫn tương đối) để có thể copy-paste sang máy tính khác là chạy được ngay.
3. **Hiệu năng khởi động (2-Second Limit):**
   - *Câu hỏi:* Thời gian khởi động của ứng dụng khi mở lên có dưới 2 giây không? Các module nặng có đang được tải đồng bộ (synchronous import) ngay lúc đầu không?
   - *Yêu cầu:* Sử dụng cơ chế Lazy Loading (chỉ import khi cần) để tối ưu hóa thời gian mở ứng dụng ban đầu.

## 2. Phân tích Kịch bản Lỗi (Edge Case Analysis)

Đối với mỗi tính năng mới được yêu cầu, tôi phải liệt kê ra ít nhất **3 kịch bản có khả năng gây lỗi** và thiết kế sẵn phương án dự phòng (fallback) trong mã nguồn trước khi bắt đầu code:

*   *Kịch bản lỗi 1 (Môi trường mạng):* Lỗi kết nối, timeout hoặc bị website chặn (Anti-bot).
    *   *Phương án:* Cấu hình timeout hợp lý, thêm cơ chế tự động thử lại (Retry) và xoay vòng User-Agent.
*   *Kịch bản lỗi 2 (Tương tác UI):* SAP GUI phản hồi chậm hoặc Excel bị khóa bởi tiến trình khác.
    *   *Phương án:* Kiểm tra trạng thái tiến trình trước khi kết nối, thêm hàm đợi thông minh thay vì sleep tĩnh.
*   *Kịch bản lỗi 3 (Dữ liệu đầu vào):* File ảnh đầu vào bị mờ, không đúng định dạng, hoặc trống rỗng.
    *   *Phương án:* Thêm validation kiểm tra định dạng và kích thước file, trả về thông báo lỗi chi tiết thay vì để chương trình bị sập.

## 3. Quy trình Kiểm thử & Tự động vá lỗi (QA & Self-Healing)

1. **Tích hợp module log nội bộ (Telemetry):**
   Mọi ứng dụng phải có file ghi log nội bộ (ví dụ: `app_debug.log`) để dễ dàng ghi nhận lỗi thời gian thực (runtime error).
   ```python
   import logging
   logging.basicConfig(
       filename='app_debug.log',
       level=logging.ERROR,
       format='%(asctime)s - %(levelname)s - %(message)s'
   )
   ```
2. **Kiểm thử tự động trước khi bàn giao:**
   - Tôi phải tự chạy thử chương trình sau khi thay đổi (sử dụng python thực thi cục bộ hoặc chạy test script).
   - Kiểm tra log `app_debug.log` để xem có bất kỳ ngoại lệ (Exception) nào xảy ra trong quá trình chạy thử không.
   - **Tự động vá lỗi:** Nếu phát hiện lỗi trong log chạy thử, tôi phải tự phân tích nguyên nhân, sửa đổi code trực tiếp và chạy kiểm thử lại cho tới khi kết quả chạy thử hoàn toàn sạch lỗi rồi mới báo cáo cho người dùng.

## 4. Tinh chỉnh & Làm sạch (Code Cleanup)

Trước khi bàn giao kết quả cuối cùng:
1. Loại bỏ các dòng print/console.log phục vụ quá trình debug tạm thời.
2. Kiểm tra xem có import thư viện nào không sử dụng không và xóa bỏ chúng.
3. Đảm bảo cấu trúc file nhật ký phát triển `development_log.csv` được cập nhật chính xác.

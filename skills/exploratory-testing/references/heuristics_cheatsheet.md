# Heuristics Cheatsheet for Exploratory Testing

Tài liệu tham khảo chuyên sâu về các mô hình Heuristic phục vụ kiểm thử sản phẩm và truy quét lỗi.

---

## 1. Chi tiết Mô hình FEW HICCUPS

Mô hình oracles giúp xác định sự sai khác giữa thực tế phần mềm và tiêu chuẩn kỳ vọng:

| Tiêu chuẩn (Oracle) | Ý nghĩa | Câu hỏi thẩm định khi kiểm thử |
| :--- | :--- | :--- |
| **F - Familiar Problems** | Các lỗi kinh điển thường gặp | Tính năng này có dính các lỗi kinh điển như null-pointer, rò rỉ bộ nhớ, off-by-one không? |
| **E - Explainability** | Tính minh bạch | Khi phần mềm xử lý hoặc báo lỗi, người dùng có hiểu được tại sao không? |
| **W - World** | Sự hòa hợp với thế giới thực | Dữ liệu, múi giờ, tiền tệ, định dạng ngày tháng có phù hợp với thực tế không? |
| **H - History** | Lịch sử phiên bản trước | Tính năng này ở bản cũ chạy bình thường nhưng bản này lại hỏng (Regression)? |
| **I - Image** | Hình ảnh thương hiệu | Giao diện có chuyên nghiệp không, câu chữ có tôn trọng người dùng không? |
| **C - Comparable Products** | Sản phẩm tương đương | Phần mềm đối thủ giải quyết tính năng này mượt hơn ra sao? |
| **C - Claims** | Cam kết tài liệu | Tài liệu mô tả tính năng ghi gì và code thực tế chạy ra sao? |
| **U - User Expectations** | Kỳ vọng người dùng | Người dùng phổ thông sẽ mong đợi điều gì xảy ra tiếp theo? |
| **P - Product** | Tính nhất quán nội bộ | Cùng là nút "Xóa", tại sao trang A có popup xác nhận mà trang B lại xóa ngay? |
| **S - Statutes / Standards** | Quy chuẩn kỹ thuật | Có tuân thủ tiêu chuẩn UTF-8, bảo mật dữ liệu cá nhân, accessibility không? |

---

## 2. Kỹ thuật Phá vỡ Luồng (Negative Testing Scenarios)

1. **Kiểm tra giới hạn ký tự (String Boundaries):**
   - 0 ký tự (chuỗi rỗng).
   - Ký tự trắng (chỉ có spaces, tabs, newlines).
   - Chuỗi dài 1.000, 10.000 ký tự (tràn bộ đệm, vỡ giao diện layout).
   - Chuỗi chứa mã độc / payload đặc biệt: `<script>alert(1)</script>`, `SELECT * FROM`, `../../etc/passwd`, `{"key": null}`.
   - Chuỗi tiếng Việt Telex phức tạp: `nghiêng`, `khuấy`, `thuế xuất khẩu`, emoji đa tầng `👨‍👩‍👧‍👦`.

2. **Kiểm tra số học (Numeric Boundaries):**
   - Giá trị 0, giá trị âm (`-1`, `-999999`).
   - Giá trị cực đại int: `2147483647` (32-bit), `9223372036854775807` (64-bit).
   - Số thập phân có nhiều số sau dấu phẩy: `0.0000001`, `0.3333333333333333`.
   - Lỗi chia cho 0 (Divide by Zero).

3. **Kiểm tra thời gian và phiên làm việc (Time & State):**
   - Đặt múi giờ máy tính sai lệch (UTC vs Local time).
   - Chờ phiên làm việc hết hạn (Session timeout) rồi mới bấm Submit.
   - Chạy 2 tab trình duyệt cùng sửa đổi 1 tài liệu (Concurrent editing).

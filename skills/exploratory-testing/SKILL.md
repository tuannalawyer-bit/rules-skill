---
name: exploratory-testing
description: "Kiểm thử thăm dò sản phẩm (Exploratory Testing), rà soát hành vi bất thường, kịch bản phá bĩnh và phát hiện lỗi tiềm ẩn."
---

# Exploratory Testing & Bug Hunting Skill

Kỹ năng này hướng dẫn trợ lý AI đóng vai trò một Chuyên viên Kiểm thử Thăm dò (Exploratory Tester / QA) cao cấp, chủ động khám phá phần mềm, thử nghiệm các kịch bản người dùng phi truyền thống, tìm kiếm các lỗi không lường trước và đánh giá trải nghiệm thực tế của sản phẩm.

---

## 1. Nguyên lý Kiểm thử Thăm dò (Session-Based Testing - SBTM)

Thay vì chỉ kiểm tra "happy path" (luồng chạy thuận lợi), kỹ năng này áp dụng phương pháp kiểm thử dựa trên mục tiêu phiên (Test Charter):
*   **Khám phá (Explore):** Tìm hiểu các ngóc ngách, luồng nghiệp vụ chưa được kiểm thử trong tính năng hoặc sản phẩm.
*   **Thử thách (Challenge):** Thao tác như một người dùng bất cẩn, người dùng tò mò hoặc kẻ tấn công để tìm điểm yếu của hệ thống.
*   **Ghi nhận (Observe & Record):** Quan sát phản ứng bất thường của hệ thống (giật lag, đơ UI, dữ liệu sai lệch, ngoại lệ ngầm).

---

## 2. Hệ Heuristic Phát hiện Lỗi (FEW HICCUPS)

Áp dụng bộ câu hỏi heuristic để chỉ ra các điểm bất thường và lỗi của sản phẩm:
*   **H - History:** Hành vi hiện tại có khác hoặc suy thoái so với các phiên bản trước không (Regression)?
*   **I - Image:** Giao diện, câu từ, phản hồi có giữ đúng hình ảnh chuyên nghiệp không (lỗi chính tả, vỡ layout, hiển thị code lỗi thô)?
*   **C - Comparable Products:** Tính năng này có kém mượt hoặc khó dùng hơn so với sản phẩm tương đương trên thị trường không?
*   **C - Claims:** Sản phẩm có hoạt động đúng như tài liệu/yêu cầu đã cam kết không?
*   **U - User Expectations:** Người dùng có bị bối rối, thất vọng hoặc gặp cản trở khi thao tác không?
*   **P - Product:** Các phần khác nhau trong cùng một sản phẩm có mâu thuẫn hành vi không?
*   **S - Statutes / Standards:** Có vi phạm các tiêu chuẩn kỹ thuật (REST API chuẩn, HTTP Status, định dạng dữ liệu UTF-8)?

> Chi tiết các mẫu câu hỏi và kỹ thuật cụ thể xem tại [heuristics_cheatsheet.md](references/heuristics_cheatsheet.md).

---

## 3. Các Tuyến Tấn công Tìm Lỗi (Attack Vectors)

Khi kiểm thử một tính năng hoặc màn hình sản phẩm, bắt buộc phải rà soát qua 5 tuyến tấn công sau:

1.  **Biên và Dữ liệu Dị thường (Boundary & Malformed Inputs):**
    *   Chuỗi ký tự cực dài, chuỗi rỗng (`""`), ký tự khoảng trắng dư thừa, ký tự Unicode đặc biệt (tiếng Việt có dấu, emoji, ký tự điều khiển `\x00`, `\r\n`).
    *   Số âm, số thực phân số, số 0, số vượt giới hạn int32/int64.
    *   Tệp tải lên rỗng (0 bytes), tệp sai định dạng (đổi đuôi file), tệp dung lượng cực lớn.

2.  **Trạng thái & Chuỗi Hành động Phi tuần tự (State & Workflow Interruption):**
    *   Bấm nút gửi/submit nhiều lần liên tiếp (Double-click / Rapid submission).
    *   Hủy thao tác giữa chừng hoặc quay lại (Back/Refresh) trong lúc tiến trình đang xử lý.
    *   Mở nhiều tab/tiến trình cùng truy cập và sửa đổi một bản ghi cùng lúc (Concurrency/Race condition).

3.  **Xử lý Ngoại lệ Môi trường (Environmental Faults):**
    *   Mất mạng đột ngột hoặc timeout phản hồi từ API/cơ sở dữ liệu.
    *   Tệp tin hoặc tài nguyên cục bộ bị khóa bởi phần mềm khác (file locking).
    *   Bộ nhớ tạm đầy hoặc đường dẫn không có quyền ghi.

4.  **Kiểm tra tính Toàn vẹn Dữ liệu (Data Integrity):**
    *   Sau khi lưu, cập nhật, xóa: Dữ liệu hiển thị lại có khớp 100% với dữ liệu đã nhập không?
    *   Có xảy ra tình trạng "mất mát dữ liệu ngầm" (silent data loss) mà không hề báo lỗi cho người dùng không?

5.  **Phản hồi Giao diện & Trợ năng (Feedback & UX):**
    *   Khi có lỗi, thông báo lỗi có rõ ràng, hướng dẫn cách khắc phục không (tránh thông báo chung chung "Đã có lỗi xảy ra")?
    *   Có trạng thái tải (Loading state / Spinner) khi tác vụ mất hơn 1 giây không?

---

## 4. Cấu trúc Báo cáo Phiên Kiểm thử Thăm dò (Debrief Report)

Khi hoàn tất phiên kiểm thử một sản phẩm, xuất kết quả theo định dạng:

```markdown
### [BÁO CÁO KIỂM THỬ THĂM DÒ] <Tên sản phẩm / Tính năng>
- **Mục tiêu phiên:** <Mô tả phạm vi kiểm thử>
- **Thời gian thực hiện:** <Thời gian>
- **Môi trường thử nghiệm:** <Hệ điều hành, trình duyệt, phiên bản runtime>

#### 1. Danh sách Lỗi phát hiện (Defects Found)
- [BUG-01] [Mức độ: Cao/Trung bình/Thấp] <Tiêu đề lỗi ngắn gọn>
  - **Kịch bản thao tác:** <Các bước dẫn tới lỗi>
  - **Hiện tượng thực tế:** <Hành vi lỗi ghi nhận được>
  - **Hệ quả rủi ro:** <Ảnh hưởng tới người dùng hoặc hệ thống>

#### 2. Điểm yếu Trải nghiệm & Rủi ro Tiềm ẩn (Observations & Concerns)
- <Liệt kê các điểm chưa mượt, giao diện bất tiện hoặc thiếu sót validation>

#### 3. Kết luận Đánh giá (Pass/Fail Gate)
- **Đánh giá chung:** [Đạt / Cần sửa chữa trước khi phát hành]
- **Khuyến nghị hành động tiếp theo:** <Hướng dẫn cụ thể>
```

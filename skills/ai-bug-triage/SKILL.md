---
name: ai-bug-triage
description: "Phân loại, gom cụm lỗi, đánh giá mức độ nghiêm trọng (P0-P3) và lập báo cáo lỗi (Bug Report) chi tiết chuẩn công nghiệp."
---

# AI Bug Triage & Defect Classification Skill

Kỹ năng này hướng dẫn trợ lý AI vận hành quy trình tiếp nhận, sàng lọc, phân loại mức độ nghiêm trọng và xuất báo cáo lỗi chi tiết theo chuẩn công nghiệp phần mềm khi phát hiện lỗi hoặc tiếp nhận log lỗi từ hệ thống.

---

## 1. Quy trình Sàng lọc Lỗi 4 Bước (Triage Workflow)

1.  **Tiếp nhận & Chuẩn hóa (Ingestion & Sanitization):**
    *   Trích xuất stack trace, mã lỗi (error code), log ngoại lệ (exception) và trạng thái ứng dụng trước khi xảy ra sự cố.
    *   Loại bỏ các thông tin nhạy cảm (mật khẩu, access token, thông tin cá nhân) khỏi log trước khi lập báo cáo.
2.  **Khử trùng lặp & Gom cụm (Clustering & Deduplication):**
    *   Đối chiếu với các lỗi đã biết. Nếu nhiều lỗi có chung stack trace gốc hoặc chung điểm gãy, gom nhóm thành 1 bug duy nhất với danh sách các kịch bản kích hoạt.
3.  **Định mức Độ nghiêm trọng (Severity Assignment):**
    *   Đánh giá tác động thực tế tới trải nghiệm người dùng, tính toàn vẹn dữ liệu và an toàn hệ thống theo thang P0 - P3.
4.  **Tạo Phiếu Báo cáo Lỗi Hành động được (Actionable Bug Report):**
    *   Lập phiếu báo cáo có các bước tái hiện (Steps to Reproduce) rõ ràng để lập trình viên có thể mô phỏng lại lỗi ngay lập tức.

---

## 2. Ma trận Phân loại Mức độ Nghiêm trọng (Severity & Priority)

| Mức độ | Định danh | Tiêu chí đánh giá | Hành động yêu cầu |
| :--- | :--- | :--- | :--- |
| **P0** | **Blocker / Critical** | Ứng dụng bị crash hoàn toàn, mất mát dữ liệu, lỗ hổng bảo mật nghiêm trọng, chặn hoàn toàn luồng chính của sản phẩm (không có phương án thay thế). | Dừng phát hành, xử lý khẩn cấp ngay lập tức. |
| **P1** | **Major / High** | Một tính năng quan trọng bị hỏng, kết quả tính toán sai lệch nặng, nhưng hệ thống vẫn còn chạy được hoặc có đường vòng tạm thời (workaround). | Ưu tiên sửa đổi trong phiên làm việc hiện tại. |
| **P2** | **Normal / Medium** | Lỗi hiển thị, tính năng phụ hoạt động chập chờn, lỗi kiểm tra dữ liệu đầu vào (validation) chưa chặt chẽ, người dùng vẫn hoàn thành được mục tiêu. | Lên lịch khắc phục trong đợt cập nhật tiếp theo. |
| **P3** | **Minor / Trivial** | Lỗi thẩm mỹ, căn chỉnh lề (alignment), sai chính tả câu chữ, micro-animation chưa mượt mà. | Sửa khi có thời gian rảnh (nice-to-have). |

---

## 3. Quy chuẩn Báo cáo Lỗi Chuẩn Công nghiệp

Mỗi lỗi được phát hiện phải được ghi nhận theo cấu trúc chuẩn sau:

```markdown
### [BUG-<ID>] [<Mức độ: P0/P1/P2/P3>] <Tiêu đề mô tả lỗi ngắn gọn, chính xác>

* **Thành phần ảnh hưởng (Component):** <Ví dụ: Module Đăng nhập, API Thanh toán, UI Header>
* **Môi trường ghi nhận (Environment):** <Hệ điều hành, phiên bản phần mềm, trình duyệt/runtime>
* **Tần suất xuất hiện (Reproducibility):** <Luôn luôn (100%) / Thỉnh thoảng (Intermittent) / Chỉ gặp 1 lần>

#### 1. Điều kiện tiên quyết (Prerequisites)
- <Ví dụ: Người dùng chưa đăng nhập, hoặc file đầu vào rỗng>

#### 2. Các bước tái hiện (Steps to Reproduce)
1. Mở tính năng X tại màn hình Y.
2. Nhập dữ liệu: `<giá_trị_thử_nghiệm>`.
3. Bấm nút `<Tên_Nút>`.

#### 3. Kết quả thực tế (Actual Result)
- Ứng dụng báo lỗi: `ZeroDivisionError: division by zero` và giao diện bị đơ không phản hồi.

#### 4. Kết quả mong đợi (Expected Result)
- Ứng dụng hiển thị thông báo validation: "Mẫu số không thể bằng 0, vui lòng nhập lại" và cho phép tiếp tục thao tác.

#### 5. Đính kèm Log & Dấu vết (Logs / Stack Trace)
```text
<Trích dẫn 5-15 dòng log hoặc stack trace liên quan trực tiếp>
```

#### 6. Phân tích Nguyên nhân & Đề xuất Khắc phục (Root Cause & Fix)
* **Nguyên nhân cốt lõi:** Chưa kiểm tra giá trị đầu vào của biến trước khi thực hiện phép chia tại hàm `calculate_ratio()`.
* **Đề xuất khắc phục:** Thêm kiểm tra điều kiện `if divisor == 0: raise CustomValidationError(...)`.
```

> Chi tiết mẫu báo cáo đầy đủ xem tại [bug_report_template.md](references/bug_report_template.md).

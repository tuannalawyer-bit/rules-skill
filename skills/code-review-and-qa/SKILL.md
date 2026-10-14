---
name: code-review-and-qa
description: "Rà soát mã nguồn và kiểm định chất lượng sản phẩm đa trục (Tính đúng đắn, bảo mật, xử lý lỗi biên và chất lượng kiểm thử)."
---

# Code Review & Multi-Axis QA Skill

Kỹ năng này thiết lập một cổng kiểm soát chất lượng (Quality Gate) nghiêm ngặt trước khi hợp nhất mã nguồn, phát hành phiên bản hoặc bàn giao tính năng sản phẩm cho người dùng.

---

## 1. Khi nào Kích hoạt Kỹ năng này?

*   Trước khi bàn giao một tính năng, bản sửa lỗi (bug fix) hoặc refactor code.
*   Khi người dùng yêu cầu rà soát tổng thể mã nguồn hoặc đánh giá chất lượng sản phẩm.
*   Khi cần săn lùng các lỗi ngầm (silent bugs, race conditions, memory leaks, security vulnerabilities).
*   Khi đánh giá độ tin cậy của các bài kiểm thử tự động.

---

## 2. Bốn Trục Kiểm định Chất lượng Cốt lõi (4 Review Axes)

Mỗi lần rà soát sản phẩm/mã nguồn, bắt buộc phải thẩm định qua 4 trục:

### Trục 1: Tính Đúng đắn & Săn Lùng Lỗi (Correctness & Bug Hunting)
- [ ] **Khớp đặc tả (Spec Alignment):** Code có đáp ứng 100% mục tiêu ban đầu không? Có bị sửa lệch yêu cầu không?
- [ ] **Lỗi biên (Edge Cases):** Các trường hợp ranh giới (0, âm, chuỗi rỗng, None/Null/Undefined) có được xử lý an toàn không?
- [ ] **Xung đột luồng (Concurrency & Race Conditions):** Có tình trạng hai tiến trình cùng sửa đổi dữ liệu mà không có cơ chế khóa/đồng bộ không?
- [ ] **Rò rỉ tài nguyên (Resource Leaks):** Các kết nối (file handles, database connections, network sockets, subprocesses) có được đóng trong khối `finally` hoặc `with` context manager không?

### Trục 2: Bảo mật & Gia cố Hệ thống (Security & Hardening)
- [ ] **Lọc dữ liệu đầu vào (Input Sanitization):** Dữ liệu từ người dùng hoặc API bên ngoài có được kiểm duyệt trước khi đưa vào câu lệnh SQL, lệnh shell hoặc hiển thị lên giao diện không?
- [ ] **Quản lý bí mật (Secrets Protection):** Tuyệt đối không chứa hardcoded API key, token, mật khẩu trong mã nguồn.
- [ ] **Nguyên tắc quyền tối thiểu (Least Privilege):** Không đòi hỏi quyền Administrator / root khi không thực sự cần thiết.

### Trục 3: Khả năng Chống chịu & Phục hồi (Resilience & Error Paths)
- [ ] **Không nuốt lỗi âm thầm (No Silent Failures):** Tránh các khối `try...except: pass` hoặc `catch (e) {}` không ghi log và không thông báo.
- [ ] **Chiến lược Timeout & Retry:** Các lời gọi mạng, đọc tệp, hoặc tiến trình phụ có thời gian chờ (timeout) hợp lý để tránh treo ứng dụng vĩnh viễn không?
- [ ] **Phương án dự phòng (Graceful Degradation):** Khi dịch vụ phụ bị lỗi, ứng dụng có tiếp tục chạy các tính năng cơ bản được không?

### Trục 4: Thực chất Kiểm thử (Test Substance Gate)
- [ ] **Chống kiểm thử hình thức (No Hollow Tests):** Loại bỏ các bài test chỉ gọi hàm mà không có câu lệnh `assert`, hoặc các `assert` luôn đúng (`assert True`).
- [ ] **Bao phủ kịch bản thất bại:** Bộ test phải kiểm tra cả kịch bản báo lỗi (Negative Testing) chứ không chỉ chạy kịch bản thành công (Happy Path).
- [ ] **Kiểm thử hồi quy (Regression Test):** Mỗi khi sửa lỗi, phải bổ sung ít nhất một ca kiểm thử mô phỏng lại đúng lỗi đó để đảm bảo lỗi không bao giờ tái xuất hiện.

---

## 3. Thang Phân loại Phát hiện (Finding Severity Taxonomy)

*   **[CRITICAL / P0 - Nguy cấp]:** Lỗ hổng bảo mật, nguy cơ mất dữ liệu, sập hệ thống (crash), hoặc lỗi logic cốt lõi. *Bắt buộc phải sửa ngay lập tức trước khi tiếp tục.*
*   **[WARNING / P1 - Cảnh báo]:** Thiếu kiểm tra lỗi biên, nguy cơ nghẽn hiệu năng (bottleneck/N+1), hoặc thiếu kiểm thử bảo vệ. *Khuyến nghị sửa trước khi bàn giao.*
*   **[NIT / P2 - Góp ý nhỏ]:** Làm sạch code, chuẩn hóa tên biến, bổ sung tài liệu hoặc format chưa chuẩn.

---

## 4. Định dạng Báo cáo Đánh giá (Review Output Format)

```markdown
### [BÁO CÁO REVIEW & QA CHẤT LƯỢNG]

#### 1. Đánh giá Theo Trục (Status per Axis)
* **Tính đúng đắn (Correctness):** [PASS / CONDITIONAL / FAIL]
* **Bảo mật (Security):** [PASS / FAIL]
* **Khả năng chịu lỗi (Resilience):** [PASS / WARNING]
* **Chất lượng kiểm thử (Test Substance):** [PASS / WARNING / FAIL]

#### 2. Các Vấn đề Cần Khắc phục (Actionable Findings)
- **[CRITICAL]** `src/module.py#L42`: <Mô tả lỗi cụ thể và rủi ro>
  - *Đề xuất sửa:* `<Mã nguồn hoặc hướng xử lý>`
- **[WARNING]** `src/api.py#L88`: <Mô tả trường hợp biên chưa được kiểm soát>
  - *Đề xuất sửa:* `<Mã nguồn hoặc hướng xử lý>`

#### 3. Kết luận Cuối cùng (Verdict)
- **Quyết định:** [ACCEPT (Chấp thuận) / CHANGES_REQUESTED (Yêu cầu chỉnh sửa)]
```

> Tham khảo bảng checklist chi tiết tại [review_checklist.md](references/review_checklist.md).

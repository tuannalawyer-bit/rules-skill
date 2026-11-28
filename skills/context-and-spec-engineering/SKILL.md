---
name: context-and-spec-engineering
description: "Kỹ thuật đặc tả ràng buộc (Spec-Driven), quản lý ngữ cảnh (Context Engineering) và bảo toàn kiến trúc (Hyrum's Law, Chesterton's Fence) chắt lọc từ Addy Osmani Agent Skills & Superpowers."
---

# Context & Spec Engineering Skill

Kỹ năng này chuẩn hóa giai đoạn **Define → Context Prep → Architectural Safety** trước khi triển khai các tính năng phức tạp hoặc refactor hệ thống lớn, giúp loại bỏ tình trạng AI đoán mò hoặc phá vỡ hợp đồng (contract) hiện có.

---

## 1. Khi nào Kích hoạt?
* Khi nhận yêu cầu xây dựng tính năng mới có nhiều ràng buộc hoặc ảnh hưởng chéo nhiều module.
* Khi chuẩn bị refactor, xóa bỏ code cũ hoặc chia nhỏ tác vụ cho nhiều subagent (`invoke_subagent`).
* Kết hợp tự nhiên sau bước phỏng vấn `grill-me` và trước bước `code-review-and-qa`.

---

## 2. Nguyên tắc Đặc tả & Ràng buộc (Spec & Constraint-Driven)
Trước khi viết code, phải chốt 3 phần ngắn gọn:
1. **Inputs / Outputs & Contract:** Định dạng dữ liệu vào/ra, mã lỗi, và bất biến (invariants) không được vi phạm.
2. **Non-Goals (Ngoài phạm vi):** Liệt kê rõ những gì **không** làm trong đợt này để ngăn AI tự ý mở rộng phạm vi (scope creep).
3. **Acceptance Criteria:** Các điều kiện kiểm thử cụ thể (Happy Path & Edge Cases) để chứng minh hoàn thành.

---

## 3. Nguyên tắc Bảo toàn Kiến trúc (Architectural Guardrails)
* **Chesterton's Fence:** Tuyệt đối **không** xóa hoặc thay đổi một đoạn code, cấu hình hay nhánh `if` có vẻ "dư thừa" nếu chưa xác định được lý do lịch sử tại sao nó tồn tại (hãy kiểm tra call sites, git blame hoặc hỏi người dùng).
* **Hyrum's Law:** Mọi hành vi quan sát được của một API/script (kể cả định dạng log, thứ tự cột CSV, mã thoát exit code) đều có thể đang được người dùng hoặc script khác phụ thuộc. Không tự ý thay đổi hành vi mặc định khi chưa có lộ trình migration.
* **Clarity over Cleverness:** Ưu tiên mã nguồn dễ đọc, tường minh hơn là các thủ thuật viết tắt khó hiểu.

---

## 4. Quản lý Ngữ cảnh cho Subagent (Context Engineering)
* **Minimum Viable Context:** Chỉ truyền cho subagent đúng đường dẫn file, symbol và ràng buộc liên quan; tránh nhồi toàn bộ lịch sử hội thoại.
* **File-based Handoff:** Với tác vụ nhiều bước, lưu đặc tả hoặc kết quả trung gian ra file/artifact để các bước sau đọc lại chính xác, không dựa vào trí nhớ hội thoại.

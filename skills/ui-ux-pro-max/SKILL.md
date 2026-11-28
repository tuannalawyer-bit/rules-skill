---
name: ui-ux-pro-max
description: "Công cụ tra cứu Design Intelligence cục bộ (BM25 search cho bảng màu, typography, layout, chart, accessibility) được tối ưu để bổ trợ và không xung đột với các design system nội bộ."
---

# UI/UX Pro Max (Design Intelligence Search — Trimmed)

Kỹ năng này cung cấp bộ máy tìm kiếm cục bộ (`scripts/search.py` + `data/`) giúp tra cứu nhanh các nguyên tắc thiết kế, cặp font chữ, bảng màu, biểu đồ và chuẩn tiếp cận (a11y) bằng Python chuẩn mà không cần cài thêm thư viện ngoài.

---

## 1. Quy tắc Ưu tiên Bắt buộc (Tránh xung đột Brand)
Trước khi chạy tra cứu hoặc áp dụng style từ kỹ năng này, bắt buộc kiểm tra ngữ cảnh dự án:
1. **Nếu là dự án WinCommerce:** Bắt buộc ưu tiên tuyệt đối `wincommerce-luminous-liquid-glass`.
2. **Nếu người dùng yêu cầu phong cách Vịnh Ngọc:** Bắt buộc ưu tiên tuyệt đối `vinh-ngoc-ui`.
3. **Nếu cần thư viện 480 UI components sẵn có:** Ưu tiên `lucian-uxui` hoặc `adaptive-product-ui` / `premium-ui-assets`.
4. **Khi nào dùng `ui-ux-pro-max`:** Dùng cho các ứng dụng web/landing page/dashboard độc lập chưa có brand token cố định, hoặc chỉ dùng để tra cứu bổ trợ về **typography, chart type, UX checklist, W3C design tokens**.

---

## 2. Cách Chạy Tra cứu Cục bộ
Sử dụng `search.py` (hỗ trợ UTF-8 trên Windows) để lấy gợi ý chính xác trước khi viết giao diện:

```powershell
# Tra cứu theo ngữ cảnh sản phẩm / phong cách
python "d:\Tool\AI\rule & skill\skills\ui-ux-pro-max\scripts\search.py" "saas analytics dashboard" --design-system -p "TenDuAn"

# Tra cứu theo domain cụ thể (style, color, typography, chart, ux, landing, product)
python "d:\Tool\AI\rule & skill\skills\ui-ux-pro-max\scripts\search.py" "glassmorphism dark" --domain style --max-results 3

# Xuất Design Tokens dạng CSS hoặc W3C DTCG JSON
python "d:\Tool\AI\rule & skill\skills\ui-ux-pro-max\scripts\search.py" "fintech dashboard" --design-system --tokens css
```

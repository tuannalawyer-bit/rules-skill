---
name: graphify
description: "Quét mã nguồn, tài liệu và cấu hình dự án thành bản đồ tri thức (Knowledge Graph) bằng AST Tree-sitter cục bộ để AI hiểu kiến trúc nhanh và tiết kiệm token."
---

# Graphify Knowledge Graph Skill

Kỹ năng này sử dụng công cụ CLI `graphify` (đã cài ở user-space qua `uv`) để biến mã nguồn, tài liệu Markdown, SQL, JSON, hình ảnh của một dự án thành **Knowledge Graph** truy vấn được, thay vì để AI tốn hàng chục nghìn token đọc lại từng file thủ công.

---

## 1. Khi nào Kích hoạt?
* Khi bắt đầu làm việc trên một repository lạ hoặc dự án có nhiều thư mục/module phụ thuộc chéo.
* Khi cần truy vết quan hệ gọi hàm (call hierarchy), phụ thuộc import hoặc bản đồ kiến trúc tổng thể.
* Khi người dùng gọi `/graphify` hoặc yêu cầu lập bản đồ tri thức dự án.

---

## 2. Quy trình Sử dụng Chuẩn
1. **Kiểm tra công cụ:** Đảm bảo thư mục user-space (`%USERPROFILE%\.local\bin`) nằm trong `PATH` và chạy:
   ```powershell
   graphify "<đường-dẫn-dự-án>"
   ```
   *(Lưu ý: Luôn bọc đường dẫn chứa khoảng trắng hoặc tiếng Việt trong dấu ngoặc kép `"..."`)*
2. **Đọc kết quả đồ thị:** Công cụ xuất ra thư mục `graphify-out/` (gồm báo cáo kiến trúc `GRAPH_REPORT.md` và dữ liệu đồ thị `graph.json`). Hãy đọc `GRAPH_REPORT.md` trước để nắm các cụm module (communities) và điểm nút trung tâm (god nodes).
3. **Bảo vệ Git sạch sẽ:** Nếu dự án chưa muốn commit cache đồ thị lên Git, hãy kiểm tra `.gitignore` và thêm `graphify-out/` trước khi kết thúc phiên.

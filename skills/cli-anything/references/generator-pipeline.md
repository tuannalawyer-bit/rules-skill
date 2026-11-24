# Quy trình 7 Bước Tự Động Sinh CLI Wrapper (Generator Pipeline)

Khi cần tích hợp một phần mềm hoặc thư viện nội bộ mới chưa có sẵn trong CLI-Hub, CLI-Anything cung cấp pipeline 7 bước tự động hóa chuyển đổi mã nguồn thành một CLI hoàn chỉnh chuẩn Agent-Native.

---

## 7 Giai đoạn trong Pipeline

### Giai đoạn 1: Phân tích mã nguồn (Analyze Codebase)
* Quét toàn bộ repository hoặc cấu trúc thư mục của ứng dụng.
* Phân tích các API nội bộ, các hàm export, các module headless hoặc scripting binding (ví dụ: Python bindings, C++ exports, REST/RPC endpoints).
* Lập bản đồ liên kết từ tính năng người dùng sang các hàm thực thi cốt lõi.

### Giai đoạn 2: Thiết kế kiến trúc CLI (Design CLI Layout)
* Xác định các nhóm lệnh (`command groups`) tương ứng với phân hệ tính năng (ví dụ: `project`, `layer`, `filter`, `export`).
* Thiết kế mô hình dữ liệu biểu diễn trạng thái ứng dụng (State Model) dưới dạng JSON.
* Chuẩn hóa danh sách cờ tham số (Flags & Options).

### Giai đoạn 3: Hiện thực hóa mã nguồn (Implement Harness)
Xây dựng CLI bằng Python (thường dùng thư viện `Click`):
* **Bắt buộc hỗ trợ cờ `--json`**:
  ```python
  if json_mode:
      click.echo(json.dumps(result, indent=2))
  else:
      click.echo(format_human_readable(result))
  ```
* **Quản lý trạng thái (State & Session Management)**:
  Lưu trữ lịch sử thay đổi vào tệp dự án JSON để cho phép `undo`, `redo` và hoàn tác tác vụ khi gặp lỗi.
* **Chế độ REPL tương tác**:
  Duy trì kết nối tiến trình nền nhằm tránh chi phí khởi động lại phần mềm ở mỗi bước gọi lệnh.

### Giai đoạn 4: Lập kế hoạch kiểm thử (Plan Tests - `TEST.md`)
* Sinh tài liệu `TEST.md` chi tiết liệt kê các ca kiểm thử:
  * Ca kiểm thử thành công (Happy path).
  * Ca kiểm thử xử lý dữ liệu sai và lỗi biên (Edge cases & validation).
  * Kiểm thử toàn vẹn dữ liệu JSON đầu ra.

### Giai đoạn 5: Viết bộ kiểm thử tự động (Write Tests)
* Triển khai bộ kiểm thử tự động toàn diện bằng `pytest`.
* Giả lập hoặc kích hoạt engine phần mềm thật để đảm bảo mọi lệnh đều trả về mã thoát hợp lệ (`exit code 0`).

### Giai đoạn 6: Xác minh & Chạy kiểm thử (Verify Execution)
* Chạy kiểm thử tự động cục bộ:
  ```powershell
  pytest tests/ -v
  ```
* Chỉ khi 100% ca kiểm thử vượt qua thành công mới tiến hành đóng gói.

### Giai đoạn 7: Sinh tài liệu chuẩn Agent (`SKILL.md`)
* Tự động sinh tệp `SKILL.md` chứa:
  * YAML Frontmatter chuẩn (`name`, `description`).
  * Danh mục lệnh và tham số chi tiết.
  * Lệnh trích xuất schema động (`cli-anything-<app> schema`).
  * Ví dụ mẫu theo phong cách Prompt-Engineering cho AI Agent.

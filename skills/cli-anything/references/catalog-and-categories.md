# Danh mục 103+ Công cụ trong CLI-Hub

CLI-Hub cung cấp hơn 100 công cụ dòng lệnh được tối ưu hóa cho AI Agent (Agent-Native), chia thành 35 danh mục chuyên môn. Mỗi công cụ đều có tài liệu `SKILL.md` và mã schema tự mô tả.

---

## 1. 3D & Mô hình hóa Không gian (3D & CAD)
* **`blender`**: Mô hình hóa 3D, dựng hoạt cảnh và kết xuất đồ họa (render) qua chế độ `blender --background` với các lệnh Python nội bộ (`bpy`).
* **`freecad`**: Thiết kế cơ khí và mô hình CAD tham số 3D với hơn 258 lệnh CLI.
* **`meerk40t`**: Điều khiển và tự động hóa máy cắt/khắc laser thông qua nhân MeerK40t.

## 2. Trí tuệ Nhân tạo & LLM (AI)
* **`comfyui`**: Quản lý và thực thi đồ thị sinh ảnh/video AI qua REST API của ComfyUI.
* **`dify-workflow`**: Chỉnh sửa và vận hành quy trình tự động hóa DSL trên nền tảng Dify.
* **`generate-veo-video`**: Công cụ CLI sinh video bằng Google Veo 3.1 qua Vertex AI.
* **`jimeng`**: CLI chính thức của ByteDance phục vụ tạo ảnh và video AI.
* **`magnific`**: Harness kết nối điều khiển công cụ phóng to/nâng cấp ảnh AI Magnific.
* **`minimax` / `minimax-cli`**: Quản lý API thoại, Text-to-Speech và chat của MiniMax.
* **`notebooklm`**: Scaffold tự động hóa tài liệu nghiên cứu qua NotebookLM.
* **`novita`**: Gọi suy luận các mô hình AI mã nguồn mở qua API chuẩn OpenAI của Novita.
* **`ollama`**: Quản lý và chạy suy luận mô hình ngôn ngữ lớn (LLM) cục bộ trên máy tính.
* **`openwebui`**: Tương tác và điều khiển backend OpenWebUI cho AI Agent.
* **`vivideo`**: CLI sinh video AI, avatar ảo từ văn bản.

## 3. Âm thanh & Xử lý Giọng nói (Audio)
* **`audacity`**: Xử lý, lọc tạp âm và hiệu chỉnh âm thanh hàng loạt qua nhân SoX.
* **`elevenlabs`**: Quản lý giọng nói nhân tạo và voice agent qua ElevenLabs CLI.
* **`wavetone`**: Xử lý và chuẩn bị dữ liệu phiên âm âm thanh.

## 4. Tự động hóa Quy trình (Automation)
* **`eez-studio`**: Tự động hóa dự án EEZ Studio, giao diện LVGL và lệnh SCPI.
* **`macrocli`**: Chuyển đổi các luồng thao tác GUI phức tạp thành macro dòng lệnh phân lớp.
* **`n8n`**: Quản lý và kích hoạt các workflow tự động hóa n8n qua REST API (hơn 55 lệnh).

## 5. Truyền thông & Mạng xã hội (Communication)
* **`feishu`**: CLI chính thức của Lark/Feishu để quản lý bot, tin nhắn và lịch làm việc.
* **`wecom`**: Tự động hóa liên lạc và tác vụ doanh nghiệp WeCom.
* **`ve-twini` / `x-twitter-scraper`**: Truy vấn GraphQL API, tìm kiếm và trích xuất dữ liệu Twitter/X.
* **`zoom`**: Quản lý cuộc họp và người tham gia qua Zoom REST API (OAuth2).

## 6. Khoa học Dữ liệu & Cơ sở dữ liệu (Data & Databases)
* **`chromadb`**: Thao tác vector database: quản lý collection, nhúng tài liệu, tìm kiếm tương đồng.
* **`openrefine`**: Nhập, làm sạch và áp dụng lịch sử biến đổi dữ liệu tabular qua OpenRefine.
* **`py4csr`**: Harness tuân chuẩn GxP phục vụ phân tích báo cáo nghiên cứu lâm sàng CDISC.

## 7. Thiết kế & Đồ họa (Design & Graphics)
* **`gimp`**: Xử lý đồ họa raster chuyên sâu thông qua chế độ batch script (`gimp -i -b`).
* **`inkscape`**: Biên tập đồ họa vector SVG và xuất định dạng qua `inkscape --export-filename`.
* **`krita`**: Thao tác vẽ kỹ thuật số và chỉnh sửa ảnh qua Krita CLI.
* **`sketch`**: Tạo và chỉnh sửa tệp thiết kế `.sketch` từ định dạng JSON.
* **`inkstitch`**: Số hóa mẫu thêu máy công nghiệp và kiểm tra đường chỉ thêu.
* **`cloudcompare`**: Xử lý đám mây điểm 3D và lưới đa giác (Point cloud & Mesh).

## 8. Văn phòng & Quản lý Tri thức (Office & Knowledge)
* **`libreoffice`**: Tạo, chỉnh sửa tài liệu ODF và chuyển đổi tài liệu hàng loạt sang PDF/DOCX/XLSX/PPTX.
* **`zotero`**: Tích hợp CLI & MCP cho Zotero 7/8 với hơn 52 công cụ MCP và 70+ lệnh CLI.
* **`calibre`**: Quản lý thư viện sách điện tử: chuyển đổi định dạng, sửa metadata, tìm kiếm.
* **`obsidian` / `obsidian-cli` / `obsidian-agent-cli`**: Quản lý kho ghi chú Obsidian, canvas và liên kết tri thức.
* **`joplin`**: Tự động hóa ghi chú và to-do list qua Joplin Data API.
* **`siyuan`**: Quản lý khối tri thức qua HTTP API của SiYuan.

## 9. Biên tập Video & Streaming (Video & Streaming)
* **`kdenlive` / `shotcut`**: Dựng và xuất video tự động qua MLT Media Lovin' Toolkit và FFmpeg.
* **`obs-studio`**: Quản lý scene, nguồn âm thanh/hình ảnh và kích hoạt livestream/ghi hình trên OBS Studio.
* **`openscreen`**: Biên tập video quay màn hình: zoom thông minh, tạo hiệu ứng speed ramp, cắt cúp.
* **`videocaptioner`**: Tự động nhận dạng tiếng nói, tối ưu hóa và gắn phụ đề vào video.

## 10. Trình duyệt & Tương tác Web (Web)
* **`browser`**: Tự động hóa trình duyệt qua DOMShell MCP server, ánh xạ DOM thành các lệnh CLI.
* **`browser-cdp`**: Điều khiển trình duyệt thông qua giao thức Chrome DevTools Protocol (CDP) gốc.
* **`clibrowser`**: Trình duyệt dòng lệnh phi phụ thuộc (zero-dependency) tối ưu cho AI Agent.
* **`shopify`**: CLI chính thức quản lý app, giao diện và sản phẩm Shopify.
* **`mailchimp`**: Quản lý chiến dịch email marketing và danh sách độc giả qua Mailchimp API v3.

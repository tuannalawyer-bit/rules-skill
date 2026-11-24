---
name: cli-anything
description: "Điều khiển và tự động hóa phần mềm desktop, ứng dụng đồ họa và sáng tạo (Blender, GIMP, Inkscape, LibreOffice, Kdenlive, OBS, FreeCAD, Zotero,...) dưới dạng Agent-Native CLI qua CLI-Anything & CLI-Hub. Tự động tìm kiếm, cài đặt công cụ CLI wrapper, thực thi lệnh dạng JSON và quản lý workflow không phụ thuộc GUI."
---

# CLI-Anything (HKUDS) - Tự động hóa Phần mềm Desktop chuẩn Agent-Native

Kỹ năng này hướng dẫn trợ lý AI (Antigravity / Gemini / Claude) điều khiển, vận hành và tự động hóa các phần mềm desktop phức tạp (sáng tạo 3D, xử lý ảnh raster/vector, dựng video, tự động hóa văn phòng, biên tập âm thanh, nghiên cứu khoa học) thông qua kiến trúc **Agent-Native CLI** từ dự án **CLI-Anything** (Data Intelligence Lab - HKUDS).

Thay vì phụ thuộc vào thị giác máy tính (VLM Computer Use) với chi phí token cao và độ trễ lớn, CLI-Anything chuyển đổi các phần mềm desktop thành các giao diện dòng lệnh (CLI) có cấu trúc, trả về dữ liệu JSON, hỗ trợ quản lý trạng thái (`undo`/`redo`) và tự động hóa đa công cụ.

---

## 1. Vòng lặp làm việc chuẩn: Khám phá - Cài đặt - Thực thi (Discover - Install - Execute)

```
[1. cli-hub search / matrix] ───> [2. cli-hub install] ───> [3. cli-anything-<app> --json] ───> [4. Verify & Next]
```

### Bước 1: Khám phá công cụ (Discover)
Khi nhận một tác vụ phức tạp liên quan đến phần mềm chuyên dụng, AI Agent tìm kiếm công cụ phù hợp trong hơn 103+ phần mềm có sẵn:

```powershell
# Tìm kiếm công cụ theo từ khóa
cli-hub search "3d modeling"
cli-hub search "image"
cli-hub search "pdf"

# Xem danh sách các ma trận năng lực phối hợp đa công cụ (Curated Matrices)
cli-hub matrix list

# Xem chi tiết cấu hình và tiền điều kiện của một công cụ
cli-hub info blender
cli-hub info gimp
cli-hub info libreoffice
```

### Bước 2: Cài đặt công cụ (Install)
Cài đặt wrapper harness tự động cho phần mềm mong muốn:

```powershell
# Cài đặt CLI wrapper
cli-hub install gimp
cli-hub install blender
cli-hub install libreoffice

# Hoặc cài đặt nguyên một ma trận năng lực (ví dụ xử lý hình ảnh, video)
cli-hub matrix install image-design
```

> [!NOTE] 
> Nhiều phần mềm yêu cầu máy tính đã cài đặt sẵn engine phần mềm gốc (ví dụ: Blender, GIMP, LibreOffice, Inkscape). Công cụ `cli-hub info <app>` sẽ hiển thị rõ tiền điều kiện trong trường `Requires:`.

### Bước 3: Thực thi tác vụ chuẩn Agent-Native (Execute)
Mỗi công cụ được sinh ra tuân thủ nghiêm ngặt các quy tắc Agent-Native:
1. **Luôn sử dụng cờ `--json`**: Đảm bảo phản hồi trả về là đối tượng JSON có cấu trúc giúp AI phân tích kết quả chính xác, không dùng regex hay đoán text.
2. **Khám phá schema động (`schema`)**: Khi chưa biết rõ các lệnh con, Agent truy vấn schema để đọc toàn bộ capability map:
   ```powershell
   cli-anything-gimp schema
   cli-anything-blender schema
   ```
3. **Quản lý trạng thái (State & Undo/Redo)**: Tận dụng cơ chế project session để khôi phục hoặc hoàn tác:
   ```powershell
   # Tạo project mới
   cli-anything-gimp project new --width 1920 --height 1080 -o canvas.json --json

   # Thêm layer và áp bộ lọc
   cli-anything-gimp layer add --project canvas.json --name "Background" --color "#FFFFFF" --json
   cli-anything-gimp filter apply --project canvas.json --filter gaussian-blur --radius 5 --json

   # Hoàn tác nếu bước trước chưa đạt yêu cầu
   cli-anything-gimp project undo --project canvas.json --json
   ```

---

## 2. Hệ sinh thái 103+ Công cụ theo 35 Danh mục

CLI-Hub phân loại các công cụ thành các nhóm năng lực chính:

| Nhóm lĩnh vực | Công cụ tiêu biểu trong Hub | Mô tả năng lực chính |
| :--- | :--- | :--- |
| **3D & CAD** | `blender`, `freecad`, `meerk40t` | Dựng hình 3D, render headless, mô hình CAD tham số, cắt laser. |
| **Đồ họa & Ảnh** | `gimp`, `inkscape`, `krita`, `sketch` | Xử lý ảnh raster hàng loạt qua batch engine, đồ họa vector SVG, vẽ kỹ thuật số. |
| **Video & Streaming**| `kdenlive`, `shotcut`, `obs-studio`, `openscreen` | Cắt ghép video qua Melt/FFmpeg, điều khiển scene quay phát OBS Studio. |
| **Văn phòng & Tri thức**| `libreoffice`, `zotero`, `obsidian`, `calibre` | Xuất tài liệu PDF/DOCX/ODF, quản lý trích dẫn nghiên cứu, kho tri thức cá nhân. |
| **Âm thanh & Âm nhạc** | `audacity`, `musescore`, `wavetone`, `elevenlabs` | Xử lý audio qua SoX, ký âm chuyển giọng nốt nhạc, Text-to-Speech API. |
| **Tự động hóa & Web** | `n8n`, `browser`, `browser-cdp`, `shopify`, `mailchimp` | Điều khiển workflow n8n, cào web qua CDP, quản lý sàn thương mại điện tử. |
| **AI & LLM Client** | `comfyui`, `ollama`, `openwebui`, `minimax`, `novita` | Kích hoạt pipeline sinh ảnh ComfyUI, quản lý model LLM cục bộ. |

> Xem danh mục chi tiết tại [catalog-and-categories.md](file:///skills/cli-anything/references/catalog-and-categories.md).

---

## 3. Các Ma trận Năng lực Phối hợp Đa công cụ (Curated Matrices)

Khi giải quyết các tác vụ phức tạp có tính chất đa bước (end-to-end), sử dụng các ma trận chuyên đề (`cli-hub matrix`):

* **`S1: video-creation`** (14 CLIs): Kết hợp kịch bản, âm thanh (Audacity, Suno), hình ảnh (ComfyUI) và dựng video (Kdenlive/Shotcut/OpenScreen).
* **`S2: knowledge-research`** (13 CLIs): Thu thập tài liệu khoa học, trích dẫn (Zotero), ghi chú (Obsidian, Joplin) và xuất báo cáo (LibreOffice).
* **`S3: 3d-cad`** (6 CLIs): Thiết kế mô hình kỹ thuật (FreeCAD), điêu khắc và kết xuất hoạt cảnh (Blender).
* **`S4: game-development`** (9 CLIs): Quản lý tài nguyên, xuất asset và biên soạn màn chơi (Godot, s&box, RenderDoc).
* **`S5: image-design`** (7 CLIs): Thiết kế đồ họa đa lớp kết hợp vector (Inkscape) và xử lý hiệu ứng raster (GIMP, Krita).

> Xem chi tiết ma trận tại [curated-matrices.md](file:///skills/cli-anything/references/curated-matrices.md).

---

## 4. Phối hợp giữa CLI-Anything và Agent-Desktop

Trong môi trường Antigravity, việc tự động hóa desktop đạt hiệu quả cao nhất khi kết hợp linh hoạt hai kỹ năng:

```
                  ┌────────────────────────────────────────┐
                  │ Tác vụ tự động hóa ứng dụng Desktop    │
                  └──────────────────┬─────────────────────┘
                                     │
                 Phần mềm có Engine / API / CLI-Hub?
                     ┌───────────────┴───────────────┐
                    CÓ                              KHÔNG
                     │                               │
        ┌────────────▼─────────────┐   ┌─────────────▼─────────────┐
        │       cli-anything       │   │       agent-desktop       │
        │ - Xử lý ngầm (Headless)  │   │ - Phần mềm đóng (closed)  │
        │ - Chạy hàng loạt (Batch) │   │ - Thao tác trực tiếp GUI  │
        │ - Dữ liệu JSON chuẩn xác │   │ - Cây Accessibility (UIA) │
        │ - Tiết kiệm tối đa token │   │ - Click/Gõ theo @ref      │
        └──────────────────────────┘   └───────────────────────────┘
```

* **Ưu tiên `cli-anything`**: Khi ứng dụng có trong CLI-Hub (Blender, GIMP, LibreOffice, OBS,...) hoặc cần chạy tác vụ nền, render số lượng lớn, không muốn làm phiền màn hình người dùng.
* **Sử dụng `agent-desktop`**: Khi ứng dụng là phần mềm độc quyền nội bộ, phần mềm doanh nghiệp đóng gói kín (ERP, win32 kế toán, giao diện web trong webview tùy chỉnh) không có CLI/API.

---

## 5. Tài liệu tham khảo chi tiết

* [Danh mục 103+ Công cụ CLI-Hub](file:///skills/cli-anything/references/catalog-and-categories.md)
* [5 Ma trận Năng lực Phối hợp Đa công cụ](file:///skills/cli-anything/references/curated-matrices.md)
* [Quy trình 7 bước tạo CLI Wrapper mới](file:///skills/cli-anything/references/generator-pipeline.md)
* [Kịch bản mẫu ứng dụng thực tế](file:///skills/cli-anything/references/agent-workflows.md)

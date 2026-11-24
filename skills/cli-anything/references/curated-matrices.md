# 5 Ma trận Năng lực Phối hợp Đa công cụ (Curated Matrices)

Ma trận năng lực (Curated Matrices) trong CLI-Hub gom nhóm các công cụ có tính bổ trợ cao nhằm giải quyết trọn vẹn một quy trình sản xuất (end-to-end workflow) từ khâu ý tưởng đến thành phẩm.

Xem danh sách ma trận trên hệ thống:
```powershell
cli-hub matrix list
```

---

## Ma trận S1: video-creation (Sản xuất Video Toàn diện)
Bao gồm 14 công cụ chuyên sâu từ lên kịch bản, tạo tài nguyên đến dựng và xuất video:

| Công cụ | Vai trò trong quy trình |
| :--- | :--- |
| **`comfyui`** / **`jimeng`** | Sinh hình ảnh phân cảnh (storyboard) và khung hình mẫu. |
| **`generate-veo-video`** / **`vivideo`** | Sinh chuyển động và clip video ngắn bằng AI. |
| **`audacity`** | Thu âm, khử ồn và tinh chỉnh giọng đọc/âm thanh nền. |
| **`elevenlabs`** / **`suno`** | Sinh lời bình thuyết minh AI (TTS) và nhạc nền tự động. |
| **`kdenlive`** / **`shotcut`** | Dựng phim đa rãnh, ghép âm thanh, áp hiệu ứng chuyển cảnh. |
| **`openscreen`** | Chèn các đoạn quay màn hình hướng dẫn kèm hiệu ứng zoom mượt. |
| **`videocaptioner`** | Tạo phụ đề tự động (Auto-transcription) và gắn vietsub/hardsub. |

Lệnh cài đặt toàn bộ ma trận:
```powershell
cli-hub matrix install video-creation
```

---

## Ma trận S2: knowledge-research (Nghiên cứu & Biên soạn Tri thức)
Bao gồm 13 công cụ hỗ trợ đọc tài liệu, quản lý trích dẫn và xuất bản báo cáo:

| Công cụ | Vai trò trong quy trình |
| :--- | :--- |
| **`zotero`** | Quản lý kho bài báo khoa học, lấy metadata và trích dẫn theo chuẩn BibTeX/APA. |
| **`obsidian-agent-cli`** / **`joplin`** | Ghi chép tài liệu, lập biểu đồ liên kết tri thức (Knowledge Graph). |
| **`exa`** | Tìm kiếm dữ liệu học thuật và nội dung trực tuyến thông qua AI Search. |
| **`libreoffice`** | Soạn thảo tài liệu ODF, chèn bảng biểu số liệu và xuất ra PDF/DOCX. |
| **`calibre`** | Lưu trữ, lập chỉ mục và chuyển đổi các định dạng sách/báo cáo e-book. |

Lệnh cài đặt:
```powershell
cli-hub matrix install knowledge-research
```

---

## Ma trận S3: 3d-cad (Mô hình hóa & Thiết kế Không gian 3D)
Bao gồm 6 công cụ phục vụ thiết kế kỹ thuật và đồ họa hoạt cảnh 3D:

| Công cụ | Vai trò trong quy trình |
| :--- | :--- |
| **`freecad`** | Thiết kế cơ khí, mô hình tham số chính xác từng milimét. |
| **`blender`** | Điêu khắc (sculpting), gán vật liệu (texturing), chiếu sáng và render hoạt cảnh. |
| **`3mf`** | Kiểm tra lỗi hình học của lưới đa giác (mesh integrity) trước khi in 3D. |
| **`meerk40t`** | Tự động sinh đường cắt laser trên vật liệu. |

Lệnh cài đặt:
```powershell
cli-hub matrix install 3d-cad
```

---

## Ma trận S4: game-development (Phát triển Trò chơi)
Bao gồm 9 công cụ hỗ trợ xây dựng game và tài nguyên đồ họa kỹ thuật số:

| Công cụ | Vai trò trong quy trình |
| :--- | :--- |
| **`godot`** | Quản lý dự án Godot Engine, biên dịch scene, cấu hình physics và xuất game. |
| **`sbox`** | Xây dựng màn chơi trên nền Source 2 engine. |
| **`renderdoc`** | Phân tích frame GPU, trích xuất shader và kiểm tra hiệu năng đồ họa. |
| **`live2d`** | Kiểm tra, gắn xương và xuất hoạt ảnh nhân vật 2D. |

Lệnh cài đặt:
```powershell
cli-hub matrix install game-development
```

---

## Ma trận S5: image-design (Thiết kế Đồ họa & Xử lý Ảnh)
Bao gồm 7 công cụ phục vụ xử lý hình ảnh đa lớp và đồ họa vector:

| Công cụ | Vai trò trong quy trình |
| :--- | :--- |
| **`inkscape`** | Thiết kế logo, icon, sơ đồ biểu tượng dưới dạng vector SVG sắc nét. |
| **`gimp`** | Cắt ghép layer ảnh bitmap, điều chỉnh dải màu, tách nền và áp bộ lọc mờ. |
| **`krita`** | Vẽ minh họa số, tô màu và tạo chất liệu đồ họa đặc thù. |
| **`sketch`** | Xuất layout giao diện và bố cục đồ họa chuẩn mobile/web. |

Lệnh cài đặt:
```powershell
cli-hub matrix install image-design
```

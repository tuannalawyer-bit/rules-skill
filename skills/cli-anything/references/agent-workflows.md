# Kịch bản Mẫu Ứng dụng Thực tế với CLI-Anything

Dưới đây là các kịch bản mẫu minh họa cách AI Agent trong Antigravity phối hợp với các công cụ từ CLI-Hub để tự động hóa công việc.

---

## 1. Xử lý Ảnh Hàng loạt với GIMP (`cli-anything-gimp`)

**Bài toán:** Chuẩn hóa kích thước hàng loạt ảnh sản phẩm về 1080x1080, thêm viền mờ và chèn watermark bản quyền.

```powershell
# 1. Tạo project session
cli-anything-gimp project new --width 1080 --height 1080 -o output_product.json --json

# 2. Nhập ảnh gốc và căn giữa
cli-anything-gimp layer import --project output_product.json --file "raw_product.png" --fit center --json

# 3. Thêm lớp watermark text
cli-anything-gimp text add --project output_product.json --text "© WinCommerce 2026" --font "Segoe UI" --size 24 --color "#888888" --pos "bottom-right" --json

# 4. Xuất ảnh thành phẩm
cli-anything-gimp project export --project output_product.json --format png --quality 95 -o "final_product.png" --json
```

---

## 2. Kết xuất 3D Headless với Blender (`cli-anything-blender`)

**Bài toán:** Nhập file mô hình 3D (.obj / .gltf), thiết lập ánh sáng studio 3 điểm và xuất ảnh render 4K không cần mở GUI Blender.

```powershell
# 1. Tạo cảnh mới (Scene)
cli-anything-blender scene create --name "StudioRender" --resolution 3840x2160 --samples 128 --json

# 2. Nhập mô hình 3D
cli-anything-blender object import --file "assets/gadget.gltf" --scale 1.0 --json

# 3. Thiết lập hệ thống chiếu sáng Studio 3-Point Light
cli-anything-blender light add --type "KEY" --energy 500 --pos "4, -4, 5" --json
cli-anything-blender light add --type "FILL" --energy 200 --pos "-4, -2, 3" --json
cli-anything-blender light add --type "BACK" --energy 300 --pos "0, 5, 4" --json

# 4. Render và lưu ảnh thành phẩm
cli-anything-blender render execute --engine "CYCLES" --device "GPU" -o "renders/gadget_4k.png" --json
```

---

## 3. Tự động hóa Văn bản Báo cáo với LibreOffice (`cli-anything-libreoffice`)

**Bài toán:** Tạo báo cáo tổng kết kinh doanh từ dữ liệu JSON và xuất thành file PDF có chữ ký số.

```powershell
# 1. Khởi tạo tài liệu văn bản từ mẫu template
cli-anything-libreoffice doc create --template "templates/monthly_report.ott" -o "draft_report.odt" --json

# 2. Điền dữ liệu bảng số liệu doanh thu
cli-anything-libreoffice table fill --doc "draft_report.odt" --table-name "RevenueTable" --data "data/q4_sales.json" --json

# 3. Xuất tài liệu ra định dạng PDF chuẩn in ấn
cli-anything-libreoffice doc export --doc "draft_report.odt" --format pdf -o "dist/Bao_Cao_Q4_2026.pdf" --json
```

---

## 4. Điều khiển Phòng Thu và Livestream với OBS Studio (`cli-anything-obs-studio`)

**Bài toán:** Tự động chuyển đổi scene quay bài thuyết trình khi người dùng bắt đầu nói.

```powershell
# 1. Kiểm tra trạng thái kết nối OBS WebSocket
cli-anything-obs-studio status --json

# 2. Chuyển scene sang màn hình chia sẻ kèm camera góc phải
cli-anything-obs-studio scene switch --name "Screen + Camera PIP" --json

# 3. Mở micro và bắt đầu ghi hình
cli-anything-obs-studio audio unmute --source "Mic/Aux" --json
cli-anything-obs-studio record start --json
```

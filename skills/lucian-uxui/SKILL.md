---
name: lucian-uxui
description: "Thư viện 480 thành phần giao diện tương tác không phụ thuộc thư viện (Lucian UX/UI Prompt) chạy chế độ Hybrid Offline-Ready cho Antigravity, hỗ trợ tìm kiếm cục bộ tức thì, port sang React/Next/Vue/Svelte/Astro/HTML và ánh xạ token sang WinCommerce/Vịnh Ngọc."
---

# Lucian UX/UI (Hybrid Offline-Ready)

Thư viện **Lucian UX/UI Prompt** cung cấp **480 thành phần giao diện tương tác không phụ thuộc thư viện ngoài** (HTML + CSS scoped `.uNNN` + Vanilla JS + `--ux-*` Light/Dark tokens), hỗ trợ chuột, chạm, bàn phím (`focus-visible`, ARIA) và `prefers-reduced-motion`.

- **Phạm vi dữ liệu cục bộ**: Snapshot tiếng Anh gồm **480 elements** được đóng gói sẵn trong `data/api/v1/` (ghim từ commit `8749838d` của `Seokwoooo/lucian-uxui-prompt`, bản quyền MIT):
  - **80 Essentials (`#401–480`)**: Đăng nhập Google/Social, Cookie banner, Pricing, FAQ, Checkout, Date picker, Upload và nhóm **AI Patterns (`#451–459`)**.
  - **200 Website Sections & Motion (`#201–400`)**: Hero, Scroll/Text/Data Motion, Social Proof, Commerce & Pricing.
  - **200 Interface Parts (`#001–200`)**: Buttons, Toggles, Inputs, Menus, Cards, Charts, Kanban, Scheduler, Editors, Workflow.

---

## 1. Cách gọi CLI (Node.js 18+, Zero-Dependency)

Luôn bọc đường dẫn trong dấu ngoặc kép `"..."` trên PowerShell (phòng thư mục chứa khoảng trắng hoặc `&`). Thay `<skill-dir>` bằng đường dẫn tới thư mục chứa tệp `SKILL.md` này (ví dụ `"$HOME\.gemini\config\skills\lucian-uxui"` hoặc `"skills\lucian-uxui"`):

```powershell
node "<skill-dir>\scripts\lucian-uxui.mjs" <command> [options]
```

| Lệnh | Chức năng | Ví dụ |
| --- | --- | --- |
| `search <words...>` | Tìm element phù hợp nhất (hỗ trợ `--category <slug>`, `--limit n`) | `node "<skill-dir>\scripts\lucian-uxui.mjs" search "ai prompt"` |
| `list [--category slug]` | Liệt kê 27 danh mục hoặc toàn bộ element trong 1 danh mục | `node "<skill-dir>\scripts\lucian-uxui.mjs" list --category buttons` |
| `get <id> [<id>...]` | Lấy mã nguồn đầy đủ (tối đa **8** element mỗi lần) | `node "<skill-dir>\scripts\lucian-uxui.mjs" get 452 458` |
| `tokens` | Lấy bộ biến màu `--ux-*` (Light/Dark) và lớp nền `.ux` | `node "<skill-dir>\scripts\lucian-uxui.mjs" tokens` |
| `info` | Kiểm tra chế độ chạy, nguồn dữ liệu, snapshot cục bộ và cache | `node "<skill-dir>\scripts\lucian-uxui.mjs" info` |

### Chế độ Hybrid & Các cờ tùy chọn
- **Mặc định (Hybrid Local-First)**: Đọc trực tiếp từ `data/api/v1/` (`< 100ms`, không gọi mạng). Nếu tìm element mới chưa có cục bộ hoặc dùng `--lang ko`, tự động fallback sang CDN `lucianlabs.dev` → GitHub mirror.
- **`--offline`**: Bắt buộc chỉ đọc dữ liệu cục bộ; cấm mọi kết nối mạng (trả mã thoát `3` nếu thiếu tài nguyên cục bộ).
- **`--online`**: Ưu tiên tải bản mới nhất từ CDN/GitHub trước, chỉ dùng snapshot cục bộ khi mất mạng.
- **`--lang en|ko`**: Ngôn ngữ mẫu (mặc định `en`).
- **`--out <path>`**: Xuất mã nguồn ra tệp thay vì in ra stdout.

> **Lưu ý khi không có Node.js**: Có thể dùng `curl.exe -fsSL https://lucianlabs.dev/uxui-prompt/api/v1/en/catalog.tsv` hoặc đọc trực tiếp từ `data\api\v1\en\` cục bộ.

---

## 2. Quy trình 7 bước khi xây dựng giao diện

1. **Khảo sát dự án đích**: Xác định framework (`React`, `Next.js`, `Vue`, `Svelte`, `Astro`, hay `HTML/CSS/JS` thuần), hệ thống style (Global CSS, CSS Modules, Tailwind), cơ chế theme (`data-theme`, `.dark`, biến CSS thương hiệu) và ngôn ngữ giao diện. Nếu là trang mới chưa chọn stack, dùng HTML/CSS/JS thuần chuẩn Portable.
2. **Phân rã thành các phần UI & dịch từ khóa**: Tách yêu cầu thành từng thành phần (ví dụ: thanh điều hướng, nút CTA, bảng giá, ô nhập AI, toast thông báo...). **Dịch từ khóa tiếng Việt sang tiếng Anh** trước khi chạy `search` (vì snapshot cục bộ sử dụng catalog tiếng Anh).
3. **Tìm kiếm từng thành phần**: Chạy `search` theo từ khóa tiếng Anh (hoặc `get` thẳng nếu người dùng đã chỉ định số `#ID` hoặc link `lucianlabs.dev/uxui-prompt/#ID`). Ưu tiên chọn element có hành vi khớp nhất thay vì viết lại từ đầu.
4. **Tải mã nguồn vừa đủ**: Chạy `get <ids>` (tối đa 8 ID/lần) và `tokens` (1 lần cho mỗi dự án). Không đổ toàn bộ `catalog.tsv` vào ngữ cảnh.
5. **Port mã nguồn & ánh xạ Theme**:
   - Đọc kỹ **[references/porting.md](references/porting.md)** trước khi port sang React/Next/Vue/Svelte/Astro/HTML (đặc biệt phần cleanup `window`/`document` listeners, timers, `rAF` và Observers cho React StrictMode).
   - Đọc **[references/token-bridges.md](references/token-bridges.md)** để ánh xạ `--ux-*` sang hệ màu **WinCommerce Luminous Liquid Glass** hoặc **Vịnh Ngọc / Adaptive Product UI**, đồng thời áp dụng quy tắc sửa typography Tiếng Việt.
   - Giữ nguyên cấu trúc CSS scoped `.uNNN`, giữ nguyên thông số bo góc/chuyển động, và nếu phần tử có `Footprint: fixed size` rộng hơn `375px`, bổ sung `max-width: 100%` trên khối gốc và kiểm tra lại bố cục.
6. **Kiểm tra chất lượng trước khi bàn giao**:
   - Giao diện Light/Dark (kể cả khi chuyển theme trực tiếp).
   - Màn hình hẹp `375px` không tràn ngang (`horizontal scroll`).
   - Điều hướng bàn phím (`Tab`, `Enter`, `Space`, phím mũi tên) và vòng focus rõ ràng.
   - Chế độ `prefers-reduced-motion: reduce` vẫn hoàn tất trạng thái cuối.
   - Không có lỗi console hay hiệu ứng nhân đôi khi remount.
7. **Báo cáo rõ ràng**: Kết thúc câu trả lời bằng danh sách các element đã dùng theo mẫu:
   `- #<ID> <Tên>: <vị trí sử dụng>, <những gì đã chỉnh sửa>, https://lucianlabs.dev/uxui-prompt/#<ID>`
   và nêu rõ các mục chưa thể kiểm tra thực tế (nếu có).

---

## 3. Quy tắc bắt buộc

- **Tuyệt đối không tự bịa mã element hoặc đoán code từ trí nhớ**: Chỉ dùng mã nguồn trả về bởi lệnh `get`.
- **Tuân thủ bản quyền MIT**: Luôn giữ nguyên dòng chú thích bản quyền ở đầu mỗi component được port:
  `<!-- Lucian UX/UI Prompt #ID · MIT License (c) 2026 Seokwoooo · https://lucianlabs.dev/uxui-prompt/#ID -->` (hoặc dạng `//` / `/* */` trong tệp JS/TS).
- **Khắc phục hiển thị Tiếng Việt**: Luôn ghi đè `.ux { font-family: inherit; word-break: normal; }` sau `tokens.css` để tránh lỗi ngắt chữ của `word-break: keep-all` (mặc định dành cho tiếng Hàn).
- **Tối ưu Context Window**: Không đọc toàn bộ `catalog.tsv` hay tải hàng loạt quá 8 element mỗi lượt `get`.

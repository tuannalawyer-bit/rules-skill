# Token Bridges & Quy chuẩn Tích hợp Nội bộ

Tài liệu này hướng dẫn cách nối bộ biến `--ux-*` của **Lucian UX/UI Prompt** với các hệ thống thiết kế nội bộ (**WinCommerce Luminous Liquid Glass**, **Vịnh Ngọc / Adaptive Product UI**) và khắc phục hiển thị Tiếng Việt.

---

## 1. Sửa lỗi Typography Tiếng Việt (Bắt buộc)

Tệp `tokens.css` gốc đặt `font-family: "Pretendard Variable", ...` và `word-break: keep-all` (tối ưu cho tiếng Hàn/CJK). Với giao diện Tiếng Việt, luôn đặt đoạn ghi đè ngay sau phần khai báo của `tokens.css`:

```css
.ux {
  font-family: inherit;
  word-break: normal;
  overflow-wrap: break-word;
}
```

---

## 2. Cầu nối Token: WinCommerce Luminous Liquid Glass

Khi ghép các component Lucian (như `#452 AI prompt box`, `#458 AI voice orb`, `#454 Agent task steps`) vào ứng dụng **WinCommerce** (xem `skills/wincommerce-luminous-liquid-glass/references/tokens-and-css.md`), giữ lớp `.ux` cơ bản rồi ánh xạ `--ux-*` sang bảng màu **Bạch Ngọc & Đỏ WinCommerce Rực Rỡ**:

```css
:root {
  --ux-page: #f8f9fc;
  --ux-surface: rgba(255, 255, 255, 0.72);
  --ux-surface-2: rgba(255, 255, 255, 0.88);
  --ux-surface-3: rgba(240, 242, 248, 0.92);

  --ux-ink: #18191f;
  --ux-ink-2: #585d6e;
  --ux-ink-3: #8e93a4;

  --ux-line: rgba(210, 215, 230, 0.45);
  --ux-line-2: rgba(210, 215, 230, 0.65);

  --ux-accent: #ea1d2d;                 /* Đỏ WinCommerce */
  --ux-accent-2: #c89c56;               /* Vàng Commerce */
  --ux-accent-soft: rgba(234, 29, 45, 0.12);
  --ux-accent-ink: #ffffff;

  --ux-mint: #119c72;
  --ux-warn: #c89c56;
  --ux-danger: #ea1d2d;

  --ux-glass: rgba(255, 255, 255, 0.72);
  --ux-glass-line: rgba(255, 255, 255, 0.95);
  --ux-shadow: rgba(234, 29, 45, 0.12);
  --ux-shadow-strong: rgba(234, 29, 45, 0.24);
  --ux-grad: linear-gradient(120deg, #ea1d2d, #c89c56);
  --ux-ease: cubic-bezier(0.16, 1, 0.3, 1);
}
```

> **Lưu ý**: Nếu dùng các bảng màu WinCommerce khác (như *Pha Lê Băng & Ruby San Hô* hoặc *Kính Cực Quang Tán Sắc*), chỉ cần thay giá trị `--ux-page`, `--ux-accent`, `--ux-accent-2` và `--ux-shadow` tương ứng, đồng thời kiểm tra lại những chỗ element dùng `light-dark(...)` hoặc `@property` trên nền sáng.

---

## 3. Cầu nối Token: Vịnh Ngọc / Adaptive Product UI

Khi thiết kế sản phẩm mới không gắn thương hiệu WinCommerce theo phong cách **Vịnh Ngọc** (xem `skills/vinh-ngoc-ui/references/design-system.md`):

```css
:root {
  --ux-page: #eaf4f2;
  --ux-surface: #fbfdfc;
  --ux-surface-2: #ddefea;
  --ux-surface-3: #c7dad7;

  --ux-ink: #244254;
  --ux-ink-2: #526c7a;
  --ux-ink-3: #6f8794;

  --ux-line: #c7dad7;
  --ux-line-2: rgba(36, 66, 84, 0.22);

  --ux-accent: #147f99;                 /* Ocean Teal */
  --ux-accent-2: #4168c7;               /* Cobalt */
  --ux-accent-soft: rgba(20, 127, 153, 0.12);
  --ux-accent-ink: #ffffff;

  --ux-mint: #238f79;
  --ux-warn: #b97818;
  --ux-danger: #d96550;                 /* Coral */

  --ux-glass: rgba(251, 253, 252, 0.78);
  --ux-glass-line: rgba(255, 255, 255, 0.9);
  --ux-shadow: rgba(20, 127, 153, 0.12);
  --ux-shadow-strong: rgba(36, 66, 84, 0.22);
  --ux-grad: linear-gradient(120deg, #147f99, #238f79 55%, #4168c7);
}
```

- **Nguyên tắc phối hợp**: Giữ các khối nội dung chính đủ đục (`#fbfdfc`) để đọc rõ; chỉ dùng hiệu ứng kính mờ cho thanh điều hướng, popover, toolbar; giữ mỗi màn hình 1 màu nhấn chính.

---

## 4. Bảng tra cứu nhanh các Element nổi bật

| ID | Tên gốc | Danh mục | Gợi ý ứng dụng |
| --- | --- | --- | --- |
| `#451` | Mention picker | `inputs-search` | Gõ `@` gợi ý người dùng/tài liệu trong ô bình luận hoặc chat |
| `#452` | AI prompt box | `inputs-search` | Ô nhập prompt AI tự giãn dòng, nút Send chuyển thành Stop kèm viền sáng |
| `#453` | Thinking text | `loading-progress` | Trạng thái AI đang suy luận (shimmer + mở rộng log suy nghĩ) |
| `#454` | Agent task steps | `loading-progress` | Tiến trình các bước làm việc của AI Agent theo thời gian thực |
| `#455` | Tool call approval | `alerts-feedback` | Thẻ xin phép người dùng trước khi Agent chạy lệnh/tool |
| `#456` | Ghost suggestion | `inputs-search` | Gợi ý hoàn thiện câu mờ sau con trỏ (nhấn `Tab` để nhận) |
| `#457` | Voice input button | `buttons` | Nút thu âm kèm waveform chuyển thành chip văn bản |
| `#458` | AI voice orb | `loading-progress` | Quả cầu giọng nói 4 trạng thái (chờ, nghe, nghĩ, nói) |
| `#459` | Dynamic Island | `alerts-feedback` | Thanh trạng thái động cho tác vụ nền / media / thông báo |
| `#423` | Plan switch | `commerce-pricing` | Thẻ gói cước chuyển đổi Tháng/Năm kiểu odometer |
| `#431` | Date picker | `inputs-search` | Lịch chọn ngày mượt mà, khóa ngày quá khứ |
| `#432` | File upload | `inputs-search` | Vùng kéo thả tệp có vòng tiến độ và tick hoàn tất |
| `#435` | Toast notifications | `alerts-feedback` | Cụm thông báo toast xếp chồng, hover tạm dừng đếm giờ, có Undo |
| `#436` | Delete confirmation | `alerts-feedback` | Hộp thoại xác nhận xóa có vi hoạt ảnh |

---

## 5. Cập nhật Snapshot cục bộ trong tương lai

Snapshot hiện tại được ghim từ commit `8749838ddc0987a0f7356ba9e2968fe419e7e06a` của `Seokwoooo/lucian-uxui-prompt`. Khi cần nâng cấp thư viện offline trong repo:
1. Kiểm tra thay đổi tại `Seokwoooo/lucian-uxui-prompt` (`api/v1/index.json`, `api/v1/en/*`).
2. Tải lại bộ tệp `index.json`, `en/catalog.tsv`, `en/tokens.css` và `en/e/*.txt` vào `skills/lucian-uxui/data/api/v1/`.
3. Đối chiếu SHA-256 từng tệp `.txt` với cột `hash` trong `catalog.tsv` và chạy lại bộ kiểm thử của skill.

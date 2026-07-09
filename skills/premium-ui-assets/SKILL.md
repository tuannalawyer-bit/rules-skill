---
name: premium-ui-assets
description: "Cung cấp thư viện mã CSS/HTML mẫu chuẩn premium (gradient, glassmorphism, dark mode, micro-animations, màu HSL) để thiết kế giao diện cao cấp."
---

# Premium UI Assets & Styling Guidelines

Kỹ năng này cung cấp các nguyên mẫu thiết kế và đoạn CSS/HTML mẫu đã được chuẩn hóa theo phong cách thiết kế hiện đại (premium, tinh tế) để áp dụng ngay lập tức khi xây dựng các ứng dụng có giao diện người dùng (UI/UX) cho bạn.

## 1. Hệ màu sắc chuẩn HSL (Premium Palette)

Tuyệt đối không dùng các màu gốc thô (ví dụ: `#ff0000`, `blue`). Sử dụng hệ màu HSL dưới đây:

*   **Primary (Màu chủ đạo):** `hsl(250, 85%, 65%)` (Màu tím neon mượt) hoặc `hsl(210, 100%, 50%)` (Xanh đại dương sâu).
*   **Secondary (Màu phụ):** `hsl(320, 80%, 60%)` (Hồng/đỏ ánh neon).
*   **Background (Nền Dark Mode):** `hsl(220, 15%, 10%)` (Xám đen mượt, không dùng đen tuyền).
*   **Card Background (Nền hộp):** `hsla(220, 15%, 15%, 0.7)` (Để áp dụng hiệu ứng kính).
*   **Border/Glow:** `hsla(250, 85%, 65%, 0.2)`.

---

## 2. Hiệu ứng Kính (Glassmorphism CSS)

Áp dụng cho các bảng thông tin, hộp thoại, hoặc thanh menu điều hướng:

```css
.premium-card {
  background: rgba(30, 30, 40, 0.65);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 16px;
  box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
  color: #f3f4f6;
  padding: 24px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.premium-card:hover {
  transform: translateY(-4px);
  border-color: rgba(250, 100, 250, 0.25);
  box-shadow: 0 12px 40px 0 rgba(140, 80, 250, 0.15);
}
```

---

## 3. Hiệu ứng Gradient Nền Chuyển Động (Animated Gradient)

Tạo ấn tượng thị giác cao cho trang chủ hoặc màn hình chính:

```css
.animated-bg {
  background: linear-gradient(-45deg, #151522, #1b152d, #0d1b2a, #1a0f1a);
  background-size: 400% 400%;
  animation: gradientBG 15s ease infinite;
}

@keyframes gradientBG {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
```

---

## 4. Vi Hiệu ứng Động (Micro-animations)

Áp dụng cho các nút tương tác (Buttons), liên kết, hoặc thẻ menu:

```css
.interactive-btn {
  background: linear-gradient(135deg, hsl(250, 85%, 65%) 0%, hsl(320, 80%, 60%) 100%);
  border: none;
  border-radius: 8px;
  color: white;
  padding: 12px 24px;
  font-weight: 600;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.interactive-btn:hover {
  transform: scale(1.03);
  box-shadow: 0 0 20px rgba(160, 80, 250, 0.4);
}

.interactive-btn:active {
  transform: scale(0.98);
}
```

---

## 5. Quy tắc Sử dụng Ảnh & Placeholders

*   **Không sử dụng text placeholder** như "Chờ cập nhật hình ảnh" hoặc khung hình xám xịt trống rỗng.
*   Nếu cần hình ảnh minh họa, tôi phải tự gọi công cụ tạo ảnh hoặc sinh mã SVG tương tác đẹp mắt (Inline SVG) có sẵn các màu sắc neon để thể hiện đúng tính năng của trang web.

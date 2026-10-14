# WinCommerce Luminous Liquid Glass Tokens & CSS Specifications

Tài liệu đặc tả kỹ thuật CSS và các bảng mã màu (Tokens) chuẩn dành cho hệ thống thiết kế WinCommerce Luminous Liquid Glass.

---

## 1. 5 Bảng Phối Màu Nền Sáng (Luminous Palettes Tokens)

### Palette 1: Bạch Ngọc & Đỏ WinCommerce Rực Rỡ (Bản Chuẩn Logo)
*Khuyên dùng cho: Ứng dụng chính của WinCommerce, Cổng thông tin Hội viên WiN, Dashboard Quản trị.*
```css
:root {
  --bg-ambient: radial-gradient(at 15% 15%, rgba(255, 230, 235, 0.8) 0px, transparent 55%),
                radial-gradient(at 85% 20%, rgba(254, 243, 220, 0.9) 0px, transparent 50%),
                #f8f9fc;
  --glass-surface: rgba(255, 255, 255, 0.72);
  --glass-pill: rgba(255, 255, 255, 0.88);
  --glass-border-top: rgba(255, 255, 255, 0.95);
  --glass-border-bottom: rgba(210, 215, 230, 0.6);
  --text-primary: #18191f;
  --text-secondary: #585d6e;
  --accent-red: #ea1d2d;               /* WinCommerce Red */
  --accent-red-glow: rgba(234, 29, 45, 0.28);
  --accent-gold: #c89c56;              /* WinCommerce Gold */
  --accent-gold-glow: rgba(200, 156, 86, 0.28);
  --shadow-ambient: 0 24px 48px -12px rgba(234, 29, 45, 0.12), 0 6px 16px -2px rgba(0, 0, 0, 0.04);
}
```

### Palette 2: Lụa Sâm Panh & Cam Bình Minh (Ấm Áp & Thịnh Vượng)
*Khuyên dùng cho: Khuyến mãi cuối tuần, Chiến dịch lễ tết, Kích cầu tiêu dùng.*
```css
:root {
  --bg-ambient: radial-gradient(at 20% 15%, rgba(255, 240, 220, 0.9) 0px, transparent 50%),
                radial-gradient(at 80% 20%, rgba(255, 225, 210, 0.8) 0px, transparent 50%),
                #fcf8f3;
  --glass-surface: rgba(255, 252, 248, 0.75);
  --glass-pill: rgba(255, 255, 255, 0.9);
  --accent-red: #ff3d52;
  --accent-gold: #f5a623;
  --shadow-ambient: 0 24px 48px -12px rgba(245, 166, 35, 0.15);
}
```

### Palette 3: Pha Lê Băng & Ruby San Hô (Tương Phản Thanh Mát)
*Khuyên dùng cho: Chuỗi thực phẩm sạch MEATDeli & nông sản WinEco, Quản lý kho lạnh.*
```css
:root {
  --bg-ambient: radial-gradient(at 15% 15%, rgba(224, 242, 254, 0.85) 0px, transparent 55%),
                radial-gradient(at 85% 20%, rgba(255, 228, 230, 0.8) 0px, transparent 50%),
                #f0f7fc;
  --glass-surface: rgba(255, 255, 255, 0.75);
  --accent-red: #ea1d2d;
  --accent-gold: #0284c7;              /* Glacial Ice Blue */
  --shadow-ambient: 0 24px 48px -12px rgba(2, 132, 199, 0.12);
}
```

### Palette 4: Mật Vàng Hoàng Gia & Kem Sữa (Phú Quý & Tài Lộc)
*Khuyên dùng cho: Báo cáo tài chính doanh nghiệp, Khách hàng VIP WiN, Vinh danh bán hàng.*
```css
:root {
  --bg-ambient: radial-gradient(at 15% 15%, rgba(254, 249, 195, 0.85) 0px, transparent 55%),
                radial-gradient(at 85% 20%, rgba(254, 226, 226, 0.8) 0px, transparent 50%),
                #faf8f0;
  --accent-red: #dc2626;
  --accent-gold: #eab308;              /* Royal Gold */
}
```

### Palette 5: Kính Cực Quang Tán Sắc Apple (Mộng Mơ & Đột Phá Vision Pro)
*Khuyên dùng cho: Tính năng Trợ lý Giọng nói WinVoice, Giao diện AI thử nghiệm tương lai.*
```css
:root {
  --bg-ambient: radial-gradient(at 15% 15%, rgba(245, 208, 254, 0.8) 0px, transparent 55%),
                radial-gradient(at 85% 20%, rgba(254, 215, 226, 0.85) 0px, transparent 50%),
                #faf5ff;
  --accent-red: #e11d48;
  --accent-gold: #8b5cf6;              /* Prismatic Purple */
}
```

---

## 2. Quy Chuẩn Kỹ Thuật CSS (Implementation Specs)

### a. Khối Kính Lỏng Nền Sáng (Luminous Liquid Card)
```css
.luminous-glass {
  background: linear-gradient(135deg, var(--glass-surface) 0%, rgba(255, 255, 255, 0.55) 100%);
  backdrop-filter: blur(32px) saturate(200%);
  -webkit-backdrop-filter: blur(32px) saturate(200%);
  border-top: 1.5px solid var(--glass-border-top);
  border-left: 1px solid rgba(255, 255, 255, 0.8);
  border-right: 1px solid rgba(210, 215, 230, 0.45);
  border-bottom: 1.5px solid var(--glass-border-bottom);
  box-shadow: 
    inset 0 1.5px 2px rgba(255, 255, 255, 0.95),  /* Phản xạ tinh thể mép trên */
    inset 0 -1.5px 2px rgba(0, 0, 0, 0.03),       /* Vát nhẹ mép dưới */
    var(--shadow-ambient);                        /* Bóng đổ màu bồng bềnh */
  border-radius: 1.5rem;                           /* 24px bo góc mềm mại */
  position: relative;
  transition: all 0.45s cubic-bezier(0.16, 1, 0.3, 1);
}
```

### b. Thanh Nhập Liệu / Nút Dạng Viên Thuốc (Luminous Pill)
```css
.luminous-pill {
  background: linear-gradient(135deg, var(--glass-pill) 0%, rgba(255, 255, 255, 0.8) 100%);
  backdrop-filter: blur(28px) saturate(210%);
  -webkit-backdrop-filter: blur(28px) saturate(210%);
  border-top: 1.5px solid #ffffff;
  border-left: 1px solid rgba(255, 255, 255, 0.9);
  border-bottom: 1.5px solid rgba(210, 215, 230, 0.6);
  box-shadow: 
    inset 0 1px 2px rgba(255, 255, 255, 1),
    0 12px 28px -6px rgba(0, 0, 0, 0.07);
  border-radius: 9999px;
}
```

### c. Hiệu Ứng Nổi Khối Xúc Giác (Tactile Interaction)
```css
.tactile-card {
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}
.tactile-card:hover {
  transform: translateY(-3px) scale(1.01);
  box-shadow: 
    inset 0 2px 2px rgba(255, 255, 255, 1),
    0 28px 50px -12px var(--accent-red-glow),
    0 10px 20px -3px rgba(0, 0, 0, 0.06);
  border-top-color: #ffffff;
}
.tactile-card:active {
  transform: translateY(1px) scale(0.992);
  box-shadow: 
    inset 0 2px 4px rgba(0, 0, 0, 0.06),
    0 8px 16px -4px rgba(0, 0, 0, 0.05);
}
```

### d. Chuyển Vùng Chức Năng (Fluid Zone Transitions)
```css
.zone-box {
  transition: opacity 0.4s cubic-bezier(0.16, 1, 0.3, 1), transform 0.45s cubic-bezier(0.16, 1, 0.3, 1);
}
.zone-box.zone-hide {
  display: none;
  opacity: 0;
  transform: scale(0.98) translateY(12px);
}
.zone-box.zone-show {
  display: flex;
  opacity: 1;
  transform: scale(1) translateY(0);
}
```

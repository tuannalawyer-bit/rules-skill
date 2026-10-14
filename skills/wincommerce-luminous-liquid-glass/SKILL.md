---
name: wincommerce-luminous-liquid-glass
description: >-
  Design and implement high-end, luminous liquid glass UI/UX interfaces for WinCommerce applications.
  Use when designing or developing web or mobile interfaces, ChatGPT-style AI chat assistants,
  Canvas split-pane dashboards, or 3D voice interfaces tailored to WinCommerce's brand identity
  (Vibrant Red & Gold) using Apple-inspired luminous liquid glassmorphism, 3D tactile depth,
  and smooth fluid transitions.
---

# WinCommerce Luminous Liquid Glass UI/UX Design System Skill

Hệ thống hướng dẫn thiết kế và triển khai giao diện phần mềm AI & Web App cao cấp dành riêng cho **WinCommerce (Tập đoàn Masan)**. Kết hợp nhận diện thương hiệu **Đỏ Win (`#EA1D2D`) & Vàng Commerce (`#C89C56`)** với triết lý thiết kế **Kính Lỏng Nền Sáng (Luminous Liquid Glassmorphism)** của Apple, hiệu ứng **Nổi khối 3D xúc giác (Tactile 3D Depth)** và **Chuyển vùng chức năng siêu mượt mà (Fluid Zone Transitions)**.

---

## 1. Triết Lý Thiết Kế Cốt Lõi (Core Design Philosophy)

1. **Luminous & Eye-catching (Tươi sáng & Rực rỡ)**:
   - Loại bỏ nền tối u ám (Dark mode u tối), sử dụng nền trắng ngọc trai (`#F8F9FC`) kết hợp quầng sáng Ambient đa sắc mềm mại.
   - Logo WinCommerce nổi bật tự nhiên 100%, bảo toàn trọn vẹn giá trị nhận diện thương hiệu bán lẻ.

2. **Apple Luminous Liquid Glass (Kính lỏng nền sáng)**:
   - Chất liệu kính sữa trong mờ (Frosted Milk Acrylic) với độ khúc xạ cao (`backdrop-filter: blur(32px) saturate(200%)`).
   - Mép kính trên có đường phản quang trắng tinh thể 1.5px (`border-top: 1.5px solid rgba(255, 255, 255, 0.95)`), viền dưới bóng nhẹ tạo độ dày vật lý.

3. **Tactile Volumetric Depth (Nổi khối 3D xúc giác)**:
   - Bóng đổ bồng bềnh đa tầng màu đỏ nhạt mềm mại (`0 20px 40px -12px rgba(234, 29, 45, 0.12)`) giúp các khối kính trắng nổi hẳn lên khỏi mặt bàn mà không bị chìm.
   - Thao tác hover nâng thẻ lên 3px, click lún nhẹ 1px tạo phản hồi xúc giác cơ học.

4. **Fluid Zone Transitions (Chuyển vùng không gián đoạn)**:
   - Chuyển tiếp giữa Hội thoại AI (Chat), Bảng điều khiển kép (Canvas) và Giọng nói (Voice) bằng đường cong gia tốc lò xo Apple (`cubic-bezier(0.16, 1, 0.3, 1)`).

---

## 2. Hướng Dẫn Kỹ Thuật & Tài Liệu Tham Chiếu

Trước khi viết code CSS hoặc HTML/React/Flutter, hãy đọc kỹ tệp tham chiếu:
👉 **[references/tokens-and-css.md](references/tokens-and-css.md)**

Tệp tham chiếu cung cấp:
- **5 Bảng phối màu chuẩn nghiệp vụ**:
  1. *Bạch Ngọc & Đỏ WinCommerce Rực Rỡ*: Chuẩn thương hiệu WinCommerce, cổng WiN, Dashboard.
  2. *Lụa Sâm Panh & Cam Bình Minh*: Khuyến mãi, Tết, kích cầu.
  3. *Pha Lê Băng & Ruby San Hô*: Nông sản WinEco & thịt sạch MEATDeli, kho lạnh.
  4. *Mật Vàng Hoàng Gia & Kem Sữa*: Báo cáo tài chính, VIP WiN, vinh danh.
  5. *Kính Cực Quang Tán Sắc Apple*: Trợ lý giọng nói WinVoice, giao diện AI tương lai.
- **Mã CSS hoàn chỉnh sẵn dùng**:
  - Khối kính lỏng (`.luminous-glass`)
  - Nút / Thanh nhập liệu dạng viên thuốc (`.luminous-pill`)
  - Thẻ tương tác nổi khối xúc giác (`.tactile-card`)
  - Chuyển vùng mượt mà không giật trang (`.zone-box`)

---

## 3. Cấu Trúc 3 Vùng Chức Năng Chuẩn Cho WinCommerce AI

1. **Vùng 1: Cố Vấn Bán Lẻ (Retail AI Chat)**:
   - Hội thoại 1 cột tối ưu cho việc đọc số liệu phân tích sản phẩm, khách hàng WiN, MeatDeli, WinEco.
   - Bong bóng tin nhắn dạng kính sữa, viền sáng khúc xạ, chữ than chì đen đậm tương phản cao.

2. **Vùng 2: Canvas Quản Trị Kép (Split Management Dashboard)**:
   - Màn hình kép mở rộng tự nhiên (không giật trang).
   - Bên trái là chỉ đạo chiến lược, bên phải là lưới chỉ số doanh thu realtime từ 3,850+ siêu thị WinMart và cửa hàng WinMart+.

3. **Vùng 3: Quả Cầu Giọng Nói Không Gian (Spatial WinVoice Orb)**:
   - Quả cầu pha lê 3D phát sáng trên nền sáng, chuyển động co giãn theo sóng âm Đỏ Win & Vàng Commerce.

---

## 4. Danh Sách Kiểm Tra Thiết Kế (Quality Checklist)

- [ ] **Độ tương phản**: Văn bản chính dùng màu `#18191F` trên nền kính trắng, đạt tỉ lệ tương phản tối thiểu 10:1 (chuẩn **WCAG AAA**).
- [ ] **Nhận diện Logo**: Logo WinCommerce phải được đặt trên platter kính trắng trong mờ có độ mờ tối thiểu 70% để giữ sắc nét.
- [ ] **Bóng đổ không dùng màu đen tuyền**: Luôn pha màu đỏ nhạt hoặc vàng cam nhạt vào bóng đổ ambient (`rgba(234, 29, 45, 0.12)`) để giao diện luôn tươi tắn.
- [ ] **Gia tốc chuyển động**: Tuyệt đối không dùng `ease` mặc định; luôn dùng đường cong lò xo Apple: `cubic-bezier(0.16, 1, 0.3, 1)`.

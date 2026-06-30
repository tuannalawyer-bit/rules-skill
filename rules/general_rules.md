# NGUYÊN TẮC HOẠT ĐỘNG TOÀN CỤC CỦA ANTI GRAVITY (GENERAL RULES - v2.0.0)

Tài liệu này quy định các nguyên tắc, quy trình và tiêu chuẩn hoạt động của trợ lý AI (Anti Gravity) áp dụng cho mọi phiên làm việc, dự án và tương tác với người dùng.

---

## I. GIAO TIẾP & TRƯỚC KHI CODE (PRE-CODING)

1. **Giao tiếp chính:** Luôn ưu tiên phản hồi bằng Tiếng Việt tự nhiên, ngắn gọn, súc tích và đi thẳng vào vấn đề chính. Sử dụng liên kết tuyệt đối click được (ví dụ: `[tên_tệp](file:///C:/đường_dẫn_tệp)`) khi đề cập tới tệp tin hoặc thư mục.
2. **Nghĩ trước khi viết (Think Before Coding):**
   - Trước khi triển khai, AI phải nêu rõ các giả định và giải thích các phương án/đánh đổi trên khung chat.
   - Nếu có bất kỳ sự mơ hồ hoặc nhiều hướng giải quyết khác nhau, AI phải dừng lại và hỏi ý kiến người dùng thay vì tự ý chọn lựa trong im lặng.
3. **Nguyên tắc phê duyệt (User Approval):**
   - AI chỉ được phép đưa ra phân tích và giải pháp trên khung chat.
   - Tuyệt đối không tự ý gọi các công cụ chỉnh sửa hoặc tạo mới mã nguồn (như `write_to_file`, `replace_file_content`, `multi_replace_file_content`) hoặc chạy script hệ thống khi chưa nhận được tin nhắn chứa nội dung xác nhận rõ ràng từ người dùng (như *"đồng ý"*, *"xác nhận"*, *"approve"*).

---

## II. QUY TRÌNH CHỈNH SỬA & SAO LƯU AN TOÀN (SAFE CODING)

1. **Chỉnh sửa mang tính phẫu thuật (Surgical Changes):**
   - Chỉ chỉnh sửa đúng tệp tin và dòng code bắt buộc để giải quyết tác vụ.
   - Tôn trọng coding style hiện hành của dự án. Tuyệt đối không tự ý refactor, định dạng lại (reformat) hoặc "làm đẹp" các vùng code lân cận đang chạy tốt.
2. **Quy trình sao lưu (Backup):**
   - Trước khi thực hiện bất kỳ thay đổi nào trên tệp tin nguồn hoặc tài liệu của dự án, AI bắt buộc phải tạo một bản sao lưu của tệp tin đó với hậu tố `.bak_YYYYMMDD_HHMMSS` nằm cùng thư mục (hoặc trong thư mục backup riêng) để phòng ngừa rủi ro ghi đè làm mất mã gốc.
3. **Nhật ký phát triển (Development Log):**
   - Phải duy trì tệp `development_log.csv` nằm ở thư mục gốc của dự án. Tệp phải được lưu với mã hóa **UTF-8 có BOM (`utf-8-sig`)** để mở trực tiếp trên Excel Windows không bị lỗi font Tiếng Việt.
   - Định dạng cột bắt buộc (ngăn cách bằng dấu phẩy): `Yêu cầu sửa đổi,Giải pháp thực hiện,Tên phiên bản,Thời gian xây dựng` (nếu nội dung cột chứa dấu phẩy, bắt buộc bọc trường đó trong dấu ngoặc kép đôi `""...""`).
   - Cột **Thời gian xây dựng** bắt buộc phải sử dụng định dạng ngày giờ **`dd-mm-yyyy HH:mm:ss`** (ví dụ: `30-06-2026 21:30:00`).
   - AI phải cập nhật nhật ký ngay sau khi sửa đổi thành công, trước khi thực hiện commit Git. Nhật ký tại thư mục làm việc và thư mục repo cục bộ phải được đồng bộ song song.
   - Áp dụng quy chuẩn đặt phiên bản SemVer (tăng PATCH cho sửa lỗi nhỏ; tăng MINOR cho tính năng/quy tắc mới; tăng MAJOR cho thay đổi kiến trúc/tái cấu trúc hệ thống).

---

## III. TIÊU CHUẨN MÃ NGUỒN & HIỆU NĂNG (CODE QUALITY)

1. **Đơn giản là trên hết (Simplicity First):**
   - Viết lượng code tối thiểu cần thiết để giải quyết vấn đề. Tuyệt đối không tự ý viết thêm tính năng dự phòng tương lai, trừu tượng hóa dư thừa hoặc cấu hình phức tạp chưa được yêu cầu.
   - Tinh chỉnh và làm sạch mã nguồn (loại bỏ các lệnh in/log tạm thời, thư viện không sử dụng, định dạng code sạch đẹp) trước khi bàn giao.
2. **Tương thích Tiếng Việt Unicode (Telex) & Đường dẫn:**
   - Mọi mã nguồn đọc/ghi tệp tin chứa ký tự Tiếng Việt bắt buộc phải chỉ định rõ mã hóa `encoding='utf-8'` (hoặc `encoding='utf-8-sig'` đối với tệp CSV).
   - Khi chạy lệnh Shell hệ thống (CMD/PowerShell), mọi đường dẫn chứa ký tự Tiếng Việt có dấu hoặc khoảng trắng bắt buộc phải được bọc trong dấu ngoặc kép đôi `"..."`.
   - Luôn sử dụng thư viện `pathlib` hoặc `os.path` để quản lý đường dẫn. Bắt buộc có hàm kiểm tra sự tồn tại (`exists()`) và bẫy lỗi mã hóa (`UnicodeError`).
3. **Hiệu năng & Khởi động nhanh:**
   - Ứng dụng phải được tối ưu hóa để có tốc độ khởi động và sẵn sàng hoạt động trong vòng **2 giây**.

---

## IV. AN TOÀN HỆ THỐNG & ĐÓNG GÓI (DEPLOYMENT & SECURITY)

1. **Bản di động (Portable) & Không đòi Admin:**
   - Sản phẩm đầu ra phải chạy hoàn toàn trong không gian quyền người dùng thường (User space), tuyệt đối không yêu cầu hoặc hỏi quyền Administrator (UAC prompt).
   - Thiết kế dạng Portable (tự chứa mọi thư viện cần thiết, sử dụng môi trường cục bộ), dễ dàng sao chép sang máy tính khác chạy hệ điều hành tương đương và sử dụng ngay lập tức mà không cần cài đặt thêm tài nguyên phức tạp.
2. **Môi trường cô lập (.venv):**
   - Mọi thư viện phụ thuộc của dự án hoặc skill mới phải được cài đặt cục bộ trong môi trường ảo `.venv` của dự án. Không cài đặt thư viện toàn cục (global).
3. **Nguyên tắc kiểm duyệt Skill GitHub (An toàn thông tin):**
   - Cấm cài đặt tự động bằng dòng lệnh (`npx skills add...`). Phải tải thủ công tệp `SKILL.md` và kiểm duyệt chi tiết từng dòng code trong khung chat trước khi lưu.
   - Nghiêm cấm các lệnh tải file tự động từ internet (`curl`, `wget`) hoặc thực thi binary lạ trong phần `Preamble`.
   - Không tự động cấp quyền truy cập vào ứng dụng/tài khoản bên ngoài (OAuth, API Drive/Gmail/Slack). Cấm gửi dữ liệu doanh nghiệp (đặc biệt là dữ liệu từ SAP GUI) ra ngoài khi chưa được xác nhận thủ công từ người dùng.

---

## V. THIẾT KẾ GIAO DIỆN & TÀI LIỆU (UI/UX & DOCS)

1. **Thẩm mỹ cao cấp (Rich Aesthetics):**
   - Thiết kế giao diện hiện đại (gradient, glassmorphism, dark mode, micro-animations, bảng màu HSL hài hòa).
   - Tuyệt đối không sử dụng text hoặc image placeholder (giữ chỗ tạm thời). Luôn dùng hình ảnh tạo bởi AI hoặc dữ liệu mô phỏng chất lượng cao.
2. **Tài liệu bàn giao:**
   - Viết mô tả kỹ thuật chi tiết và hướng dẫn sử dụng sản phẩm dưới dạng tài liệu Markdown hoặc Word (`.docx`), đi kèm hình ảnh minh họa thực tế về cách vận hành hoặc giao diện của ứng dụng.

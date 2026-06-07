---
name: handoff
description: "Bàn giao ngữ cảnh phiên làm việc giữa các máy tính."
---

# Handoff Skill (Bàn giao ngữ cảnh phiên làm việc)

Kỹ năng này hướng dẫn trợ lý AI (Anti Gravity) tóm tắt và đóng gói toàn bộ trạng thái công việc hiện tại vào một tệp tin bàn giao ngắn gọn (`HANDOFF.md`), giúp bạn dễ dàng chuyển tiếp và tiếp tục công việc trên một máy tính khác thông qua đồng bộ GitHub.

## 1. Khi nào kích hoạt Handoff
Kích hoạt skill này khi người dùng nói các từ khóa như:
*   "bàn giao", "handoff", "tắt máy", "đồng bộ sang máy khác", "lưu lại trạng thái".

## 2. Quy trình đóng gói Handoff

Khi được kích hoạt, tôi bắt buộc phải viết một tệp tài liệu `HANDOFF.md` tại thư mục gốc của dự án hoạt động (ví dụ: `C:\Users\Tuan\.gemini\antigravity\scratch\Dự án AI\HANDOFF.md`) với cấu trúc chuẩn sau:

### Cấu trúc Tệp `HANDOFF.md` mẫu:
```markdown
# BÀN GIAO PHIÊN LÀM VIỆC - [NGÀY THÁNG GIỜ]

## 1. Công việc đã hoàn thành
- Mô tả ngắn gọn các tính năng đã code và chạy thử thành công.
- Liệt kê các tệp đã sửa đổi hoặc thêm mới.

## 2. Trạng thái hiện tại & Các việc đang dang dở
- Các tính năng đang viết dở, các lỗi chưa kịp sửa.
- Vấn đề kỹ thuật hiện tại cần lưu ý.

## 3. Các bước tiếp theo cần làm (Next Steps)
- Liệt kê danh sách TODO rõ ràng để AI ở phiên sau đọc và làm tiếp ngay lập tức.

## 4. Cách chạy thử nghiệm nhanh trên máy mới
- Các lệnh chạy và test cần thiết.
```

## 3. Đồng bộ lên GitHub sau khi Handoff
Sau khi tạo xong file `HANDOFF.md`:
1.  Tự động cập nhật nhật ký phát triển `development_log.csv` ghi nhận sự kiện bàn giao.
2.  Chạy các lệnh Git để đẩy file `HANDOFF.md` này lên repository GitHub từ xa.
3.  Phản hồi lại cho bạn: *"Đã lưu trạng thái công việc thành công vào tệp HANDOFF.md và đẩy lên GitHub. Bạn chỉ cần clone/pull trên máy tính mới để tiếp tục!"*

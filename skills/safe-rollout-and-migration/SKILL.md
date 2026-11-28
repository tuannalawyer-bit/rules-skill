---
name: safe-rollout-and-migration
description: "Chiến lược phát hành an toàn (Feature Flags, Rollback), di trú dữ liệu/schema (Migration) và loại bỏ tính năng cũ (Deprecation) chắt lọc từ Addy Osmani Agent Skills."
---

# Safe Rollout & Migration Skill

Kỹ năng này bao phủ giai đoạn **Ship & Operate** (phát hành và vận hành an toàn), đảm bảo mọi thay đổi về cấu trúc dữ liệu, cấu hình hệ thống hoặc quy trình tự động hóa đều có đường lùi (rollback) và không làm gián đoạn hệ thống đang chạy.

---

## 1. Khi nào Kích hoạt?
* Khi thay đổi schema cơ sở dữ liệu, cấu trúc tệp CSV/JSON đầu ra, hoặc định dạng cấu hình.
* Khi nâng cấp thư viện lõi, thay đổi đường dẫn đồng bộ hoặc thay thế công cụ cũ bằng công cụ mới.
* Khi triển khai tính năng có rủi ro cao lên môi trường sản xuất (production).

---

## 2. Nguyên tắc Di trú An toàn (Expand & Contract Pattern)
Khi thay đổi cấu trúc dữ liệu hoặc API đang được sử dụng:
1. **Expand (Mở rộng):** Hỗ trợ song song cả định dạng cũ và định dạng mới (hoặc thêm cột/trường mới mà chưa xóa trường cũ).
2. **Migrate (Chuyển đổi):** Chuyển dữ liệu/người gọi sang dùng định dạng mới, kèm script kiểm tra tính toàn vẹn trước và sau khi chuyển.
3. **Contract (Thu hẹp):** Chỉ xóa bỏ định dạng cũ sau khi đã xác minh 100% luồng phụ thuộc không còn dùng nó.

---

## 3. Kế hoạch Phát hành & Hoàn tác (Rollout & Rollback Plan)
Trước khi áp dụng thay đổi có rủi ro, bắt buộc phải có:
* **Sao lưu điểm khôi phục:** Lưu bản `.bak_*` vào `.backups/` hoặc tạo Git commit/tag trước khi chạy migration.
* **Cơ chế tắt nhanh (Kill Switch / Feature Flag):** Cho phép quay lại luồng cũ bằng 1 biến cấu hình hoặc 1 lệnh hoàn tác duy nhất mà không cần sửa code.
* **Kiểm tra sau phát hành (Post-Ship Smoke Check):** Chạy ngay một ca kiểm thử nhẹ (smoke test) để xác nhận hệ thống khởi động sạch, không lỗi runtime hoặc lỗi encoding.

---

## 4. Quy trình Loại bỏ Tính năng Cũ (Deprecation)
* Không xóa đột ngột tính năng/script cũ đang có người dùng.
* Đánh dấu cảnh báo `[DEPRECATED]` kèm hướng dẫn chuyển sang phương án mới trước ít nhất 1 chu kỳ phát hành.

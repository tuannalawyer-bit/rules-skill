# Bug Report & Triage Reference Template

Tài liệu tham khảo chi tiết về khuôn mẫu báo cáo lỗi và bảng ma trận phân loại lỗi.

---

## 1. Mẫu Báo cáo Lỗi Mở rộng (Extended Bug Report)

Sử dụng mẫu này khi cần bàn giao báo cáo lỗi cho đội ngũ phát triển hoặc lưu trữ vào hệ thống theo dõi lỗi (GitHub Issues / Jira):

```markdown
# [BUG] <Tiêu đề ngắn gọn tóm tắt hành vi lỗi>

## Thông tin Chung
- **Mã lỗi (Bug ID):** BUG-XXXX
- **Mức độ nghiêm trọng (Severity):** [P0 - Critical | P1 - Major | P2 - Medium | P3 - Minor]
- **Độ ưu tiên xử lý (Priority):** [Khẩn cấp | Cao | Bình thường | Thấp]
- **Người báo cáo:** AI QA Agent
- **Ngày phát hiện:** YYYY-MM-DD HH:mm:ss
- **Môi trường:** OS: Windows 11 / Python: 3.14.7 / Node: v22.x / Runtime: Portable

---

## Mô tả Chi tiết
<Mô tả ngắn 1-2 câu giải thích hiện tượng lỗi xảy ra khi làm gì.>

## Các bước Tái hiện Lỗi (Steps to Reproduce)
1. Bước 1...
2. Bước 2...
3. Bước 3...

## Hiện tượng Lỗi (Actual Behavior)
- Mô tả chính xác điều gì đã xảy ra (kèm mã lỗi nếu có).

## Kỳ vọng Hệ thống (Expected Behavior)
- Mô tả chính xác hệ thống nên phản hồi như thế nào theo đúng thiết kế hoặc logic nghiệp vụ.

## Phân tích Kỹ thuật (Technical Notes)
- **Tệp tin nghi vấn:** `path/to/source/file.py#L45-L60`
- **Hàm/Phương thức:** `process_data()`
- **Dữ liệu gây lỗi (Payload):**
```json
{
  "test_input": null
}
```

## Giải pháp Đề xuất (Recommended Fix)
- Bước 1: Thêm validation tại tầng Controller / Service.
- Bước 2: Bổ sung ca kiểm thử tự động (Unit Test) để đảm bảo không bị tái phát lỗi (Regression prevention).
```

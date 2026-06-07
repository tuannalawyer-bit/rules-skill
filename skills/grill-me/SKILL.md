---
name: grill-me
description: "Phỏng vấn sâu chất vấn giải pháp để đồng bộ lên GitHub."
---

# Grill Me Skill (Phỏng vấn sâu chất vấn giải pháp)

Kỹ năng này hướng dẫn trợ lý AI (Anti Gravity) thực hiện quy trình chất vấn ("grilling") kế hoạch hoặc thiết kế của người dùng bằng cách hỏi từng câu hỏi một cách có hệ thống, nhằm làm rõ mọi điểm mơ hồ trước khi viết code.

## 1. Mục tiêu của Grill Me
*   **Tránh đoán mò:** Ngăn chặn AI tự giả định hoặc viết code sai hướng do yêu cầu chưa rõ ràng.
*   **Làm rõ miền nghiệp vụ (Domain Model):** Giúp thống nhất cấu trúc dữ liệu, các thực thể chính và luồng xử lý.
*   **Tìm ra kịch bản biên (Edge Cases):** Giúp người dùng phát hiện ra các lỗ hổng trong kế hoạch của họ.

## 2. Quy trình thực hiện Chất vấn (Grilling)

Khi người dùng kích hoạt skill này (hoặc khi tôi phát hiện yêu cầu có nhiều điểm mơ hồ cần làm rõ):

1.  **Chỉ hỏi duy nhất 1 câu hỏi tại một thời điểm:** Tuyệt đối không đưa ra một danh sách dài các câu hỏi khiến người dùng bị ngợp.
2.  **Tập trung vào tính phản biện:** Mỗi câu hỏi phải thử thách một giả định trong kế hoạch của người dùng.
    *   *Ví dụ:* *"Nếu trang web bạn muốn cào dữ liệu chuyển sang sử dụng Cloudflare chặn bot, phương án dự phòng của bạn là gì?"*
    *   *Ví dụ:* *"Khi chạy tự động hóa SAP, nếu phiên kết nối SAP bị timeout giữa chừng, hệ thống có cần tự động đăng nhập lại không?"*
3.  **Lắng nghe phản hồi:** Chờ người dùng trả lời câu hỏi đó, sau đó phân tích câu trả lời và đặt câu hỏi tiếp theo dựa trên thông tin mới nhận được.
4.  **Tóm tắt khi hoàn thành:** Quy trình kết thúc khi hai bên đạt được sự thống nhất hoàn toàn. Tôi sẽ tóm tắt lại toàn bộ thiết kế nghiệp vụ đã thống nhất trước khi tiến hành viết code hoặc lập kế hoạch triển khai chính thức.

# Mô hình Thác nước (Waterfall Model)

**Category:** Traditional Process Model

## 1. Định nghĩa (Definition)

Mô hình Thác nước (Waterfall Model) là mô hình quy trình phát triển phần mềm tuần tự và cổ điển nhất. Trong mô hình này, các giai đoạn của dự án được thực hiện một cách tuần tự, nối tiếp nhau như một dòng thác chảy. Giai đoạn sau chỉ được bắt đầu khi giai đoạn trước đã hoàn thành 100% và đã được nghiệm thu. Không có việc quay trở lại giai đoạn trước để sửa đổi khi đã chuyển sang giai đoạn mới.

Đây là mô hình đầu tiên được giới thiệu và đặt nền móng cho nhiều mô hình quy trình phát triển phần mềm sau này.

## 2. Các Giai đoạn (Phases)

Mô hình Thác nước điển hình bao gồm các giai đoạn sau:

1.  **Phân tích Yêu cầu (Requirements Analysis):** Thu thập, phân tích và tài liệu hóa tất cả các yêu cầu của khách hàng và hệ thống. Kết quả của giai đoạn này là một tài liệu đặc tả yêu cầu phần mềm (Software Requirement Specification - SRS).

2.  **Thiết kế Hệ thống (System Design):** Dựa trên tài liệu SRS, các kiến trúc sư và nhà thiết kế sẽ tạo ra bản thiết kế tổng thể cho hệ thống, bao gồm kiến trúc, module, giao diện, và cơ sở dữ liệu.

3.  **Hiện thực (Implementation / Coding):** Các lập trình viên sẽ dựa trên bản thiết kế để viết mã nguồn cho từng module của hệ thống.

4.  **Kiểm thử (Testing):** Sau khi hoàn thành việc viết mã, đội kiểm thử sẽ tích hợp các module lại và tiến hành kiểm thử toàn bộ hệ thống để tìm và sửa lỗi.

5.  **Triển khai (Deployment):** Sau khi hệ thống đã được kiểm thử và nghiệm thu, nó sẽ được triển khai và cài đặt cho khách hàng sử dụng.

6.  **Bảo trì (Maintenance):** Giai đoạn cuối cùng và kéo dài nhất. Đội phát triển sẽ sửa các lỗi phát sinh trong quá trình sử dụng, nâng cấp hệ thống và thêm các chức năng mới theo yêu cầu.

## 3. Ưu điểm (Advantages)

- **Đơn giản, dễ hiểu và dễ quản lý:** Các giai đoạn rõ ràng, mục tiêu và kết quả của mỗi giai đoạn được xác định cụ thể, giúp việc lập kế hoạch và theo dõi tiến độ trở nên dễ dàng.
- **Kỷ luật cao:** Yêu cầu tài liệu hóa chi tiết ở mỗi giai đoạn, giúp giảm thiểu sự mơ hồ.
- **Phân công rõ ràng:** Vai trò và trách nhiệm của các thành viên trong dự án (như BA, Designer, Developer, Tester) được phân chia rạch ròi theo từng giai đoạn.
- **Phù hợp cho các dự án nhỏ:** Hiệu quả đối với các dự án có quy mô nhỏ, yêu cầu đã được xác định rõ ràng và ít có khả năng thay đổi.

## 4. Nhược điểm (Disadvantages)

- **Thiếu linh hoạt, cứng nhắc:** Đây là nhược điểm lớn nhất. Mô hình này không cho phép quay lại các giai đoạn trước, khiến việc thay đổi yêu cầu trở nên cực kỳ khó khăn và tốn kém.
- **Rủi ro cao:** Sản phẩm cuối cùng chỉ được giao cho khách hàng ở giai đoạn cuối. Nếu có sự hiểu lầm về yêu cầu ngay từ đầu, toàn bộ dự án có thể thất bại.
- **Thời gian chờ đợi lâu:** Khách hàng phải chờ đến khi dự án kết thúc mới thấy được sản phẩm.
- **Không phù hợp cho các dự án phức tạp và dài hạn:** Trong thực tế, yêu cầu của khách hàng và công nghệ thường xuyên thay đổi, làm cho mô hình này trở nên không thực tế.

## 5. Khi nào nên sử dụng (When to Use)

Mô hình Thác nước chỉ nên được áp dụng trong một số trường hợp rất cụ thể:

- Khi các yêu cầu của dự án đã được hiểu rõ, được xác định đầy đủ và gần như không có khả năng thay đổi.
- Khi công nghệ sử dụng trong dự án đã ổn định và được đội ngũ phát triển nắm vững.
- Khi dự án có quy mô nhỏ và thời gian thực hiện ngắn.
- Khi không có sự không chắc chắn hoặc rủi ro lớn về mặt kỹ thuật.

---
title: "Các Nguyên tắc và Thuộc tính Chính của Kỹ nghệ Phần mềm"
category: "Các Khái niệm Nền tảng"
priority: 2
---

# Các Nguyên tắc và Thuộc tính Chính của Kỹ nghệ Phần mềm

Để xây dựng phần mềm mạnh mẽ, có khả năng mở rộng và dễ bảo trì, các kỹ sư tuân thủ một bộ các nguyên tắc cốt lõi và luôn cố gắng đạt được những thuộc tính chất lượng nhất định. Các khái niệm này tạo nên xương sống lý thuyết cho việc thiết kế và phát triển phần mềm tốt.

## Các Nguyên tắc Chính của Kỹ nghệ Phần mềm (Key Principles)

Đây là những kim chỉ nam nền tảng, có ảnh hưởng đến các quyết định kỹ thuật trong suốt quá trình phát triển.

- **Tính Mô-đun (Modularity):** Nguyên tắc này bao gồm việc chia nhỏ một hệ thống phần mềm lớn thành các thành phần nhỏ hơn, độc lập và có thể thay thế được gọi là các mô-đun. Mỗi mô-đun có một trách nhiệm cụ thể, có thể được phát triển, kiểm thử và bảo trì riêng biệt, giúp đơn giản hóa sự phức tạp và thúc đẩy sự hợp tác.

- **Tính Trừu tượng (Abstraction):** Trừu tượng là kỹ thuật che giấu các chi tiết triển khai phức tạp và chỉ hiển thị các tính năng thiết yếu của một đối tượng hoặc hệ thống. Nó cho phép các nhà phát triển tập trung vào _cái_ mà một đối tượng làm thay vì _cách_ nó làm, giúp giảm độ phức tạp và làm cho hệ thống dễ hiểu hơn.

- **Tính Đóng gói (Encapsulation):** Đây là việc gói gọn dữ liệu (thuộc tính) và các phương thức (hàm) hoạt động trên dữ liệu đó vào một đơn vị duy nhất, hay "đối tượng". Nó hạn chế quyền truy cập trực tiếp vào trạng thái nội bộ của một đối tượng, bảo vệ nó khỏi các sửa đổi không mong muốn từ bên ngoài và đảm bảo tính toàn vẹn của dữ liệu.

- **Tính Tái sử dụng (Reusability):** Nguyên tắc tạo ra các thành phần phần mềm (như mô-đun, hàm hoặc lớp) có thể được sử dụng trong nhiều dự án khác nhau hoặc các phần khác nhau của cùng một dự án mà không cần hoặc cần rất ít sửa đổi. Tái sử dụng giúp tiết kiệm đáng kể thời gian, công sức và tài nguyên.

- **Khả năng Bảo trì (Maintenance):** Nguyên tắc này yêu cầu phần mềm phải được thiết kế và viết theo cách giúp dễ dàng sửa lỗi, cải thiện hiệu suất hoặc thích ứng với môi trường thay đổi. Tài liệu tốt, mã nguồn sạch và thiết kế mô-đun là chìa khóa để đạt được khả năng bảo trì cao.

- **Kiểm thử (Testing):** Một nguyên tắc cốt lõi khẳng định rằng phần mềm phải được xác minh nghiêm ngặt ở mọi giai đoạn phát triển để đảm bảo nó đáp ứng các yêu cầu và không có lỗi. Điều này bao gồm kiểm thử đơn vị, kiểm thử tích hợp và kiểm thử hệ thống.

- **Mẫu Thiết kế (Design Patterns):** Nguyên tắc này liên quan đến việc sử dụng các giải pháp đã được kiểm chứng và có thể tái sử dụng cho các vấn đề thường xảy ra trong một bối cảnh nhất định của thiết kế phần mềm. Việc tuân theo các mẫu thiết kế giúp tạo ra mã nguồn mạnh mẽ và dễ bảo trì hơn.

- **Phương pháp Agile (Agile Methodologies):** Đề cập đến một tập hợp các nguyên tắc phát triển phần mềm dựa trên sự phát triển lặp đi lặp lại và tăng dần, nơi các yêu cầu và giải pháp phát triển thông qua sự hợp tác giữa các nhóm tự tổ chức và đa chức năng.

- **Tích hợp/Triển khai Liên tục (CI/CD):** Một nguyên tắc phát triển phần mềm hiện đại, trong đó các nhà phát triển thường xuyên hợp nhất các thay đổi mã nguồn của họ vào một kho lưu trữ trung tâm, sau đó các bản dựng và kiểm thử tự động sẽ được chạy. Triển khai liên tục mở rộng điều này bằng cách tự động triển khai tất cả các thay đổi mã nguồn vượt qua giai đoạn kiểm thử lên môi trường sản phẩm.

## Các Thuộc tính Chính của một Phần mềm Tốt (Main Attributes)

Đây là những đặc tính mong muốn mà một sản phẩm phần mềm cuối cùng nên có. Chúng thường được sử dụng làm thước đo để đánh giá chất lượng của phần mềm.

- **Tính Hiệu quả (Efficiency):** Phần mềm nên sử dụng tối ưu các tài nguyên hệ thống như bộ nhớ, thời gian xử lý của CPU và không gian đĩa. Một ứng dụng hiệu quả thực hiện các tác vụ của mình một cách nhanh chóng mà không gây lãng phí.

- **Tính Tin cậy (Reliability):** Phần mềm phải thực hiện các chức năng được yêu cầu một cách nhất quán và chính xác trong các điều kiện đã nêu trong một khoảng thời gian xác định. Người dùng có thể tin tưởng vào một phần mềm đáng tin cậy để không bị lỗi bất ngờ.

- **Tính Tái sử dụng (Reusability):** Thuộc tính này có nghĩa là các bộ phận của phần mềm có thể được sử dụng trong các dự án khác. Khả năng tái sử dụng cao là một dấu hiệu của một hệ thống được thiết kế tốt, theo hướng mô-đun.

- **Khả năng Bảo trì (Maintainability):** Đề cập đến sự dễ dàng mà một hệ thống phần mềm có thể được sửa đổi để sửa lỗi, cải thiện hiệu suất, thêm tính năng mới hoặc thích ứng với môi trường thay đổi. Mã nguồn sạch, được tài liệu hóa tốt có khả năng bảo trì cao.

- **Khả năng Chuyển đổi (Portability):** Phần mềm có thể dễ dàng được chuyển từ một môi trường phần cứng hoặc phần mềm này sang một môi-trường khác. Phần mềm có tính chuyển đổi cao thường độc lập với môi trường của nó.

- **Tính Đúng đắn (Correctness):** Phần mềm phải đáp ứng các yêu cầu chức năng và phi chức năng được chỉ định trong tài liệu yêu cầu. Nó phải làm đúng những gì nó được cho là phải làm.

- **Khả năng Kiểm thử (Testability):** Phần mềm nên được cấu trúc theo cách giúp dễ dàng kiểm thử và xác minh. Điều này bao gồm việc viết mã có thể kiểm thử và cung cấp các tiêu chí rõ ràng để thành công.

- **Khả năng Tương tác (Interoperability):** Đây là khả năng của một hệ thống phần mềm làm việc và giao tiếp với các hệ thống bên ngoài khác. Phần mềm hiện đại thường dựa vào các API và các giao thức tiêu chuẩn để đạt được khả năng tương tác.

- **Tính Bảo mật (Security):** Phần mềm phải có khả năng tự bảo vệ khỏi việc truy cập, sử dụng, tiết lộ, thay đổi hoặc phá hủy trái phép. Bảo mật là một thuộc tính quan trọng đối với hầu hết các ứng dụng hiện đại.

# Giới thiệu về Thiết kế Phần mềm (Introduction to Software Design)

## Định nghĩa

Thiết kế Phần mềm là quá trình chuyển đổi các yêu cầu của người dùng, đã được định nghĩa trong giai đoạn phân tích, thành một "bản thiết kế chi tiết" (blueprint) cho việc xây dựng phần mềm. Nó đóng vai trò là cây cầu nối giữa việc xác định **"Cần làm gì?"** (What to do?) và việc hiện thực **"Làm như thế nào?"** (How to do it?).

Một bản thiết kế tốt sẽ định rõ cấu trúc, các thành phần, các module, các giao diện và dữ liệu của hệ thống, giúp đội ngũ lập trình có thể xây dựng phần mềm một cách hiệu quả và chính xác.

## Tầm quan trọng

Giai đoạn thiết kế là một trong những giai đoạn quan trọng nhất trong vòng đời phát triển phần mềm. Một thiết kế tồi có thể dẫn đến một sản phẩm khó bảo trì, khó mở rộng, nhiều lỗi và tốn kém chi phí để sửa chữa về sau. Ngược lại, một thiết kế tốt sẽ mang lại nhiều lợi ích:

- **Tăng tính dễ bảo trì (Maintainability):** Dễ dàng sửa lỗi và thay đổi khi có yêu cầu mới.
- **Tăng tính tái sử dụng (Reusability):** Các thành phần có thể được sử dụng lại trong các dự án khác.
- **Tăng hiệu quả (Efficiency):** Giảm thiểu sự phức tạp và tối ưu hóa hiệu năng.
- **Cải thiện sự hợp tác (Collaboration):** Cung cấp một ngôn ngữ chung và một cái nhìn tổng thể cho cả đội ngũ phát triển.

## Các cấp độ của Thiết kế Phần mềm

Quá trình thiết kế thường được chia thành hai cấp độ chính:

### 1. Thiết kế Kiến trúc (Architectural Design)

- **Mục tiêu:** Xác định cấu trúc tổng thể của hệ thống ở mức độ cao.
- **Nội dung:**
  - Phân chia hệ thống thành các hệ thống con (sub-systems) hoặc các module chính.
  - Xác định cách các module này tương tác và giao tiếp với nhau.
  - Lựa chọn các công nghệ, framework và mẫu kiến trúc (ví dụ: Microservices, Client-Server).
- **Ví dụ:** Thiết kế kiến trúc của một trang web thương mại điện tử sẽ xác định các khối chính như: Dịch vụ Quản lý Người dùng, Dịch vụ Sản phẩm, Dịch vụ Giỏ hàng, và cách chúng giao tiếp qua API.

### 2. Thiết kế Chi tiết (Detailed Design)

- **Mục tiêu:** Đi sâu vào bên trong mỗi module đã được xác định ở cấp độ kiến trúc.
- **Nội dung:**
  - Định nghĩa các lớp (classes), các thuộc tính (attributes) và phương thức (methods).
  - Đặc tả các thuật toán và logic xử lý bên trong.
  - Thiết kế cấu trúc dữ liệu và các giao diện (interfaces) cụ thể.
- **Ví dụ:** Trong Dịch vụ Quản lý Người dùng, thiết kế chi tiết sẽ định nghĩa lớp `User` với các thuộc tính như `username`, `password` và các phương thức như `login()`, `register()`.

## Các đặc tính của một Thiết kế Tốt

Một bản thiết kế phần mềm được coi là tốt nếu nó đạt được các đặc tính sau:

- **Tính đúng đắn (Correctness):** Đáp ứng đầy đủ tất cả các yêu cầu đã được xác định.
- **Tính hoàn chỉnh (Completeness):** Bao quát tất cả các khía cạnh của hệ thống.
- **Tính hiệu quả (Efficiency):** Sử dụng tài nguyên hệ thống (CPU, bộ nhớ) một cách tối ưu.
- **Tính linh hoạt (Flexibility):** Dễ dàng thích ứng với các thay đổi trong tương lai.
- **Tính nhất quán (Consistency):** Sử dụng các quy tắc đặt tên, phong cách thiết kế và các mẫu một cách đồng bộ trong toàn bộ hệ thống.
- **Tính đơn giản (Simplicity):** Thiết kế nên đơn giản nhất có thể nhưng vẫn đảm bảo giải quyết được vấn đề (theo nguyên lý KISS).

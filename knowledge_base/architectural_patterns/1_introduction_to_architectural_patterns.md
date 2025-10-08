# Giới thiệu về Mẫu Kiến trúc (Architectural Patterns)

---

## 1. Mẫu Kiến trúc là gì?

**Mẫu Kiến trúc (Architectural Pattern)** là một giải pháp tổng thể, có thể tái sử dụng để giải quyết các vấn đề thường gặp trong quá trình thiết kế kiến trúc phần mềm trong một bối cảnh nhất định.

Hãy tưởng tượng bạn đang xây dựng một thành phố. Mẫu kiến trúc không phải là bản vẽ chi tiết của từng ngôi nhà, mà là **quy hoạch tổng thể của thành phố**:

- Khu dân cư ở đâu?
- Khu công nghiệp ở đâu?
- Hệ thống đường sá, điện, nước kết nối chúng như thế nào?

Tương tự, trong phần mềm, mẫu kiến trúc quyết định "bộ xương" của hệ thống, cách các thành phần chính được tổ chức và cách chúng tương tác với nhau. Nó là quyết định thiết kế ở cấp độ cao nhất.

## 2. Tại sao Mẫu Kiến trúc lại quan trọng?

Việc lựa chọn một mẫu kiến trúc phù hợp ngay từ đầu sẽ ảnh hưởng sâu sắc đến toàn bộ dự án:

- **Chất lượng hệ thống:** Ảnh hưởng trực tiếp đến các thuộc tính chất lượng như hiệu năng (performance), khả năng mở rộng (scalability), độ tin cậy (reliability), và tính bảo mật (security).
- **Năng suất phát triển:** Cung cấp một bộ khung và các quy tắc rõ ràng, giúp đội ngũ phát triển làm việc nhất quán và hiệu quả hơn.
- **Khả năng bảo trì và phát triển:** Một kiến trúc tốt giúp hệ thống dễ dàng sửa lỗi, nâng cấp và thêm tính năng mới trong tương lai.
- **Giao tiếp hiệu quả:** Cung cấp một "ngôn ngữ chung" cho các kiến trúc sư và nhà phát triển. Khi nói "chúng ta dùng kiến trúc Microservices", mọi người đều hiểu ngay cấu trúc và các ràng buộc cơ bản của hệ thống.

## 3. So sánh Mẫu Kiến trúc và Mẫu Thiết kế

Đây là một điểm rất quan trọng và thường gây nhầm lẫn.

| Tiêu chí       | **Mẫu Kiến trúc (Architectural Pattern)**                                       | **Mẫu Thiết kế (Design Pattern)**                                                                                            |
| :------------- | :------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------- |
| **Phạm vi**    | **Toàn bộ hệ thống.** Quyết định cấu trúc vĩ mô, cách các module lớn tương tác. | **Một phần cụ thể của hệ thống.** Giải quyết vấn đề thiết kế trong một module, giữa các lớp (class) hoặc đối tượng (object). |
| **Cấp độ**     | **Chiến lược (Strategic).** Là quyết định ở cấp độ cao nhất, khó thay đổi.      | **Chiến thuật (Tactical).** Là quyết định ở cấp độ chi tiết, có thể áp dụng và thay đổi linh hoạt hơn.                       |
| **Ví dụ**      | - Microservices<br>- Monolithic<br>- Client-Server<br>- Event-Driven            | - Singleton<br>- Factory Method<br>- Adapter<br>- Observer                                                                   |
| **Phép ẩn dụ** | **Quy hoạch thành phố.**                                                        | **Bản vẽ thiết kế một ngôi nhà cụ thể (nhà bếp, phòng khách...).**                                                           |

**Mối quan hệ:** Một mẫu kiến trúc có thể sử dụng nhiều mẫu thiết kế khác nhau bên trong nó.

- Ví dụ, trong một hệ thống có **kiến trúc Microservices**, mỗi service riêng lẻ có thể sử dụng **mẫu thiết kế Singleton** để quản lý kết nối cơ sở dữ liệu hoặc **mẫu Observer** để thông báo các thay đổi trạng thái nội bộ.

---

Việc hiểu và lựa chọn đúng mẫu kiến trúc là một trong những kỹ năng quan trọng nhất của một kỹ sư phần mềm, quyết định sự thành bại lâu dài của một dự án.

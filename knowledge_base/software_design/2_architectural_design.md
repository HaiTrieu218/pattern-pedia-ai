# Thiết kế Kiến trúc (Architectural Design)

---

## 1. Định nghĩa (Definition)

**Thiết kế Kiến trúc** là quá trình định nghĩa một tập hợp các thành phần phần mềm, các thuộc tính hữu hình bên ngoài của chúng, và mối quan hệ giữa chúng ở mức độ cao. Nó là "bản vẽ tổng thể" của hệ thống, tập trung vào việc hệ thống sẽ được cấu trúc như thế nào thay vì đi sâu vào chi tiết hiện thực của từng thành phần.

Thiết kế kiến trúc là một trong những quyết định kỹ thuật sớm nhất và quan trọng nhất trong vòng đời phát triển phần mềm, vì nó đặt nền móng cho tất cả các hoạt động thiết kế và lập trình sau này.

---

## 2. Mục tiêu (Goals)

Mục tiêu chính của thiết kế kiến trúc bao gồm:

- **Xác định cấu trúc tổng thể:** Chia hệ thống thành các hệ thống con (sub-systems) hoặc các thành phần (components) chính.
- **Phân bổ trách nhiệm:** Chỉ định trách nhiệm cho từng hệ thống con, quyết định thành phần nào sẽ làm gì.
- **Định nghĩa giao diện và tương tác:** Xác định cách các thành phần giao tiếp và tương tác với nhau.
- **Đáp ứng các thuộc tính phi chức năng:** Đảm bảo hệ thống đáp ứng được các yêu cầu về hiệu năng (performance), bảo mật (security), độ tin cậy (reliability), khả năng mở rộng (scalability), và khả năng bảo trì (maintainability).
- **Tạo nền tảng cho thiết kế chi tiết:** Cung cấp một bộ khung vững chắc để các nhóm phát triển có thể tiến hành thiết kế chi tiết và lập trình một cách độc lập nhưng vẫn nhất quán.

---

## 3. Các quyết định chính trong Thiết kế Kiến trúc

Khi thực hiện thiết kế kiến trúc, kiến trúc sư phần mềm phải đưa ra một số quyết định quan trọng:

1.  **Sử dụng Mẫu Kiến trúc nào?** (Which Architectural Pattern to use?): Lựa chọn một mẫu kiến trúc phù hợp với bài toán (ví dụ: Monolith, Microservices, Client-Server). Đây là quyết định ảnh hưởng lớn nhất.
2.  **Phân rã hệ thống như thế nào?** (How to decompose the system?): Làm thế nào để chia nhỏ hệ thống thành các module, thành phần một cách logic và hiệu quả?
3.  **Chiến lược kiểm soát (Control Strategy):** Hệ thống sẽ được điều khiển theo kiểu tập trung (centralized) hay phi tập trung (decentralized)? Luồng điều khiển sẽ đi như thế nào?
4.  **Xử lý dữ liệu như thế nào?** (How to handle data?): Dữ liệu sẽ được lưu trữ và truy cập ra sao? Sử dụng cơ sở dữ liệu quan hệ hay NoSQL?
5.  **Công nghệ và Nền tảng (Technology Stack):** Lựa chọn ngôn ngữ lập trình, framework, cơ sở dữ liệu, và các nền tảng hạ tầng (ví dụ: cloud, on-premise) nào sẽ được sử dụng.

---

## 4. Mối quan hệ với các Giai đoạn khác

- **Với Phân tích Yêu cầu:** Thiết kế kiến trúc lấy các yêu cầu phi chức năng (non-functional requirements) làm đầu vào chính. Một yêu cầu về "hệ thống phải xử lý 1 triệu người dùng đồng thời" sẽ dẫn đến một kiến trúc hoàn toàn khác so với yêu cầu "hệ thống chỉ phục vụ 100 người dùng nội bộ".
- **Với Thiết kế Chi tiết:** Thiết kế kiến trúc là **đầu vào** cho thiết kế chi tiết. Sau khi có kiến trúc tổng thể, các lập trình viên sẽ đi vào thiết kế chi tiết cho từng thành phần đã được định nghĩa.
- **Với Các Mẫu Kiến trúc (Architectural Patterns):** Các mẫu kiến trúc (PHẦN VII) chính là các "giải pháp mẫu" đã được chứng minh để giải quyết các vấn đề trong giai đoạn thiết kế kiến trúc.

---

## 5. Ví dụ (Example)

Hãy xem xét việc thiết kế kiến trúc cho một trang web thương mại điện tử đơn giản:

1.  **Quyết định Mẫu Kiến trúc:** Chọn kiến trúc `Client-Server` 3 lớp (3-Tier).
2.  **Phân rã Hệ thống:**
    - **Lớp Trình diễn (Presentation Layer):** Giao diện người dùng web (HTML, CSS, JavaScript). Chịu trách nhiệm hiển thị sản phẩm, giỏ hàng...
    - **Lớp Nghiệp vụ (Business Logic Layer):** Server xử lý các logic chính như quản lý người dùng, xử lý đơn hàng, quản lý sản phẩm.
    - **Lớp Dữ liệu (Data Layer):** Hệ quản trị cơ sở dữ liệu (ví dụ: MySQL) để lưu trữ thông tin sản phẩm, người dùng, đơn hàng.
3.  **Định nghĩa Tương tác:**
    - Client (trình duyệt) sẽ gửi các yêu cầu HTTP đến Lớp Nghiệp vụ.
    - Lớp Nghiệp vụ sẽ truy vấn hoặc cập nhật dữ liệu từ Lớp Dữ liệu.
    - Lớp Dữ liệu trả kết quả về cho Lớp Nghiệp vụ.
    - Lớp Nghiệp vụ xử lý và trả về kết quả (dưới dạng HTML hoặc JSON) cho Lớp Trình diễn.

Bản thiết kế này cung cấp một cái nhìn tổng quan, rõ ràng về cách hệ thống được cấu trúc mà chưa cần quan tâm đến việc `class Product` sẽ có những phương thức nào.

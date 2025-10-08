# Bảo trì Phần mềm (Software Maintenance)

---

## 1. Định nghĩa

**Bảo trì Phần mềm** là tập hợp tất cả các hoạt động cần thiết để sửa đổi một sản phẩm phần mềm _sau khi_ nó đã được bàn giao cho khách hàng hoặc triển khai ra môi trường thực tế. Đây là giai đoạn dài nhất và thường tốn kém nhất trong vòng đời của một phần mềm, chiếm từ 60% đến 80% tổng chi phí.

Mục tiêu của bảo trì không chỉ là sửa lỗi, mà còn là cải tiến chức năng, nâng cao hiệu suất và đảm bảo phần mềm có thể thích ứng với những thay đổi của môi trường bên ngoài.

---

## 2. Vấn đề giải quyết

Một phần mềm sau khi được phát hành sẽ phải đối mặt với một thế giới luôn thay đổi:

- **Lỗi tiềm ẩn:** Không có phần mềm nào là hoàn hảo. Các lỗi không được phát hiện trong giai đoạn kiểm thử sẽ xuất hiện khi người dùng thực tế sử dụng.
- **Thay đổi Môi trường:** Hệ điều hành được nâng cấp, các thư viện bên thứ ba thay đổi, các API bên ngoài không còn được hỗ trợ, hoặc phần cứng mới ra đời. Phần mềm cần phải thích ứng để tiếp tục hoạt động.
- **Yêu cầu mới từ người dùng:** Sau một thời gian sử dụng, người dùng sẽ có những ý tưởng mới, mong muốn thêm chức năng hoặc cải thiện những tính năng hiện có để công việc của họ hiệu quả hơn.
- **Sự "xuống cấp" của thiết kế:** Code và kiến trúc ban đầu có thể trở nên lỗi thời, khó hiểu và khó thay đổi sau nhiều lần sửa đổi, làm chậm quá trình phát triển trong tương lai.

Bảo trì phần mềm giải quyết tất cả những vấn đề này để đảm bảo sản phẩm luôn hữu ích, ổn định và có giá trị theo thời gian.

---

## 3. Các loại hình Bảo trì

Bảo trì phần mềm được phân thành bốn loại chính:

### a. Bảo trì Sửa lỗi (Corrective Maintenance)

- **Mục tiêu:** Sửa các lỗi (bugs), sai sót hoặc khiếm khuyết được người dùng hoặc hệ thống giám sát phát hiện ra sau khi sản phẩm đã được triển khai.
- **Ví dụ:** Người dùng báo cáo rằng ứng dụng bị treo khi bấm vào một nút nhất định. Đội phát triển sẽ tìm nguyên nhân và phát hành một bản vá lỗi.

### b. Bảo trì Thích ứng (Adaptive Maintenance)

- **Mục tiêu:** Sửa đổi phần mềm để nó có thể hoạt động ổn định trong một môi trường đã thay đổi (cả về phần cứng lẫn phần mềm).
- **Ví dụ:**
  - Cập nhật ứng dụng di động để tương thích với phiên bản iOS hoặc Android mới nhất.
  - Thay đổi cách gọi API thanh toán vì nhà cung cấp dịch vụ đã nâng cấp hệ thống của họ.

### c. Bảo trì Hoàn thiện (Perfective Maintenance)

- **Mục tiêu:** Nâng cấp và cải tiến phần mềm bằng cách thêm các chức năng mới hoặc cải thiện các tính năng hiện có dựa trên phản hồi của người dùng. Loại bảo trì này chiếm tỷ trọng lớn nhất (hơn 50%).
- **Ví dụ:**
  - Thêm chức năng "Xuất báo cáo ra file Excel" cho một phần mềm quản lý.
  - Cải thiện tốc độ tải của trang chủ để mang lại trải nghiệm tốt hơn.

### d. Bảo trì Phòng ngừa (Preventive Maintenance)

- **Mục tiêu:** Chủ động thay đổi phần mềm để làm cho nó dễ bảo trì hơn trong tương lai, ngay cả khi chưa có lỗi nào xảy ra.
- **Ví dụ:**
  - **Tái cấu trúc (Refactoring):** Viết lại một đoạn code phức tạp, khó đọc để nó trở nên rõ ràng và dễ hiểu hơn.
  - **Cập nhật tài liệu:** Bổ sung comment, viết lại tài liệu kỹ thuật để các lập trình viên mới có thể dễ dàng tiếp cận.

---

## 4. Thách thức trong Bảo trì

- **Hiểu code của người khác:** Thường thì người bảo trì không phải là người viết ra đoạn code đó.
- **Tài liệu thiếu hoặc lỗi thời:** Gây khó khăn trong việc tìm hiểu hệ thống.
- **Tác động phụ:** Một thay đổi nhỏ ở một nơi có thể gây ra lỗi không mong muốn ở một nơi khác trong hệ thống (testing hồi quy là rất quan trọng).
- **Chi phí cao và ít được coi trọng:** Ban lãnh đạo thường ưu tiên phát triển tính năng mới hơn là các hoạt động bảo trì.

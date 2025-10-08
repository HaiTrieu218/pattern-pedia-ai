# Các Loại Yêu cầu trong Công nghệ Phần mềm

Trong Kỹ nghệ Yêu cầu (Requirements Engineering), việc phân loại các yêu cầu giúp chúng ta hiểu rõ hơn về các khía cạnh khác nhau của hệ thống cần xây dựng. Về cơ bản, yêu cầu được chia thành hai nhóm chính: **Yêu cầu Chức năng (Functional Requirements)** và **Yêu cầu Phi chức năng (Non-functional Requirements)**.

---

## 1. Yêu cầu Chức năng (Functional Requirements)

### Định nghĩa

**Yêu cầu Chức năng** mô tả những gì hệ thống **phải làm** (what the system should do). Chúng định nghĩa các chức năng, dịch vụ, hành vi cụ thể của phần mềm mà người dùng có thể tương tác hoặc quan sát được.

Nói cách khác, nếu thiếu một yêu cầu chức năng, hệ thống sẽ không thể thực hiện được nhiệm vụ cốt lõi của nó.

### Đặc điểm

- Mô tả hành vi của hệ thống dưới một điều kiện cụ thể.
- Thường được diễn đạt dưới dạng: "Hệ thống phải cho phép người dùng [làm một việc gì đó]".
- Có thể kiểm tra được một cách rõ ràng (hành động đó thực hiện được hoặc không).

### Ví dụ

Đối với một hệ thống **Thương mại Điện tử**:

- Hệ thống phải cho phép người dùng tìm kiếm sản phẩm theo tên hoặc danh mục.
- Người dùng phải có thể thêm sản phẩm vào giỏ hàng.
- Hệ thống phải tính toán tổng giá trị đơn hàng, bao gồm cả thuế và phí vận chuyển.
- Người dùng phải có thể thanh toán đơn hàng bằng thẻ tín dụng hoặc ví điện tử.
- Hệ thống phải gửi email xác nhận cho người dùng sau khi đặt hàng thành công.

---

## 2. Yêu cầu Phi chức năng (Non-functional Requirements - NFRs)

### Định nghĩa

**Yêu cầu Phi chức năng** mô tả hệ thống **phải như thế nào** (how the system should be). Chúng không mô tả một chức năng cụ thể, mà định nghĩa các thuộc tính, ràng buộc và tiêu chuẩn chất lượng mà hệ thống phải tuân thủ.

Chúng thường được gọi là các yêu cầu về chất lượng (quality attributes) của hệ thống. Nếu thiếu một yêu cầu phi chức năng, hệ thống vẫn có thể hoạt động, nhưng có thể sẽ chạy rất chậm, không an toàn, hoặc khó sử dụng.

### Đặc điểm

- Mô tả các đặc tính như hiệu năng, độ tin cậy, bảo mật, tính khả dụng.
- Thường khó đo lường hơn yêu cầu chức năng và cần được định nghĩa một cách cụ thể.
- Ví dụ, thay vì nói "Hệ thống phải nhanh", hãy nói "Thời gian phản hồi của trang tìm kiếm phải dưới 2 giây với 1000 người dùng truy cập đồng thời".

### Các loại Yêu cầu Phi chức năng phổ biến

| Loại                                 | Mô tả                                                                | Ví dụ                                                                                                                                                        |
| :----------------------------------- | :------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Hiệu năng (Performance)**          | Tốc độ phản hồi, thông lượng, khả năng chịu tải của hệ thống.        | - Trang chủ phải tải hoàn toàn trong vòng 3 giây.<br>- Hệ thống phải xử lý được 500 giao dịch mỗi phút.                                                      |
| **Bảo mật (Security)**               | Các yêu cầu về xác thực, phân quyền, mã hóa, chống tấn công.         | - Mật khẩu người dùng phải được mã hóa bằng thuật toán SHA-256.<br>- Người dùng chỉ có thể xem lịch sử đơn hàng của chính mình.                              |
| **Độ tin cậy (Reliability)**         | Khả năng hệ thống hoạt động liên tục mà không gặp lỗi.               | - Hệ thống phải có thời gian hoạt động (uptime) đạt 99.9%.<br>- Tỷ lệ lỗi giao dịch phải thấp hơn 0.01%.                                                     |
| **Tính khả dụng (Usability)**        | Mức độ dễ dàng và thuận tiện khi người dùng học và sử dụng hệ thống. | - Một người dùng mới phải có thể hoàn thành việc đặt hàng trong vòng 5 phút.<br>- Giao diện phải tương thích với các trình đọc màn hình cho người khiếm thị. |
| **Tính tương thích (Compatibility)** | Khả năng hệ thống hoạt động tốt trên các môi trường khác nhau.       | - Ứng dụng web phải hoạt động tốt trên các trình duyệt Chrome, Firefox và Safari phiên bản mới nhất.                                                         |
| **Tính bảo trì (Maintainability)**   | Mức độ dễ dàng trong việc sửa lỗi, nâng cấp hoặc cải tiến hệ thống.  | - Mã nguồn phải tuân thủ theo chuẩn code convention PEP 8 của Python.                                                                                        |

---

## 3. Yêu cầu Tên miền (Domain Requirements)

### Định nghĩa

**Yêu cầu Tên miền** là các yêu cầu xuất phát từ lĩnh vực hoạt động (domain) của ứng dụng. Chúng có thể là yêu cầu chức năng hoặc phi chức năng, nhưng chúng phản ánh các quy tắc, luật lệ, hoặc tiêu chuẩn của ngành đó.

### Ví dụ

- **Hệ thống quản lý bệnh viện:** "Hệ thống phải tuân thủ theo tiêu chuẩn bảo mật thông tin y tế HIPAA." (Đây là một yêu cầu pháp lý của ngành y tế).
- **Phần mềm kế toán:** "Công thức tính khấu hao tài sản cố định phải theo đúng chuẩn mực kế toán Việt Nam (VAS)."
- **Ứng dụng đặt vé máy bay:** "Một hành khách không được phép đặt quá 9 ghế trong một lần giao dịch." (Đây là quy định của ngành hàng không).

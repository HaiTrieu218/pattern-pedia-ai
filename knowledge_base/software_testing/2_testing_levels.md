# Các Cấp độ Kiểm thử (Software Testing Levels)

## 1. Định nghĩa

Các cấp độ kiểm thử (Testing Levels) là một quy trình phân cấp nhằm xác minh hiệu suất và chức năng của một phần mềm ở các giai đoạn khác nhau của Vòng đời Phát triển Phần mềm (SDLC). Mỗi cấp độ kiểm thử tập trung vào một phạm vi cụ thể của hệ thống, từ thành phần nhỏ nhất cho đến toàn bộ ứng dụng, nhằm phát hiện lỗi sớm và đảm bảo chất lượng tổng thể.

Bốn cấp độ kiểm thử chính thường được sắp xếp theo mô hình Kim tự tháp Kiểm thử (Test Pyramid), bao gồm: Unit Testing, Integration Testing, System Testing, và Acceptance Testing.

## 2. Các Cấp độ Chi tiết

### 2.1. Kiểm thử Đơn vị (Unit Testing)

- **Mục tiêu:** Kiểm tra từng thành phần (unit) hoặc module nhỏ nhất của mã nguồn một cách độc lập. Một "unit" thường là một hàm, một phương thức, một lớp, hoặc một đối tượng.
- **Người thực hiện:** Lập trình viên (Developer).
- **Thời điểm:** Trong suốt quá trình lập trình.
- **Đặc điểm:**

  - **Phạm vi:** Rất nhỏ và cô lập. Thường sử dụng các kỹ thuật "mocking" hoặc "stubbing" để giả lập các thành phần phụ thuộc bên ngoài (ví dụ: database, API).
  - **Tốc độ:** Rất nhanh. Có thể chạy hàng trăm hoặc hàng nghìn test case trong vài giây.
  - **Mục đích:** Đảm bảo logic bên trong của từng unit hoạt động chính xác theo thiết kế.

- **Ví dụ:**
  - Viết một test case để kiểm tra hàm `calculate_discount(price, percentage)` trả về kết quả đúng với các giá trị đầu vào khác nhau (số dương, số không, số âm).
  - Kiểm tra một phương thức `user.is_password_valid()` trả về `True` khi mật khẩu hợp lệ và `False` khi không hợp lệ.

### 2.2. Kiểm thử Tích hợp (Integration Testing)

- **Mục tiêu:** Kiểm tra sự tương tác và giao tiếp giữa các unit hoặc module đã được kiểm thử đơn vị. Mục đích là để phát hiện các lỗi khi các thành phần này được kết hợp lại với nhau.
- **Người thực hiện:** Lập trình viên hoặc Kỹ sư QA (QA Engineer).
- **Thời điểm:** Sau khi các unit liên quan đã vượt qua Unit Test.
- **Đặc điểm:**

  - **Phạm vi:** Tập trung vào các giao diện (interfaces) và luồng dữ liệu giữa các module.
  - **Tốc độ:** Chậm hơn Unit Testing.
  - **Mục đích:** Phát hiện các lỗi như: dữ liệu truyền sai định dạng, các lời gọi API không chính xác, lỗi tương tác với database.

- **Ví dụ:**
  - Kiểm tra luồng "Thêm sản phẩm vào giỏ hàng": Module `ProductPage` gọi đến module `ShoppingCartService`. Test case sẽ xác nhận rằng khi người dùng bấm nút "Thêm vào giỏ", sản phẩm đó thực sự được thêm vào dữ liệu của giỏ hàng.

### 2.3. Kiểm thử Hệ thống (System Testing)

- **Mục tiêu:** Kiểm tra toàn bộ hệ thống phần mềm đã được tích hợp hoàn chỉnh để xác minh rằng nó đáp ứng các yêu cầu chức năng và phi chức năng đã được đặc tả.
- **Người thực hiện:** Kỹ sư QA.
- **Thời điểm:** Sau khi toàn bộ hệ thống đã được tích hợp và vượt qua Integration Test.
- **Đặc điểm:**

  - **Phạm vi:** Toàn bộ ứng dụng, từ đầu đến cuối (end-to-end). Kiểm thử được thực hiện trong một môi trường gần giống với môi trường thực tế nhất có thể.
  - **Tốc độ:** Chậm. Mỗi test case có thể mất vài giây đến vài phút.
  - **Mục đích:** Đảm bảo hệ thống hoạt động như một thể thống nhất, đáp ứng các yêu cầu về nghiệp vụ, hiệu năng, bảo mật, và khả năng sử dụng. Đây là kiểm thử hộp đen (black-box testing).

- **Ví dụ:**
  - Thực hiện một kịch bản người dùng hoàn chỉnh: Đăng nhập, tìm kiếm sản phẩm, thêm vào giỏ hàng, nhập địa chỉ giao hàng, thanh toán và đăng xuất. Toàn bộ luồng phải hoạt động chính xác.
  - Kiểm tra hiệu năng: Hệ thống có thể xử lý 100 người dùng truy cập cùng lúc không?

### 2.4. Kiểm thử Chấp nhận (Acceptance Testing)

- **Mục tiêu:** Xác minh rằng hệ thống đáp ứng các tiêu chí chấp nhận và các yêu cầu kinh doanh của khách hàng hoặc người dùng cuối. Đây là cấp độ kiểm thử cuối cùng trước khi sản phẩm được phát hành.
- **Người thực hiện:** Khách hàng (Client), Người dùng cuối (End-user), hoặc đội QA đại diện cho người dùng.
- **Thời điểm:** Sau khi hệ thống đã vượt qua System Test.
- **Đặc điểm:**

  - **Phạm vi:** Tập trung vào góc nhìn của người dùng và mục tiêu kinh doanh. "Hệ thống có giải quyết được vấn đề của tôi không?"
  - **Các loại phổ biến:**
    - **User Acceptance Testing (UAT):** Người dùng cuối trực tiếp sử dụng sản phẩm để xem nó có đáp ứng nhu cầu của họ trong môi trường làm việc thực tế hay không.
    - **Alpha Testing & Beta Testing:** Phát hành sản phẩm cho một nhóm người dùng hạn chế (Alpha) hoặc một cộng đồng lớn hơn (Beta) để thu thập phản hồi.

- **Ví dụ:**
  - Một nhân viên kế toán sử dụng chức năng "Xuất báo cáo tháng" và xác nhận rằng báo cáo được tạo ra đúng định dạng và chứa đủ các thông tin cần thiết cho công việc của họ.

## 3. Mô hình Kim tự tháp Kiểm thử (Test Pyramid)

Kim tự tháp Kiểm thử là một mô hình trực quan hóa chiến lược kiểm thử hiệu quả. Nó gợi ý rằng một bộ kiểm thử (test suite) nên có:

- **Nhiều** bài kiểm thử ở tầng đáy (Unit Tests) vì chúng nhanh, ổn định và chi phí thấp.
- **Ít hơn** bài kiểm thử ở tầng giữa (Integration Tests).
- **Rất ít** bài kiểm thử ở tầng đỉnh (System/E2E Tests) vì chúng chậm, dễ bị lỗi và chi phí cao.

![Minh họa Kim tự tháp Kiểm thử](https://martinfowler.com/bliki/images/testPyramid/test-pyramid.png)

Việc tuân theo mô hình này giúp phát hiện lỗi sớm nhất có thể ở các cấp độ thấp, giảm thiểu chi phí và thời gian sửa lỗi.

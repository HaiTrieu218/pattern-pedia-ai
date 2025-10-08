# Mô hình Chế tạo mẫu (Prototyping Model)

## 1. Định nghĩa

Mô hình Chế tạo mẫu (Prototyping Model) là một mô hình phát triển phần mềm trong đó một **bản mẫu (prototype)** – phiên bản sớm, chưa hoàn chỉnh của hệ thống – được xây dựng, thử nghiệm, và tinh chỉnh dựa trên phản hồi của khách hàng trước khi bắt đầu phát triển sản phẩm cuối cùng.

Mục tiêu chính của mô hình này là để **làm rõ các yêu cầu** và **giảm thiểu rủi ro hiểu sai ý tưởng** của khách hàng ngay từ giai đoạn đầu. Nó trả lời cho câu hỏi: "Đây có đúng là thứ bạn muốn chúng tôi xây dựng không?".

## 2. Sơ đồ các bước thực hiện

Mô hình này hoạt động theo một vòng lặp gồm các bước sau:

_(Lưu ý: Bạn có thể tìm một hình ảnh sơ đồ khác và thay link vào đây)_

1.  **Thu thập Yêu cầu ban đầu (Requirements Gathering):** Thu thập các yêu cầu cơ bản và tổng quan nhất từ khách hàng để có cái nhìn ban đầu về hệ thống.
2.  **Thiết kế Nhanh (Quick Design):** Thực hiện một bản thiết kế đơn giản, chỉ tập trung vào các khía cạnh mà người dùng cuối có thể thấy được, như giao diện người dùng (UI) và luồng xử lý chính.
3.  **Xây dựng Bản mẫu (Build Prototype):** Dựa trên thiết kế nhanh, các nhà phát triển xây dựng một phiên bản mô phỏng của hệ thống. Bản mẫu này có thể chỉ là các bản vẽ trên giấy, các màn hình giao diện có thể click được, hoặc một chương trình có chức năng hạn chế.
4.  **Khách hàng Đánh giá (Customer Evaluation):** Trình bày bản mẫu cho khách hàng hoặc người dùng cuối. Họ sẽ sử dụng thử và đưa ra các phản hồi, góp ý, hoặc yêu cầu thay đổi.
5.  **Tinh chỉnh và Lặp lại (Refine and Iterate):** Dựa trên phản hồi, đội phát triển sẽ tinh chỉnh lại yêu cầu và cập nhật bản mẫu. Vòng lặp này (bước 3, 4, 5) tiếp tục cho đến khi khách hàng hoàn toàn hài lòng với bản mẫu.
6.  **Phát triển Sản phẩm Cuối cùng (Implement Final Product):** Khi bản mẫu đã được duyệt, nó sẽ trở thành "bản thiết kế" cho sản phẩm cuối cùng. Đội phát triển sẽ bắt đầu xây dựng sản phẩm hoàn chỉnh dựa trên các yêu cầu đã được làm rõ.

## 3. Các loại Prototyping

- **Throwaway Prototyping (Bản mẫu "vứt bỏ"):** Bản mẫu được tạo ra nhanh chóng chỉ để làm rõ yêu cầu, sau đó sẽ bị "vứt đi". Sản phẩm cuối cùng được phát triển lại từ đầu dựa trên những gì đã học được.
- **Evolutionary Prototyping (Bản mẫu tiến hóa):** Bản mẫu ban đầu được xây dựng một cách cẩn thận và sẽ được "tiến hóa" dần dần, thêm các chức năng mới qua mỗi vòng lặp để cuối cùng trở thành sản phẩm hoàn chỉnh.
- **Incremental Prototyping (Bản mẫu tăng tiến):** Xây dựng nhiều bản mẫu nhỏ, mỗi bản mẫu thể hiện một chức năng riêng biệt của hệ thống. Cuối cùng, các bản mẫu này được ghép lại với nhau.

## 4. Ưu điểm (Advantages)

- **Giảm rủi ro hiểu sai yêu cầu:** Khách hàng được "nhìn tận mắt, sờ tận tay" sản phẩm từ sớm, giúp phát hiện các hiểu lầm về yêu cầu ngay lập tức.
- **Tăng sự tham gia của khách hàng:** Khách hàng cảm thấy được tham gia vào quá trình phát triển và sản phẩm cuối cùng thường đáp ứng đúng nhu-cầu của họ hơn.
- **Phát hiện sớm các vấn đề về thiết kế:** Các vấn đề về luồng sử dụng (usability) hoặc thiết kế giao diện có thể được phát hiện và sửa chữa dễ dàng.
- **Phản hồi nhanh:** Đội phát triển nhận được phản hồi giá trị một cách nhanh chóng để cải thiện sản phẩm.

## 5. Nhược điểm (Disadvantages)

- **Tăng chi phí và thời gian:** Việc xây dựng bản mẫu có thể làm tăng tổng chi phí và kéo dài thời gian của dự án nếu không được quản lý tốt.
- **Khách hàng có thể hiểu lầm:** Khách hàng có thể nhìn vào bản mẫu (vốn được làm nhanh) và nghĩ rằng sản phẩm gần như đã hoàn thành, dẫn đến kỳ vọng không thực tế về thời gian giao hàng.
- **Nhà phát triển có thể "lười":** Với Evolutionary Prototyping, nhà phát triển có thể bị cám dỗ sử dụng các giải pháp kỹ thuật chưa tối ưu trong bản mẫu cho sản phẩm cuối cùng, dẫn đến chất lượng code kém.
- **Khó quản lý:** Vòng đời của dự án trở nên khó dự đoán hơn so-với mô hình Thác nước.

## 6. Khi nào nên sử dụng?

- Khi yêu cầu của hệ thống **chưa rõ ràng, mơ hồ** hoặc có khả năng thay đổi cao.
- Các dự án có nhiều tương tác với người dùng, đặc biệt là các dự án có **giao diện người dùng (UI) phức tạp**.
- Khi cần phát triển một sản phẩm hoàn toàn mới, chưa có tiền lệ trên thị trường.

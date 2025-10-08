# Phân phối & Triển khai Liên tục (Continuous Delivery & Continuous Deployment - CD)

---

## 1. Định nghĩa

**Phân phối & Triển khai Liên tục (CD)** là một tập hợp các thực hành trong phát triển phần mềm, nơi các thay đổi về code—bao gồm tính năng mới, sửa lỗi, và các thay đổi cấu hình—được tự động chuẩn bị và phát hành đến môi trường sản phẩm (production) một cách an toàn và nhanh chóng.

CD là bước tiếp theo một cách logic sau Tích hợp Liên tục (CI). Trong khi CI đảm bảo code luôn ở trạng thái "build" được và đã qua kiểm thử đơn vị, thì CD sẽ tự động hóa quá trình phát hành những thay đổi đó.

## 2. Vấn đề giải quyết

Trong các quy trình truyền thống, việc "phát hành" (release) một phiên bản mới thường là một sự kiện lớn, căng thẳng, tốn nhiều công sức và tiềm ẩn nhiều rủi ro. Các vấn đề thường gặp là:

- **Quy trình thủ công phức tạp:** Yêu cầu nhiều bước thực hiện bằng tay, dễ gây ra lỗi của con người (human error).
- **Thời gian chết (Downtime):** Việc triển khai phiên bản mới có thể yêu cầu phải tạm dừng hệ thống.
- **Khó khăn khi sửa lỗi:** Nếu phiên bản mới có lỗi nghiêm trọng, việc quay trở lại (rollback) phiên bản ổn định trước đó rất phức tạp và tốn thời gian.
- **Vòng lặp phản hồi chậm:** Mất hàng tuần hoặc hàng tháng để một tính năng mới từ lúc hoàn thành code đến tay người dùng cuối.

## 3. Giải pháp

CD giải quyết các vấn đề trên bằng cách tự động hóa "đường ống" (pipeline) phát hành. Một pipeline CD điển hình sẽ trông như sau:

**Build -> Test -> Release -> Deploy**

Mỗi khi một thay đổi vượt qua tất cả các giai đoạn kiểm thử tự động trong CI, pipeline CD sẽ:

1.  **Tự động build** gói phần mềm (artifact) sẵn sàng để phát hành.
2.  **Tự động triển khai** gói phần mềm đó lên một môi trường tương tự môi trường production (ví dụ: Staging, UAT) để thực hiện các bài kiểm thử chấp nhận tự động.
3.  Nếu tất cả các bước đều thành công, phần mềm được xem là **"sẵn sàng để phát hành"**.

Tại đây, có một sự khác biệt quan trọng giữa **Continuous Delivery** và **Continuous Deployment**.

### 3.1. Phân phối Liên tục (Continuous Delivery)

![Continuous Delivery Pipeline](https://example.com/continuous_delivery.png)
_(Lưu ý: Bạn nên tìm một hình ảnh minh họa phù hợp để thay vào đây)_

Trong Continuous Delivery, sau khi tất cả các kiểm thử tự động đã qua, việc triển khai lên môi trường production cuối cùng **yêu cầu một sự phê duyệt thủ công**. Đây thường là một nút bấm do người quản lý sản phẩm (Product Manager) hoặc trưởng nhóm kỹ thuật (Tech Lead) quyết định.

- **Khi nào nên bấm nút:** Việc này thường được quyết định dựa trên các yếu tố kinh doanh, như thời điểm ra mắt chiến dịch marketing, hoặc sau khi đã hoàn thành một nhóm các tính năng có liên quan.

### 3.2. Triển khai Liên tục (Continuous Deployment)

![Continuous Deployment Pipeline](https://example.com/continuous_deployment.png)
_(Lưu ý: Bạn nên tìm một hình ảnh minh họa phù hợp để thay vào đây)_

Continuous Deployment là bước tiến xa hơn. Nếu một thay đổi đã vượt qua tất cả các bài kiểm thử tự động, nó sẽ được **tự động triển khai thẳng lên môi trường production mà không cần bất kỳ sự can thiệp nào của con người**.

- **Điều kiện:** Để làm được điều này, hệ thống kiểm thử tự động phải cực kỳ toàn diện và đáng tin cậy. Các công ty lớn như Amazon, Netflix, Google thường triển khai code lên production hàng trăm, thậm chí hàng ngàn lần mỗi ngày bằng phương pháp này.

## 4. Ưu điểm

- **Giảm rủi ro:** Phát hành các thay đổi nhỏ, thường xuyên sẽ ít rủi ro hơn là phát hành một bản cập nhật khổng lồ. Việc xác định và sửa lỗi cũng dễ dàng hơn nhiều.
- **Tăng tốc độ phát hành:** Các tính năng mới đến tay người dùng nhanh hơn, giúp công ty có lợi thế cạnh tranh.
- **Tăng năng suất cho lập trình viên:** Tự động hóa các công việc lặp đi lặp lại, giúp lập trình viên tập trung vào việc viết code và tạo ra giá trị.
- **Tăng độ tin cậy:** Quy trình phát hành được tiêu chuẩn hóa và tự động hóa giúp giảm thiểu lỗi do con người.

## 5. Nhược điểm

- **Yêu cầu văn hóa phù hợp:** Đòi hỏi sự tin tưởng cao và trách nhiệm lớn từ đội ngũ phát triển.
- **Đầu tư lớn vào tự động hóa kiểm thử:** Chất lượng của pipeline CD phụ thuộc hoàn toàn vào chất lượng của bộ kiểm thử tự động. Nếu kiểm thử không đủ tốt, lỗi có thể lọt ra môi trường production.
- **Phức tạp trong thiết lập ban đầu:** Xây dựng một pipeline CI/CD hoàn chỉnh đòi hỏi kiến thức chuyên môn và thời gian.

## 6. Ví dụ trong thực tế

Một nhóm phát triển đang làm việc trên một trang web thương mại điện tử.

1.  Một lập trình viên hoàn thành tính năng "Thêm sản phẩm vào Wishlist" và đẩy code lên Git.
2.  **(CI)** Hệ thống CI (ví dụ: GitHub Actions) tự động nhận diện thay đổi, build code và chạy tất cả các bài unit test và integration test. -> **Thành công.**
3.  **(CD - Delivery)** Pipeline CD tự động đóng gói ứng dụng và triển khai nó lên môi trường Staging. Một bộ kiểm thử giao diện tự động (ví dụ: Selenium) được chạy để giả lập hành vi người dùng thêm sản phẩm vào wishlist. -> **Thành công.**
4.  Lúc này, phiên bản mới ở trạng thái "sẵn sàng". Người Product Manager nhận được thông báo. Sau khi kiểm tra lại trên môi trường Staging và thấy tính năng hoạt động tốt, anh ấy bấm nút "Deploy to Production".
5.  Hệ thống tự động triển khai phiên bản mới lên server production. Người dùng cuối bây giờ đã có thể sử dụng tính năng Wishlist.

_(Nếu công ty này áp dụng Continuous Deployment, bước 4 sẽ được bỏ qua và hệ thống sẽ tự động triển khai ngay sau khi kiểm thử trên Staging thành công.)_

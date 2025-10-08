# Prototyping (Tạo mẫu thử)

## Định nghĩa

**Prototyping** là quá trình tạo ra một phiên bản mô phỏng hoặc một mô hình ban đầu của sản phẩm phần mềm. Mục tiêu chính của prototyping không phải là tạo ra một sản phẩm hoàn chỉnh, mà là để kiểm tra, xác thực các ý tưởng thiết kế, và thu thập phản hồi sớm từ các bên liên quan (stakeholders) và người dùng cuối trước khi đầu tư nhiều thời gian và công sức vào việc lập trình.

Hãy tưởng tượng bạn muốn xây một ngôi nhà. Thay vì xây ngay lập tức, kiến trúc sư sẽ tạo ra một mô hình 3D trên máy tính. Mô hình đó chính là một prototype.

## Vấn đề giải quyết

Prototyping giúp giải quyết các vấn đề cốt lõi sau:

1.  **Sự mơ hồ trong yêu cầu:** Khách hàng thường khó hình dung sản phẩm sẽ trông như thế nào và hoạt động ra sao chỉ qua các tài liệu văn bản. Một prototype giúp "hiện thực hóa" các yêu cầu đó.
2.  **Rủi ro thiết kế sai:** Phát hiện ra các lỗi về luồng sử dụng (user flow) hoặc các yếu tố giao diện khó dùng ở giai đoạn muộn sẽ cực kỳ tốn kém để sửa chữa.
3.  **Giao tiếp kém hiệu quả:** Một prototype là một "ngôn ngữ chung" giúp đội phát triển, nhà thiết kế và khách hàng có thể thảo luận và đóng góp ý kiến một cách trực quan.

## Các loại Prototype

Có nhiều cách phân loại, nhưng phổ biến nhất là dựa trên mức độ chi tiết và trung thực (fidelity) so với sản phẩm cuối cùng.

### 1. Low-fidelity Prototyping (Mẫu thử Chi tiết thấp)

Đây là các phiên bản đơn giản, nhanh chóng và chi phí thấp, thường không có tính tương tác cao.

- **Đặc điểm:**
  - Thường là bản vẽ tay trên giấy (sketches) hoặc các khung xương (wireframes) đơn giản được tạo bằng các công cụ như Balsamiq.
  - Tập trung vào cấu trúc, bố cục (layout) và luồng di chuyển giữa các màn hình.
  - Không quan tâm đến màu sắc, font chữ hay hình ảnh chi tiết.
- **Mục đích:** Kiểm tra ý tưởng tổng thể, sắp xếp các thành phần một cách logic.

### 2. High-fidelity Prototyping (Mẫu thử Chi tiết cao)

Đây là các phiên bản trông rất giống và hoạt động gần như sản phẩm thật.

- **Đặc điểm:**
  - Được tạo bằng các công cụ thiết kế chuyên nghiệp như Figma, Adobe XD, Sketch.
  - Bao gồm màu sắc, icon, font chữ, hình ảnh và thậm chí cả các hiệu ứng chuyển động (animation).
  - Có tính tương tác cao, người dùng có thể bấm vào các nút và di chuyển giữa các màn hình như đang dùng ứng dụng thật.
- **Mục đích:** Kiểm tra tính khả dụng (usability), thu thập phản hồi chi tiết về giao diện và trải nghiệm người dùng.

## Ưu điểm

- **Thu thập phản hồi sớm:** Giúp phát hiện các vấn đề và hiểu lầm về yêu cầu ngay từ đầu.
- **Tiết kiệm chi phí:** Sửa một bản thiết kế trên Figma rẻ và nhanh hơn rất nhiều so với việc sửa code đã được viết.
- **Tăng cường giao tiếp:** Tạo ra một điểm tham chiếu trực quan cho tất cả các bên liên quan.
- **Cải thiện trải nghiệm người dùng (UX):** Cho phép thử nghiệm và lặp lại các ý tưởng thiết kế để tìm ra giải pháp tốt nhất cho người dùng.

## Nhược điểm

- **Gây hiểu lầm cho khách hàng:** Khách hàng có thể nhìn vào một high-fidelity prototype và nghĩ rằng sản phẩm đã gần hoàn thành, dẫn đến kỳ vọng sai về thời gian bàn giao.
- **Tốn thời gian và nguồn lực:** Tạo ra một high-fidelity prototype chi tiết có thể tốn nhiều công sức.
- **Nhà phát triển có thể bị "bám" vào thiết kế:** Đôi khi, đội phát triển có thể cố gắng hiện thực hóa y hệt prototype mà bỏ qua các hạn chế về mặt kỹ thuật.

## Ví dụ thực tế

Một nhóm phát triển ứng dụng đặt đồ ăn muốn thiết kế quy trình thanh toán.

1.  **Low-fidelity:** Họ vẽ tay 3 màn hình ra giấy: "Giỏ hàng", "Nhập thông tin giao hàng", và "Chọn phương thức thanh toán". Họ trình bày luồng này cho cả nhóm để đảm bảo không ai bị nhầm lẫn về các bước.
2.  **High-fidelity:** Sau khi thống nhất về luồng, một nhà thiết kế UI/UX sử dụng Figma để tạo ra các màn hình chi tiết với màu sắc, logo, các nút bấm có thể click được. Họ đưa bản prototype này cho một nhóm người dùng thử và yêu cầu họ thực hiện một đơn hàng. Qua đó, họ phát hiện ra nút "Xác nhận đơn hàng" quá nhỏ và khó bấm trên điện thoại, và họ sửa lại ngay trên thiết kế.

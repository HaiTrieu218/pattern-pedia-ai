# 5. Xác thực Yêu cầu (Requirements Validation)

## Định nghĩa

**Xác thực Yêu cầu (Requirements Validation)** là quá trình kiểm tra xem các yêu cầu đã được định nghĩa trong tài liệu đặc tả (ví dụ: SRS, User Stories) có thực sự là những gì các bên liên quan (stakeholders), đặc biệt là khách hàng, mong muốn hay không.

Nói một cách đơn giản, đây là bước để trả lời câu hỏi: **"Chúng ta có đang xây dựng đúng sản phẩm không?"** (Are we building the right product?).

Bước này cực kỳ quan trọng để phát hiện sớm các sai sót trong yêu cầu, vì việc sửa một lỗi ở giai đoạn yêu cầu rẻ hơn hàng trăm lần so với việc sửa nó sau khi sản phẩm đã được lập trình và triển khai.

## Mục tiêu của Xác thực Yêu cầu

Quá trình xác thực nhằm kiểm tra các thuộc tính sau của bộ yêu cầu:

1.  **Tính hợp lệ (Validity):** Yêu cầu có đáp ứng đúng nhu cầu thực sự của người dùng không?
2.  **Tính nhất quán (Consistency):** Có yêu cầu nào mâu thuẫn với yêu cầu khác không?
3.  **Tính đầy đủ (Completeness):** Tất cả các chức năng và ràng buộc mà người dùng mong muốn đã được ghi lại đầy đủ chưa?
4.  **Tính thực tế (Realism):** Liệu chúng ta có thể hiện thực hóa các yêu cầu này với công nghệ, ngân sách và thời gian hiện có không?
5.  **Khả năng kiểm chứng (Verifiability):** Liệu chúng ta có thể viết các ca kiểm thử (test cases) để kiểm tra xem yêu cầu có được đáp ứng hay không? Một yêu cầu mơ hồ như "hệ thống phải thân thiện với người dùng" là rất khó kiểm chứng.

## Các Kỹ thuật Xác thực Phổ biến

Có nhiều kỹ thuật khác nhau để thực hiện việc xác thực yêu cầu. Dưới đây là những phương pháp phổ biến nhất:

### 1. Đánh giá Yêu cầu (Requirements Reviews)

Đây là một cuộc họp chính thức trong đó các tài liệu yêu cầu được trình bày cho một nhóm gồm các kỹ sư phần mềm, khách hàng, và người dùng cuối.

- **Cách hoạt động:** Nhóm sẽ cùng nhau đọc qua tài liệu, tìm kiếm các vấn đề như sự mâu thuẫn, thiếu sót, mơ hồ, hoặc các yêu cầu không thực tế.
- **Ưu điểm:** Là một phương pháp hiệu quả để nhiều người cùng đóng góp và phát hiện lỗi từ nhiều góc nhìn khác nhau.

### 2. Chế tạo mẫu (Prototyping)

Đây là kỹ thuật xây dựng một phiên bản mô phỏng hoặc một phần của hệ thống (gọi là prototype) để người dùng có thể tương tác và trải nghiệm thử.

- **Cách hoạt động:** Người dùng "chơi" với bản mẫu và đưa ra phản hồi trực tiếp. Ví dụ: "Nút này nên đặt ở đây thì tiện hơn", "Tôi cần thêm một trường thông tin ở màn hình này".
- **Ưu điểm:** Rất hiệu quả trong việc làm rõ các yêu cầu về giao diện người dùng (UI) và luồng công việc (workflow). Giúp người dùng hình dung rõ hơn về sản phẩm cuối cùng.

### 3. Tạo các Ca kiểm thử (Test Case Generation)

Đây là quá trình thiết kế các ca kiểm thử (test cases) cho các yêu cầu ngay từ giai đoạn đầu, trước cả khi bắt đầu lập trình.

- **Cách hoạt động:** Với mỗi yêu cầu, nhóm sẽ cố gắng viết ra các kịch bản để kiểm tra nó. Nếu một yêu cầu quá mơ hồ đến mức không thể viết được test case cho nó (ví dụ: yêu cầu "hệ thống phải nhanh"), thì yêu cầu đó cần được làm rõ lại (ví dụ: "thời gian phản hồi cho chức năng X phải dưới 1 giây").
- **Ưu điểm:** Giúp bộc lộ các yêu cầu mơ hồ, không đầy đủ, hoặc không thể kiểm chứng được.

### 4. Kiểm tra Mô hình Tự động (Automated Model Checking)

Đây là một kỹ thuật nâng cao, thường áp dụng cho các hệ thống phức tạp và đòi hỏi độ an toàn cao (ví dụ: hệ thống điều khiển không lưu).

- **Cách hoạt động:** Các yêu cầu được biểu diễn dưới dạng một mô hình logic hình thức. Sau đó, một công cụ phần mềm sẽ tự động phân tích mô hình này để tìm kiếm các mâu thuẫn hoặc các trạng thái không mong muốn.
- **Ưu điểm:** Có khả năng phát hiện các lỗi tinh vi mà con người có thể bỏ sót.

## Kết quả của quá trình Xác thực

Kết quả của quá trình xác thực là một danh sách các vấn đề hoặc các điểm chưa thống nhất. Danh sách này sẽ được sử dụng để thảo luận lại với các bên liên quan và cập nhật lại tài liệu đặc tả yêu cầu cho đến khi tất cả mọi người đều đồng thuận rằng nó đã chính xác và đầy đủ.

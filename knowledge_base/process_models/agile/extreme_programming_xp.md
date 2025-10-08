# Lập trình Cực đoan (Extreme Programming - XP)

## 1. Định nghĩa (Definition)

**Lập trình Cực đoan (Extreme Programming - XP)** là một phương pháp phát triển phần mềm linh hoạt (Agile) nhằm mục đích sản xuất ra phần mềm có chất lượng cao hơn và nâng cao chất lượng cuộc sống cho đội ngũ phát triển. XP nhấn mạnh vào các **thực hành kỹ thuật (technical practices)** và thúc đẩy các giá trị cốt lõi để tạo ra một môi trường làm việc hiệu quả và bền vững.

Điểm đặc trưng nhất của XP là nó đưa các thực hành tốt (good practices) đã được công nhận lên một mức độ "cực đoan" (extreme). Ví dụ, nếu việc review code là tốt, thì trong XP chúng ta sẽ review code liên tục (thông qua lập trình đôi).

## 2. Vấn đề giải quyết (Problem Solved)

XP được thiết kế để giải quyết các vấn đề thường gặp trong các dự án phần mềm, đặc biệt là các dự án có **yêu cầu không rõ ràng hoặc thay đổi thường xuyên**:

- **Chất lượng code thấp:** Code khó đọc, khó bảo trì, nhiều lỗi.
- **Sợ thay đổi:** Việc thay đổi yêu cầu giữa chừng gây ra sự hỗn loạn và tốn kém.
- **Giao tiếp kém:** Giữa khách hàng và đội ngũ phát triển, hoặc ngay trong nội bộ đội ngũ.
- **Tích hợp muộn:** Việc tích hợp các phần của hệ thống vào cuối dự án thường gây ra rất nhiều lỗi không lường trước ("integration hell").
- **Thiếu sự hài lòng:** Cả khách hàng và lập trình viên đều cảm thấy căng thẳng và không hài lòng với quy trình làm việc.

## 3. Các Giá trị Cốt lõi (Core Values)

XP được xây dựng dựa trên 5 giá trị cốt lõi, là kim chỉ nam cho mọi hoạt động:

- **Giao tiếp (Communication):** Khuyến khích giao tiếp trực tiếp, mặt đối mặt thay vì thông qua các tài liệu dài dòng. Lập trình đôi là một ví dụ điển hình.
- **Đơn giản (Simplicity):** Luôn tìm giải pháp đơn giản nhất cho vấn đề hiện tại ("Do the simplest thing that could possibly work"). Không thiết kế thừa cho những yêu cầu chưa chắc đã có trong tương lai (YAGNI).
- **Phản hồi (Feedback):** Lấy phản hồi càng sớm càng tốt và ở mọi cấp độ: từ khách hàng (thông qua các bản demo thường xuyên), từ hệ thống (thông qua unit test), và từ các thành viên khác trong nhóm (thông qua lập trình đôi).
- **Can đảm (Courage):** Can đảm để nói sự thật về tiến độ và các ước tính. Can đảm để tái cấu trúc (refactor) code khi cần thiết, dù nó đang hoạt động. Can đảm để loại bỏ những thứ không còn giá trị.
- **Tôn trọng (Respect):** Các thành viên trong nhóm tôn trọng lẫn nhau, tôn trọng chuyên môn của nhau. Tôn trọng khách hàng và các bên liên quan.

## 4. Các Thực hành Chính (Key Practices)

XP nổi tiếng với bộ 12 (hoặc nhiều hơn) thực hành cụ thể, có thể được nhóm lại như sau:

### Vòng lặp Phản hồi Nhanh (Fine-scale Feedback)

- **Phát triển Hướng Kiểm thử (Test-Driven Development - TDD):** Viết một unit test thất bại trước, sau đó mới viết code để pass qua test đó, và cuối cùng là tái cấu trúc code.
- **Lập trình Đôi (Pair Programming):** Hai lập trình viên cùng làm việc trên một máy tính. Một người viết code (driver), người còn lại suy nghĩ về bức tranh tổng thể và review code ngay lập tức (navigator).
- **Khách hàng tại chỗ (On-site Customer):** Một người đại diện thực sự của khách hàng luôn có mặt cùng đội ngũ phát triển để trả lời các câu hỏi và làm rõ yêu cầu ngay lập tức.

### Quy trình Liên tục (Continuous Process)

- **Tích hợp Liên tục (Continuous Integration - CI):** Tích hợp code mới vào nhánh chính nhiều lần trong ngày. Mỗi lần tích hợp sẽ tự động chạy bộ test để đảm bảo không có lỗi mới phát sinh.
- **Tái cấu trúc (Refactoring):** Liên tục cải thiện thiết kế của code mà không làm thay đổi hành vi bên ngoài của nó.
- **Phát hành từng phần nhỏ (Small Releases):** Phát hành các phiên bản hoạt động của sản phẩm cho khách hàng một cách thường xuyên (vài tuần hoặc vài tháng một lần) để nhận được phản hồi giá trị.

### Sự thấu hiểu Chung (Shared Understanding)

- **Thiết kế Đơn giản (Simple Design):** Hệ thống nên được thiết kế đơn giản nhất có thể.
- **Tiêu chuẩn Code chung (Coding Standards):** Cả nhóm tuân theo một bộ quy tắc chung về cách viết code để đảm bảo tính nhất quán.
- **Sở hữu Code chung (Collective Code Ownership):** Bất kỳ ai trong nhóm cũng có quyền thay đổi bất kỳ phần nào của code.
- **Phép ẩn dụ Hệ thống (System Metaphor):** Tạo ra một câu chuyện hoặc một phép ẩn dụ đơn giản, dễ hiểu để mọi người cùng hình dung về cách hệ thống hoạt động.

### Phúc lợi cho Lập trình viên (Programmer Welfare)

- **Tuần làm việc 40 giờ (40-hour Week):** XP tin rằng làm việc ngoài giờ sẽ làm giảm năng suất và chất lượng code trong dài hạn.

## 5. Ưu điểm (Pros)

- **Chất lượng sản phẩm cao:** Nhờ vào TDD, CI và lập trình đôi.
- **Tính linh hoạt cao:** Rất dễ dàng thích ứng với các yêu cầu thay đổi.
- **Tăng sự hài lòng của khách hàng:** Khách hàng được tham gia sâu và nhận được sản phẩm thường xuyên.
- **Cải thiện tinh thần đồng đội và chia sẻ kiến thức:** Nhờ vào lập trình đôi và sở hữu code chung.

## 6. Nhược điểm (Cons)

- **Đòi hỏi kỷ luật cao:** Các thực hành như TDD và lập trình đôi cần sự cam kết và kỷ luật từ tất cả các thành viên.
- **Khó áp dụng cho các nhóm lớn hoặc phân tán về địa lý.**
- **Cần có sự tham gia tích cực từ khách hàng,** điều này không phải lúc nào cũng khả thi.
- **Có thể tập trung quá nhiều vào code mà bỏ qua các tài liệu thiết kế ở mức độ cao.**

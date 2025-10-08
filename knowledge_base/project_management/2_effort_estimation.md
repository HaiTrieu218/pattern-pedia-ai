# Ước lượng Nỗ lực (Effort Estimation)

## 1. Định nghĩa

**Ước lượng Nỗ lực (Effort Estimation)** là quá trình dự đoán lượng công sức (thường được đo bằng đơn vị người-giờ, người-ngày, hoặc người-tháng) cần thiết để hoàn thành một công việc hoặc toàn bộ dự án phần mềm.

Đây là một trong những hoạt động quản lý dự án quan trọng và thách thức nhất. Một ước lượng tốt là nền tảng cho việc lập kế hoạch, lập ngân sách và quản lý kỳ vọng của các bên liên quan.

---

## 2. Vấn đề cần giải quyết

Việc phát triển phần mềm vốn dĩ rất phức tạp và khó lường. Nếu không có một phương pháp ước lượng, các nhà quản lý và đội phát triển sẽ phải đối mặt với các câu hỏi khó:

- **Khi nào dự án sẽ hoàn thành?** (Lập lịch)
- **Chi phí để thực hiện dự án là bao nhiêu?** (Lập ngân sách)
- **Chúng ta có đủ nhân lực để làm dự án này không?** (Quản lý nguồn lực)
- **Chúng ta nên báo giá cho khách hàng bao nhiêu?** (Kinh doanh)

Ước lượng nỗ lực giúp cung cấp những câu trả lời dựa trên dữ liệu và kinh nghiệm, thay vì chỉ là phỏng đoán.

---

## 3. Các Kỹ thuật Ước lượng Phổ biến

Có nhiều kỹ thuật ước lượng, mỗi kỹ thuật có ưu và nhược điểm riêng, phù hợp với các loại dự án khác nhau.

### 3.1. Ước lượng dựa trên Mô hình (Algorithmic Models)

Sử dụng các công thức toán học dựa trên các thuộc tính của dự án để tính toán nỗ lực.

- **COCOMO (Constructive Cost Model):**

  - Là một trong những mô hình nổi tiếng nhất, do Barry Boehm phát triển.
  - Ước lượng nỗ lực (người-tháng) và thời gian phát triển dựa trên **số dòng code ước tính (Lines of Code - LOC)** của dự án.
  - Có các phiên bản khác nhau (Basic, Intermediate, Detailed) để tính đến các yếu tố khác như kinh nghiệm của đội ngũ, độ phức tạp của sản phẩm, v.v.

- **Function Points (Điểm chức năng):**
  - Thay vì đếm dòng code, kỹ thuật này đo lường **chức năng mà phần mềm cung cấp cho người dùng**.
  - Nó đếm các yếu tố như: đầu vào của người dùng, đầu ra, các truy vấn, file logic, và giao diện bên ngoài.
  - Ưu điểm: Ít phụ thuộc vào ngôn ngữ lập trình và công nghệ sử dụng.

### 3.2. Ước lượng dựa trên Kinh nghiệm (Expert Judgment)

Dựa vào kinh nghiệm và trực giác của các chuyên gia hoặc thành viên trong nhóm.

- **Delphi Technique:**

  - Một nhóm chuyên gia đưa ra các ước lượng một cách ẩn danh.
  - Các kết quả được tổng hợp và thảo luận. Quá trình này được lặp lại nhiều lần cho đến khi các ước lượng hội tụ lại gần nhau.
  - Mục đích: Tránh bị ảnh hưởng bởi ý kiến của người có chức vụ cao nhất.

- **Planning Poker (Trong Agile/Scrum):**
  - Là một kỹ thuật ước lượng dựa trên sự đồng thuận của cả nhóm.
  - Mỗi thành viên trong nhóm nhận một bộ bài có các số theo dãy Fibonacci (0, 1, 2, 3, 5, 8, 13...).
  - Product Owner giải thích một User Story (tính năng).
  - Mỗi người bí mật chọn một lá bài đại diện cho độ phức tạp của tính năng đó.
  - Tất cả cùng lật bài. Nếu có sự chênh lệch lớn, người có ước lượng cao nhất và thấp nhất sẽ giải thích lý do, sau đó cả nhóm tiếp tục bỏ phiếu lại cho đến khi đạt được sự đồng thuận.

---

## 4. Ưu điểm

- **Nền tảng cho Kế hoạch:** Cung cấp dữ liệu đầu vào quan trọng cho việc lập lịch và ngân sách.
- **Quản lý Kỳ vọng:** Giúp đặt ra các kỳ vọng thực tế cho khách hàng và các bên liên quan.
- **Hỗ trợ Ra quyết định:** Giúp quyết định xem một dự án có khả thi về mặt tài chính và nguồn lực hay không.

---

## 5. Nhược điểm và Thách thức

- **Khó chính xác:** Ước lượng, đặc biệt là ở giai đoạn đầu của dự án, thường không chính xác do có nhiều yếu tố chưa rõ ràng.
- **Phụ thuộc vào dữ liệu đầu vào:** Các mô hình như COCOMO phụ thuộc rất nhiều vào việc ước tính số dòng code, vốn dĩ cũng rất khó.
- **Yếu tố con người:** Kinh nghiệm, năng suất và sự phối hợp của đội ngũ có thể ảnh hưởng lớn đến nỗ lực thực tế nhưng lại khó đo lường.
- **Áp lực từ bên ngoài:** Ước lượng có thể bị ảnh hưởng bởi áp lực về thời gian hoặc ngân sách, dẫn đến những con số phi thực tế.

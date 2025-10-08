# Thu thập Yêu cầu (Requirements Elicitation)

## Định nghĩa

**Thu thập Yêu cầu** (Requirements Elicitation) là quá trình khám phá, tìm hiểu, và xác định các yêu cầu cho một hệ thống phần mềm thông qua việc giao tiếp và hợp tác với các bên liên quan (stakeholders) như khách hàng, người dùng cuối, và các chuyên gia trong lĩnh vực.

Đây là giai đoạn đầu tiên và là một trong những hoạt động quan trọng nhất của Kỹ nghệ Yêu cầu, vì chất lượng của toàn bộ dự án phụ thuộc rất lớn vào việc chúng ta có hiểu đúng và đủ những gì các bên liên quan thực sự cần hay không.

## Mục tiêu chính

- **Hiểu rõ bối cảnh:** Nắm bắt được lĩnh vực hoạt động (domain), mục tiêu kinh doanh, và các quy trình hiện tại của khách hàng.
- **Xác định các bên liên quan:** Nhận diện tất cả những người hoặc nhóm người có ảnh hưởng hoặc bị ảnh hưởng bởi hệ thống.
- **Khám phá nhu cầu:** Thu thập tất cả các nhu cầu, mong muốn, và ràng buộc từ các bên liên quan, bao gồm cả những yêu cầu ẩn mà họ có thể không nói ra trực tiếp.
- **Xây dựng nền tảng cho phân tích:** Cung cấp "dữ liệu thô" đầu vào cho các giai đoạn tiếp theo như phân tích, đặc tả, và xác thực yêu cầu.

## Các Kỹ thuật Thu thập Yêu cầu Phổ biến

Không có một kỹ thuật nào là hoàn hảo cho mọi tình huống. Một kỹ sư yêu cầu giỏi thường phải kết hợp nhiều kỹ thuật khác nhau để có được một bức tranh toàn cảnh và chính xác nhất.

### 1. Phỏng vấn (Interviews)

Đây là kỹ thuật truyền thống và phổ biến nhất. Kỹ sư yêu cầu sẽ trao đổi trực tiếp với các bên liên quan để đặt câu hỏi và lắng nghe câu trả lời.

- **Các loại phỏng vấn:**
  - **Phỏng vấn có cấu trúc (Structured):** Sử dụng một bộ câu hỏi đã được chuẩn bị trước. Phù hợp để thu thập thông tin cụ thể.
  - **Phỏng vấn phi cấu trúc (Unstructured):** Mang tính trò chuyện cởi mở, không có kịch bản cứng. Phù hợp để khám phá các vấn đề chung và bối cảnh.
- **Ưu điểm:**
  - Cho phép đào sâu vào các vấn đề phức tạp.
  - Xây dựng được mối quan hệ tốt với khách hàng.
- **Nhược điểm:**
  - Tốn thời gian và chi phí.
  - Thông tin thu được có thể mang tính chủ quan của người được phỏng vấn.

### 2. Bảng câu hỏi (Questionnaires / Surveys)

Phương pháp này sử dụng một bộ câu hỏi được thiết kế sẵn và gửi đến một số lượng lớn các bên liên quan để thu thập thông tin.

- **Ưu điểm:**
  - Nhanh chóng thu thập dữ liệu từ nhiều người.
  - Chi phí thấp, dễ dàng phân tích dữ liệu định lượng.
- **Nhược điểm:**
  - Tỷ lệ phản hồi có thể thấp.
  - Khó để đặt các câu hỏi sâu và không thể hỏi thêm các câu hỏi nối tiếp để làm rõ vấn đề.

### 3. Quan sát (Observation)

Kỹ sư yêu cầu sẽ trực tiếp quan sát người dùng làm việc trong môi trường thực tế của họ để hiểu rõ các quy trình, nhiệm vụ, và khó khăn mà họ gặp phải.

- **Các loại quan sát:**
  - **Quan sát thụ động (Passive):** Chỉ quan sát mà không can thiệp.
  - **Quan sát chủ động (Active):** Vừa quan sát vừa đặt câu hỏi hoặc tham gia vào quy trình.
- **Ưu điểm:**
  - Cung cấp cái nhìn sâu sắc về cách công việc thực sự diễn ra, thay vì chỉ là những gì người ta kể lại.
  - Giúp phát hiện ra những yêu cầu ẩn mà người dùng không nhận thức được.
- **Nhược điểm:**
  - Sự có mặt của người quan sát có thể làm thay đổi hành vi tự nhiên của người dùng (Hiệu ứng Hawthorne).
  - Tốn thời gian.

### 4. Phân tích Tài liệu (Document Analysis)

Nghiên cứu các tài liệu hiện có của tổ chức như báo cáo, biểu mẫu, sổ tay quy trình, tài liệu hệ thống cũ... để hiểu về lĩnh vực hoạt động và các yêu cầu đã được định hình.

- **Ưu điểm:**
  - Cung cấp thông tin nền tảng quan trọng về bối cảnh của hệ thống.
  - Giúp chuẩn bị cho các buổi phỏng vấn hiệu quả hơn.
- **Nhược điểm:**
  - Tài liệu có thể đã lỗi thời hoặc không đầy đủ.
  - Thông tin có thể không phản ánh đúng quy trình làm việc thực tế.

### 5. Hội thảo (Workshops)

Tổ chức các buổi họp tập trung với sự tham gia của các bên liên quan chính (khách hàng, người dùng, đội phát triển) để cùng nhau thảo luận, xác định và ưu tiên hóa các yêu cầu. Kỹ thuật phổ biến là **JAD (Joint Application Development)**.

- **Ưu điểm:**
  - Thúc đẩy sự hợp tác và đồng thuận giữa các bên.
  - Giải quyết các xung đột yêu cầu một cách nhanh chóng.
  - Rút ngắn thời gian thu thập yêu cầu so với việc phỏng vấn từng người.
- **Nhược điểm:**
  - Khó khăn trong việc điều phối và lên lịch.
  - Đòi hỏi một người điều phối (facilitator) có kỹ năng tốt để buổi họp diễn ra hiệu quả.

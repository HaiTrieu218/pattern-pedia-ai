# Lập kế hoạch Dự án (Project Planning)

**Danh mục:** Quản lý Dự án Phần mềm
**Tên tiếng Anh:** Project Planning

---

## I. Định nghĩa

**Lập kế hoạch Dự án Phần mềm (Software Project Planning)** là một trong những hoạt động quản lý dự án quan trọng nhất, diễn ra ở giai đoạn đầu của vòng đời phát triển. Đây là quá trình xác định một cách có hệ thống các công việc, nguồn lực, chi phí và lịch trình cần thiết để hoàn thành một dự án phần mềm thành công, đáp ứng các mục tiêu đã đề ra.

Một kế hoạch dự án tốt đóng vai trò như một bản đồ chi tiết, dẫn dắt đội ngũ phát triển và các bên liên quan trong suốt quá trình thực hiện dự án.

---

## II. Các Hoạt động chính trong Lập kế hoạch

Quá trình lập kế hoạch không phải là một công việc đơn lẻ mà là một tập hợp các hoạt động có liên quan mật thiết với nhau.

### 1. Xác định Phạm vi và Mục tiêu (Scope and Objectives Definition)

Đây là bước nền tảng, trả lời cho câu hỏi: "Chúng ta sẽ xây dựng cái gì và tại sao?".

- **Xác định Mục tiêu (Objectives):** Các mục tiêu phải tuân theo nguyên tắc SMART (Specific - Cụ thể, Measurable - Đo lường được, Achievable - Khả thi, Relevant - Liên quan, Time-bound - Có thời hạn). Ví dụ: "Xây dựng một hệ thống thương mại điện tử cho phép xử lý 1000 giao dịch mỗi phút và ra mắt vào cuối Quý 4."
- **Xác định Phạm vi (Scope):** Liệt kê rõ ràng những gì sẽ **được làm** (in-scope) và những gì sẽ **không được làm** (out-of-scope). Việc này giúp tránh "scope creep" - hiện tượng phạm vi dự án bị phình to không kiểm soát.

### 2. Phân rã Công việc (Work Breakdown Structure - WBS)

Là quá trình chia nhỏ toàn bộ công việc của dự án thành các phần nhỏ hơn, dễ quản lý hơn.

- **Cấu trúc:** WBS thường có dạng hình cây, với dự án là gốc và các công việc cụ thể (tasks) là lá.
- **Lợi ích:** Giúp ước lượng nỗ lực và chi phí chính xác hơn, dễ dàng giao việc và theo dõi tiến độ cho từng phần nhỏ.

### 3. Ước lượng Nỗ lực và Chi phí (Effort and Cost Estimation)

Sau khi đã có WBS, nhà quản lý sẽ ước lượng thời gian (tính bằng người-giờ, người-ngày) và chi phí cần thiết để hoàn thành mỗi công việc.

- **Kỹ thuật:** Sử dụng các mô hình ước lượng như COCOMO, Function Points, hoặc các phương pháp dựa trên kinh nghiệm như Planning Poker trong Agile.

### 4. Lập lịch trình (Project Scheduling)

Sắp xếp các công việc theo một trình tự thời gian hợp lý, xác định các mốc quan trọng (milestones) và ngày hoàn thành dự kiến (deadline).

- **Công cụ:** Biểu đồ Gantt và sơ đồ PERT là hai công cụ trực quan phổ biến để lập và theo dõi lịch trình.

### 5. Phân bổ Nguồn lực (Resource Allocation)

Xác định và phân công nguồn lực (con người, thiết bị, phần mềm) cho từng công việc trong dự án.

### 6. Lập Kế hoạch Quản lý Rủi ro (Risk Management Planning)

Nhận diện các rủi ro tiềm ẩn có thể ảnh hưởng đến dự án (ví dụ: công nghệ mới, thay đổi yêu cầu, nhân sự nghỉ việc) và xây dựng kế hoạch để đối phó hoặc giảm thiểu tác động của chúng.

---

## III. Tầm quan trọng của việc Lập kế hoạch

- **Cung cấp Lộ trình Rõ ràng:** Giúp mọi thành viên trong nhóm hiểu rõ mục tiêu chung và vai trò của mình.
- **Nền tảng để Theo dõi và Kiểm soát:** Kế hoạch là cơ sở để so sánh tiến độ thực tế, từ đó phát hiện các sai lệch và đưa ra điều chỉnh kịp thời.
- **Cải thiện Giao tiếp:** Một bản kế hoạch được tài liệu hóa tốt là công cụ giao tiếp hiệu quả giữa đội dự án, khách hàng và các bên liên quan.
- **Giảm thiểu Rủi ro và Sự không Chắc chắn:** Bằng cách lường trước các vấn đề, dự án có thể chuẩn bị sẵn các phương án đối phó.

---

## IV. Ví dụ thực tế

Một đội phát triển phần mềm nhận yêu cầu xây dựng ứng dụng di động đặt lịch hẹn khám bệnh. Quá trình lập kế hoạch sẽ bao gồm:

1.  **Phạm vi:** Ứng dụng sẽ có tính năng đăng ký/đăng nhập, tìm kiếm bác sĩ, đặt lịch, xem lại lịch sử. _Không bao gồm_ tính năng tư vấn trực tuyến trong phiên bản đầu.
2.  **WBS:** Chia dự án thành các gói công việc: Thiết kế UI/UX, Phát triển Backend (API, Database), Phát triển App (iOS, Android), Kiểm thử, Triển khai.
3.  **Ước lượng:** Đội ước tính cần 500 người-giờ cho toàn bộ dự án.
4.  **Lập lịch:** Sử dụng biểu đồ Gantt để lên lịch các công việc trong 3 tháng, với mốc quan trọng là hoàn thành bản Beta sau 2 tháng.
5.  **Quản lý rủi ro:** Nhận diện rủi ro "API của bệnh viện cung cấp có thể không ổn định" và lên kế hoạch dự phòng bằng cách tạo một lớp giả lập (mocking) để phát triển song song.

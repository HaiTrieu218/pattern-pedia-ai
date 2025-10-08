# Lập lịch Dự án (Project Scheduling)

---

## 1. Định nghĩa

**Lập lịch Dự án (Project Scheduling)** là quá trình phân bổ các công việc (tasks) của dự án theo một dòng thời gian cụ thể, xác định thứ tự thực hiện, thời điểm bắt đầu, thời điểm kết thúc và các tài nguyên cần thiết cho mỗi công việc. Mục tiêu của việc lập lịch là tạo ra một kế hoạch khả thi để hoàn thành dự án đúng thời hạn và trong phạm vi ngân sách.

Lập lịch là một hoạt động cốt lõi trong Quản lý Dự án Phần mềm, chuyển đổi từ câu hỏi "Cần làm **cái gì**?" (từ bản kế hoạch) sang "Sẽ làm **khi nào** và **ai làm**?".

---

## 2. Vấn đề giải quyết

Việc lập lịch giúp giải quyết các vấn đề quan trọng sau:

- **Hiểu rõ sự phụ thuộc:** Xác định công việc nào phải hoàn thành trước khi các công việc khác có thể bắt đầu.
- **Xác định Đường găng (Critical Path):** Tìm ra chuỗi công việc dài nhất quyết định thời gian hoàn thành sớm nhất của toàn bộ dự án. Bất kỳ sự chậm trễ nào trên đường găng sẽ làm trễ cả dự án.
- **Quản lý tài nguyên:** Đảm bảo rằng nhân lực, thiết bị và các tài nguyên khác được phân bổ hợp lý, tránh tình trạng quá tải hoặc lãng phí.
- **Theo dõi tiến độ:** Cung cấp một "thước đo" (baseline) để so sánh tiến độ thực tế với kế hoạch, từ đó có những điều chỉnh kịp thời.
- **Giao tiếp hiệu quả:** Giúp tất cả các bên liên quan (đội phát triển, khách hàng, quản lý) có một cái nhìn chung và rõ ràng về tiến trình của dự án.

---

## 3. Các Công cụ và Kỹ thuật Phổ biến

### 3.1. Biểu đồ Gantt (Gantt Chart)

- **Mô tả:** Là một loại biểu đồ thanh ngang, công cụ phổ biến và trực quan nhất để lập lịch.
- **Cấu trúc:**
  - **Trục dọc:** Liệt kê danh sách các công việc.
  - **Trục ngang:** Biểu diễn dòng thời gian.
  - **Thanh ngang:** Mỗi thanh đại diện cho một công việc, với điểm bắt đầu, điểm kết thúc và độ dài của thanh thể hiện thời gian thực hiện.
- **Ưu điểm:** Rất dễ đọc, dễ hiểu, phù hợp để trình bày cho cả đội ngũ kỹ thuật và các bên quản lý.

### 3.2. Sơ đồ PERT (Program Evaluation and Review Technique)

- **Mô tả:** Là một công cụ biểu diễn các công việc và sự phụ thuộc giữa chúng dưới dạng sơ đồ mạng lưới.
- **Cấu trúc:**
  - **Nút (Node):** Đại diện cho các sự kiện hoặc cột mốc (milestones).
  - **Cung (Arc):** Đại diện cho các công việc, có hướng chỉ ra trình tự thực hiện và thường đi kèm với ước lượng thời gian.
- **Ưu điểm:** Thể hiện rất rõ các mối quan hệ phụ thuộc phức tạp và là công cụ chính để xác định Đường găng (Critical Path) của dự án. Thường được sử dụng cho các dự án lớn và phức tạp.

---

## 4. Ví dụ Thực tế

Giả sử chúng ta có một dự án xây dựng ứng dụng di động đơn giản với các công việc sau:

1.  **Phân tích Yêu cầu** (5 ngày)
2.  **Thiết kế Giao diện (UI/UX)** (7 ngày) - _Phải sau khi Phân tích Yêu cầu_
3.  **Thiết kế Cơ sở dữ liệu** (4 ngày) - _Phải sau khi Phân tích Yêu cầu_
4.  **Lập trình Backend** (10 ngày) - _Phải sau khi Thiết kế CSDL_
5.  **Lập trình Frontend** (12 ngày) - _Phải sau khi Thiết kế Giao diện_
6.  **Tích hợp & Kiểm thử** (5 ngày) - _Phải sau khi cả Backend và Frontend hoàn thành_

Khi lập lịch, người quản lý sẽ tạo ra một Biểu đồ Gantt để trực quan hóa kế hoạch, đồng thời dùng Sơ đồ PERT để xác định Đường găng. Trong ví dụ này, Đường găng sẽ là chuỗi: `Phân tích Yêu cầu -> Thiết kế Giao diện -> Lập trình Frontend -> Tích hợp & Kiểm thử`.

---

## 5. Ưu điểm của việc Lập lịch Tốt

- **Tăng khả năng thành công:** Giảm thiểu rủi ro chậm tiến độ.
- **Sử dụng tài nguyên hiệu quả:** Phân bổ công việc hợp lý cho các thành viên.
- **Cải thiện tinh thần đội nhóm:** Mọi người đều biết rõ công việc, mục tiêu và thời hạn của mình.

## 6. Nhược điểm và Thách thức

- **Ước lượng không chính xác:** Thời gian thực tế có thể khác xa so với kế hoạch ban đầu.
- **Khó áp dụng cứng nhắc:** Đặc biệt trong các dự án Agile, nơi yêu cầu thường xuyên thay đổi, một lịch trình cố định có thể trở nên lỗi thời nhanh chóng.
- **Đòi hỏi kinh nghiệm:** Việc tạo ra một lịch trình khả thi đòi hỏi kinh nghiệm và sự hiểu biết sâu sắc về dự án.

# Giới thiệu về Kỹ nghệ Yêu cầu (Introduction to Requirements Engineering)

---

## 1. Yêu cầu (Requirement) là gì?

**Yêu cầu (Requirement)** là một sự mô tả về một dịch vụ hoặc một ràng buộc mà hệ thống phần mềm phải cung cấp hoặc tuân thủ. Nói một cách đơn giản, yêu cầu định nghĩa:

- **Hệ thống phải làm gì?** (What the system should do)
- **Hệ thống phải hoạt động như thế nào?** (How the system should perform)
- **Các điều kiện hoặc ràng buộc mà hệ thống phải tuân theo là gì?** (What constraints the system must operate under)

Yêu cầu là cầu nối giao tiếp quan trọng nhất giữa các bên liên quan (stakeholders) - như khách hàng, người dùng cuối - và đội ngũ phát triển phần mềm.

**Ví dụ:**

- "Hệ thống phải cho phép người dùng tìm kiếm sản phẩm theo tên." (Mô tả một dịch vụ)
- "Kết quả tìm kiếm phải được hiển thị trong vòng 2 giây." (Mô tả một ràng buộc về hiệu năng)
- "Hệ thống phải được viết bằng ngôn ngữ Java." (Mô tả một ràng buộc về kỹ thuật)

---

## 2. Kỹ nghệ Yêu cầu (Requirements Engineering) là gì?

**Kỹ nghệ Yêu cầu (Requirements Engineering - RE)** là một quy trình có hệ thống và kỷ luật bao gồm việc thu thập, phân tích, đặc tả, xác thực, và quản lý các yêu cầu cho một hệ thống phần mềm.

Đây là một trong những giai đoạn đầu tiên và quan trọng nhất trong vòng đời phát triển phần mềm, vì nó đặt nền móng cho tất cả các hoạt động tiếp theo như thiết kế, lập trình, và kiểm thử.

Mục tiêu chính của Kỹ nghệ Yêu cầu là đảm bảo rằng đội ngũ phát triển xây dựng **đúng sản phẩm** (building the right product) đáp ứng được nhu cầu thực sự của người dùng và khách hàng.

---

## 3. Tầm quan trọng của Kỹ nghệ Yêu cầu

Việc thực hiện tốt giai đoạn Kỹ nghệ Yêu cầu là yếu tố sống còn đối với sự thành công của một dự án phần mềm. Hậu quả của việc làm sai hoặc thiếu yêu cầu là rất nghiêm trọng:

- **Làm lại (Rework):** Các lỗi liên quan đến yêu cầu thường chỉ được phát hiện ở các giai đoạn sau (kiểm thử, hoặc sau khi bàn giao). Việc sửa lỗi ở giai đoạn muộn có thể tốn kém gấp **100 đến 200 lần** so với việc sửa nó ở giai đoạn yêu cầu.
- **Sản phẩm không đáp ứng nhu cầu:** Hệ thống được xây dựng đúng về mặt kỹ thuật nhưng lại không giải quyết được vấn đề của người dùng, dẫn đến việc sản phẩm bị từ chối hoặc không được sử dụng.
- **Vượt ngân sách và trễ tiến độ:** Việc phải sửa chữa và làm lại liên tục do yêu cầu không rõ ràng là nguyên nhân chính gây ra tình trạng chậm trễ và phát sinh chi phí.
- **Xung đột giữa các bên:** Yêu cầu mơ hồ, không đầy đủ gây ra sự hiểu lầm giữa khách hàng và đội ngũ phát triển, dẫn đến các tranh cãi và làm giảm lòng tin.

---

## 4. Các Hoạt động chính trong Kỹ nghệ Yêu cầu

Quy trình Kỹ nghệ Yêu cầu không phải là một đường thẳng mà là một vòng lặp liên tục, bao gồm các hoạt động chính sau:

1.  **Thu thập Yêu cầu (Requirements Elicitation):**

    - **Mục tiêu:** Khám phá, thu thập và tìm hiểu các yêu cầu từ các bên liên quan.
    - **Hoạt động:** Phỏng vấn khách hàng, tổ chức hội thảo, quan sát người dùng, phân tích tài liệu...

2.  **Phân tích Yêu cầu (Requirements Analysis):**

    - **Mục tiêu:** Phân loại, đàm phán, và giải quyết các xung đột giữa các yêu cầu. Sắp xếp thứ tự ưu tiên cho chúng.
    - **Hoạt động:** Tạo mô hình hóa, phân loại yêu cầu (chức năng/phi chức năng), ưu tiên hóa.

3.  **Đặc tả Yêu cầu (Requirements Specification):**

    - **Mục tiêu:** Ghi lại các yêu cầu đã được thống nhất vào một tài liệu chính thức (như Software Requirements Specification - SRS) một cách rõ ràng, nhất quán và không mơ hồ.
    - **Hoạt động:** Viết tài liệu SRS, User Stories, hoặc Use Cases.

4.  **Xác thực Yêu cầu (Requirements Validation):**

    - **Mục tiêu:** Kiểm tra lại tài liệu yêu cầu để đảm bảo rằng nó thực sự phản ánh đúng nhu cầu của các bên liên quan.
    - **Hoạt động:** Tổ chức các buổi đánh giá (reviews), xây dựng các bản mẫu (prototypes), viết các ca kiểm thử.

5.  **Quản lý Yêu cầu (Requirements Management):**
    - **Mục tiêu:** Quản lý các sự thay đổi không thể tránh khỏi của yêu cầu trong suốt vòng đời dự án.
    - **Hoạt động:** Theo dõi trạng thái của từng yêu cầu, quản lý các phiên bản của tài liệu yêu cầu, phân tích tác động của sự thay đổi.

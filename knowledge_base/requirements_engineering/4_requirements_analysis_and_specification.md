# Phân tích và Đặc tả Yêu cầu (Requirements Analysis and Specification)

---

## 1. Giới thiệu

**Phân tích và Đặc tả Yêu cầu** là giai đoạn chuyển đổi các yêu cầu thô đã được thu thập từ khách hàng thành một bộ tài liệu chi tiết, rõ ràng, không mơ hồ và có cấu trúc. Giai đoạn này đóng vai trò như cây cầu nối giữa "cái khách hàng muốn" và "cái đội phát triển sẽ xây dựng".

- **Phân tích Yêu cầu (Analysis):** Là quá trình nghiên cứu, phân loại, đàm phán và ưu tiên hóa các yêu cầu đã thu thập. Mục tiêu là phát hiện các mâu thuẫn, sự thiếu hụt và định hình một bức tranh yêu cầu nhất quán.
- **Đặc tả Yêu cầu (Specification):** Là quá trình ghi lại các yêu cầu đã được phân tích vào một tài liệu chính thức. Tài liệu này sẽ là nguồn tham chiếu duy nhất cho các giai đoạn thiết kế, lập trình và kiểm thử sau này.

---

## 2. Phân tích Yêu cầu (Requirements Analysis)

Mục tiêu chính của phân tích là đảm bảo các yêu cầu có các đặc tính sau:

- **Hoàn chỉnh (Complete):** Không bỏ sót thông tin quan trọng.
- **Nhất quán (Consistent):** Không có yêu cầu nào mâu thuẫn với yêu cầu khác.
- **Khả thi (Feasible):** Có thể thực hiện được trong giới hạn về công nghệ, thời gian và ngân sách.
- **Có thể kiểm chứng (Verifiable):** Có thể viết các ca kiểm thử để xác minh yêu cầu đã được đáp ứng hay chưa.

Các hoạt động chính trong giai đoạn này bao gồm:

- **Phân loại yêu cầu:** Nhóm các yêu cầu thành các loại chức năng, phi chức năng, tên miền...
- **Mô hình hóa yêu cầu:** Sử dụng các sơ đồ (như UML) để trực quan hóa các yêu cầu và mối quan hệ giữa chúng.
- **Ưu tiên hóa yêu cầu:** Sắp xếp các yêu cầu theo mức độ quan trọng (ví dụ: Must-have, Should-have, Could-have, Won't-have - MoSCoW).
- **Đàm phán và giải quyết xung đột:** Làm việc với các bên liên quan để giải quyết các yêu cầu mâu thuẫn.

---

## 3. Đặc tả Yêu cầu (Requirements Specification)

Đây là quá trình tạo ra tài liệu **Đặc tả Yêu cầu Phần mềm (Software Requirements Specification - SRS)**. Một tài liệu SRS tốt là nền tảng cho một dự án thành công.

### 3.1. Tài liệu Đặc tả Yêu cầu Phần mềm (SRS)

SRS là một tài liệu mô tả chi tiết về hệ thống phần mềm sẽ được phát triển. Nó phục vụ nhiều đối tượng: khách hàng, nhà quản lý dự án, đội phát triển, và đội kiểm thử.

**Cấu trúc chuẩn của một tài liệu SRS (theo chuẩn IEEE 830):**

1.  **Giới thiệu (Introduction)**
    - Mục đích (Purpose)
    - Phạm vi (Scope)
    - Các định nghĩa, từ viết tắt (Definitions, Acronyms)
    - Tài liệu tham khảo (References)
    - Tổng quan tài liệu (Overview)
2.  **Mô tả tổng quan (Overall Description)**
    - Bối cảnh sản phẩm (Product Perspective)
    - Chức năng sản phẩm (Product Functions)
    - Đặc điểm người dùng (User Characteristics)
    - Các ràng buộc (Constraints)
    - Các giả định và phụ thuộc (Assumptions and Dependencies)
3.  **Các yêu cầu cụ thể (Specific Requirements)**
    - Yêu cầu về giao diện bên ngoài (External Interface Requirements)
    - **Yêu cầu chức năng (Functional Requirements)**
    - **Yêu cầu phi chức năng (Non-functional Requirements)**
    - Yêu cầu về cơ sở dữ liệu (Database Requirements)

### 3.2. User Stories (Phổ biến trong Agile)

Trong các quy trình Agile, yêu cầu thường được đặc tả dưới dạng các **User Stories** ngắn gọn, tập trung vào giá trị mang lại cho người dùng.

- **Cú pháp:** `As a <user_role>, I want <goal> so that <benefit>.`
- **Ví dụ:** `Là một người mua hàng, tôi muốn thêm sản phẩm vào giỏ hàng để có thể mua nhiều sản phẩm cùng lúc.`

- **Tiêu chí INVEST cho một User Story tốt:**
  - **I**ndependent (Độc lập): Có thể phát triển mà không phụ thuộc vào story khác.
  - **N**egotiable (Có thể đàm phán): Không phải là một hợp đồng cứng, chi tiết có thể được thảo luận.
  - **V**aluable (Có giá trị): Mang lại giá trị rõ ràng cho người dùng cuối.
  - **E**stimable (Có thể ước lượng): Đội phát triển có thể ước lượng được độ phức tạp.
  - **S**mall (Nhỏ): Đủ nhỏ để có thể hoàn thành trong một Sprint.
  - **T**estable (Có thể kiểm thử): Có thể viết các kịch bản kiểm thử để xác nhận đã hoàn thành.

### 3.3. Use Cases (Ca sử dụng)

Use Case là một kỹ thuật để mô tả sự tương tác giữa người dùng (gọi là **Actor**) và hệ thống để đạt được một mục tiêu cụ thể.

- **Thành phần chính:**

  - **Sơ đồ Use Case (Use Case Diagram):** Một sơ đồ UML trực quan hóa các Actor, các Use Case, và mối quan hệ giữa chúng.
  - **Bản mô tả Use Case (Use Case Description):** Một tài liệu văn bản mô tả chi tiết từng bước của kịch bản tương tác.

- **Ví dụ về một bản mô tả Use Case đơn giản:**
  - **Tên Use Case:** Đăng nhập Người dùng
  - **Actor:** Người dùng
  - **Tiền điều kiện:** Người dùng đã có tài khoản.
  - **Luồng sự kiện chính (Main Flow):**
    1.  Người dùng nhập email và mật khẩu.
    2.  Người dùng nhấn nút "Đăng nhập".
    3.  Hệ thống xác thực thông tin.
    4.  Hệ thống chuyển hướng người dùng đến trang chủ.
  - **Luồng sự kiện thay thế (Alternative Flow):**
    - 3a. Nếu thông tin không chính xác, hệ thống hiển thị thông báo lỗi.

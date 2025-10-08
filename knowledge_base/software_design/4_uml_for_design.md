# UML - Ngôn ngữ Mô hình hóa Thống nhất trong Thiết kế

## Định nghĩa

**UML (Unified Modeling Language)** là một ngôn ngữ mô hình hóa trực quan (visual modeling language) tiêu chuẩn được sử dụng rộng rãi trong ngành công nghệ phần mềm. Mục đích chính của UML không phải là một ngôn ngữ lập trình, mà là một bộ các quy tắc và ký hiệu đồ họa để **đặc tả (specify), trực quan hóa (visualize), xây dựng (construct), và tài liệu hóa (document)** các thành phần của một hệ thống phần mềm.

Trong giai đoạn thiết kế, UML đóng vai trò như **"bản vẽ kiến trúc"** của một ngôi nhà, giúp các kỹ sư, lập trình viên và các bên liên quan có một cái nhìn chung, rõ ràng và nhất quán về hệ thống trước khi bắt tay vào xây dựng.

## Tại sao UML quan trọng trong Thiết kế?

- **Giao tiếp hiệu quả:** Một hình ảnh có giá trị hơn ngàn lời nói. Sơ đồ UML giúp các thành viên trong nhóm phát triển (kể cả những người không chuyên về kỹ thuật) hiểu được cấu trúc và luồng hoạt động của hệ thống một cách nhanh chóng.
- **Phân tích và Phát hiện lỗi sớm:** Việc vẽ ra các sơ đồ giúp phát hiện các vấn đề về logic, các mối quan hệ phức tạp hoặc các điểm thiếu sót trong thiết kế ngay trên giấy, trước khi tốn công sức viết code.
- **Tạo tài liệu sống:** Các sơ đồ UML là một phần quan trọng của tài liệu thiết kế, giúp cho việc bảo trì và nâng cấp hệ thống trong tương lai trở nên dễ dàng hơn.

## Các Sơ đồ UML Quan trọng nhất trong Giai đoạn Thiết kế

UML có rất nhiều loại sơ đồ, nhưng trong giai đoạn thiết kế, có 4 loại sơ đồ thường được sử dụng và có giá trị nhất:

---

### 1. Sơ đồ Lớp (Class Diagram)

- **Mục đích:** Đây là sơ đồ quan trọng nhất trong thiết kế hướng đối tượng. Nó mô tả **cấu trúc tĩnh (static structure)** của hệ thống, bao gồm các lớp (classes), các thuộc tính (attributes), các phương thức (methods) của chúng, và mối quan hệ giữa các lớp đó.
- **Khi nào dùng:** Dùng để phác thảo "bộ xương" của hệ thống.
- **Các thành phần chính:**
  - **Lớp (Class):** Một hình chữ nhật chia làm 3 phần: Tên lớp, Thuộc tính, Phương thức.
  - **Mối quan hệ (Relationships):**
    - **Association (Liên kết):** Mối quan hệ giữa các đối tượng. (`-`)
    - **Aggregation (Tập hợp):** Mối quan hệ "có một" (has-a), nhưng các thành phần có thể tồn tại độc lập. (Hình thoi rỗng `◇-`)
    - **Composition (Thành phần):** Mối quan hệ "sở hữu", các thành phần không thể tồn tại nếu không có vật chứa. (Hình thoi đặc `◆-`)
    - **Inheritance (Kế thừa):** Mối quan hệ "là một" (is-a). (Mũi tên tam giác rỗng `△-`)
    - **Dependency (Phụ thuộc):** Một lớp sử dụng một lớp khác. (Mũi tên nét đứt `-->`)

---

### 2. Sơ đồ Tuần tự (Sequence Diagram)

- **Mục đích:** Mô tả **sự tương tác động (dynamic interaction)** giữa các đối tượng theo một trật tự thời gian. Nó cho thấy chính xác các đối tượng gọi phương thức của nhau như thế nào và theo thứ tự nào để hoàn thành một chức năng cụ thể (một use case).
- **Khi nào dùng:** Dùng để làm rõ luồng hoạt động của một chức năng phức tạp, ví dụ: "luồng đăng nhập", "luồng xử lý đơn hàng".
- **Các thành phần chính:**
  - **Đối tượng (Object):** Hình chữ nhật ở trên cùng.
  - **Đường đời (Lifeline):** Đường nét đứt thẳng đứng thể hiện sự tồn tại của đối tượng theo thời gian.
  - **Thanh kích hoạt (Activation Bar):** Hình chữ nhật hẹp trên đường đời, cho thấy đối tượng đang bận xử lý một tác vụ.
  - **Thông điệp (Message):** Mũi tên đi từ đối tượng này sang đối tượng khác, thể hiện một lời gọi phương thức.

---

### 3. Sơ đồ Hoạt động (Activity Diagram)

- **Mục đích:** Mô tả **luồng công việc (workflow)** hoặc luồng xử lý của hệ thống. Nó trông khá giống một lưu đồ (flowchart), tập trung vào các hoạt động và các quyết định rẽ nhánh trong một quy trình.
- **Khi nào dùng:** Dùng để mô hình hóa một quy trình nghiệp vụ phức tạp hoặc một thuật toán có nhiều bước và điều kiện.
- **Các thành phần chính:**
  - **Hành động (Action):** Hình chữ nhật bo góc, thể hiện một bước trong quy trình.
  - **Điểm bắt đầu/kết thúc (Start/End Node):** Hình tròn đặc/hình tròn có viền.
  - **Quyết định (Decision Node):** Hình thoi, thể hiện điểm rẽ nhánh (if/else).
  - **Gộp/Phân nhánh (Merge/Fork Node):** Thanh ngang, dùng để mô hình hóa các luồng xử lý song song.

---

### 4. Sơ đồ Thành phần (Component Diagram)

- **Mục đích:** Mô tả cách hệ thống được chia thành các **thành phần vật lý (physical components)** và sự phụ thuộc giữa chúng. Các thành phần này có thể là các thư viện (`.dll`, `.jar`), các file thực thi, các module, hoặc các API.
- **Khi nào dùng:** Dùng ở mức độ thiết kế kiến trúc để thấy được bức tranh tổng thể về các khối xây dựng nên phần mềm.
- **Các thành phần chính:**
  - **Thành phần (Component):** Hình chữ nhật có biểu tượng nhỏ ở góc.
  - **Giao diện (Interface):** Một vòng tròn hoặc một hình bán nguyệt, thể hiện các dịch vụ mà một thành phần cung cấp.
  - **Sự phụ thuộc (Dependency):** Mũi tên nét đứt chỉ ra rằng một thành phần này cần một thành phần khác để hoạt động.

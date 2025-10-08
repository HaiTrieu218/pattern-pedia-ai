# Kỹ thuật Kiểm thử Phần mềm (Software Testing Techniques)

## Định nghĩa

Kỹ thuật kiểm thử phần mềm là các phương pháp và chiến lược được sử dụng để thiết kế và thực thi các ca kiểm thử (test cases) nhằm tìm ra lỗi trong một sản phẩm phần mềm. Việc lựa chọn kỹ thuật phù hợp giúp tối ưu hóa nỗ lực kiểm thử, tăng độ bao phủ (test coverage) và nâng cao khả năng phát hiện lỗi.

Có hai kỹ thuật nền tảng, phân loại dựa trên việc kiểm thử viên có biết về cấu trúc mã nguồn bên trong của hệ thống hay không: Kiểm thử Hộp đen và Kiểm thử Hộp trắng.

---

## 1. Kiểm thử Hộp đen (Black-box Testing)

### Vấn đề giải quyết

Làm thế nào để kiểm tra xem một chức năng của phần mềm có hoạt động đúng như đặc tả yêu cầu hay không, mà không cần quan tâm đến việc nó được lập trình bên trong như thế nào?

### Giải pháp

Kiểm thử Hộp đen, còn được gọi là kiểm thử dựa trên đặc tả (specification-based testing) hoặc kiểm thử chức năng (functional testing), là một kỹ thuật trong đó người kiểm thử không có kiến thức về cấu trúc mã nguồn, kiến trúc bên trong, hoặc logic hoạt động của hệ thống.

Người kiểm thử xem phần mềm như một "hộp đen" bí ẩn. Họ chỉ tập trung vào mối quan hệ giữa **dữ liệu đầu vào (input)** và **kết quả đầu ra (output)**.

- **Input:** Dữ liệu, hành động của người dùng (ví dụ: nhập "admin", "123456" và nhấn nút "Đăng nhập").
- **Output:** Kết quả mà hệ thống trả về (ví dụ: thông báo "Đăng nhập thành công" hoặc "Sai mật khẩu").

Mục tiêu là xác minh xem với một input cụ thể, hệ thống có tạo ra output đúng như mong đợi trong tài liệu đặc tả yêu cầu hay không.

#### Các kỹ thuật con phổ biến:

- **Phân vùng tương đương (Equivalence Partitioning):** Chia các input có thể có thành các nhóm (lớp) mà hệ thống được cho là sẽ xử lý theo cùng một cách. Ví dụ, với trường nhập tuổi, các lớp có thể là: "số âm", "0-17", "18-60", "lớn hơn 60", "không phải số". Người kiểm thử chỉ cần chọn một giá trị đại diện trong mỗi lớp để kiểm tra.
- **Phân tích giá trị biên (Boundary Value Analysis):** Tập trung kiểm thử tại các giá trị biên của các phân vùng tương đương. Ví dụ, với lớp tuổi "18-60", các giá trị biên cần kiểm tra là 17, 18, 19 và 59, 60, 61. Lỗi thường xảy ra ở các điểm ranh giới này.

### Ưu điểm

- **Khách quan:** Các ca kiểm thử được thiết kế từ góc nhìn của người dùng cuối, dựa trên tài liệu yêu cầu.
- **Tách biệt:** Người viết code và người kiểm thử có thể làm việc độc lập.
- **Phù hợp cho kiểm thử hệ thống và chấp nhận:** Rất hiệu quả ở các cấp độ kiểm thử cao.

### Nhược điểm

- **Độ bao phủ không chắc chắn:** Không thể đảm bảo tất cả các đường đi logic trong mã nguồn đều được kiểm tra.
- **Bỏ sót lỗi logic nội bộ:** Có thể bỏ sót các lỗi không thể hiện ra ở đầu ra.

---

## 2. Kiểm thử Hộp trắng (White-box Testing)

### Vấn đề giải quyết

Làm thế nào để đảm bảo rằng tất cả các cấu trúc logic, các câu lệnh, và các nhánh rẽ bên trong mã nguồn đều đã được thực thi và kiểm tra ít nhất một lần?

### Giải pháp

Kiểm thử Hộp trắng, còn được gọi là kiểm thử cấu trúc (structural testing) hoặc kiểm thử dựa trên mã nguồn (code-based testing), là một kỹ thuật trong đó người kiểm thử có toàn bộ kiến thức về cấu trúc mã nguồn và logic hoạt động bên trong của hệ thống.

Người kiểm thử "nhìn xuyên" vào bên trong "hộp", phân tích các đường đi của mã nguồn để thiết kế các ca kiểm thử. Mục tiêu là đảm bảo rằng mọi "ngóc ngách" của code đều được kiểm tra.

#### Các mức độ bao phủ (Coverage) phổ biến:

- **Bao phủ câu lệnh (Statement Coverage):** Đảm bảo mỗi dòng lệnh trong code được thực thi ít nhất một lần.
- **Bao phủ nhánh (Branch/Decision Coverage):** Đảm bảo mỗi nhánh quyết định (ví dụ: kết quả `true` và `false` của một câu lệnh `if`) đều được thực thi ít nhất một lần. Đây là mức độ mạnh hơn bao phủ câu lệnh.
- **Bao phủ đường đi (Path Coverage):** Đảm bảo mọi đường đi có thể có từ đầu đến cuối của một hàm đều được thực thi. Đây là mức độ bao phủ mạnh nhất nhưng cũng khó đạt được nhất.

### Ưu điểm

- **Toàn diện:** Có thể kiểm tra kỹ lưỡng các logic phức tạp và các trường hợp ngoại lệ bên trong code.
- **Tối ưu hóa code:** Giúp lập trình viên tìm và loại bỏ các đoạn code "chết" (dead code).
- **Phù hợp cho kiểm thử đơn vị và tích hợp:** Rất hiệu quả ở các cấp độ kiểm thử thấp, thường do chính lập trình viên thực hiện.

### Nhược điểm

- **Phức tạp và tốn kém:** Đòi hỏi kiến thức sâu về lập trình và tốn nhiều thời gian để thiết kế ca kiểm thử.
- **Không phát hiện được lỗi yêu cầu:** Nếu chức năng được lập trình đúng theo thiết kế, nhưng thiết kế lại sai so với yêu cầu, kiểm thử hộp trắng sẽ không phát hiện ra.
- **Khó bảo trì:** Khi mã nguồn thay đổi, các ca kiểm thử hộp trắng thường phải được viết lại.

---

## So sánh Tóm tắt

| Tiêu chí              | Kiểm thử Hộp đen                      | Kiểm thử Hộp trắng                            |
| :-------------------- | :------------------------------------ | :-------------------------------------------- |
| **Góc nhìn**          | Người dùng cuối / Đặc tả yêu cầu      | Lập trình viên / Cấu trúc code                |
| **Mục tiêu**          | Xác minh chức năng (Hệ thống LÀM GÌ?) | Xác minh cấu trúc (Hệ thống LÀM NHƯ THẾ NÀO?) |
| **Kiến thức yêu cầu** | Không cần biết code                   | Phải biết code                                |
| **Áp dụng chính**     | Kiểm thử Hệ thống, Chấp nhận          | Kiểm thử Đơn vị, Tích hợp                     |

# Các Loại Kiểm thử Chuyên biệt Khác

Ngoài các cấp độ và kỹ thuật kiểm thử cơ bản, trong các dự án thực tế, có nhiều loại kiểm thử chuyên biệt được thực hiện để đảm bảo các khía cạnh phi chức năng (non-functional) của phần mềm.

---

### **1. Kiểm thử Hồi quy (Regression Testing)**

- **Định nghĩa:** Là loại kiểm thử được thực hiện sau khi có một sự thay đổi trong mã nguồn (ví dụ: sửa lỗi, thêm chức năng mới, thay đổi cấu hình) để đảm bảo rằng những thay đổi này **không vô tình làm hỏng** các chức năng đã hoạt động tốt trước đó.

- **Mục tiêu:**

  - Phát hiện các lỗi mới phát sinh (regressions) trong các khu vực không bị ảnh hưởng trực tiếp bởi sự thay đổi.
  - Đảm bảo tính ổn định và toàn vẹn của toàn bộ hệ thống sau mỗi lần cập nhật.

- **Ví dụ:**
  - Một ứng dụng ngân hàng có chức năng "Chuyển tiền" và "Xem lịch sử giao dịch".
  - Lập trình viên sửa một lỗi nhỏ trong chức năng "Chuyển tiền".
  - **Kiểm thử hồi quy:** Chạy lại tất cả các kịch bản kiểm thử cũ, bao gồm cả việc đăng nhập, xem số dư, và đặc biệt là "Xem lịch sử giao dịch" để chắc chắn rằng việc sửa lỗi kia không làm hỏng các chức năng này.

---

### **2. Kiểm thử Hiệu năng (Performance Testing)**

- **Định nghĩa:** Là một loại kiểm thử phi chức năng nhằm đánh giá tốc độ, khả năng đáp ứng, và sự ổn định của một hệ thống dưới một khối lượng công việc (workload) nhất định.

- **Mục tiêu:**

  - **Tốc độ (Speed):** Hệ thống phản hồi nhanh như thế nào?
  - **Khả năng mở rộng (Scalability):** Hệ thống có thể xử lý bao nhiêu người dùng cùng lúc?
  - **Sự ổn định (Stability):** Hệ thống có bị sập khi chịu tải nặng trong thời gian dài không?

- **Ví dụ:**
  - Kiểm tra một trang web thương mại điện tử:
    - **Load Testing:** Giả lập 1,000 người dùng cùng lúc truy cập và đặt hàng để xem thời gian tải trang có bị chậm đi không.
    - **Stress Testing:** Tăng dần số người dùng lên 5,000, 10,000... để tìm ra giới hạn mà tại đó trang web bắt đầu bị lỗi hoặc sập.

---

### **3. Kiểm thử Bảo mật (Security Testing)**

- **Định nghĩa:** Là một quá trình nhằm tìm ra các lỗ hổng, các mối đe dọa, rủi ro trong một phần mềm và ngăn chặn các cuộc tấn công độc hại từ những kẻ xâm nhập.

- **Mục tiêu:**

  - Xác định các điểm yếu trong hệ thống mà hacker có thể khai thác.
  - Đảm bảo tính **Bí mật (Confidentiality)**, **Toàn vẹn (Integrity)**, và **Sẵn sàng (Availability)** của dữ liệu và hệ thống.

- **Ví dụ:**
  - Một chuyên gia bảo mật (hoặc một công cụ tự động) cố gắng thực hiện các cuộc tấn công phổ biến vào một trang web:
    - **SQL Injection:** Cố gắng chèn các lệnh SQL độc hại vào ô tìm kiếm hoặc form đăng nhập để truy cập trái phép vào cơ sở dữ liệu.
    - **Cross-Site Scripting (XSS):** Cố gắng chèn mã JavaScript vào trang web để lấy cắp thông tin của người dùng khác.
    - Kiểm tra xem mật khẩu có được mã hóa an toàn trước khi lưu vào cơ sở dữ liệu hay không.

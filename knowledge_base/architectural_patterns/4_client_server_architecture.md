# Mẫu Kiến trúc Khách-Chủ (Client-Server Architecture)

---

### **1. Định nghĩa**

**Kiến trúc Khách-Chủ (Client-Server)** là một mô hình kiến trúc ứng dụng phân tán, trong đó các nhiệm vụ và khối lượng công việc được phân chia giữa hai thành phần chính:

1.  **Server (Máy chủ):** Là một nhà cung cấp tài nguyên hoặc dịch vụ. Nó luôn ở trạng thái "lắng nghe", chờ đợi yêu cầu từ các client. Server thường là một máy tính mạnh mẽ, chứa dữ liệu, logic nghiệp vụ, và thực hiện các tác vụ xử lý phức tạp.
2.  **Client (Máy khách):** Là một người yêu cầu tài nguyên hoặc dịch vụ. Client chủ động gửi yêu cầu đến server và chờ đợi phản hồi. Client thường là các thiết bị của người dùng cuối như máy tính cá nhân, điện thoại thông minh, và chịu trách nhiệm chính về giao diện người dùng (UI).

Mô hình này là nền tảng cho phần lớn các ứng dụng mạng hiện nay, từ việc lướt web cho đến gửi email.

### **2. Sơ đồ Minh họa**

_Trong sơ đồ này, nhiều Clients (trình duyệt web, ứng dụng di động) cùng gửi yêu cầu qua mạng Internet đến một Server trung tâm. Server xử lý yêu cầu, có thể tương tác với Cơ sở dữ liệu, và gửi phản hồi trở lại cho Client._

---

### **3. Cách hoạt động**

Luồng hoạt động của mô hình Client-Server diễn ra theo một chu trình yêu cầu-phản hồi (request-response cycle) đơn giản:

1.  **Client gửi yêu cầu (Request):** Người dùng tương tác với giao diện trên thiết bị của mình (ví dụ: bấm vào một link trên website). Client sẽ tạo một yêu cầu chứa thông tin cần thiết và gửi nó qua mạng đến địa chỉ của Server.
2.  **Server nhận và xử lý yêu cầu:** Server, đang trong trạng thái lắng nghe, nhận được yêu cầu. Nó phân tích yêu cầu, thực thi logic nghiệp vụ tương ứng (ví dụ: truy vấn cơ sở dữ liệu để lấy bài viết), và chuẩn bị dữ liệu phản hồi.
3.  **Server gửi phản hồi (Response):** Server đóng gói dữ liệu kết quả và gửi nó trở lại cho Client đã yêu cầu.
4.  **Client nhận và hiển thị phản hồi:** Client nhận được dữ liệu phản hồi từ Server. Nó sẽ xử lý dữ liệu này (ví dụ: phân tích mã HTML, CSS) và hiển thị kết quả lên màn hình cho người dùng xem.

Chu trình này lặp lại mỗi khi người dùng thực hiện một hành động mới.

---

### **4. Ví dụ Thực tế**

- **World Wide Web (WWW):** Trình duyệt web (Chrome, Firefox) của bạn là **Client**. Khi bạn gõ một địa chỉ web, nó gửi yêu cầu đến **Web Server**. Web Server trả về mã HTML, CSS, JavaScript để trình duyệt hiển thị trang web.
- **Ứng dụng Email:** Phần mềm email (Outlook, Gmail app) là **Client**. Khi bạn gửi email, nó gửi yêu cầu đến **Mail Server**. Mail Server sẽ xử lý và chuyển email đến người nhận.
- **Game Online:** Trò chơi bạn cài trên máy là **Client**, chịu trách nhiệm đồ họa và nhận lệnh từ bạn. Client gửi hành động của bạn (di chuyển, tấn công) đến **Game Server**. Game Server là "trọng tài" trung tâm, xử lý logic trò chơi, tương tác của tất cả người chơi và gửi lại trạng thái cập nhật cho tất cả các Client.

---

### **5. Ưu điểm (Pros)**

- **Tập trung hóa (Centralization):** Dữ liệu và logic quan trọng được quản lý tập trung tại Server, giúp dễ dàng bảo mật, quản lý và sao lưu.
- **Khả năng mở rộng (Scalability):** Có thể dễ dàng nâng cấp sức mạnh của Server (mở rộng dọc) hoặc thêm nhiều Server hơn (mở rộng ngang) để phục vụ nhiều Client hơn mà không ảnh hưởng đến phía Client.
- **Dễ bảo trì:** Việc cập nhật, sửa lỗi có thể được thực hiện ở một nơi duy nhất là Server, và tất cả Client sẽ tự động nhận được phiên bản mới mà không cần cài đặt lại (đối với ứng dụng web).
- **Độc lập nền tảng:** Miễn là Client và Server tuân theo cùng một giao thức giao tiếp (ví dụ: HTTP), chúng có thể được phát triển trên các nền tảng, hệ điều hành, và ngôn ngữ lập trình khác nhau.

### **6. Nhược điểm (Cons)**

- **Phụ thuộc vào Server:** Nếu Server gặp sự cố hoặc ngừng hoạt động, toàn bộ hệ thống sẽ tê liệt, không Client nào có thể sử dụng được dịch vụ.
- **Nghẽn cổ chai (Bottleneck):** Nếu có quá nhiều Client gửi yêu cầu cùng một lúc, Server có thể bị quá tải, dẫn đến hiệu năng chậm hoặc từ chối phục vụ.
- **Chi phí Server:** Việc xây dựng, vận hành và bảo trì một hệ thống Server mạnh mẽ và đáng tin cậy có thể tốn kém.
- **Phụ thuộc vào Mạng:** Hiệu suất của ứng dụng bị ảnh hưởng trực tiếp bởi chất lượng và tốc độ của kết nối mạng giữa Client và Server.

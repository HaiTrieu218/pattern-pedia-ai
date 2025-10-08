# Mã hóa Dữ liệu (Data Encryption)

---

## 1. Định nghĩa

**Mã hóa Dữ liệu** là quá trình chuyển đổi dữ liệu từ dạng có thể đọc được (plaintext - bản rõ) thành một dạng không thể đọc được, đã được mã hóa (ciphertext - bản mã). Chỉ những ai có "chìa khóa" giải mã (decryption key) chính xác mới có thể chuyển đổi bản mã trở lại thành bản rõ.

Mục tiêu chính của mã hóa là để đảm bảo **tính bảo mật (Confidentiality)**, ngăn chặn việc truy cập trái phép vào thông tin nhạy cảm.

---

## 2. Vấn đề giải quyết

Trong một hệ thống phần mềm, dữ liệu thường xuyên được lưu trữ và truyền đi. Nếu không được bảo vệ, dữ liệu này có thể bị đánh cắp và đọc bởi kẻ xấu:

- **Tin tặc tấn công cơ sở dữ liệu:** Nếu một hacker xâm nhập được vào máy chủ và lấy đi file database, họ có thể đọc được tất cả thông tin người dùng, mật khẩu, thông tin thẻ tín dụng...
- **Nghe lén trên đường truyền mạng:** Khi bạn gửi thông tin từ trình duyệt của mình đến máy chủ (ví dụ: khi đăng nhập), dữ liệu này đi qua nhiều thiết bị mạng. Kẻ xấu có thể "nghe lén" trên đường truyền này và lấy cắp thông tin nếu nó không được mã hóa.

Mã hóa giúp giải quyết cả hai vấn đề trên. Kể cả khi dữ liệu bị đánh cắp, nó vẫn vô dụng đối với kẻ tấn công nếu chúng không có chìa khóa để giải mã.

---

## 3. Các loại Mã hóa Chính

Trong phát triển phần mềm, chúng ta cần quan tâm đến hai trạng thái chính của dữ liệu và áp dụng mã hóa tương ứng:

### 3.1. Mã hóa khi Lưu trữ (Encryption at Rest)

- **Khái niệm:** Là mã hóa dữ liệu khi nó đang được lưu trữ vật lý trên một thiết bị, chẳng hạn như trong cơ sở dữ liệu trên ổ cứng, trên dịch vụ lưu trữ đám mây (cloud storage), hoặc trên USB.
- **Mục tiêu:** Bảo vệ dữ liệu trong trường hợp máy chủ vật lý hoặc thiết bị lưu trữ bị đánh cắp hoặc bị truy cập trái phép.
- **Ví dụ:**
  - Cơ sở dữ liệu mã hóa các cột chứa thông tin nhạy cảm như số an sinh xã hội.
  - Các dịch vụ như AWS S3 hoặc Google Cloud Storage tự động mã hóa tất cả các file bạn tải lên.

### 3.2. Mã hóa khi Truyền đi (Encryption in Transit)

- **Khái niệm:** Là mã hóa dữ liệu khi nó đang được truyền đi từ điểm này đến điểm khác trên mạng, ví dụ như từ trình duyệt người dùng đến máy chủ web.
- **Mục tiêu:** Bảo vệ dữ liệu khỏi bị nghe lén hoặc bị thay đổi trong quá trình truyền.
- **Ví dụ phổ biến nhất:**
  - **HTTPS (Hypertext Transfer Protocol Secure):** Khi bạn thấy biểu tượng ổ khóa trên thanh địa chỉ của trình duyệt, điều đó có nghĩa là kết nối giữa bạn và website đang được mã hóa bằng giao thức TLS/SSL. Mọi thông tin bạn gửi (form đăng nhập, số thẻ tín dụng) đều được mã hóa.
  - Kết nối đến cơ sở dữ liệu từ ứng dụng cũng cần được mã hóa.

---

## 4. Ưu điểm

- **Bảo mật Tối cao:** Là tuyến phòng thủ mạnh mẽ nhất để bảo vệ tính riêng tư của dữ liệu.
- **Đảm bảo Toàn vẹn Dữ liệu:** Một số thuật toán mã hóa cũng giúp đảm bảo rằng dữ liệu không bị thay đổi trên đường truyền.
- **Tuân thủ Pháp luật:** Nhiều quy định về bảo vệ dữ liệu (như GDPR) yêu cầu các tổ chức phải mã hóa thông tin cá nhân của người dùng.

---

## 5. Nhược điểm

- **Tăng độ phức tạp:** Việc quản lý các "chìa khóa" mã hóa một cách an toàn là một bài toán phức tạp. Nếu làm mất khóa, dữ liệu cũng sẽ bị mất.
- **Ảnh hưởng đến Hiệu năng:** Quá trình mã hóa và giải mã tiêu tốn tài nguyên CPU, có thể làm giảm một chút hiệu năng của hệ thống, đặc biệt là với lượng dữ liệu lớn.
- **Khó khăn trong Tìm kiếm:** Việc tìm kiếm trên dữ liệu đã được mã hóa trong cơ sở dữ liệu là rất khó khăn và đòi hỏi các kỹ thuật đặc biệt.

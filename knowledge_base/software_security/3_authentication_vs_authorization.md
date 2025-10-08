# Xác thực (Authentication) vs Ủy quyền (Authorization)

---

## 1. Định nghĩa

**Xác thực (Authentication)** và **Ủy quyền (Authorization)** là hai khái niệm nền tảng trong lĩnh vực an ninh phần mềm, nhưng chúng phục vụ hai mục đích hoàn toàn khác nhau.

- **Authentication (Xác thực):** Là quá trình **xác minh danh tính** của một người dùng hoặc hệ thống. Nó trả lời cho câu hỏi: **"Bạn là ai?"**.
- **Authorization (Ủy quyền):** Là quá trình **xác định quyền truy cập** hoặc các hành động mà một người dùng đã được xác thực được phép thực hiện. Nó trả lời cho câu hỏi: **"Bạn được phép làm gì?"**.

**Quy tắc bất biến:** **Ủy quyền (Authorization)** luôn luôn xảy ra **SAU KHI** **Xác thực (Authentication)** thành công. Hệ thống không thể cấp quyền cho một người mà nó không biết là ai.

---

## 2. Ví dụ trong Đời thực

Hãy tưởng tượng bạn đang đi đến một sân bay để bay một chuyến bay quốc tế.

1.  **Authentication (Xác thực):**

    - Bạn đến quầy check-in và đưa ra **Hộ chiếu (Passport)** của mình.
    - Nhân viên an ninh sẽ kiểm tra ảnh trên hộ chiếu có khớp với khuôn mặt của bạn không, kiểm tra các thông tin khác để chắc chắn **"bạn chính là người mà bạn nói bạn là"**.
    - Quá trình này chính là **Xác thực**.

2.  **Authorization (Ủy quyền):**
    - Sau khi xác thực thành công, bạn nhận được một **Thẻ lên máy bay (Boarding Pass)**.
    - Trên thẻ này ghi rõ bạn được phép làm gì: bay đến **Hạng ghế 15A**, vào phòng chờ **hạng Phổ thông**, và chỉ được lên **chuyến bay VN123**.
    - Bạn không thể dùng thẻ này để vào phòng chờ hạng Thương gia hay lên một chuyến bay khác.
    - Quá trình này chính là **Ủy quyền**. Tấm thẻ này định nghĩa các quyền của bạn.

---

## 3. Ví dụ trong Phần mềm

Hãy xem xét một ứng dụng web như một trang blog:

1.  **Authentication (Xác thực):**

    - Một người dùng truy cập vào trang `/login`.
    - Họ nhập **tên người dùng** và **mật khẩu**.
    - Hệ thống kiểm tra thông tin này với cơ sở dữ liệu. Nếu khớp, quá trình xác thực thành công. Hệ thống biết "Đây là người dùng A".

2.  **Authorization (Ủy quyền):**
    - **Người dùng A** là một người dùng thông thường (Reader).
      - Họ được phép (authorized) **đọc** các bài viết, **bình luận** vào các bài viết.
      - Họ không được phép (not authorized) **viết** bài mới, **xóa** bài viết của người khác, hay truy cập vào trang quản trị (`/admin`).
    - **Người dùng B** là một quản trị viên (Admin).
      - Sau khi xác thực, hệ thống nhận ra vai trò (role) của họ là Admin.
      - Họ được phép làm mọi thứ mà Reader làm, cộng thêm việc **viết** bài mới, **chỉnh sửa/xóa** bất kỳ bài viết nào, và truy cập vào trang `/admin`.

---

## 4. Tóm tắt So sánh

| Tiêu chí             | Authentication (Xác thực)                              | Authorization (Ủy quyền)                                                      |
| :------------------- | :----------------------------------------------------- | :---------------------------------------------------------------------------- |
| **Câu hỏi trả lời**  | "Bạn là ai?"                                           | "Bạn được phép làm gì?"                                                       |
| **Mục đích**         | Xác minh danh tính người dùng.                         | Xác định quyền và đặc quyền.                                                  |
| **Quá trình**        | Người dùng cung cấp thông tin đăng nhập (credentials). | Hệ thống kiểm tra các quy tắc/chính sách (policies/roles) gắn với người dùng. |
| **Thứ tự**           | Thực hiện trước.                                       | Thực hiện sau khi xác thực thành công.                                        |
| **Dữ liệu trao đổi** | Thông tin đăng nhập, token, sinh trắc học...           | Quyền, vai trò, đặc quyền...                                                  |

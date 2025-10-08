# Áp dụng Mẫu Thiết kế trong Thực tế

Mẫu Thiết kế (Design Patterns) không phải là những khái niệm trừu tượng chỉ tồn tại trong sách vở. Chúng là nền tảng của vô số thư viện, framework và ứng dụng mà các lập trình viên sử dụng hàng ngày. Dưới đây là phân tích một vài ví dụ kinh điển để thấy rõ cách chúng được áp dụng.

---

## **1. Observer Pattern: Trái tim của Lập trình Giao diện và Sự kiện**

**Vấn đề:** Làm thế nào để một đối tượng (Subject) có thể thông báo cho một danh sách các đối tượng khác (Observers) về sự thay đổi trạng thái của nó, mà không cần phải biết cụ thể các đối tượng đó là ai?

**Ứng dụng trong thực tế:**

- **Lập trình Giao diện Người dùng (GUI Frameworks):** Đây là ví dụ kinh điển nhất.

  - Trong các thư viện như Java Swing, JavaFX, .NET Windows Forms, hay trong JavaScript DOM, một nút bấm (`Button`) chính là **Subject**.
  - Các đoạn code xử lý sự kiện (event listeners/handlers) mà bạn viết, ví dụ `button.addEventListener('click', ...)` hay `button.addActionListener(...)`, chính là việc bạn đăng ký một **Observer**.
  - Khi người dùng click vào nút bấm, `Button` sẽ không quan tâm bạn là ai hay bạn muốn làm gì. Nó chỉ đơn giản là duyệt qua danh sách các "người đăng ký" (observers) và gọi phương thức `update()` của họ (trong trường hợp này là thực thi hàm callback). Điều này giúp hệ thống cực kỳ linh hoạt và dễ mở rộng.

- **Hệ thống Thông báo (Notification Systems):**
  - Trong một ứng dụng mạng xã hội, một người dùng (ví dụ: `User A`) là **Subject**.
  - Những người theo dõi (`Followers`) của `User A` là các **Observers**.
  - Khi `User A` đăng một bài viết mới, đối tượng `User A` sẽ gửi thông báo đến tất cả các `Followers` trong danh sách của mình.

---

## **2. Factory Method Pattern: Linh hoạt hóa việc tạo Đối tượng**

**Vấn đề:** Làm thế nào để một lớp có thể trì hoãn (defer) việc quyết định lớp cụ thể nào sẽ được khởi tạo cho các lớp con của nó?

**Ứng dụng trong thực tế:**

- **Các Framework Lớn (Frameworks):**

  - Một framework thường cung cấp các lớp cơ sở và muốn người dùng cuối (lập trình viên sử dụng framework) tự quyết định các đối tượng cụ thể sẽ được tạo ra.
  - Ví dụ: Một framework game có thể có một lớp `EnemyFactory` với một phương thức trừu tượng `createEnemy()`. Các nhà phát triển game sau đó sẽ kế thừa từ lớp này để tạo ra các nhà máy cụ thể như `GoblinFactory` (tạo ra `Goblin`) hay `DragonFactory` (tạo ra `Dragon`). Framework chỉ cần gọi `enemyFactory.createEnemy()` mà không cần biết con quái vật cụ thể nào sẽ xuất hiện.

- **JDBC (Java Database Connectivity):**
  - Đối tượng `DriverManager` trong JDBC sử dụng một dạng của Factory Pattern. Khi bạn gọi `DriverManager.getConnection(urlString)`, nó sẽ xem xét chuỗi `urlString` của bạn (`jdbc:mysql://...`, `jdbc:postgresql://...`) để quyết định "nhà máy" (Driver) nào sẽ được sử dụng để tạo ra một đối tượng `Connection` cụ thể (`MySQLConnection`, `PostgreSQLConnection`).

---

## **3. Decorator Pattern: "Trang trí" Đối tượng mà không cần Kế thừa**

**Vấn đề:** Làm thế nào để thêm các chức năng mới cho một đối tượng một cách linh hoạt tại thời điểm chạy (runtime), mà không cần phải thay đổi mã nguồn của lớp đó hoặc tạo ra vô số lớp con?

**Ứng dụng trong thực tế:**

- **Thao tác I/O (Input/Output) trong Java:**
  - Đây là ví dụ được trích dẫn nhiều nhất và rõ ràng nhất.
  - Bạn bắt đầu với một đối tượng `InputStream` cơ bản, ví dụ `FileInputStream` (chỉ biết đọc từng byte từ file).
  - Để thêm chức năng đệm (buffering) nhằm tăng hiệu suất, bạn "trang trí" nó bằng cách bọc nó trong một `BufferedInputStream`.
  - Để thêm khả năng đọc dữ liệu có cấu trúc (như `int`, `double`), bạn tiếp tục bọc nó trong một `DataInputStream`.
  - Kết quả cuối cùng là một đối tượng được "trang trí" nhiều lớp, có đầy đủ chức năng: `new DataInputStream(new BufferedInputStream(new FileInputStream("file.txt")))`.

---

## **4. Singleton Pattern: Đảm bảo Duy nhất một Thể hiện**

**Vấn đề:** Làm thế nào để đảm bảo rằng một lớp chỉ có duy nhất một thể hiện (instance) và cung cấp một điểm truy cập toàn cục đến thể hiện đó?

**Ứng dụng trong thực tế:**

- **Quản lý Cấu hình (Configuration Managers):** Trong một ứng dụng, thường chỉ nên có một đối tượng duy nhất chịu trách nhiệm đọc và cung cấp các thông tin cấu hình (ví dụ: chuỗi kết nối cơ sở dữ liệu, API keys).
- **Logging:** Một hệ thống ghi log (ví dụ: Log4j, Serilog) thường được triển khai dưới dạng Singleton để đảm bảo tất cả các phần của ứng dụng đều ghi log vào cùng một nơi, theo cùng một định dạng.
- **Quản lý Kết nối Cơ sở dữ liệu (Database Connection Pools):** Một connection pool quản lý một tập hợp các kết nối CSDL để tái sử dụng. Việc tạo nhiều pool sẽ rất lãng phí tài nguyên, do đó nó thường được thiết kế là một Singleton.

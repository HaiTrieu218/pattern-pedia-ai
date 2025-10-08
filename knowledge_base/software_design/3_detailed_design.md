# Thiết kế Chi tiết (Detailed Design)

---

### **1. Định nghĩa (Definition)**

**Thiết kế Chi tiết (Detailed Design)**, còn được gọi là Thiết kế Cấp thấp (Low-Level Design), là giai đoạn trong quy trình thiết kế phần mềm tập trung vào việc đặc tả chi tiết logic nội bộ cho từng thành phần (module) của hệ thống đã được xác định trong giai đoạn Thiết kế Kiến trúc.

Nếu **Thiết kế Kiến trúc** giống như việc vẽ ra **sơ đồ mặt bằng tổng thể của một ngôi nhà** (các phòng, hành lang, cầu thang), thì **Thiết kế Chi tiết** chính là việc vẽ ra **bản thiết kế chi tiết cho từng phòng**: vị trí đặt ổ cắm điện, loại đèn sẽ sử dụng, đường đi của ống nước, màu sơn tường, v.v.

Đây là bản thiết kế cuối cùng, đủ chi tiết để lập trình viên có thể dựa vào đó và bắt đầu viết mã nguồn.

---

### **2. Mục tiêu (Objectives)**

Mục tiêu chính của giai đoạn Thiết kế Chi tiết là:

- **Đặc tả cấu trúc dữ liệu:** Xác định các thuộc tính (attributes) và kiểu dữ liệu (data types) cụ thể cho các lớp (classes) và đối tượng (objects).
- **Đặc tả thuật toán:** Định nghĩa các thuật toán (algorithms) cụ thể sẽ được sử dụng bên trong các phương thức (methods) để xử lý logic nghiệp vụ.
- **Định nghĩa giao diện (Interfaces):** Xác định chữ ký (signature) của các phương thức, bao gồm tên phương thức, các tham số đầu vào và kiểu dữ liệu trả về.
- **Xử lý các ràng buộc:** Mô tả chi tiết cách hệ thống xử lý các ràng buộc về hiệu năng, bảo mật và các yêu cầu phi chức năng khác ở cấp độ module.
- **Tạo ra tài liệu cho lập trình:** Cung cấp đủ thông tin để lập trình viên có thể hiện thực hóa module mà không cần phải phỏng đoán hay đưa ra các quyết định thiết kế quan trọng.

---

### **3. Các thành phần chính (Key Components)**

Một bản thiết kế chi tiết thường bao gồm các thành phần sau:

- **Thiết kế Lớp và Đối tượng (Classes & Objects Design):**

  - Định nghĩa các lớp, bao gồm thuộc tính và phương thức.
  - Mô tả mối quan hệ giữa các lớp (kế thừa, hiện thực hóa, liên kết, tổng hợp...).
  - Sơ đồ Lớp (Class Diagram) của UML là công cụ chính ở đây.

- **Thiết kế Giao diện (Interface Design):**

  - Định nghĩa các giao diện (interfaces) mà các lớp sẽ phải tuân thủ.
  - Đây là "hợp đồng" quy định cách các module tương tác với nhau.

- **Thiết kế Dữ liệu (Data Design):**

  - Lựa chọn các cấu trúc dữ liệu phù hợp (mảng, danh sách liên kết, cây, bảng băm...).
  - Thiết kế lược đồ cơ sở dữ liệu (nếu có) ở cấp độ chi tiết.

- **Thiết kế Thuật toán (Algorithm Design):**
  - Mô tả từng bước của các thuật toán phức tạp bằng mã giả (pseudocode) hoặc sơ đồ khối (flowchart).
  - Phân tích độ phức tạp thời gian và không gian của thuật toán.

---

### **4. Mối quan hệ với Thiết kế Kiến trúc (Relationship with Architectural Design)**

| Tiêu chí                | Thiết kế Kiến trúc (Architectural Design)                        | Thiết kế Chi tiết (Detailed Design)                          |
| :---------------------- | :--------------------------------------------------------------- | :----------------------------------------------------------- |
| **Mức độ trừu tượng**   | Cao (High-level)                                                 | Thấp (Low-level)                                             |
| **Phạm vi**             | Toàn bộ hệ thống                                                 | Từng module hoặc thành phần riêng lẻ                         |
| **Đối tượng tập trung** | Các module lớn, các hệ thống con, và sự tương tác giữa chúng.    | Các lớp, các phương thức, các thuật toán, và logic nội bộ.   |
| **Kết quả đầu ra**      | Sơ đồ kiến trúc tổng thể, lựa chọn công nghệ, các mẫu kiến trúc. | Sơ đồ lớp chi tiết, sơ đồ tuần tự, mã giả, đặc tả giao diện. |

---

### **5. Ví dụ minh họa (Illustrative Example)**

**Bối cảnh:** Xây dựng một "Hệ thống Quản lý Thư viện".

- **Quyết định trong Thiết kế Kiến trúc:** Hệ thống sẽ được chia thành 3 khối chính: Giao diện Người dùng (UI), **Dịch vụ Quản lý Sách (Book Management Service)**, và Cơ sở dữ liệu (Database).

- **"Zoom vào" Thiết kế Chi tiết cho `Book Management Service`:**

  1.  **Định nghĩa các Lớp (Classes):**

      - Lớp `Book`:
        - Thuộc tính: `isbn: string`, `title: string`, `author: string`, `isAvailable: boolean`.
        - Phương thức: `checkOut()`, `returnBook()`.

  2.  **Định nghĩa Giao diện (Interface):**

      - Giao diện `BookRepository` (để trừu tượng hóa việc truy cập CSDL):
        - Phương thức: `addBook(book: Book): void`
        - Phương thức: `findBookByISBN(isbn: string): Book`
        - Phương thức: `updateBook(book: Book): void`

  3.  **Thiết kế Lớp Dịch vụ (Service Class):**
      - Lớp `BookManagementService`:
        - Thuộc tính: `bookRepository: BookRepository`.
        - Phương thức: `addNewBook(isbn, title, author)`:
          - _Thuật toán:_
            1.  Kiểm tra xem sách với ISBN này đã tồn tại chưa bằng cách gọi `bookRepository.findBookByISBN()`.
            2.  Nếu đã tồn tại, báo lỗi.
            3.  Nếu chưa, tạo một đối tượng `Book` mới.
            4.  Gọi `bookRepository.addBook()` để lưu sách.

  **Biểu diễn bằng mã giả (Python-like):**

  ```python
  # Interface (Abstract Base Class in Python)
  class BookRepository(ABC):
      @abstractmethod
      def addBook(self, book: Book):
          pass

      @abstractmethod
      def findBookByISBN(self, isbn: str) -> Book:
          pass

  # Class
  class Book:
      def __init__(self, isbn: str, title: str, author: str):
          self.isbn = isbn
          self.title = title
          self.author = author
          self.isAvailable = True

  # Service Class
  class BookManagementService:
      def __init__(self, repository: BookRepository):
          self.bookRepository = repository

      def addNewBook(self, isbn: str, title: str, author: str):
          # Detailed logic and algorithm
          existing_book = self.bookRepository.findBookByISBN(isbn)
          if existing_book:
              raise ValueError("Book with this ISBN already exists.")

          new_book = Book(isbn, title, author)
          self.bookRepository.addBook(new_book)
          print("Book added successfully.")
  ```

---

### **6. Kết luận (Conclusion)**

Thiết kế Chi tiết là bước không thể thiếu để đảm bảo chất lượng và tính nhất quán của mã nguồn. Nó là cây cầu vững chắc nối liền giữa tầm nhìn kiến trúc tổng thể và việc hiện thực hóa phần mềm cụ thể, giúp giảm thiểu rủi ro, tăng hiệu quả làm việc cho đội ngũ lập trình và tạo ra một sản phẩm dễ bảo trì hơn.

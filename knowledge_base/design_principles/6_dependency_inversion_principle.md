# Nguyên lý Đảo ngược Phụ thuộc (Dependency Inversion Principle - DIP)

### **I. Định nghĩa**

**Nguyên lý Đảo ngược Phụ thuộc** là nguyên lý cuối cùng trong bộ 5 nguyên lý SOLID. Nguyên lý này phát biểu rằng:

1.  **Các module cấp cao không nên phụ thuộc vào các module cấp thấp. Cả hai nên phụ thuộc vào một abstraction (giao diện trừu tượng).**
2.  **Abstractions không nên phụ thuộc vào chi tiết. Chi tiết nên phụ thuộc vào abstractions.**

Nói một cách đơn giản: Thay vì code của bạn phụ thuộc vào một "công cụ" cụ thể, nó nên phụ thuộc vào một "bản thiết kế" của công cụ đó. Điều này cho phép bạn dễ dàng thay đổi "công cụ" trong tương lai mà không cần phải sửa lại code.

---

### **II. Vấn đề cần giải quyết**

Hãy tưởng tượng một lớp `PasswordReminder` có nhiệm vụ gửi lời nhắc mật khẩu. Ban đầu, nó được thiết kế để kết nối trực tiếp với cơ sở dữ liệu MySQL.

**Ví dụ code "trước" khi áp dụng DIP (Vi phạm nguyên lý):**

```python
# Module cấp thấp: Kết nối trực tiếp với MySQL
class MySQLConnection:
    def connect(self):
        print("Connecting to MySQL database...")
        return "MySQL connection object"

# Module cấp cao: Phụ thuộc trực tiếp vào module cấp thấp
class PasswordReminder:
    def __init__(self):
        self.db_connection = MySQLConnection() # Phụ thuộc cứng vào MySQLConnection

    def get_users_to_remind(self):
        connection = self.db_connection.connect()
        # Logic để lấy danh sách người dùng từ MySQL...
        print("Getting users from MySQL to remind password.")
        return ["user1_from_mysql", "user2_from_mysql"]

# Sử dụng
reminder = PasswordReminder()
reminder.get_users_to_remind()
```

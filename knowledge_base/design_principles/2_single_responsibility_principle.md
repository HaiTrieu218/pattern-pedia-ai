# Nguyên lý Đơn trách nhiệm (Single Responsibility Principle - SRP)

---

## 1. Định nghĩa

Nguyên lý Đơn trách nhiệm là chữ **S** trong bộ 5 nguyên lý **SOLID**. Nguyên lý này phát biểu rằng:

> **"Một lớp (class) chỉ nên giữ một trách nhiệm duy nhất. Hay nói cách khác, một lớp chỉ nên có một lý do duy nhất để thay đổi."**

"Lý do để thay đổi" ở đây là nguồn gốc của sự thay đổi. Nếu bạn có thể nghĩ ra nhiều hơn một lý do để phải sửa đổi một lớp, thì lớp đó đang vi phạm SRP.

## 2. Vấn đề cần giải quyết

Khi một lớp đảm nhiệm quá nhiều trách nhiệm, nó sẽ trở nên:

- **Khó hiểu và phức tạp:** Một lập trình viên mới sẽ phải mất nhiều thời gian để đọc và hiểu tất cả các chức năng mà lớp đó đang thực hiện.
- **Khó bảo trì và sửa lỗi:** Một thay đổi ở một chức năng có thể vô tình gây ra lỗi ở một chức năng khác không liên quan, vì chúng cùng nằm trong một lớp.
- **Khó tái sử dụng:** Bạn muốn sử dụng lại chức năng A, nhưng nó lại bị "dính" chặt với chức năng B, C trong cùng một lớp. Điều này làm giảm khả năng tái sử dụng code.
- **Vi phạm sự gắn kết cao (High Cohesion):** Các phương thức và thuộc tính trong lớp không liên quan chặt chẽ với nhau.

## 3. Ví dụ minh họa

Hãy xem xét một ví dụ về một lớp `Employee` vi phạm nguyên lý SRP.

### 3.1. Code "tồi" (vi phạm SRP)

Lớp `Employee` này vừa quản lý thông tin nhân viên, vừa tính lương, vừa lưu thông tin vào cơ sở dữ liệu.

```python
# VI PHẠM SRP
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_name(self):
        return self.name

    # TRÁCH NHIỆM 1: Tính toán nghiệp vụ
    def calculate_bonus(self):
        return self.salary * 0.1

    # TRÁCH NHIỆM 2: Lưu trữ dữ liệu
    def save_to_database(self):
        # Giả lập việc kết nối và lưu vào CSDL
        print(f"Saving {self.name} to the database...")
        # ... logic kết nối CSDL và lưu dữ liệu ...

    # TRÁCH NHIỆM 3: Trình bày dữ liệu
    def generate_report_html(self):
        # Giả lập việc tạo báo cáo HTML
        return f"<h1>Employee Report for {self.name}</h1><p>Position: {self.position}</p>"
```

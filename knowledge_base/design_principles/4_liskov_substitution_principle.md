# Nguyên lý Thay thế Liskov (Liskov Substitution Principle - LSP)

**Phát biểu bởi Barbara Liskov, Nguyên lý Thay thế Liskov là chữ "L" trong SOLID. Đây là một trong những nguyên lý quan trọng nhất để đảm bảo tính đúng đắn của việc kế thừa trong lập trình hướng đối tượng.**

---

## I. Định nghĩa

> "Các đối tượng của một lớp cha phải có thể được thay thế bằng các đối tượng của lớp con mà không làm thay đổi tính đúng đắn của chương trình."

Nói một cách đơn giản hơn: **Nếu bạn có một đoạn code đang làm việc với một đối tượng của lớp cha, bạn phải có khả năng thay thế đối tượng đó bằng một đối tượng của bất kỳ lớp con nào của nó, và chương trình vẫn phải chạy đúng mà không cần bất kỳ sự thay đổi nào.**

Lớp con phải là một "sự thay thế hoàn hảo" cho lớp cha. Nó có thể mở rộng chức năng, nhưng không được phép phá vỡ hoặc thay đổi hành vi cơ bản đã được định nghĩa ở lớp cha.

---

## II. Vấn đề cần giải quyết

Nguyên lý này giải quyết một vấn đề kinh điển trong kế thừa: **Kế thừa không hợp lý (Improper Inheritance)**.

Khi một lớp con kế thừa từ một lớp cha, nó được thừa hưởng tất cả các phương thức và thuộc tính. Tuy nhiên, nếu lớp con thay đổi hành vi của một phương thức được kế thừa một cách bất ngờ, nó sẽ phá vỡ "hợp đồng" mà lớp cha đã thiết lập. Điều này dẫn đến các lỗi khó lường và làm cho code trở nên khó bảo trì.

**Dấu hiệu vi phạm LSP:**

- Một phương thức trong lớp con ghi đè phương thức của lớp cha nhưng lại không làm gì cả, hoặc ném ra một ngoại lệ `UnsupportedOperationException`.
- Bạn phải dùng `if (obj instanceof SubClass)` để kiểm tra kiểu của đối tượng trước khi gọi phương thức của nó. Đây là một "red flag" rất lớn.

---

## III. Ví dụ Minh họa

Hãy xem xét một ví dụ kinh điển: **Hình chữ nhật và Hình vuông**.

### 1. Kịch bản Vi phạm LSP

Về mặt toán học, hình vuông là một trường hợp đặc biệt của hình chữ nhật. Vì vậy, ta có thể nghĩ rằng lớp `Square` nên kế thừa từ `Rectangle`.

**Lớp cha `Rectangle`:**

```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def calculate_area(self):
        return self._width * self._height
```

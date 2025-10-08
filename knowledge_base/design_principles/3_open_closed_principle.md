# Nguyên lý Đóng/Mở (Open/Closed Principle - OCP)

---

## 1. Định nghĩa

Nguyên lý Đóng/Mở là chữ "O" trong bộ nguyên lý SOLID. Nguyên lý này phát biểu rằng:

> **"Các thực thể phần mềm (lớp, mô-đun, hàm, ...) nên có thể được mở rộng (open for extension) nhưng phải đóng với việc sửa đổi (closed for modification)."**

Nói một cách đơn giản, bạn nên có khả năng **thêm chức năng mới** vào một lớp mà **không cần phải sửa đổi mã nguồn hiện có** của lớp đó.

---

## 2. Vấn đề giải quyết

Hãy tưởng tượng bạn có một lớp `PaymentProcessor` xử lý các khoản thanh toán. Ban đầu, nó chỉ hỗ trợ thanh toán bằng thẻ tín dụng.

```python
# VI PHẠM NGUYÊN LÝ OCP
class PaymentProcessor:
    def process_credit_card(self, amount):
        print(f"Processing credit card payment of ${amount}")

# Sử dụng
processor = PaymentProcessor()
processor.process_credit_card(100)
```

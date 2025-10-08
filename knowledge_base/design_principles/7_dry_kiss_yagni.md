# Các Nguyên lý Thiết kế Phổ biến: DRY, KISS, YAGNI

Ngoài bộ 5 nguyên lý SOLID, trong ngành phát triển phần mềm còn có các nguyên lý và triết lý thiết kế khác, ngắn gọn nhưng cực kỳ mạnh mẽ, giúp định hướng cho lập trình viên trong công việc hàng ngày. Ba trong số những nguyên lý nổi tiếng nhất là DRY, KISS và YAGNI.

---

## 1. Nguyên lý DRY (Don't Repeat Yourself - Đừng Lặp lại Chính mình)

### Định nghĩa

DRY là một nguyên lý phát triển phần mềm nhằm mục đích giảm sự lặp lại của thông tin dưới mọi hình thức. Nguyên lý này nói rằng: "Mọi mẩu kiến thức trong một hệ thống phải có một đại diện duy nhất, không mơ hồ, và có thẩm quyền."

Nói một cách đơn giản, nếu bạn thấy mình đang viết cùng một đoạn code ở nhiều nơi khác nhau, đó là dấu hiệu bạn đang vi phạm DRY.

### Vấn đề giải quyết

- **Khó bảo trì:** Khi cần thay đổi một logic bị lặp lại, bạn phải tìm và sửa ở TẤT CẢ các nơi. Nếu bỏ sót một chỗ, hệ thống sẽ hoạt động không nhất quán và gây ra lỗi.
- **Tăng khả năng phát sinh lỗi:** Càng viết nhiều code, khả năng mắc lỗi càng cao. Việc sao chép-dán (copy-paste) code là một trong những nguyên nhân hàng đầu gây ra bug.
- **Code cồng kềnh và khó đọc:** Sự lặp lại làm cho mã nguồn dài hơn một cách không cần thiết.

### Ví dụ

Giả sử chúng ta có code tính toán giá cuối cùng sau khi đã áp dụng thuế cho sản phẩm.

**❌ Code vi phạm DRY:**

```python
def calculate_price_for_book(price):
    tax = price * 0.05  # 5% tax
    final_price = price + tax
    print(f"Final price for book: ${final_price}")

def calculate_price_for_electronic(price):
    tax = price * 0.05  # Logic tính thuế bị lặp lại
    final_price = price + tax
    print(f"Final price for electronic: ${final_price}")
```

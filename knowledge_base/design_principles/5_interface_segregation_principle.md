# Nguyên lý Phân tách Giao diện (Interface Segregation Principle - ISP)

---

### **Phát biểu**

> **"Clients should not be forced to depend upon interfaces that they do not use."**

> Tạm dịch: **"Máy khách (clients) không nên bị buộc phải phụ thuộc vào những giao diện (interfaces) mà chúng không sử dụng."**

Nguyên lý này là chữ **"I"** trong bộ 5 nguyên lý SOLID.

---

### **Diễn giải & Mục tiêu**

- **Mục tiêu chính:** Nguyên lý này giải quyết vấn đề của các "giao diện béo" (fat interfaces) - tức là những interface quá lớn, chứa quá nhiều phương thức. Khi một class implement một interface "béo", nó bị buộc phải định nghĩa cả những phương thức mà nó không hề cần đến, thường là để chúng trống hoặc ném ra một ngoại lệ.
- **Giải pháp:** Thay vì có một interface lớn, chúng ta nên chia nhỏ nó thành nhiều interface nhỏ hơn, chuyên biệt hơn. Mỗi interface chỉ nên chứa các phương thức có liên quan chặt chẽ đến nhau. Các class sau đó có thể implement chỉ những interface mà chúng thực sự cần.

Nói một cách đơn giản: **"Thà có nhiều giao diện nhỏ còn hơn có một giao diện lớn."**

---

### **Ví dụ Minh họa**

Hãy xem xét một ví dụ về việc quản lý các loại công nhân trong một nhà máy.

#### **TRƯỚC khi áp dụng ISP (Thiết kế tồi)**

Chúng ta có một interface `IWorker` chung cho tất cả công nhân.

```python
# Giao diện "béo" - IWorker
from abc import ABC, abstractmethod

class IWorker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass
```

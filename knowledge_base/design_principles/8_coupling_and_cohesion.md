# Coupling và Cohesion (Độ ghép nối và Độ gắn kết)

## Định nghĩa

**Coupling (Độ ghép nối)** và **Cohesion (Độ gắn kết)** là hai thước đo quan trọng để đánh giá chất lượng của một thiết kế phần mềm, đặc biệt là trong lập trình hướng đối tượng. Chúng giúp xác định mức độ tốt của việc tổ chức và phân chia trách nhiệm giữa các module (hoặc các lớp).

- **Cohesion (Độ gắn kết)** đo lường mức độ liên quan và tập trung của các thành phần **bên trong** một module.

  - **Mục tiêu:** **High Cohesion (Độ gắn kết cao).** Một module có độ gắn kết cao nghĩa là tất cả các chức năng bên trong nó đều phục vụ chung cho một mục đích duy nhất, rõ ràng.

- **Coupling (Độ ghép nối)** đo lường mức độ phụ thuộc lẫn nhau **giữa** các module khác nhau.
  - **Mục tiêu:** **Low Coupling (Độ ghép nối thấp).** Các module có độ ghép nối thấp nghĩa là chúng độc lập với nhau. Sự thay đổi trong một module sẽ ít hoặc không gây ảnh hưởng đến các module khác.

**Tóm lại, một thiết kế tốt sẽ có _High Cohesion_ và _Low Coupling_.**

---

## Vấn đề giải quyết

Việc không quản lý tốt Coupling và Cohesion sẽ dẫn đến các vấn đề nghiêm trọng trong quá trình phát triển và bảo trì phần mềm:

- **Khó bảo trì:** Một thay đổi nhỏ ở một module có thể gây ra lỗi dây chuyền ở nhiều module khác (do High Coupling).
- **Khó tái sử dụng:** Không thể tách một module ra để sử dụng ở nơi khác vì nó phụ thuộc quá nhiều vào các module khác (do High Coupling).
- **Khó hiểu:** Các module chứa các chức năng không liên quan đến nhau khiến code trở nên lộn xộn, khó đọc và khó nắm bắt logic (do Low Cohesion).
- **Khó mở rộng:** Việc thêm chức năng mới trở nên phức tạp vì phải chỉnh sửa ở nhiều nơi.

---

## Ví dụ Minh họa

Hãy xem một ví dụ về việc quản lý thông tin sinh viên và gửi email thông báo.

### **Thiết kế TỆ (Low Cohesion, High Coupling)**

```python
# Low Cohesion: Lớp này làm quá nhiều việc không liên quan
class StudentManager:
    def __init__(self, student_name, student_email, db_connection_string):
        self.student_name = student_name
        self.student_email = student_email
        self.db_connection_string = db_connection_string

    def get_student_details(self):
        # Trả về thông tin sinh viên
        return f"Name: {self.student_name}, Email: {self.student_email}"

    def save_to_database(self):
        # Logic kết nối và lưu vào CSDL
        print(f"Connecting to {self.db_connection_string}...")
        print(f"Saving {self.student_name} to database.")

    def send_notification_email(self, subject, message):
        # Logic gửi email
        # High Coupling: Phụ thuộc trực tiếp vào cách gửi email
        print(f"Sending email to {self.student_email}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")

# Sử dụng
student_manager = StudentManager("An Nguyen", "an.nguyen@example.com", "mysql://user:pass@host/db")
student_manager.save_to_database()
student_manager.send_notification_email("Welcome", "Welcome to our university!")
```

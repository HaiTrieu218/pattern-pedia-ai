# Hạ tầng dưới dạng Mã (Infrastructure as Code - IaC)

---

### **1. Định nghĩa**

**Hạ tầng dưới dạng Mã (Infrastructure as Code - IaC)** là một thực hành trong DevOps, trong đó việc quản lý và cấp phát hạ tầng (máy chủ, mạng, cơ sở dữ liệu, cân bằng tải...) được thực hiện thông qua các file cấu hình có thể đọc được bởi máy tính (code), thay vì phải cấu hình thủ công qua giao diện hoặc các dòng lệnh riêng lẻ.

Nói một cách đơn giản, thay vì "click chuột" để tạo một máy chủ ảo, bạn sẽ "viết code" để định nghĩa các thông số của máy chủ đó, và một công cụ sẽ tự động tạo ra máy chủ y hệt như những gì bạn đã viết.

---

### **2. Vấn đề giải quyết**

IaC ra đời để giải quyết các vấn đề cố hữu của việc quản lý hạ tầng thủ công:

- **Lỗi do con người (Human Error):** Cấu hình thủ công rất dễ xảy ra sai sót, quên bước, hoặc cấu hình không nhất quán giữa các môi trường.
- **Môi trường không đồng nhất (Environment Drift):** Môi trường `Staging` và `Production` ban đầu có thể giống nhau, nhưng qua thời gian, các thay đổi thủ công nhỏ lẻ làm chúng trở nên khác biệt, dẫn đến lỗi "code chạy trên staging nhưng lỗi trên production".
- **Tốn thời gian và không thể lặp lại:** Việc xây dựng lại một môi trường phức tạp từ đầu một cách thủ công tốn rất nhiều thời gian và công sức.
- **Khó theo dõi và kiểm duyệt:** Không có lịch sử rõ ràng về việc ai đã thay đổi cái gì, khi nào và tại sao.

---

### **3. Cách hoạt động và Ví dụ**

Bạn sẽ sử dụng một ngôn ngữ khai báo (declarative language) để định nghĩa "trạng thái mong muốn" (desired state) của hạ tầng. Sau đó, công cụ IaC sẽ so sánh trạng thái mong muốn này với "trạng thái thực tế" (actual state) và tự động thực hiện các hành động cần thiết (tạo, sửa, xóa) để đưa hạ tầng về đúng trạng thái mong muốn.

**Ví dụ với Terraform (một công cụ IaC phổ biến):**

Đoạn code dưới đây định nghĩa việc tạo một máy chủ ảo (EC2 instance) trên nền tảng Amazon Web Services (AWS).

```terraform
# Định nghĩa nhà cung cấp dịch vụ đám mây là AWS
provider "aws" {
  region = "us-east-1"
}

# Định nghĩa một tài nguyên: máy chủ ảo EC2
resource "aws_instance" "web_server" {
  ami           = "ami-0c55b159cbfafe1f0" # ID của hệ điều hành (Ubuntu)
  instance_type = "t2.micro"           # Loại máy chủ (cấu hình nhỏ)

  tags = {
    Name = "MyWebServer"
  }
}
```

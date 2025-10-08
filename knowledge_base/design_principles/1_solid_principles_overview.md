# Tổng quan về Các Nguyên lý SOLID

## Định nghĩa

**SOLID** là từ viết tắt của năm nguyên lý thiết kế cơ bản trong lập trình hướng đối tượng (Object-Oriented Programming - OOP). Các nguyên lý này được Robert C. Martin (hay còn gọi là "Uncle Bob") giới thiệu và phát triển, nhằm mục đích giúp các lập trình viên tạo ra những hệ thống phần mềm **dễ hiểu, linh hoạt, dễ bảo trì và dễ mở rộng**.

Việc tuân thủ SOLID giúp tránh được các thiết kế tệ, giảm thiểu sự phức tạp khi dự án lớn dần và hạn chế việc phải viết lại code (refactoring) trên quy mô lớn.

## Tại sao SOLID lại quan trọng?

Hãy tưởng tượng bạn đang xây một ngôi nhà bằng các khối LEGO.

- **Không có SOLID:** Bạn xây các bức tường bằng cách dán chết các khối LEGO lại với nhau bằng keo siêu dính. Ban đầu thì có vẻ chắc chắn, nhưng khi bạn muốn thay đổi một cửa sổ hoặc thêm một cánh cửa, bạn sẽ phải đập vỡ cả bức tường.
- **Có SOLID:** Bạn xây các bức tường bằng cách lắp ghép các khối LEGO lại với nhau một cách hợp lý. Khi cần thay đổi, bạn chỉ cần nhẹ nhàng tháo dỡ một vài khối, thay thế chúng và lắp lại. Ngôi nhà của bạn trở nên linh hoạt và dễ nâng cấp hơn rất nhiều.

Trong phần mềm, SOLID chính là các quy tắc "lắp ghép LEGO" đó. Nó giúp tạo ra các thành phần (modules, classes) độc lập, có trách nhiệm rõ ràng và liên kết với nhau một cách lỏng lẻo (loosely coupled).

## Tóm tắt 5 Nguyên lý

Dưới đây là tóm tắt ngắn gọn về "ý nghĩa" của từng chữ cái trong SOLID. Mỗi nguyên lý sẽ được giải thích chi tiết trong các bài viết riêng.

### 1. **S - Single Responsibility Principle (Nguyên lý Đơn trách nhiệm)**

- **Tư tưởng:** Một lớp (class) chỉ nên có một và chỉ một lý do để thay đổi.
- **Ví dụ đời thực:** Một chiếc dao của lính Thụy Sĩ có quá nhiều chức năng (cắt, vặn vít, mở hộp...). Nếu một chức năng bị hỏng hoặc cần nâng cấp (ví dụ lưỡi dao bị cùn), bạn có thể phải sửa cả cái dao. Thay vào đó, một con dao, một cái tuốc nơ vít, và một cái mở hộp riêng biệt sẽ dễ quản lý và thay thế hơn. Mỗi công cụ chỉ có một trách nhiệm duy nhất.

### 2. **O - Open/Closed Principle (Nguyên lý Đóng/Mở)**

- **Tư tưởng:** Các thực thể phần mềm (lớp, module, hàm) nên **mở** cho việc mở rộng (extension) nhưng **đóng** cho việc sửa đổi (modification).
- **Ví dụ đời thực:** Hãy nghĩ về các cổng cắm USB trên máy tính. Bạn có thể cắm thêm vô số thiết bị mới (chuột, bàn phím, webcam...) mà không cần phải mở máy tính ra và sửa đổi bo mạch chủ. Bo mạch chủ "đóng" cho việc sửa đổi, nhưng "mở" cho việc cắm thêm chức năng mới qua cổng USB.

### 3. **L - Liskov Substitution Principle (Nguyên lý Thay thế Liskov)**

- **Tư tưởng:** Các đối tượng của lớp con (subclass) phải có thể thay thế được cho các đối tượng của lớp cha (superclass) mà không làm thay đổi tính đúng đắn của chương trình.
- **Ví dụ đời thực:** Nếu bạn có một cái điều khiển TV, nó có thể dùng được cho tất cả các loại TV (lớp cha). Bạn có thể thay thế một chiếc TV Sony (lớp con) bằng một chiếc TV Samsung (lớp con khác) và cái điều khiển vẫn phải hoạt động đúng. Nếu có một loại "TV" nào đó mà khi thay vào, nút tăng âm lượng lại thành tắt TV, thì nó đã vi phạm nguyên lý này.

### 4. **I - Interface Segregation Principle (Nguyên lý Phân tách Giao diện)**

- **Tư tưởng:** Thà có nhiều giao diện (interface) nhỏ, chuyên biệt còn hơn là một giao diện lớn, tổng hợp. Client không nên bị buộc phải phụ thuộc vào những phương thức mà nó không sử dụng.
- **Ví dụ đời thực:** Hãy nghĩ về một nhà hàng. Thay vì đưa cho tất cả khách hàng (đầu bếp, phục vụ, thu ngân) một cuốn sổ tay hướng dẫn khổng lồ chứa tất cả các quy trình, nhà hàng sẽ có các bản hướng dẫn riêng: một bản cho đầu bếp (công thức nấu ăn), một bản cho phục vụ (cách nhận order), một bản cho thu ngân (cách dùng máy tính tiền). Mỗi người chỉ cần quan tâm đến "giao diện" công việc của mình.

### 5. **D - Dependency Inversion Principle (Nguyên lý Đảo ngược Phụ thuộc)**

- **Tư tưởng:** Các module cấp cao không nên phụ thuộc vào các module cấp thấp. Cả hai nên phụ thuộc vào một sự trừu tượng (abstraction, thường là interface). Hơn nữa, sự trừu tượng không nên phụ thuộc vào chi tiết, mà chi tiết nên phụ thuộc vào sự trừu tượng.
- **Ví dụ đời thực:** Bạn không hàn chết cái bóng đèn vào dây điện trong nhà. Thay vào đó, bạn lắp một cái đui đèn (sự trừu tượng). Cái đui đèn này không quan tâm bạn lắp bóng đèn sợi đốt, bóng đèn LED hay bóng đèn compact (chi tiết). Cả dây điện (module cấp cao) và bóng đèn (module cấp thấp) đều "phụ thuộc" vào chuẩn của cái đui đèn. Nhờ vậy, bạn có thể dễ dàng thay thế bóng đèn khi nó cháy.

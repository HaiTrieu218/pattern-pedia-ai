# Tích hợp Liên tục (Continuous Integration - CI)

---

### **1. Định nghĩa**

**Tích hợp Liên tục (Continuous Integration - CI)** là một thực hành phát triển phần mềm trong đó các lập trình viên thường xuyên tích hợp (merge) các thay đổi về mã nguồn của họ vào một kho lưu trữ chung (repository). Sau mỗi lần tích hợp, một quy trình **build và kiểm thử tự động** sẽ được kích hoạt.

Mục tiêu chính của CI là phát hiện các lỗi tích hợp một cách sớm nhất và nhanh nhất có thể, giúp cải thiện chất lượng phần mềm và tăng tốc độ phát triển.

### **2. Vấn đề giải quyết**

Hãy tưởng tượng một dự án không có CI:

- Nhiều lập trình viên làm việc trên các nhánh (branches) riêng biệt trong nhiều ngày, thậm chí nhiều tuần.
- Khi đến hạn, tất cả mọi người cùng lúc hợp nhất (merge) code của họ vào nhánh chính.
- Kết quả là một "Địa ngục Tích hợp" (Integration Hell):
  - **Xung đột mã nguồn (Merge Conflicts):** Rất nhiều file bị thay đổi bởi nhiều người cùng lúc, gây ra xung đột khó giải quyết.
  - **Lỗi tiềm ẩn:** Code của người A có thể phá vỡ chức năng của người B, nhưng chỉ được phát hiện vào phút cuối.
  - **Tốn thời gian:** Cả nhóm phải dừng lại mọi việc để sửa lỗi tích hợp, gây trễ tiến độ nghiêm trọng.

CI ra đời để giải quyết triệt để vấn đề này bằng cách biến việc tích hợp từ một sự kiện lớn, đáng sợ thành một hành động nhỏ, thường xuyên và tự động.

### **3. Luồng hoạt động của CI**

Một quy trình CI điển hình hoạt động như sau:

1.  **Commit & Push:** Một lập trình viên hoàn thành một phần công việc nhỏ và đẩy (push) mã nguồn lên kho lưu trữ (ví dụ: GitHub, GitLab).
2.  **Kích hoạt Tự động:** Hệ thống CI Server (ví dụ: GitHub Actions) phát hiện thay đổi này và tự động kích hoạt một quy trình (pipeline).
3.  **Build:** Hệ thống lấy phiên bản mã nguồn mới nhất và thực hiện "build" dự án (ví dụ: biên dịch mã Java, cài đặt các gói phụ thuộc của Python).
4.  **Kiểm thử (Test):** Nếu build thành công, hệ thống sẽ tự động chạy bộ kiểm thử đã được định nghĩa sẵn, đặc biệt là **Unit Tests** và **Integration Tests**.
5.  **Thông báo Kết quả:**
    - **Thành công:** Lập trình viên nhận được thông báo rằng thay đổi của họ an toàn và không làm hỏng hệ thống.
    - **Thất bại:** Nếu build hoặc kiểm thử thất bại, hệ thống sẽ ngay lập tức thông báo cho nhóm phát triển. Lập trình viên gây ra lỗi phải có trách nhiệm sửa nó ngay lập tức.

### **4. Ưu điểm**

- **Phát hiện lỗi sớm:** Lỗi được tìm thấy ngay sau khi chúng được tạo ra, giúp việc sửa chữa dễ dàng và ít tốn kém hơn.
- **Giảm thiểu rủi ro tích hợp:** Không còn "Integration Hell" vì việc tích hợp diễn ra liên tục với các thay đổi nhỏ.
- **Tăng tốc độ phát triển:** Lập trình viên tự tin hơn khi thay đổi code và không phải tốn thời gian cho việc tích hợp thủ công.
- **Cải thiện chất lượng mã nguồn:** Việc kiểm thử tự động đảm bảo một mức chất lượng tối thiểu cho mọi thay đổi.
- **Luôn có một phiên bản "chạy được":** Nhánh chính (main/master) gần như luôn ở trạng thái ổn định và sẵn sàng để triển khai.

### **5. Nhược điểm**

- **Chi phí thiết lập ban đầu:** Cần thời gian và kiến thức để thiết lập và cấu hình một quy trình CI hoàn chỉnh.
- **Yêu cầu văn hóa kỷ luật:** Cả nhóm phải tuân thủ quy trình: commit thường xuyên, viết unit test đầy đủ, và ưu tiên sửa lỗi build ngay lập tức.
- **Cần tài nguyên hạ tầng:** Cần có một máy chủ (CI Server) để chạy các quy trình build và test, có thể tốn chi phí nếu dự án lớn.

### **6. Các Công cụ Phổ biến**

- **Jenkins:** Một trong những công cụ CI/CD mã nguồn mở lâu đời và mạnh mẽ nhất.
- **GitHub Actions:** Tích hợp sẵn trong GitHub, rất dễ sử dụng và phổ biến.
- **GitLab CI/CD:** Tích hợp sẵn trong GitLab, cung cấp một giải pháp toàn diện.
- **CircleCI:** Một dịch vụ CI/CD trên nền tảng đám mây, nổi tiếng về tốc độ.
- **Travis CI:** Một dịch vụ phổ biến khác, đặc biệt cho các dự án mã nguồn mở.

# Quản lý Yêu cầu (Requirements Management)

### Định nghĩa

**Quản lý Yêu cầu** là quá trình quản lý sự thay đổi của các yêu cầu trong suốt vòng đời phát triển phần mềm. Đây là một hoạt động diễn ra song song và liên tục, từ khi yêu cầu được xác định lần đầu cho đến khi hệ thống bị loại bỏ.

Mục tiêu chính của Quản lý Yêu cầu không phải là để ngăn chặn sự thay đổi, mà là để **kiểm soát** và **quản lý** những thay đổi đó một cách có hệ thống, đảm bảo rằng mọi bên liên quan đều hiểu rõ về các tác động của sự thay đổi.

---

### Tại sao Cần quản lý Yêu cầu?

Các yêu cầu của một hệ thống phần mềm **luôn luôn thay đổi**. Việc quản lý chúng là cực kỳ quan trọng vì các lý do sau:

1.  **Thay đổi từ Môi trường Kinh doanh:** Doanh nghiệp có thể thay đổi chiến lược, có đối thủ cạnh tranh mới, hoặc các quy định của chính phủ thay đổi, dẫn đến việc phải điều chỉnh các yêu cầu của phần mềm.
2.  **Hiểu biết của Khách hàng Tăng lên:** Khi khách hàng nhìn thấy các phiên bản đầu tiên của hệ thống (bản mẫu, bản demo), họ sẽ hiểu rõ hơn về những gì họ thực sự cần và đề xuất các thay đổi.
3.  **Vấn đề Kỹ thuật:** Trong quá trình phát triển, đội ngũ kỹ thuật có thể nhận ra một số yêu cầu là không khả thi về mặt kỹ thuật, quá tốn kém, hoặc có thể được giải quyết bằng một phương án tốt hơn.

Nếu không có một quy trình quản lý thay đổi, dự án sẽ nhanh chóng rơi vào hỗn loạn, dẫn đến "scope creep" (phạm vi dự án phình to không kiểm soát), trễ tiến độ, và vượt ngân sách.

---

### Các Hoạt động Chính trong Quản lý Yêu cầu

#### 1. Lập kế hoạch Quản lý Yêu cầu (Management Planning)

Đây là bước đầu tiên, xác định "luật chơi" cho việc quản lý thay đổi. Kế hoạch này định nghĩa:

- **Quy trình quản lý thay đổi:** Các bước cần thực hiện khi có một yêu cầu thay đổi được đề xuất.
- **Phân tích tác động:** Cách thức đánh giá tác động của một thay đổi lên tiến độ, chi phí, và các yêu cầu khác.
- **Truy vết yêu cầu:** Chính sách và công cụ được sử dụng để theo dõi các liên kết của yêu cầu.
- **Hội đồng Kiểm soát Thay đổi (Change Control Board - CCB):** Ai là người có thẩm quyền phê duyệt hoặc từ chối các thay đổi.

#### 2. Quản lý Thay đổi (Change Management)

Đây là quy trình cốt lõi, thường bao gồm các bước sau:

1.  **Phân tích Vấn đề & Đề xuất Thay đổi:** Một bên liên quan (stakeholder) xác định vấn đề và đề xuất một yêu cầu thay đổi chính thức.
2.  **Phân tích & Đánh giá Tác động:** Yêu cầu thay đổi được phân tích để xác định chi phí, lợi ích, và tác động của nó lên hệ thống. Các yêu cầu khác bị ảnh hưởng sẽ được xác định.
3.  **Phê duyệt hoặc Từ chối:** Hội đồng Kiểm soát Thay đổi (CCB) xem xét bản phân tích và quyết định có thực hiện thay đổi hay không.
4.  **Hiện thực hóa Thay đổi:** Nếu được phê duyệt, thay đổi sẽ được đưa vào kế hoạch, tài liệu yêu cầu, thiết kế, mã nguồn và các ca kiểm thử liên quan sẽ được cập nhật.

#### 3. Truy vết Yêu cầu (Requirements Traceability)

**Truy vết yêu cầu** là khả năng theo dõi một yêu cầu theo cả hai chiều: "tiến" và "lùi" trong suốt vòng đời phát triển.

- **Truy vết tiến (Forward traceability):** Từ một yêu cầu cụ thể, chúng ta có thể tìm ra các thành phần thiết kế, các dòng code, và các ca kiểm thử đã được tạo ra để hiện thực hóa nó.
  - _Câu hỏi trả lời được:_ "Thành phần nào của hệ thống sẽ bị ảnh hưởng nếu yêu cầu này thay đổi?"
- **Truy vết lùi (Backward traceability):** Từ một đoạn code, chúng ta có thể tìm ngược lại yêu cầu ban đầu đã sinh ra nó.
  - _Câu hỏi trả lời được:_ "Tại sao đoạn code này lại tồn tại? Nó phục vụ cho mục đích kinh doanh nào?"

**Ma trận Truy vết Yêu cầu (Requirements Traceability Matrix - RTM)** là một công cụ phổ biến để tài liệu hóa các liên kết này.

| Yêu cầu ID | Mô tả Yêu cầu        | Module Thiết kế | File Mã nguồn | Ca Kiểm thử ID |
| :--------- | :------------------- | :-------------- | :------------ | :------------- |
| REQ-001    | Người dùng đăng nhập | `AuthModule`    | `login.py`    | TC-001, TC-002 |
| REQ-002    | Tìm kiếm sản phẩm    | `SearchModule`  | `search.py`   | TC-005, TC-006 |

---

### Tóm tắt

Quản lý Yêu cầu là một hoạt động thiết yếu để đảm bảo sự thành công của các dự án phần mềm phức tạp và dài hạn. Bằng cách thiết lập một quy trình quản lý thay đổi rõ ràng và duy trì khả năng truy vết, các nhóm phát triển có thể thích ứng với những thay đổi không thể tránh khỏi một cách có kiểm soát, giảm thiểu rủi ro và đảm bảo sản phẩm cuối cùng vẫn đáp ứng được mục tiêu kinh doanh.

# Quản lý Cấu hình Phần mềm (Software Configuration Management - SCM)

## Định nghĩa

**Quản lý Cấu hình Phần mềm (SCM)** là một tập hợp các hoạt động và kỹ thuật được sử dụng để quản lý một cách có hệ thống các thay đổi đối với sản phẩm phần mềm trong suốt vòng đời của nó. Mục tiêu chính của SCM là đảm bảo tính toàn vẹn, truy xuất được và kiểm soát được tất cả các thành phần cấu thành nên phần mềm.

Nói một cách đơn giản, SCM trả lời các câu hỏi:

- Ai đã thay đổi cái gì?
- Tại sao họ lại thay đổi nó?
- Khi nào sự thay đổi đó diễn ra?
- Làm thế nào để quay lại phiên bản cũ nếu thay đổi gây ra lỗi?

## Mục tiêu chính

- **Quản lý Thay đổi (Change Management):** Cung cấp một quy trình có cấu trúc để yêu cầu, đánh giá, phê duyệt và triển khai các thay đổi.
- **Kiểm soát Phiên bản (Version Control):** Theo dõi và quản lý nhiều phiên bản của các thành phần phần mềm (mã nguồn, tài liệu, file thiết kế...).
- **Đảm bảo Tính toàn vẹn (Integrity Assurance):** Đảm bảo rằng sản phẩm phần mềm được xây dựng từ đúng phiên bản của các thành phần.
- **Truy xuất Nguồn gốc (Traceability):** Khả năng theo dõi lịch sử của từng thành phần, từ yêu cầu ban đầu cho đến phiên bản hiện tại.

## Các Thành phần cốt lõi của SCM

### 1. Kiểm soát Phiên bản (Version Control)

Đây là trái tim của SCM. Hệ thống Kiểm soát Phiên bản (Version Control System - VCS) là công cụ cho phép các nhà phát triển theo dõi lịch sử thay đổi của mã nguồn và hợp tác làm việc với nhau.

- **Hệ thống Tập trung (Centralized - CVCS):** Có một máy chủ trung tâm chứa toàn bộ lịch sử. Ví dụ: SVN.
- **Hệ thống Phân tán (Distributed - DVCS):** Mỗi nhà phát triển có một bản sao đầy đủ của toàn bộ lịch sử trên máy của mình. **Git** là hệ thống DVCS phổ biến nhất hiện nay.

### 2. Quản lý Xây dựng (Build Management)

Quá trình biên dịch mã nguồn và các tài sản khác để tạo ra một sản phẩm phần mềm có thể thực thi được. Các công cụ build tự động (như Maven, Gradle, Webpack) đóng vai trò quan trọng trong SCM.

### 3. Quản lý Phát hành (Release Management)

Quản lý việc đóng gói, triển khai và phát hành các phiên bản phần mềm khác nhau cho người dùng cuối.

## Luồng làm việc Git cơ bản (Basic Git Workflow)

Git là công cụ VCS quan trọng nhất trong thực hành SCM hiện đại. Dưới đây là các khái niệm và luồng làm việc cơ bản:

- **Repository (Repo):** Kho chứa toàn bộ mã nguồn và lịch sử thay đổi của dự án.
- **Commit:** Một "ảnh chụp" (snapshot) của toàn bộ các file trong dự án tại một thời điểm nhất định. Mỗi commit có một mã định danh duy nhất và một thông điệp mô tả sự thay đổi.
- **Branch (Nhánh):** Một dòng phát triển độc lập. Nhánh `main` (hoặc `master`) thường là nhánh chính thức. Các nhà phát triển tạo ra các nhánh mới (ví dụ: `feature/add-login`) để phát triển tính năng mới mà không ảnh hưởng đến nhánh chính.
- **Merge (Trộn):** Hành động gộp lịch sử của một nhánh vào một nhánh khác. Ví dụ, sau khi hoàn thành tính năng đăng nhập, nhánh `feature/add-login` sẽ được merge vào nhánh `main`.
- **Pull Request (hoặc Merge Request):** Một yêu cầu để merge code từ nhánh này sang nhánh khác. Đây là cơ chế cốt lõi để **Code Review** (đánh giá mã nguồn), nơi các thành viên khác trong nhóm có thể xem xét, bình luận và phê duyệt các thay đổi trước khi chúng được gộp vào nhánh chính.

## Ví dụ thực tế

Một nhóm phát triển đang xây dựng một tính năng mới.

1.  Một lập trình viên tạo một nhánh mới từ nhánh `develop` tên là `feature/user-profile`.
2.  Họ thực hiện các thay đổi, viết code và `commit` nhiều lần trên nhánh của mình.
3.  Khi hoàn thành, họ đẩy (push) nhánh `feature/user-profile` lên kho chứa từ xa (GitHub, GitLab).
4.  Họ tạo một **Pull Request** để yêu cầu merge nhánh của mình vào nhánh `develop`.
5.  Các thành viên khác trong nhóm vào xem code, bình luận và yêu cầu chỉnh sửa.
6.  Sau khi được phê duyệt, Pull Request được chấp nhận và code mới được gộp vào nhánh `develop`.
    Toàn bộ quy trình này được quản lý và theo dõi bởi hệ thống SCM.

# Mẫu Kiến trúc Nguyên khối (Monolithic Architecture)

## Định nghĩa

Kiến trúc Nguyên khối (Monolithic Architecture) là một mô hình thiết kế phần mềm truyền thống, trong đó toàn bộ ứng dụng được xây dựng và triển khai như **một khối duy nhất, không thể tách rời**.

Trong một ứng dụng nguyên khối, tất cả các thành phần chức năng—chẳng hạn như giao diện người dùng (UI), logic nghiệp vụ (Business Logic), và lớp truy cập dữ liệu (Data Access Layer)—đều được liên kết chặt chẽ với nhau trong cùng một codebase và chạy trên cùng một tiến trình (process).

**Ví dụ Dễ hiểu:** Hãy tưởng tượng một trung tâm thương mại lớn. Tất cả các gian hàng (quần áo, đồ ăn, rạp chiếu phim) đều nằm chung trong một tòa nhà duy nhất. Nếu muốn sửa chữa hoặc nâng cấp rạp chiếu phim, bạn phải tác động đến một phần của cả tòa nhà. Tương tự, một thay đổi nhỏ trong ứng dụng nguyên khối cũng đòi hỏi phải triển khai lại toàn bộ "tòa nhà" ứng dụng.

## Sơ đồ Minh họa

Một kiến trúc nguyên khối điển hình có thể được minh họa đơn giản như sau:

# Giấy phép Phần mềm (Software Licensing)

## Định nghĩa

**Giấy phép Phần mềm (Software License)** là một tài liệu pháp lý quy định các quyền và hạn chế của người dùng đối với việc sử dụng, sửa đổi và phân phối một phần mềm. Nó giống như một "hợp đồng" giữa nhà phát triển và người dùng cuối, định rõ những gì người dùng được phép và không được phép làm với sản phẩm phần mềm.

---

## Vấn đề cần giải quyết

Khi một người tạo ra một phần mềm, mã nguồn của nó mặc định được bảo vệ bởi luật bản quyền. Điều này có nghĩa là không ai khác có quyền sao chép, sửa đổi hay chia sẻ nó mà không có sự cho phép của tác giả.

Tuy nhiên, điều này lại hạn chế sự phát triển và cộng tác. Giấy phép phần mềm ra đời để giải quyết vấn đề này, nó cung cấp một khung pháp lý rõ ràng để tác giả có thể cấp cho người khác một số quyền nhất định, đồng thời vẫn bảo vệ quyền sở hữu trí tuệ của mình.

---

## Các loại Giấy phép Phổ biến

Có hai loại giấy phép chính, tạo ra hai thế giới phần mềm khác nhau:

### 1. Phần mềm Sở hữu Độc quyền (Proprietary Software)

Đây còn được gọi là phần mềm "nguồn đóng".

- **Đặc điểm:**
  - Người dùng thường phải trả phí để sử dụng.
  - Mã nguồn (`source code`) không được công khai. Người dùng chỉ nhận được file thực thi (`executable file`).
  - Việc sửa đổi, sao chép, và phân phối lại phần mềm thường bị cấm hoặc hạn chế rất nghiêm ngặt.
- **Ví dụ:**
  - Hệ điều hành Microsoft Windows.
  - Bộ công cụ Adobe Photoshop.
  - Các trò chơi của các hãng lớn.

### 2. Phần mềm Nguồn mở và Miễn phí (Free and Open-Source Software - FOSS)

Đây là phần mềm "nguồn mở", được xây dựng trên tinh thần tự do và cộng tác. Chữ "Free" ở đây mang ý nghĩa "tự do" (freedom) nhiều hơn là "miễn phí" (free of charge).

- **Đặc điểm:**
  - Mã nguồn được công khai. Bất kỳ ai cũng có thể xem, nghiên cứu, và học hỏi.
  - Người dùng có quyền tự do sửa đổi mã nguồn để phù hợp với nhu cầu của mình.
  - Người dùng có quyền tự do chia sẻ (phân phối lại) cả phiên bản gốc và phiên bản đã sửa đổi.
- **Các loại giấy phép FOSS phổ biến:**
  - **Giấy phép MIT (MIT License):** Rất tự do (permissive). Bạn gần như có thể làm bất cứ điều gì với mã nguồn, miễn là bạn giữ lại thông báo bản quyền gốc.
  - **Giấy phép Apache 2.0:** Tương tự MIT nhưng chặt chẽ hơn một chút, yêu cầu ghi lại các thay đổi và cung cấp bảo vệ pháp lý về bằng sáng chế.
  - **Giấy phép Công cộng GNU (GNU GPL):** Đây là giấy phép "copyleft" mạnh mẽ. Nó yêu cầu rằng bất kỳ phần mềm nào được xây dựng dựa trên mã nguồn có giấy phép GPL cũng phải được phát hành dưới giấy phép GPL. Điều này đảm bảo rằng tinh thần "mở" sẽ được lan truyền và duy trì.

---

## Bảng so sánh nhanh

| Tiêu chí            | Phần mềm Độc quyền        | Phần mềm Nguồn mở (FOSS)               |
| :------------------ | :------------------------ | :------------------------------------- |
| **Mã nguồn**        | Đóng, bí mật              | Mở, công khai                          |
| **Chi phí**         | Thường phải trả phí       | Thường miễn phí (nhưng không bắt buộc) |
| **Quyền sửa đổi**   | Bị cấm                    | Được phép và khuyến khích              |
| **Quyền phân phối** | Bị cấm hoặc hạn chế       | Được phép và khuyến khích              |
| **Hỗ trợ**          | Từ nhà cung cấp           | Từ cộng đồng                           |
| **Ví dụ**           | Windows, MacOS, Photoshop | Linux, Android, Firefox, VS Code       |

---

## Ưu điểm và Nhược điểm

- **Phần mềm Độc quyền:**
  - **Ưu điểm:** Thường có sự hỗ trợ chuyên nghiệp, giao diện được đánh bóng, và tính ổn định cao do một công ty duy nhất chịu trách nhiệm.
  - **Nhược điểm:** Phụ thuộc vào nhà cung cấp (vendor lock-in), thiếu minh bạch, chi phí cao.
- **Phần mềm Nguồn mở:**
  - **Ưu điểm:** Linh hoạt, minh bạch, chi phí thấp, được cộng đồng lớn hỗ trợ và phát triển nhanh chóng.
  - **Nhược điểm:** Đôi khi thiếu sự hỗ trợ chính thức, giao diện có thể không thân thiện bằng, và có thể có nhiều phiên bản khác nhau gây phân mảnh.

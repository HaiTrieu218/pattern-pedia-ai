# Khái niệm Cơ bản về Kiểm thử Phần mềm (Testing Fundamentals)

---

## 1. Định nghĩa Kiểm thử Phần mềm (What is Software Testing?)

**Kiểm thử phần mềm (Software Testing)** là một quá trình điều tra, thực thi một chương trình hoặc ứng dụng với mục đích tìm ra các lỗi phần mềm (bugs, errors, defects).

Quan trọng hơn, kiểm thử không chỉ là việc tìm lỗi, mà còn là một hoạt động trong quy trình **Đảm bảo Chất lượng Phần mềm (Software Quality Assurance - SQA)** nhằm cung cấp thông tin về chất lượng của sản phẩm cho các bên liên quan (stakeholders), giúp họ đưa ra quyết định sáng suốt.

Kiểm thử trả lời các câu hỏi như:

- "Phần mềm có đáp ứng đúng các yêu cầu đã đặt ra không?"
- "Phần mềm có hoạt động đúng như người dùng mong đợi không?"
- "Phần mềm có hoạt động ổn định trên các môi trường khác nhau không?"

---

## 2. Mục tiêu của Kiểm thử (Objectives of Testing)

Mục tiêu chính của kiểm thử không phải là để chứng minh phần mềm "không có lỗi", vì điều này gần như là không thể. Thay vào đó, mục tiêu bao gồm:

- **Tìm kiếm lỗi (Finding Defects):** Phát hiện càng nhiều lỗi càng sớm càng tốt trong vòng đời phát triển.
- **Ngăn ngừa lỗi (Preventing Defects):** Quá trình thiết kế các ca kiểm thử (test cases) có thể giúp lập trình viên và nhà phân tích nhận ra các vấn đề trong yêu cầu hoặc thiết kế trước cả khi viết code.
- **Xác minh (Verification):** Đảm bảo rằng phần mềm được xây dựng "đúng cách", tức là tuân thủ đúng các tiêu chuẩn, quy tắc và thiết kế đã đề ra.
- **Xác nhận (Validation):** Đảm bảo rằng phần mềm xây dựng ra là "đúng sản phẩm", tức là đáp ứng được nhu cầu và mong đợi của người dùng cuối.
- **Cung cấp sự tự tin (Gaining Confidence):** Cung cấp bằng chứng cho thấy hệ thống hoạt động ở một mức chất lượng có thể chấp nhận được, giảm thiểu rủi ro khi phát hành sản phẩm.

---

## 3. Xác minh vs. Xác nhận (Verification vs. Validation)

Đây là hai khái niệm cốt lõi thường bị nhầm lẫn trong đảm bảo chất lượng.

| Tiêu chí         | **Xác minh (Verification)**                                                                                | **Xác nhận (Validation)**                                                                                                     |
| :--------------- | :--------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------- |
| **Câu hỏi**      | "Are we building the product right?" (Chúng ta có đang xây dựng sản phẩm đúng cách không?)                 | "Are we building the right product?" (Chúng ta có đang xây dựng đúng sản phẩm không?)                                         |
| **Mục đích**     | Kiểm tra xem phần mềm có tuân thủ các tài liệu thiết kế, yêu cầu, và các tiêu chuẩn coding không.          | Kiểm tra xem phần mềm có đáp ứng được nhu cầu thực tế và mong đợi của khách hàng không.                                       |
| **Hoạt động**    | Thường là các hoạt động tĩnh (static), không cần chạy code. Ví dụ: Code Review, Walkthroughs, Inspections. | Thường là các hoạt động động (dynamic), yêu cầu phải thực thi code. Ví dụ: Unit Testing, Integration Testing, System Testing. |
| **Thời điểm**    | Thường diễn ra trước Validation.                                                                           | Thường diễn ra sau Verification.                                                                                              |
| **Ai thực hiện** | Thường do đội ngũ phát triển, QA nội bộ thực hiện.                                                         | Có thể bao gồm cả khách hàng, người dùng cuối (ví dụ: User Acceptance Testing).                                               |

**Ví dụ dễ hiểu:**

- **Verification:** Kiểm tra bản vẽ thiết kế của một ngôi nhà xem có đúng tiêu chuẩn xây dựng, vật liệu có đúng loại đã ghi không.
- **Validation:** Mời chủ nhà đến xem ngôi nhà đã xây xong và hỏi: "Ngôi nhà này có đúng như những gì ông/bà mong muốn không?"

---

## 4. Đảm bảo Chất lượng Phần mềm (Software Quality Assurance - SQA)

**SQA** là một tập hợp các hoạt động nhằm đảm bảo chất lượng trong _toàn bộ quy trình_ phát triển phần mềm, chứ không chỉ ở giai đoạn kiểm thử.

- **Kiểm thử (Testing)** là một **tập hợp con** của SQA.
- **SQA** là một hoạt động **phòng ngừa (proactive)**, tập trung vào việc cải thiện quy trình để ngăn lỗi xảy ra ngay từ đầu.
- **Testing** là một hoạt động **phát hiện (reactive)**, tập trung vào việc tìm ra các lỗi đã tồn tại trong sản phẩm.

Các hoạt động của SQA bao gồm:

- Định nghĩa các tiêu chuẩn (coding standards, design standards).
- Thực hiện các buổi review (code review, design review).
- Phân tích và quản lý rủi ro.
- Quản lý quy trình và công cụ.
- Và dĩ nhiên, bao gồm cả hoạt động **Kiểm thử Phần mềm (Testing)**.

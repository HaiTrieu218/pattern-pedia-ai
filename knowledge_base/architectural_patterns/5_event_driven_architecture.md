**Các bước diễn ra:**

1.  Người dùng bấm nút "Đặt hàng". Dịch vụ `OrderService` xử lý, lưu đơn hàng vào database và tạo ra một sự kiện là `OrderPlaced` chứa thông tin đơn hàng (ID, mã khách hàng, sản phẩm...). Sau đó, nó gửi sự kiện này đến Kênh sự kiện và **hoàn thành nhiệm vụ của mình**.
2.  Kênh sự kiện nhận được sự kiện và chuyển nó đến tất cả các dịch vụ đã đăng ký lắng nghe `OrderPlaced`:
    - Dịch vụ `InventoryService` nhận sự kiện và tiến hành trừ số lượng sản phẩm trong kho.
    - Dịch vụ `NotificationService` nhận sự kiện và gửi email xác nhận cho khách hàng.
    - Dịch vụ `ShippingService` nhận sự kiện và tạo một yêu cầu vận chuyển mới.

Quan trọng là `OrderService` không hề biết đến sự tồn tại của 3 dịch vụ kia. Nếu sau này có thêm Dịch vụ `AnalyticsService` muốn phân tích đơn hàng, nó chỉ cần đăng ký lắng nghe sự kiện `OrderPlaced` mà không cần thay đổi bất kỳ dòng code nào của `OrderService`.

---

### 5. Ưu điểm (Pros)

- **Tách rời (Decoupling):** Các dịch vụ hoạt động độc lập, giúp hệ thống linh hoạt, dễ phát triển và bảo trì.
- **Khả năng mở rộng (Scalability):** Có thể dễ dàng thêm các Consumer mới hoặc tăng số lượng instance của một Consumer đang bị quá tải mà không ảnh hưởng đến phần còn lại.
- **Tăng khả năng phục hồi (Resilience):** Nếu dịch vụ gửi email bị lỗi, các dịch vụ khác (trừ kho, giao vận) vẫn hoạt động bình thường. Kênh sự kiện có thể lưu lại sự kiện và thử gửi lại sau.
- **Xử lý bất đồng bộ:** Cải thiện trải nghiệm người dùng vì họ nhận được phản hồi ngay lập tức sau khi Producer hoàn thành nhiệm vụ, không cần chờ tất cả các Consumer xử lý xong.

---

### 6. Nhược điểm (Cons)

- **Phức tạp hơn (Increased Complexity):** Việc quản lý, theo dõi và gỡ lỗi một luồng sự kiện đi qua nhiều dịch vụ sẽ khó khăn hơn so với một cuộc gọi trực tiếp.
- **Tính nhất quán cuối cùng (Eventual Consistency):** Vì các dịch vụ cập nhật bất đồng bộ, sẽ có một khoảng trễ nhỏ trước khi toàn bộ hệ thống đạt được trạng thái nhất quán. Ví dụ, người dùng có thể thấy đơn hàng đã đặt thành công nhưng email xác nhận thì vài giây sau mới tới.
- **Xử lý trùng lặp và thứ tự sự kiện:** Cần có cơ chế để xử lý trường hợp một sự kiện được gửi đến nhiều lần hoặc đến không đúng thứ tự.

---

### 7. Ví dụ thực tế

- **Thương mại điện tử:** Xử lý đơn hàng, cập nhật kho, gửi thông báo.
- **Mạng xã hội:** Khi bạn đăng một bài viết, sự kiện "PostCreated" được tạo ra và gửi đến dịch vụ thông báo (để báo cho bạn bè), dịch vụ news feed, dịch vụ phân tích...
- **Hệ thống IoT:** Một cảm biến (Producer) gửi sự kiện "Nhiệt độ thay đổi" đến Kênh sự kiện. Các Consumer khác có thể là hệ thống điều hòa (để điều chỉnh nhiệt độ) hoặc hệ thống cảnh báo (để gửi thông báo nếu nhiệt độ quá cao).

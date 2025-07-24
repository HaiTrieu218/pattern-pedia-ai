import json
from pathlib import Path

def main():
    """
    Hàm chính để thực thi kịch bản xử lý dữ liệu.
    """
    # Xác định đường dẫn gốc của dự án
    # Path(__file__) là file hiện tại (process_data.py)
    # .parent là thư mục chứa nó (src)
    # .parent một lần nữa là thư mục gốc của dự án (PatternPedia)
    project_root = Path(__file__).parent.parent
    
    # Đường dẫn tới các file dữ liệu
    structured_data_path = project_root / "data" / "structured_data.json"
    final_data_path = project_root / "data" / "patterns_final.json"
    
    print(f"Đang đọc dữ liệu từ: {structured_data_path}")
    
    # Mở và đọc file JSON thô
    try:
        with open(structured_data_path, 'r', encoding='utf-8') as f:
            structured_data = json.load(f)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {structured_data_path}. Hãy chắc chắn bạn đã chạy scraper trước.")
        return
    except json.JSONDecodeError:
        print(f"Lỗi: File {structured_data_path} không phải là một file JSON hợp lệ.")
        return

    # --- BƯỚC KIỂM TRA ---
    print(f"Đọc thành công! Tổng cộng có {len(structured_data)} patterns.")
    
    if structured_data:
        print(f"Tên pattern đầu tiên: {structured_data[0].get('name')}")
        print("-" * 20)
        # Ở đây chúng ta sẽ thêm các bước xử lý dữ liệu ở các ngày tiếp theo
        processed_patterns = structured_data # Tạm thời gán bằng dữ liệu thô
        print("Chưa có bước xử lý nào, dữ liệu vẫn là dữ liệu thô.")
        print("-" * 20)
    
    # (Chưa ghi file vội, sẽ làm ở các bước sau)
    # print(f"Sẽ ghi dữ liệu đã xử lý vào: {final_data_path}")
    
    print("Hoàn thành việc thiết lập script.")


if __name__ == "__main__":
    main()
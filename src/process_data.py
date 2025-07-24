import json
from pathlib import Path

def clean_text(text: str) -> str:
    """
    Nhận một chuỗi văn bản và thực hiện các bước làm sạch cơ bản.
    - Thay thế các ký tự xuống dòng, tab bằng khoảng trắng.
    - Loại bỏ các ký tự không thể in được (như \u00a0 - non-breaking space).
    - Loại bỏ các khoảng trắng thừa.
    """
    if not isinstance(text, str):
        return "" # Trả về chuỗi rỗng nếu đầu vào không phải là string

    # Thay thế ký tự xuống dòng và tab bằng khoảng trắng
    text = text.replace('\n', ' ').replace('\t', ' ')
    
    # Loại bỏ các ký tự đặc biệt (ví dụ: \u00a0)
    # Bằng cách chỉ giữ lại các ký tự có thể in được (printable)
    text = ''.join(char for char in text if char.isprintable())
    
    # Loại bỏ các khoảng trắng thừa ở giữa chuỗi
    # Bằng cách tách chuỗi thành các từ rồi nối lại
    cleaned_text = ' '.join(text.split())
    
    return cleaned_text

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
        
        # --- BẮT ĐẦU XỬ LÝ DỮ LIỆU ---
        processed_patterns = []
        for pattern in structured_data:
            # Tạo một bản sao của pattern để xử lý, tránh thay đổi dữ liệu gốc
            processed_pattern = pattern.copy()

            # Áp dụng hàm làm sạch cho các trường văn bản
            if 'problem' in processed_pattern:
                processed_pattern['problem'] = clean_text(processed_pattern['problem'])

            if 'solution' in processed_pattern:
                processed_pattern['solution'] = clean_text(processed_pattern['solution'])

            # (Chúng ta sẽ xử lý 'code_examples' ở bước sau)

            processed_patterns.append(processed_pattern)

        print("Đã hoàn thành bước làm sạch văn bản cơ bản.")
        # --- KẾT THÚC XỬ LÝ DỮ LIỆU ---

        # --- BƯỚC KIỂM TRA SAU KHI LÀM SẠCH ---
        print("Kiểm tra kết quả sau khi làm sạch:")
        print(f"Problem của pattern đầu tiên:\n>>> {processed_patterns[0].get('problem')[:200]}...") # In ra 200 ký tự đầu
        print("-" * 20)
    
    # (Chưa ghi file vội, sẽ làm ở các bước sau)
    # print(f"Sẽ ghi dữ liệu đã xử lý vào: {final_data_path}")
    
    print("Hoàn thành việc thiết lập script.")


if __name__ == "__main__":
    main()
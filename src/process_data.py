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

            # --- Tái cấu trúc & Tạo các trường mới ---
            pattern_name = processed_pattern.get('name', '')

            # Ví dụ: "Factory Method" -> "factory-method"
            pattern_id = pattern_name.lower().replace(' ', '-')
            processed_pattern['id'] = pattern_id

            # Kết hợp các thông tin quan trọng nhất để AI "học"
            problem_text = processed_pattern.get('problem', '')
            solution_text = processed_pattern.get('solution', '')

            # Dùng f-string để tạo một đoạn văn bản giàu ngữ nghĩa
            text_for_embedding = (
                f"Pattern Name: {pattern_name}. "
                f"Problem it solves: {problem_text} "
                f"Solution: {solution_text}"
            )
            processed_pattern['text_for_embedding'] = text_for_embedding

            processed_patterns.append(processed_pattern)

        print("Đã hoàn thành bước làm sạch văn bản cơ bản.")
        # --- KẾT THÚC XỬ LÝ DỮ LIỆU ---

        # --- BƯỚC KIỂM TRA SAU KHI TÁI CẤU TRÚC ---
        print("Kiểm tra kết quả sau khi tái cấu trúc:")
        first_processed_pattern = processed_patterns[0]
        print(f"ID của pattern đầu tiên: {first_processed_pattern.get('id')}")
        print(f"Text for Embedding của pattern đầu tiên:\n>>> {first_processed_pattern.get('text_for_embedding')[:300]}...")
        print("-" * 20)
    
    # --- BƯỚC CUỐI: GHI DỮ LIỆU ĐÃ XỬ LÝ RA FILE ---
    if processed_patterns:
        print(f"Chuẩn bị ghi {len(processed_patterns)} patterns đã xử lý vào file...")
        try:
            with open(final_data_path, 'w', encoding='utf-8') as f:
                json.dump(processed_patterns, f, ensure_ascii=False, indent=2)
            print(f"Ghi dữ liệu thành công vào: {final_data_path}")
        except IOError as e:
            print(f"Lỗi: Không thể ghi file. Chi tiết: {e}")
    else:
        print("Không có dữ liệu để ghi.")
        
    print("Hoàn thành việc thiết lập script.")


if __name__ == "__main__":
    main()
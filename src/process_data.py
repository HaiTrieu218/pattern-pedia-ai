# file: src/process_data.py

import json
from pathlib import Path

def clean_text(text: str) -> str:
    """Làm sạch một chuỗi văn bản."""
    if not isinstance(text, str):
        return ""
    text = text.replace('\n', ' ').replace('\t', ' ')
    text = ''.join(char for char in text if char.isprintable())
    cleaned_text = ' '.join(text.split())
    return cleaned_text

def clean_list_of_strings(string_list: list) -> list:
    """Làm sạch từng chuỗi trong một danh sách."""
    if not isinstance(string_list, list):
        return []
    # Trả về danh sách các chuỗi đã được làm sạch, loại bỏ các chuỗi rỗng
    return [clean_text(s) for s in string_list if clean_text(s)]

def main():
    """Hàm chính để thực thi kịch bản xử lý dữ liệu."""
    project_root = Path(__file__).parent.parent
    
    # Đọc từ file dữ liệu thô đầy đủ nhất
    raw_data_path = project_root / "data" / "structured_data.json"
    final_data_path = project_root / "data" / "patterns_final.json"
    
    print(f"Đang đọc dữ liệu từ: {raw_data_path}")
    
    try:
        with open(raw_data_path, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {raw_data_path}. Hãy chắc chắn bạn đã chạy scraper trước.")
        return
    except json.JSONDecodeError:
        print(f"Lỗi: File {raw_data_path} không phải là một file JSON hợp lệ.")
        return

    print(f"Đọc thành công! Tổng cộng có {len(raw_data)} patterns.")
    
    if not raw_data:
        print("Không có dữ liệu để xử lý.")
        return
        
    processed_patterns = []
    for pattern in raw_data:
        processed_pattern = {}

        # --- LÀM SẠCH VÀ CHUẨN HÓA CÁC TRƯỜNG DỮ LIỆU ---
        
        # Các trường dạng chuỗi đơn
        processed_pattern['name'] = clean_text(pattern.get('name', ''))
        processed_pattern['url'] = pattern.get('url', '')
        processed_pattern['category'] = clean_text(pattern.get('category', ''))
        processed_pattern['intent'] = clean_text(pattern.get('intent', ''))
        processed_pattern['problem'] = clean_text(pattern.get('problem', ''))
        processed_pattern['solution'] = clean_text(pattern.get('solution', ''))
        processed_pattern['uml_image_url'] = pattern.get('uml_image_url', '')
        # **BỔ SUNG CÁC TRƯỜNG MỚI (DẠNG CHUỖI)**
        processed_pattern['structure_text'] = clean_text(pattern.get('structure_text', ''))
        processed_pattern['pseudocode'] = clean_text(pattern.get('pseudocode', ''))
        processed_pattern['applicability'] = clean_text(pattern.get('applicability', ''))

        # Các trường dạng danh sách chuỗi
        processed_pattern['pros'] = clean_list_of_strings(pattern.get('pros', []))
        processed_pattern['cons'] = clean_list_of_strings(pattern.get('cons', []))
        processed_pattern['relations'] = clean_list_of_strings(pattern.get('relations', []))
        # **BỔ SUNG CÁC TRƯỜNG MỚI (DẠNG LIST)**
        processed_pattern['how_to_implement'] = clean_list_of_strings(pattern.get('how_to_implement', []))
        processed_pattern['extra_content'] = clean_list_of_strings(pattern.get('extra_content', []))
        
        # --- TẠO CÁC TRƯỜDỮ LIỆU MỚI ---
        pattern_name = processed_pattern.get('name', '')
        pattern_id = pattern_name.lower().replace(' ', '-').replace('/', '-')
        processed_pattern['id'] = pattern_id

        
        intent_text = processed_pattern.get('intent', '')
        applicability_text = processed_pattern.get('applicability', '')
        problem_text = processed_pattern.get('problem', '')

        # Lấy ưu điểm đầu tiên, thường là ưu điểm quan trọng nhất
        first_pro = processed_pattern.get('pros', [''])[0] if processed_pattern.get('pros') else ''

        text_for_embedding = (
            f"The main intent of this pattern is: {intent_text}. "
            f"In summary, the goal is: {intent_text}. " # Lặp lại Intent
            f"You should use this pattern when: {applicability_text}. "
            f"It is designed to solve the following problem: {problem_text}. "
            f"A key benefit is: {first_pro}"
        )

        # Làm sạch lần cuối để đảm bảo
        processed_pattern['text_for_embedding'] = clean_text(text_for_embedding)

        processed_patterns.append(processed_pattern)

    print("Hoàn thành xử lý và làm sạch tất cả các trường dữ liệu.")

    # --- KIỂM TRA ---
    print("\n" + "="*20)
    print("KIỂM TRA KẾT QUẢ CUỐI CÙNG")
    print("="*20)
    if processed_patterns:
        first_pattern = processed_patterns[0]
        print(f"ID: {first_pattern.get('id')}")
        print(f"Name: {first_pattern.get('name')}")
        print(f"Structure text (trích đoạn): {first_pattern.get('structure_text', '')[:100]}...")
        print(f"Pros (mục đầu tiên): {first_pattern.get('pros', ['N/A'])[0]}")

    # --- GHI FILE ---
    print("\n" + "="*20)
    print(f"Chuẩn bị ghi {len(processed_patterns)} patterns vào file: {final_data_path}")
    try:
        with open(final_data_path, 'w', encoding='utf-8') as f:
            json.dump(processed_patterns, f, ensure_ascii=False, indent=2)
        print(f"GHI DỮ LIỆU THÀNH CÔNG!")
    except IOError as e:
        print(f"LỖI: Không thể ghi file. Chi tiết: {e}")
        
    print("Hoàn thành script.")

if __name__ == "__main__":
    main()
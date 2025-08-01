import json
from pathlib import Path
from sentence_transformers import SentenceTransformer
import numpy as np # Thường dùng để lưu file numpy

def main():
    """
    Hàm chính để xây dựng cơ sở dữ liệu vector.
    ... (docstring giữ nguyên)
    """
    print("--- Bắt đầu Script Xây dựng Cơ sở dữ liệu Vector ---")
    
    # --- CÔNG ĐOẠN 1: ĐỊNH NGHĨA ĐƯỜNG DẪN ---
    project_root = Path(__file__).parent.parent
    final_data_path = project_root / "data" / "patterns_final.json"
    
    # --- CÔNG ĐOẠN 2: ĐỌC DỮ LIỆU ĐÃ XỬ LÝ ---
    print(f"1. Đang đọc dữ liệu từ: {final_data_path}")
    try:
        with open(final_data_path, 'r', encoding='utf-8') as f:
            patterns_data = json.load(f)
        print(f"   => Đọc thành công {len(patterns_data)} patterns.")
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {final_data_path}. Hãy chạy 'process_data.py' trước.")
        return

    # --- CÔNG ĐOẠN 3: LOAD MÔ HÌNH AI ---
    model_name = 'all-MiniLM-L6-v2'
    print(f"2. Đang tải mô hình Sentence Transformer: '{model_name}'...")
    model = SentenceTransformer(model_name)
    print("   => Tải mô hình thành công.")

    # --- CÔNG ĐOẠN 4: CHUẨN BỊ DỮ LIỆU ĐỂ MÃ HÓA ---
    print("3. Đang chuẩn bị dữ liệu để mã hóa...")
    texts_to_encode = [pattern['text_for_embedding'] for pattern in patterns_data]
    print(f"   => Đã có {len(texts_to_encode)} đoạn văn bản cần mã hóa.")
    
    # --- CÔNG ĐOẠN 5: MÃ HÓA DỮ LIỆU ---
    print("4. Bắt đầu quá trình mã hóa (có thể mất một chút thời gian)...")
    embeddings = model.encode(texts_to_encode, show_progress_bar=True)
    print("   => Mã hóa hoàn tất!")
    print(f"   => Kích thước của ma trận embedding: {embeddings.shape}")
    
    # Ở các bước sau, chúng ta sẽ thêm code để lưu embeddings vào ChromaDB ở đây.
    # Ví dụ: save_to_chromadb(patterns_data, embeddings)

    print("--- Hoàn thành Script ---")


if __name__ == "__main__":
    # Dòng này đảm bảo hàm main() chỉ chạy khi file này được thực thi trực tiếp
    main()
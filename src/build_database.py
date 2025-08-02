import json
from pathlib import Path
from sentence_transformers import SentenceTransformer
import time
import chromadb

# --- CẤU HÌNH ---
# THÊM DÒNG NÀY VÀO:
COLLECTION_NAME = "design_patterns" 

def main():
    """
    Hàm chính để xây dựng cơ sở dữ liệu vector.
    """
    print("--- Bắt đầu Script Xây dựng Cơ sở dữ liệu Vector ---")
    
    # --- Đọc Dữ liệu ---
    project_root = Path(__file__).parent.parent
    final_data_path = project_root / "data" / "patterns_final.json"
    
    print(f"1. Đang đọc dữ liệu từ: {final_data_path}")
    try:
        with open(final_data_path, 'r', encoding='utf-8') as f:
            patterns_data = json.load(f)
        print(f"   => Đọc thành công {len(patterns_data)} patterns.")
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {final_data_path}. Hãy chạy 'process_data.py' trước.")
        return

    # --- Chuẩn bị dữ liệu cho ChromaDB (THÊM PHẦN NÀY VÀO) ---
    print("2. Đang chuẩn bị các danh sách (ids, documents, metadatas)...")
    ids = [p['id'] for p in patterns_data]
    documents = [p['text_for_embedding'] for p in patterns_data]
    metadatas = [{'name': p['name'], 'url': p['url']} for p in patterns_data]
    print("   => Đã chuẩn bị xong.")

    # --- Load Mô hình AI ---
    model_name = 'all-mpnet-base-v2'
    print(f"3. Đang tải mô hình Sentence Transformer: '{model_name}'...")
    model = SentenceTransformer(model_name)
    print("   => Tải mô hình thành công.")

    # --- Mã hóa Dữ liệu ---
    print("4. Bắt đầu quá trình mã hóa (có thể mất một chút thời gian)...")
    # Thay texts_to_encode thành documents
    embeddings = model.encode(documents, show_progress_bar=True)
    print("   => Mã hóa hoàn tất!")
    print(f"   => Kích thước của ma trận embedding: {embeddings.shape}")
    
    # --- Lưu trữ vào ChromaDB ---
    print("5. Đang thiết lập và lưu trữ vào ChromaDB...")
    db_path = project_root / "db"
    client = chromadb.PersistentClient(path=str(db_path))
    
    if COLLECTION_NAME in [c.name for c in client.list_collections()]:
        print(f"   Collection '{COLLECTION_NAME}' đã tồn tại. Đang xóa để xây dựng lại...")
        client.delete_collection(name=COLLECTION_NAME)

    collection = client.create_collection(
    name=COLLECTION_NAME,
    metadata={"hnsw:space": "cosine"}  # Báo cho ChromaDB dùng thước đo Cosine
)
    
    # Sửa lại `embeddings.tolist()` nếu embeddings là numpy array
    collection.add(
        embeddings=embeddings.tolist(),
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )
    print("   => Đã thêm thành công toàn bộ dữ liệu vào ChromaDB.")
    
    count = collection.count()
    print(f"   Kiểm tra: Collection '{COLLECTION_NAME}' hiện có {count} mục.")
    
    print("--- Kịch bản xây dựng cơ sở dữ liệu đã hoàn thành! ---")


if __name__ == "__main__":
    main()
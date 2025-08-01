import chromadb
from sentence_transformers import SentenceTransformer
from pathlib import Path
import pprint

# --- CÁC HẰNG SỐ CẤU HÌNH ---
DB_PATH = Path(__file__).parent.parent / "db"
COLLECTION_NAME = "design_patterns"
MODEL_NAME = 'all-mpnet-base-v2'

def search(query_text: str, n_results: int = 3):
    """
    Thực hiện tìm kiếm ngữ nghĩa trên collection design_patterns.

    Args:
        query_text: Chuỗi văn bản truy vấn của người dùng.
        n_results: Số lượng kết quả trả về.

    Returns:
        Dictionary chứa kết quả truy vấn từ ChromaDB.
    """
    # 1. Tải mô hình embedding (giống hệt model khi xây dựng DB)
    print(f"Đang tải model: {MODEL_NAME}...")
    model = SentenceTransformer(MODEL_NAME)
    
    # 2. Kết nối tới ChromaDB
    print(f"Đang kết nối tới DB tại: {DB_PATH}")
    client = chromadb.PersistentClient(path=str(DB_PATH))
    collection = client.get_collection(name=COLLECTION_NAME)
    
    # 3. Mã hóa câu hỏi của người dùng
    print(f"Đang mã hóa câu hỏi: '{query_text}'")
    query_embedding = model.encode(query_text).tolist()
    
    # 4. Thực hiện truy vấn
    print(f"Đang truy vấn {n_results} kết quả gần nhất...")
    results = collection.query(
        query_embeddings=[query_embedding], # Phải là một list các embedding
        n_results=n_results,
        include=['documents', 'metadatas', 'distances'] # Yêu cầu trả về các trường này
    )
    
    return results

if __name__ == "__main__":
    # --- KỊCH BẢN KIỂM TRA ---
    
    # Câu hỏi ví dụ
    user_query = "how to simplify a complex interface of a system?"
    
    print("-" * 50)
    print(f"Bắt đầu tìm kiếm cho câu hỏi: '{user_query}'")
    print("-" * 50)
    
    # Gọi hàm tìm kiếm
    search_results = search(user_query, n_results=3)
    
    print("\n" + "="*50)
    print("KẾT QUẢ TÌM KIẾM:")
    print("="*50)
    
    # In kết quả ra màn hình
    pprint.pprint(search_results)
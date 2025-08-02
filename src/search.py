import json
import chromadb
from sentence_transformers import SentenceTransformer
from pathlib import Path
import pprint


# --- CÁC HẰNG SỐ CẤU HÌNH ---
# (Chuyển chúng vào trong class hoặc để ở ngoài đều được)
DB_PATH = Path(__file__).parent.parent / "db"
DATA_PATH = Path(__file__).parent.parent / "data" / "patterns_final.json"
COLLECTION_NAME = "design_patterns"
MODEL_NAME = 'all-mpnet-base-v2'

class SearchEngine:
    def __init__(self):
        """
        Khởi tạo các tài nguyên nặng MỘT LẦN DUY NHẤT.
        """
        print("Đang khởi tạo SearchEngine...")
        # 1. Tải mô hình
        print(f"Đang tải model: {MODEL_NAME}...")
        self.model = SentenceTransformer(MODEL_NAME)
        
        # 2. Kết nối tới ChromaDB
        print(f"Đang kết nối tới DB tại: {DB_PATH}")
        self.client = chromadb.PersistentClient(path=str(DB_PATH))
        self.collection = self.client.get_collection(name=COLLECTION_NAME)

        # 3. Tải dữ liệu JSON để tra cứu thông tin chi tiết
        print(f"Đang tải dữ liệu từ: {DATA_PATH}")
        with open(DATA_PATH, 'r', encoding='utf-8') as f:
            self.patterns_data = {p['id']: p for p in json.load(f)} # Dùng dict để tra cứu nhanh hơn
        
        print("SearchEngine đã sẵn sàng!")

    def search(self, query_text: str, n_results: int = 3):
        """
        Thực hiện tìm kiếm, TÁI SỬ DỤNG các tài nguyên đã được tải.
        """
        # 1. Mã hóa câu hỏi (nhanh vì model đã được tải)
        query_embedding = self.model.encode(query_text).tolist()
        
        # 2. Thực hiện truy vấn (nhanh vì đã có kết nối)
        results_from_db = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )
        
        # 3. Kết hợp kết quả từ DB với dữ liệu chi tiết từ JSON
        final_results = []
        if results_from_db['ids']:
            for item_id in results_from_db['ids'][0]:
                if item_id in self.patterns_data:
                    final_results.append(self.patterns_data[item_id])
        
        return final_results


if __name__ == "__main__":
    # Khởi tạo engine (chỉ một lần)
    engine = SearchEngine()
    
    # Câu hỏi ví dụ
    user_query = "How to let an object's behavior be selected at runtime?"
    
    # Gọi hàm tìm kiếm nhiều lần mà không cần tải lại model
    print("\n--- Bắt đầu tìm kiếm ---")
    search_results = engine.search(user_query, n_results=3)

    print("\n" + "="*50)
    print("KẾT QUẢ TÌM KIẾM:")
    pprint.pprint(search_results)
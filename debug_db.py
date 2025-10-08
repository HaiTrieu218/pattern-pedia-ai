# file: debug_db.py

import chromadb
from pathlib import Path

# --- SỬ DỤNG LẠI CÁC CẤU HÌNH TỪ SEARCHENGINE ---
# Đảm bảo các hằng số này GIỐNG HỆT với file search.py của bạn
DB_PATH = Path(__file__).parent / "db"
COLLECTION_NAME = "design_patterns"

print("--- Bắt đầu Script Kiểm tra Cơ sở dữ liệu ChromaDB ---")
print(f"Đang cố gắng kết nối tới DB tại: {DB_PATH}")

try:
    # Kết nối tới client
    client = chromadb.PersistentClient(path=str(DB_PATH))

    # Lấy collection
    print(f"Đang cố gắng lấy collection có tên: '{COLLECTION_NAME}'")
    collection = client.get_collection(name=COLLECTION_NAME)
    
    # --- ĐÂY LÀ PHẦN QUAN TRỌNG NHẤT ---
    count = collection.count()
    print("\n" + "="*50)
    print(f"✅ TRẠNG THÁI COLLECTION '{COLLECTION_NAME}':")
    print(f"   -> Số lượng mục (documents) trong collection: {count}")
    print("="*50 + "\n")

    # Nếu có dữ liệu, hãy xem thử vài mục đầu tiên
    if count > 0:
        print("👀 Xem trước 5 mục đầu tiên trong collection:")
        peek_results = collection.peek(limit=5)
        print(peek_results)
    else:
        print("❌ LỖI: Collection rỗng! Đây là nguyên nhân gây ra lỗi trong ứng dụng của bạn.")
        print("   -> BẠN CẦN CHẠY SCRIPT NẠP DỮ LIỆU (ví dụ: build_knowledge_base.py) ĐỂ THÊM DỮ LIỆU VÀO ĐÂY.")

except ValueError as e:
    # Bắt lỗi nếu collection không tồn tại
    print("\n" + "="*50)
    print(f"❌ LỖI: Không tìm thấy collection có tên '{COLLECTION_NAME}'.")
    print(f"   Lỗi chi tiết: {e}")
    print("   -> Có thể bạn chưa bao giờ tạo collection này. Hãy chạy script nạp dữ liệu.")
    print("="*50)
except Exception as e:
    print(f"Một lỗi không xác định đã xảy ra: {e}")
import os
import re
from pathlib import Path
from typing import List

# --- CÁC IMPORT MỚI CHO LANGCHAIN ---
from langchain.docstore.document import Document
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

# --- CÁC HÀM PARSE CỦA BẠN (GIỮ NGUYÊN VÌ NÓ RẤT TỐT) ---
def parse_markdown_to_dict(file_path: Path, root_dir: Path) -> dict:
    """
    Phân tích một file Markdown, trích xuất thông tin và trả về một dictionary.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    title_match = re.search(r'^#\s(.+)', content)
    name = title_match.group(1).strip() if title_match else file_path.stem

    sections = re.split(r'\n##\s', content)
    
    # _CHANGED_: Sử dụng đường dẫn tương đối thay vì tuyệt đối
    relative_path_str = str(file_path.relative_to(root_dir))
    # Chuyển đổi dấu \ thành / để tương thích đa nền tảng
    source_file = relative_path_str.replace('\\', '/')

    knowledge_item = {'name': name, 'source': source_file} # _CHANGED_: Đổi 'source_file' thành 'source' cho chuẩn LangChain

    # Lấy category từ thư mục cha
    if len(file_path.relative_to(root_dir).parts) > 1:
        knowledge_item['category'] = file_path.relative_to(root_dir).parts[-2]
    else:
        knowledge_item['category'] = 'general'

    for section in sections[1:]:
        parts = section.split('\n', 1)
        if len(parts) == 2:
            section_title = parts[0].strip().lower().replace(' ', '_')
            section_content = parts[1].strip()
            knowledge_item[section_title] = section_content
            
    return knowledge_item

def create_documents_from_knowledge_base(root_dir: Path) -> List[Document]:
    """
    _NEW_: Hàm mới để quét, phân tích và tạo ra danh sách các đối tượng Document của LangChain.
    """
    all_documents = []
    
    for md_file in root_dir.rglob('*.md'):
        print(f"Đang xử lý file: {md_file.name}")
        try:
            item_data = parse_markdown_to_dict(md_file, root_dir)
            
            # --- TẠO CẤU TRÚC CHUẨN CỦA LANGCHAIN ---

            # 1. Tạo page_content: Ghép nối các phần văn bản quan trọng nhất
            # Đây chính là nội dung sẽ được embedding
            name_text = item_data.get('name', '')
            definition_text = item_data.get('định_nghĩa', '')
            problem_text = item_data.get('vấn_đề_giải_quyết', '')
            # Bạn có thể thêm các phần khác vào đây nếu muốn
            
            page_content = (
                f"Chủ đề: {name_text}.\n\n"
                f"Định nghĩa: {definition_text}\n\n"
                f"Vấn đề giải quyết: {problem_text}"
            )
            
            # 2. Tạo metadata: Các thông tin phụ, không cần embedding nhưng rất quan trọng
            # Lấy tất cả các key còn lại ngoại trừ các key đã dùng cho page_content
            metadata = {
                "source": item_data['source'],
                "category": item_data['category'],
                "name": item_data['name']
            }

            # 3. Tạo đối tượng Document
            doc = Document(page_content=page_content, metadata=metadata)
            all_documents.append(doc)
            
        except Exception as e:
            print(f"Lỗi khi xử lý file {md_file.name}: {e}")
            
    print(f"\nĐã tạo thành công {len(all_documents)} tài liệu từ knowledge base.")
    return all_documents


# --- HÀM CHÍNH ĐỂ THỰC THI ---
if __name__ == "__main__":
    # 1. Xác định các đường dẫn
    PROJECT_ROOT = Path(__file__).parent.parent.parent # Điều chỉnh cho đúng với cấu trúc src/components
    KNOWLEDGE_BASE_DIR = PROJECT_ROOT / "knowledge_base"
    VECTOR_DB_PATH = PROJECT_ROOT / "db"
    
    # 2. Tạo danh sách các Document từ file .md
    documents = create_documents_from_knowledge_base(KNOWLEDGE_BASE_DIR)
    
    # 3. Cắt các Document thành các chunks nhỏ hơn (rất quan trọng cho RAG)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs_chunks = text_splitter.split_documents(documents)
    print(f"Đã chia {len(documents)} tài liệu thành {len(docs_chunks)} chunks.")

    # 4. Khởi tạo model embedding
    # (Bạn có thể cần cài đặt: pip install sentence-transformers InstructorEmbedding)
    print("Đang tải model embedding (có thể mất vài phút)...")
    embedding_model = HuggingFaceEmbeddings(
    model_name="bkai-foundation-models/vietnamese-bi-encoder",
    model_kwargs={'device': 'cpu'})
    print("Tải model thành công.")
    
    # 5. Tạo và lưu Vector Database
    print(f"Đang tạo Vector Database tại: {VECTOR_DB_PATH}")
    # Xóa DB cũ nếu có để tạo mới (chỉ nên làm trong quá trình phát triển)
    if VECTOR_DB_PATH.exists():
        import shutil
        shutil.rmtree(VECTOR_DB_PATH)

    vectordb = Chroma.from_documents(
        documents=docs_chunks,
        embedding=embedding_model,
        persist_directory=str(VECTOR_DB_PATH)
    )
    print("Tạo Vector Database thành công!")
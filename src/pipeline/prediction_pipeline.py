# File: src/pipeline/prediction_pipeline.py
# PHIÊN BẢN HOÀN CHỈNH VÀ ĐÃ SỬA LỖI

from pathlib import Path
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationalRetrievalChain 
from langchain.memory import ConversationBufferMemory
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.llms import CTransformers
from huggingface_hub import hf_hub_download
import streamlit as st

# --- CẤU HÌNH ---
PROJECT_ROOT = Path(__file__).parent.parent.parent
DB_PATH = str(PROJECT_ROOT / "db")

# Prompt chính để trả lời câu hỏi dựa trên ngữ cảnh
prompt_template = """
Sử dụng bối cảnh sau đây để trả lời câu hỏi của người dùng bằng tiếng Việt một cách chi tiết và chuyên nghiệp.

QUAN TRỌNG:
1. Khi câu trả lời có mã nguồn, hãy bọc nó trong khối Markdown với tên ngôn ngữ (ví dụ: ```python ... ```).
2. Khi câu hỏi yêu cầu vẽ sơ đồ, giải thích luồng hoạt động, hoặc trình bày các bước, HÃY tạo ra một sơ đồ bằng cú pháp Mermaid.js và bọc nó trong khối ```mermaid ... ```.

Ví dụ về cú pháp Mermaid cho sơ đồ luồng:
```mermaid
graph TD
    A[Client] --> B{{Creator}};
    B --> C[Product];
Ngữ cảnh: {context}
Câu hỏi: {question}
Câu trả lời:
"""

@st.cache_resource
def load_llm():
    """
    Tải model LLM từ Hugging Face Hub và lưu vào cache.
    """
    model_path = hf_hub_download(
        repo_id="Trieu1/MyAwesomeMistral-GGUF", 
        filename="mistral-7b-instruct-v0.2.Q4_K_M.gguf"
    )
    
    llm = CTransformers(
        model=model_path,
        model_type='llama',
        config={'max_new_tokens': 1024, 'temperature': 0.1, 'context_length': 4096}
    )
    return llm

def create_conversational_chain():
    # ... (phần embedding và retriever giữ nguyên)
    
    # 4. Tải LLM
    llm = load_llm() # <<< SỬA DÒNG NÀY, THAY VÌ TẠO CTransformers TRỰC TIẾP
    
    # 5. TẠO BỘ NHỚ
    memory = ConversationBufferMemory(
        memory_key="chat_history", 
        return_messages=True, 
        output_key='answer' 
    )

    # 6. TẠO CHAIN
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=True,
        combine_docs_chain_kwargs={"prompt": PromptTemplate(template=prompt_template, input_variables=["context", "question"])}
    )
    
    return qa_chain

def get_answer(query, chain):
    result = chain.invoke({"question": query}) 
    return result

# --- Phần test để debug ---
if __name__ == '__main__':
    print("Để test pipeline này, hãy chạy ứng dụng Streamlit bằng lệnh:")
    print("streamlit run app/app.py")
    print("Tạo chain thành công!")

    print("\nBắt đầu cuộc hội thoại:")
    
    # Test câu hỏi 1
    q1 = "SOLID là gì?"
    print(f"\nUser: {q1}")
    r1 = get_answer(q1, chain)
    print(f"AI: {r1['answer']}")

    # Test câu hỏi 2 (nối tiếp)
    q2 = "Giải thích nguyên lý thứ hai."
    print(f"\nUser: {q2}")
    r2 = get_answer(q2, chain)
    print(f"AI: {r2['answer']}")
# File: app/app.py

import streamlit as st
import os
import re # <<< THÊM VÀO
from pathlib import Path
from streamlit_mermaid import st_mermaid
import uuid

# --- IMPORT CÁC THÀNH PHẦN TỪ PIPELINE MỚI ---
import sys
sys.path.append(str(Path(__file__).parent.parent))
from src.pipeline.prediction_pipeline import create_conversational_chain, get_answer

# --- CẤU HÌNH GIAO DIỆN STREAMLIT ---
st.set_page_config(
    page_title="Pattern-pedia AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Pattern-pedia AI: Trợ lý Công nghệ Phần mềm")
st.markdown("Chào mừng bạn! Hãy đặt một câu hỏi về các chủ đề như Design Patterns, SOLID, Agile, Software Architectures...")

# --- CACHING: TẢI MODEL MỘT LẦN DUY NHẤT ---
@st.cache_resource
def load_chain():
    try:
        chain = create_conversational_chain()
        return chain
    except Exception as e:
        st.error(f"Lỗi khi khởi tạo AI pipeline: {e}")
        st.error("Vui lòng kiểm tra lại đường dẫn tới model LLM và chắc chắn rằng bạn đã tải model về.")
        return None

with st.spinner("Đang khởi động AI, vui lòng chờ một lát..."):
    chain = load_chain()

# --- KHỞI TẠO SESSION STATE ---
# Đổi tên 'messages' thành 'chat_history' để nhất quán hơn
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- HÀM HELPER ĐỂ HIỂN THỊ CÂU TRẢ LỜI CỦA AI ---
# Tách logic hiển thị ra một hàm riêng để code gọn gàng hơn
def display_assistant_message(message_content, sources_text, message_index):
    
    # <<< LOGIC MỚI BẮT ĐẦU TỪ ĐÂY >>>
    # Ưu tiên tìm và vẽ sơ đồ Mermaid trước
    mermaid_pattern = re.compile(r"```mermaid(.*?)```", re.DOTALL)
    mermaid_match = mermaid_pattern.search(message_content)

    if mermaid_match:
        # Nếu tìm thấy sơ đồ, tách nội dung ra và vẽ
        before_mermaid = message_content[:mermaid_match.start()]
        mermaid_code = mermaid_match.group(1).strip()
        after_mermaid = message_content[mermaid_match.end():]

        if before_mermaid.strip():
            st.markdown(before_mermaid)
        
        # Dùng st_mermaid để VẼ sơ đồ
        st_mermaid(mermaid_code, key=f"mermaid_{message_index}_{uuid.uuid4()}")

        with st.expander("Xem mã Mermaid"):
            st.code(mermaid_code, language='mermaid')
        
        if after_mermaid.strip():
            st.markdown(after_mermaid)
    else:
        # <<< LOGIC CŨ CỦA BẠN NẰM TRONG ELSE >>>
        # Nếu không có Mermaid, xử lý Python và văn bản như bình thường
        parts = re.split(r"(```python[\s\S]*?```)", message_content)
        for part in parts:
            if part.strip() == "":
                continue
            if part.startswith("```python"):
                code = part.replace("```python", "").replace("```", "").strip()
                st.code(code, language='python')
            else:
                st.markdown(part.strip())

    # Hiển thị nguồn tham khảo
    if sources_text:
        st.info(sources_text)
        
    # --- CƠ CHẾ FEEDBACK ---
    feedback_key_prefix = f"feedback_{message_index}"
    
    if st.session_state.get(f"{feedback_key_prefix}_submitted") is None:
        col1, col2, _ = st.columns([1, 1, 10])
        with col1:
            if st.button("👍", key=f"{feedback_key_prefix}_like"):
                st.session_state[f"{feedback_key_prefix}_submitted"] = "like"
                # TODO: Lưu feedback này vào file log hoặc CSDL
                st.rerun()
        with col2:
            if st.button("👎", key=f"{feedback_key_prefix}_dislike"):
                st.session_state[f"{feedback_key_prefix}_submitted"] = "dislike"
                # TODO: Lưu feedback này vào file log hoặc CSDL
                st.rerun()
    else:
        feedback = st.session_state[f"{feedback_key_prefix}_submitted"]
        if feedback == 'like':
            st.success("Cảm ơn bạn đã thích câu trả lời này! 👍")
        elif feedback == 'dislike':
            st.warning("Cảm ơn bạn đã phản hồi. Chúng tôi sẽ cải thiện. 👎")


# --- HIỂN THỊ LỊCH SỬ HỘI THOẠI ---
# Dùng enumerate để có index cho key của nút feedback
for i, message in enumerate(st.session_state.chat_history):
    with st.chat_message(message["role"]):
        if message["role"] == "user":
            st.markdown(message["content"])
        else: # role == "assistant"
            display_assistant_message(
                message.get("content", ""),
                message.get("sources", ""),
                i
            )

# --- XỬ LÝ INPUT CỦA NGƯỜI DÙNG ---
if prompt := st.chat_input("Câu hỏi của bạn là gì?"):
    if not chain:
        st.warning("Hệ thống AI chưa sẵn sàng. Vui lòng kiểm tra lại lỗi ở trên.")
    else:
        # Thêm tin nhắn của người dùng vào lịch sử và hiển thị
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Lấy câu trả lời từ AI và hiển thị
        with st.chat_message("assistant"):
            with st.spinner("AI đang suy nghĩ..."):
                response = get_answer(prompt, chain)
                
                answer = response.get('answer', "Xin lỗi, đã có lỗi xảy ra.")
                source_documents = response.get('source_documents', [])

                sources_text = ""
                if source_documents:
                    unique_sources = {os.path.basename(doc.metadata.get('source', 'N/A')) for doc in source_documents}
                    if unique_sources:
                        sources_text = "Nguồn tham khảo: " + ", ".join(sorted(list(unique_sources)))
                
                # Hiển thị câu trả lời mới bằng hàm helper
                display_assistant_message(answer, sources_text, len(st.session_state.chat_history))
        
        # Thêm câu trả lời của AI vào lịch sử để lưu lại
        st.session_state.chat_history.append({
            "role": "assistant", 
            "content": answer, # Chỉ lưu nội dung câu trả lời
            "sources": sources_text # Lưu nguồn riêng
        })
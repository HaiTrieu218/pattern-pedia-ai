import streamlit as st
from pathlib import Path
# Dòng import này có thể gây lỗi nếu chạy từ thư mục gốc,
# hãy đảm bảo cấu trúc thư mục và cách bạn chạy file là đúng.
# Một cách an toàn hơn là thêm sys.path
import sys
sys.path.append(str(Path(__file__).parent))
from src.search import SearchEngine

# Sử dụng cache của Streamlit để chỉ tải model và engine một lần duy nhất
@st.cache_resource
def load_search_engine():
    project_root = Path(__file__).parent
    data_file_path = project_root / "data" / "patterns_final.json"
    engine = SearchEngine() 
    return engine

# Thiết lập cấu hình trang
st.set_page_config(page_title="PatternPedia", page_icon="🧠", layout="wide")

# Nội dung chính của trang
st.title("PatternPedia: Trợ lý AI Khám phá Design Patterns 🚀")
st.header("Một công cụ giúp bạn tìm kiếm và học hỏi các mẫu thiết kế phần mềm một cách trực quan.")
st.info("Hãy thử mô tả một vấn đề thiết kế mà bạn đang gặp phải, AI sẽ gợi ý các giải pháp phù hợp!")

st.markdown("---")

# --- Khu vực Nhập liệu ---
st.subheader("📝 Mô tả vấn đề của bạn")

with st.form(key='search_form'):
    user_query = st.text_area(
        label="Mô tả vấn đề thiết kế phần mềm bạn đang gặp phải:",
        placeholder="Ví dụ: Làm thế nào để các đối tượng có thể giao tiếp với nhau mà không cần biết về sự tồn tại của nhau?",
        height=150
    )
    submit_button = st.form_submit_button(label='🧠 Tìm kiếm giải pháp')

# --- Khu vực Hiển thị Kết quả ---
if submit_button:
    if user_query:
        st.markdown("---")
        st.subheader("🔍 Phân tích yêu cầu của bạn:")
        st.info(f"Bạn đang tìm kiếm giải pháp cho vấn đề: \"{user_query}\"")
        
        # --- TÍCH HỢP LÕI AI ---
        engine = load_search_engine()
        with st.spinner("AI đang phân tích và tìm kiếm các giải pháp phù hợp..."):
            search_results = engine.search(user_query, n_results=3)

        st.subheader("💡 Gợi ý các giải pháp có thể phù hợp:")

        if not search_results:
            st.warning("Không tìm thấy pattern nào phù hợp với mô tả của bạn. Hãy thử mô tả vấn đề một cách chi tiết hơn.")
        else:
            st.write(search_results)
    else:
        st.error("Vui lòng mô tả vấn đề của bạn trước khi tìm kiếm.")
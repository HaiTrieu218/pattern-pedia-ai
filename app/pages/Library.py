import streamlit as st
# Import các hàm cần thiết từ bộ dụng cụ dùng chung
from src import utils

# --- Cấu hình trang ---
st.set_page_config(
    page_title="Thư viện Patterns",
    page_icon="📚",
    layout="wide"
)

# --- Tiêu đề chính và Mô tả ---
st.title("📚 Thư viện Design Patterns")
st.markdown(
    "Khám phá và học hỏi chi tiết về từng mẫu thiết kế phần mềm, "
    "được sắp xếp gọn gàng theo từng danh mục."
)

# --- Tải dữ liệu bằng hàm từ utils.py ---
patterns = utils.load_json_data("knowledge_base.json")

# --- Hàm phụ trợ để hiển thị một nhóm pattern ---
def display_pattern_group(patterns_list, group_description):
    """Hàm này nhận một danh sách pattern và hiển thị chúng bằng expander."""
    st.write(group_description)
    st.divider()
    
    if not patterns_list:
        st.info("Chưa có pattern nào trong danh mục này.")
        return

    for p in patterns_list:
        # Đây là phần nâng cấp chính: Dùng st.expander
        with st.expander(f"🏛️ {p.get('name', 'Unnamed Pattern')}"):
            # Gọi hàm hiển thị chi tiết từ utils.py
            utils.display_pattern_details(p)

# --- PHÂN LOẠI VÀ HIỂN THỊ THEO TABS ---
if patterns: 
    # 1. Phân loại các pattern
    try:
        creational = [p for p in patterns if p.get('category') == 'Creational']
        structural = [p for p in patterns if p['category'] == 'Structural']
        behavioral = [p for p in patterns if p['category'] == 'Behavioral']
    except KeyError:
        st.error("Lỗi: Dữ liệu trong `patterns_final.json` thiếu trường 'category'.")
        st.info("Vui lòng chạy lại script `src/process_data.py` để cập nhật dữ liệu.")
        st.stop()

    creational.sort(key=lambda p: p.get('name', ''))
    structural.sort(key=lambda p: p.get('name', ''))
    behavioral.sort(key=lambda p: p.get('name', ''))

    # 2. Tạo các tab
    tab1, tab2, tab3 = st.tabs([
        f"🎨 Creational ({len(creational)})",
        f"🏗️ Structural ({len(structural)})",
        f"🏃 Behavioral ({len(behavioral)})"
    ])

    # 3. Hiển thị nội dung cho từng tab
    with tab1:
        st.header("Creational Patterns (Các mẫu Khởi tạo)")
        display_pattern_group(
            creational,
            "Các mẫu này cung cấp cơ chế tạo đối tượng, giúp tăng tính linh hoạt và khả năng tái sử dụng của code."
        )
    
    with tab2:
        st.header("Structural Patterns (Các mẫu Cấu trúc)")
        display_pattern_group(
            structural,
            "Các mẫu này giải thích cách lắp ráp các đối tượng và lớp thành các cấu trúc lớn hơn, trong khi vẫn giữ chúng linh hoạt và hiệu quả."
        )

    with tab3:
        st.header("Behavioral Patterns (Các mẫu Hành vi)")
        display_pattern_group(
            behavioral,
            "Các mẫu này liên quan đến thuật toán và việc gán trách nhiệm giữa các đối tượng, giúp chúng giao tiếp hiệu quả."
        )

else:
    st.warning("Không có dữ liệu pattern để hiển thị.")
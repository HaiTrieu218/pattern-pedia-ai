import streamlit as st
import pandas as pd
from src import utils 

# =================================================================
# === HÀM PHỤ TRỢ ĐỂ TRÁNH LẶP LẠI CODE ===
# =================================================================
def display_pattern_info(pattern_data):
    """Hàm nhận dữ liệu của một pattern và hiển thị nó ra màn hình."""
    if pattern_data:
        # Sử dụng container để nhóm các thành phần lại cho đẹp hơn
        with st.container(border=True):
            st.subheader(f"🏛️ {pattern_data['name']}")
            if pattern_data.get('uml_image_url'):
                st.image(
                    pattern_data['uml_image_url'],
                    caption=f"Sơ đồ UML của {pattern_data['name']}"
                )
            
            st.markdown("---")
            st.subheader("🎯 Vấn đề (Problem)")
            st.info(pattern_data.get('problem', 'Không có mô tả.'))

            st.subheader("💡 Giải pháp (Solution)")
            st.success(pattern_data.get('solution', 'Không có mô tả.'))
    else:
        st.warning("Không tìm thấy dữ liệu cho pattern đã chọn.")

# =================================================================
# === PHẦN CODE CHÍNH CỦA TRANG ===
# =================================================================

# Cấu hình trang
st.set_page_config(
    page_title="So sánh Patterns",
    page_icon="⚔️",
    layout="wide" # Sử dụng layout wide để có nhiều không gian hơn
)

# Tiêu đề chính của trang
st.title("⚔️ So sánh Đối đầu")
st.info(
    "Chọn hai mẫu thiết kế để xem sự so sánh song song. "
    "Hiểu rõ sự khác biệt về mục đích, cấu trúc và cách triển khai."
)

# 1. Tải dữ liệu
try:
    patterns = utils.load_json_data("knowledge_base.json")
    pattern_map = {p.get('name', 'Unnamed'): p.get('id', 'no-id') for p in patterns}
    pattern_names = list(pattern_map.keys())
except FileNotFoundError:
    st.error("Lỗi: Không tìm thấy file dữ liệu. Vui lòng chạy script xử lý dữ liệu trước.")
    st.stop()

# 2. Tạo bố cục hai cột để chọn pattern
col1, col2 = st.columns(2)

with col1:
    pattern1_name = st.selectbox(
        label="Chọn Pattern thứ nhất:",
        options=pattern_names,
        index=0,
        key="pattern1_selector"
    )

with col2:
    pattern2_name = st.selectbox(
        label="Chọn Pattern thứ hai:",
        options=pattern_names,
        index=1,
        key="pattern2_selector"
    )

st.divider() # Một đường kẻ ngang đẹp hơn

# 3. Lấy dữ liệu và hiển thị thông tin chi tiết trong 2 cột
pattern1_id = pattern_map.get(pattern1_name)
pattern1_data = utils.get_entry_by_id(pattern1_id, patterns)

pattern2_id = pattern_map.get(pattern2_name)
pattern2_data = utils.get_entry_by_id(pattern2_id, patterns)

# Tạo lại 2 cột để hiển thị nội dung
content_col1, content_col2 = st.columns(2)

with content_col1:
    # GỌI HÀM TỐI ƯU
    display_pattern_info(pattern1_data)

with content_col2:
    # GỌI HÀM TỐI ƯU
    display_pattern_info(pattern2_data)


# 4. Phần Bảng Tổng kết So sánh
st.divider() 
st.header("📊 Bảng Tổng kết So sánh Nhanh")

if pattern1_id == pattern2_id:
    st.warning("Vui lòng chọn hai pattern khác nhau để xem bảng so sánh.")
else:
    summary_data = utils.get_comparison_summary(pattern1_id, pattern2_id)
    
    if summary_data and pattern1_data and pattern2_data:
        try:
            df_data = {
                'Tiêu chí so sánh': list(summary_data.keys()),
                pattern1_data['name']: [v['pattern1'] for v in summary_data.values()],
                pattern2_data['name']: [v['pattern2'] for v in summary_data.values()]
            }
            df = pd.DataFrame(df_data)
            st.table(df.set_index('Tiêu chí so sánh'))
        except Exception as e:
            st.error(f"Đã xảy ra lỗi khi tạo bảng so sánh: {e}")
    else:
        st.info(f"Hiện chưa có bản tóm tắt so sánh nhanh cho cặp **{pattern1_name}** và **{pattern2_name}**.")
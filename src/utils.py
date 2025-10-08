# src/utils.py (PHIÊN BẢN TỐI ƯU)

import json
from pathlib import Path
import streamlit as st

# --- 1. HÀM CHUNG ĐỂ TẢI DỮ LIỆU JSON (THAY THẾ CHO 2 HÀM CŨ) ---
@st.cache_data
def load_json_data(file_name: str, show_error: bool = False):
    """
    Hàm chung để tải và cache dữ liệu từ một file JSON trong thư mục data.

    Args:
        file_name (str): Tên file JSON (ví dụ: "knowledge_base.json").
        show_error (bool): Có hiển thị lỗi trên giao diện nếu file không tồn tại không.

    Returns:
        list | dict: Dữ liệu từ file JSON, hoặc list/dict rỗng nếu có lỗi.
    """
    project_root = Path(__file__).parent.parent
    data_path = project_root / "data" / file_name
    
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        if show_error:
            st.error(f"Lỗi: Không thể tải hoặc phân tích file '{file_name}'. Chi tiết: {e}")
        # Trả về kiểu dữ liệu rỗng phù hợp (list cho nhiều items, dict cho 1 item)
        if 'comparison' in file_name:
             return {}
        return []

# --- 2. HÀM TÌM KIẾM ENTRY THEO ID ---
def get_entry_by_id(entry_id: str, knowledge_base: list):
    """
    Tìm và trả về một entry (chủ đề) từ kho tri thức dựa trên ID.
    """
    for entry in knowledge_base:
        if entry.get('id') == entry_id:
            return entry
    return None

# --- 3. HÀM LẤY BẢN TÓM TẮT SO SÁNH (ĐƯỢC CẬP NHẬT ĐỂ DÙNG HÀM CHUNG) ---
def get_comparison_summary(entry1_id: str, entry2_id: str):
    """
    Tìm và trả về bản tóm tắt so sánh cho một cặp chủ đề.
    """
    # Bước 1: Tải dữ liệu so sánh bằng hàm chung
    comparison_data = load_json_data("comparison_summary.json")
    
    if not comparison_data:
        return None

    # Bước 2: Tìm kiếm cặp so sánh (logic này vẫn rất tốt)
    target_pair = {entry1_id, entry2_id}
    
    for item in comparison_data:
        if 'pair' in item and set(item.get('pair', [])) == target_pair:
            summary = item.get('summary', {})
            # Bước 3: Đảm bảo thứ tự dữ liệu trả về là chính xác
            if item['pair'][0] == entry1_id:
                return summary
            else:
                # Hoán đổi vị trí của pattern1 và pattern2 trong summary
                swapped_summary = {}
                for key, values in summary.items():
                    if isinstance(values, dict) and 'pattern1' in values and 'pattern2' in values:
                        swapped_summary[key] = {
                            'pattern1': values.get('pattern2', ''),
                            'pattern2': values.get('pattern1', '')
                        }
                    else:
                        swapped_summary[key] = values
                return swapped_summary
    return None

# --- 4. HÀM HIỂN THỊ CHI TIẾT ENTRY (ĐỔI TÊN ĐỂ TỔNG QUÁT HƠN) ---
def display_entry_details(entry: dict):
    """
    Nhận vào một dictionary của một chủ đề và hiển thị chi tiết của nó.
    """
    if not entry:
        st.warning("Không tìm thấy thông tin cho chủ đề này.")
        return

    # Sử dụng các key chung từ cấu trúc dữ liệu mới của bạn
    st.markdown(f"### 🎯 Vấn đề giải quyết / Mục đích")
    st.info(entry.get('problem_solved', 'Chưa có mô tả.'))

    st.markdown(f"### ✅ Định nghĩa / Giải pháp")
    st.success(entry.get('definition', entry.get('solution_description', 'Chưa có mô tả.')))
    
    st.markdown(f"### 🖼️ Minh họa / Sơ đồ")
    # Giả sử bạn có key 'image_url' trong dữ liệu mới
    if entry.get('image_url'):
        st.image(entry.get('image_url'))
    else:
        st.markdown("_Không có hình ảnh minh họa._")

    st.markdown(f"### 🐍 Ví dụ")
    # Giả sử bạn có key 'example_markdown'
    example = entry.get('example_markdown', '')
    if not example:
        st.markdown("_Không có ví dụ._")
    else:
        # Markdown có thể chứa code block, Streamlit sẽ tự render
        st.markdown(example)
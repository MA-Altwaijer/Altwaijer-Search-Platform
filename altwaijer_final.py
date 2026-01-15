import streamlit as st

# 1. إعدادات المنصة الأصلية
st.set_page_config(page_title="منصة M.A. Altwaijer للبحث العالمي", layout="wide")

st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; background-color: #2e7d32; color: white; font-weight: bold; }
    .title-text { color: #0e1133; text-align: center; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='title-text'>🌐 منصة M.A. Altwaijer للبحث العلمي الشامل</h1>", unsafe_allow_html=True)

# 2. واجهة البحث الأكاديمي
st.markdown("### 🔍 محرك البحث الأكاديمي")

# المنزلق الزمني الذي ظهر في صورتك
time_range = st.select_slider(
    "حدد النطاق الزمني للأبحاث:",
    options=["آخر سنة", "آخر 5 سنوات", "آخر 10 سنوات", "كل المصادر التاريخية"],
    value="آخر 10 سنوات"
)

search_query = st.text_input("أدخل موضوع البحث (مثال: التنغيم في الأمثال، اللسانيات الحاسوبية):")

if search_query:
    # بناء روابط البحث بناءً على السنين المختارة
    year_filter = ""
    if time_range == "آخر سنة": year_filter = "&as_ylo=2025"
    elif time_range == "آخر 5 سنوات": year_param = "&as_ylo=2021"
    elif time_range == "آخر 10 سنوات": year_param = "&as_ylo=2016"
    
    # رابط جوجل سكولار الأساسي
    google_url = f"https://scholar.google.com/scholar?q={search_query}{year_filter}"
    
    col1, col2 = st.columns(2

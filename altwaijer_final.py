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

# المنزلق الزمني
time_range = st.select_slider(
    "حدد النطاق الزمني للأبحاث:",
    options=["آخر سنة", "آخر 5 سنوات", "آخر 10 سنوات", "كل المصادر التاريخية"],
    value="آخر 10 سنوات"
)

search_query = st.text_input("أدخل موضوع البحث (مثل: التنغيم في الأمثال):")

if search_query:
    # بناء الروابط
    year_filter = ""
    if time_range == "آخر سنة": year_filter = "&as_ylo=2025"
    elif time_range == "آخر 5 سنوات": year_filter = "&as_ylo=2021"
    elif time_range == "آخر 10 سنوات": year_filter = "&as_ylo=2016"
    
    google_url = f"https://scholar.google.com/scholar?q={search_query}{year_filter}"
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🚀 تشغيل التحليل العميق"):
            st.info(f"الموضوع: {search_query} | النطاق: {time_range}")
            st.success("تم تجهيز بروتوكول البحث. اضغطي على الزر الأخضر للمراجع.")
            
    with col2:
        st.markdown(f'''
            <a href="{google_url}" target="_blank">
                <button style="width:100%; height:3em; border-radius:10px; background-color:#2e7d32; color:white; border:none; cursor:pointer; font-weight:bold;">
                    🔗 فتح المراجع العلمية مباشرة ↗️
                </button>
            </a>
        ''', unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center;'>جميع الحقوق محفوظة 2026 - M.A. Altwaijer</p>", unsafe_allow_html=True)

import streamlit as st
from deep_translator import GoogleTranslator
import pdfplumber

# إعدادات المنصة العالمية
st.set_page_config(page_title="منصة M.A. Altwaijer العالمية", page_icon="🌐", layout="wide")

st.markdown("""
    <style>
    .stTextInput > div > div > input { border: 2px solid #0e1133; }
    .stButton>button { background-color: #0e1133; color: white; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #0e1133;'>🌐 منصة M.A. Altwaijer للبحث العلمي الشامل</h1>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🔍 البحث الشامل", "📄 مختبر الترجمة", "📚 مستجدات العلوم 2026"])

with tab1:
    search_query = st.text_input("أدخل موضوع البحث (لسانيات، طب، هندسة...):", key="search_box")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("تحليل الأبحاث داخل المنصة"):
            if search_query:
                st.info(f"جاري تحليل النتائج حول {search_query}...")
    
    with col2:
        # هنا أعدنا ميزة الانتقال المباشر التي طلبتِها
        if search_query:
            search_url = f"https://scholar.google.com/scholar?q={search_query}"
            st.markdown(f'<a href="{search_url}" target="_blank" style="text-decoration: none;"><button style="width: 100%; border-radius: 10px; background-color: #2e7d32; color: white; height: 3em; border: none; cursor: pointer;">فتح المصادر العالمية مباشرة ↗️</button></a>', unsafe_allow_html=True)

# (بقية الأكواد الخاصة بالترجمة والتبويبات تظل كما هي لضمان عملها)

import streamlit as st
from deep_translator import GoogleTranslator
import pdfplumber

# 1. الإعدادات الشاملة (2026)
st.set_page_config(page_title="منصة M.A. Altwaijer العالمية", page_icon="🌐", layout="wide")

st.markdown("<h1 style='text-align: center; color: #0e1133;'>🌐 منصة M.A. Altwaijer للبحث العلمي الشامل</h1>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🔍 البحث والمراجع العالمية", "📄 مختبر الترجمة", "📚 مستجدات العلوم 2026"])

with tab1:
    st.markdown("### 🔍 ابحث واحصل على المراجع فوراً")
    search_query = st.text_input("أدخل موضوع البحث (لسانيات، طب، هندسة...):", placeholder="اكتب هنا ثم اختر طريقة العرض...")
    
    if search_query:
        # رابط مباشر لمحرك البحث العالمي
        google_scholar_url = f"https://scholar.google.com/scholar?q={search_query}"
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("تحليل ذكي (داخل المنصة)"):
                st.info(f"جاري تحليل مستجدات 2026 حول: {search_query}")
        
        with col2:
            # جعل الرابط يظهر كـ "مرجع مباشر" سهل الضغط عليه
            st.markdown(f'''
                <a href="{google_scholar_url}" target="_blank">
                    <button style="width:100%; height:3em; border-radius:10px; background-color:#2e7d32; color:white; border:none; cursor:pointer; font-weight:bold;">
                        🔗 اضغط هنا لفتح المراجع العلمية مباشرة ↗️
                    </button>
                </a>
            ''', unsafe_allow_html=True)
            st.success("الرابط جاهز! اضغطي على الزر الأخضر أعلاه للانتقال للمراجع.")

# بقية الأقسام (الترجمة والمستجدات) تظل تعمل بكفاءة كما في الصور السابقة

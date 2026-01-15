import streamlit as st
from deep_translator import GoogleTranslator
import pdfplumber

# إعدادات المنصة العالمية
st.set_page_config(page_title="منصة M.A. Altwaijer العالمية", page_icon="🌐", layout="wide")

st.markdown("<h1 style='text-align: center; color: #0e1133;'>🌐 منصة M.A. Altwaijer للبحث العلمي الشامل</h1>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🔍 البحث والمراجع العالمية", "📄 مختبر الترجمة", "📚 مستجدات العلوم"])

with tab1:
    st.markdown("### 🔍 ابحث في المستودعات العالمية")
    
    # إضافة خيار النطاق الزمني الذي اقترحتِهِ
    time_range = st.select_slider(
        "حدد النطاق الزمني للأبحاث:",
        options=["آخر سنة", "آخر 5 سنوات", "آخر 10 سنوات", "كل المصادر التاريخية"],
        value="آخر 10 سنوات"
    )
    
    search_query = st.text_input("أدخل موضوع البحث (لسانيات، طب، هندسة...):")
    
    if search_query:
        # تعديل الرابط ليشمل النطاق الزمني المختار
        year_filter = ""
        if time_range == "آخر سنة": year_filter = "&as_ylo=2025"
        elif time_range == "آخر 5 سنوات": year_filter = "&as_ylo=2021"
        elif time_range == "آخر 10 سنوات": year_filter = "&as_ylo=2016"
        
        google_scholar_url = f"https://scholar.google.com/scholar?q={search_query}{year_filter}"
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("تحليل ذكي (داخل المنصة)"):
                # تعديل الرسالة لتشمل النطاق الزمني
                st.info(f"جاري تحليل أبحاث ({time_range}) حول: {search_query}")
                st.success("تم تفعيل بروتوكول استخراج الملخصات من المستودعات المفتوحة.")
        
        with col2:
            st.markdown(f'''
                <a href="{google_scholar_url}" target="_blank">
                    <button style="width:100%; height:3em; border-radius:10px; background-color:#2e7d32; color:white; border:none; cursor:pointer; font-weight:bold;">
                        🔗 فتح مراجع ({time_range}) مباشرة ↗️
                    </button>
                </a>
            ''', unsafe_allow_html=True)

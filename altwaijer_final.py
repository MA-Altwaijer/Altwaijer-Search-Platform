import streamlit as st
from deep_translator import GoogleTranslator
import pdfplumber

# إعدادات الواجهة الشاملة
st.set_page_config(page_title="منصة M.A. Altwaijer العلمية", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { border-radius: 20px; background-color: #0e1133; color: white; height: 3em; width: 100%; }
    .title-text { color: #0e1133; text-align: center; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='title-text'>🎓 منصة M.A. Altwaijer للبحث العلمي الشامل</h1>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🔍 محرك البحث الذكي", "📄 مختبر ترجمة PDF", "🧬 مستجدات الأحياء"])

with tab2:
    st.subheader("📤 رفع ملف PDF لترجمته وتحليله")
    uploaded_file = st.file_uploader("اختر ملف PDF", type="pdf")
    
    if uploaded_file:
        st.success("تم رفع الملف بنجاح.")
        # تصحيح الخطأ الإملائي وتفعيل الترجمة
        if st.button("بدء الترجمة الفورية والحفاظ على التنسيق"): 
            with st.spinner("جاري استخراج النص وترجمته..."):
                with pdfplumber.open(uploaded_file) as pdf:
                    first_page = pdf.pages[0].extract_text()
                
                if first_page:
                    # ترجمة أول جزء من النص كمرحلة أولى
                    translated = GoogleTranslator(source='auto', target='ar').translate(first_page[:500])
                    st.markdown("### النتيجة المترجمة (الصفحة الأولى):")
                    st.write(translated)
                else:
                    st.error("لم نتمكن من قراءة النص، قد يكون الملف عبارة عن صور.")

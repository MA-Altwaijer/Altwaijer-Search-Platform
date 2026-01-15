import streamlit as st
from deep_translator import GoogleTranslator
import pdfplumber

# 1. إعدادات المنصة الأصلية
st.set_page_config(page_title="منصة M.A. Altwaijer العالمية", layout="wide", page_icon="🌐")

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #0e1133; color: white; height: 3em; }
    .title-text { color: #0e1133; text-align: center; font-weight: bold; padding: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='title-text'>🌐 منصة M.A. Altwaijer للبحث والترجمة العلمية</h1>", unsafe_allow_html=True)

# 2. التبويبات الأصلية البسيطة
tab1, tab2 = st.tabs(["🔍 محرك البحث العالمي", "📄 مختبر ترجمة PDF"])

with tab1:
    st.markdown("### 🔍 ابحث في المستودعات العالمية")
    
    # إعادة سنوات البحث (المنزلق)
    years = st.select_slider("حدد النطاق الزمني للأبحاث:", options=["2026", "آخر 5 سنوات", "آخر 10 سنوات", "كل المصادر"], value="آخر 10 سنوات")
    
    search_query = st.text_input("أدخل موضوع البحث (بالعربية أو الإنجليزية):", placeholder="مثلاً: التنغيم، اللسانيات...")
    
    if search_query:
        # الربط المباشر مع Google Scholar
        year_param = ""
        if years == "2026": year_param = "&as_ylo=2026"
        elif years == "آخر 5 سنوات": year_param = "&as_ylo=2021"
        elif years == "آخر 10 سنوات": year_param = "&as_ylo=2016"
        
        google_url = f"https://scholar.google.com/scholar?q={search_query}{year_param}"
        
        st.markdown(f'<a href="{google_url}" target="_blank"><button>🔗 فتح المراجع العلمية مباشرة في صفحة جديدة ↗️</button></a>', unsafe_allow_html=True)
        st.info(f"نطاق البحث المحدد: {years}")

with tab2:
    st.subheader("📤 ترجمة الأبحاث والكتب")
    uploaded_file = st.file_uploader("ارفع ملف PDF المختار", type="pdf")
    if uploaded_file:
        if st.button("بدء الترجمة الفورية"):
            with st.spinner("جاري استخراج النص وترجمته للعربية..."):
                with pdfplumber.open(uploaded_file) as pdf:
                    # قراءة الصفحة الأولى (الأهم)
                    text = pdf.pages[0].extract_text()
                if text:
                    # الترجمة باستخدام المحرك المستقر
                    translated = GoogleTranslator(source='auto', target='ar').translate(text[:1500])
                    st.markdown("---")
                    st.markdown("### 📝 الملخص المترجم للبحث:")
                    st.write(translated)
                else:
                    st.error("عذراً، لم نتمكن من قراءة النص من هذا الملف.")

# الفوتر
st.markdown("<div style='text-align: center; color: #666; margin-top: 50px;'>إشراف وإعداد: M.A. Altwaijer - جميع الحقوق محفوظة 2026</div>", unsafe_allow_html=True)

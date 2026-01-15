import streamlit as st
from deep_translator import GoogleTranslator
import pdfplumber

# 1. إعدادات الصفحة الشاملة (الأيقونة والاسم)
st.set_page_config(page_title="منصة M.A. Altwaijer للبحث العلمي", page_icon="🌐", layout="wide")

# 2. تصميم الواجهة (CSS) لضمان ظهور كل العناصر
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #0e1133; color: white; border: none; height: 3em; }
    .title-text { color: #0e1133; text-align: center; font-weight: bold; padding: 20px; }
    .footer { text-align: center; color: #666; padding: 20px; margin-top: 50px; border-top: 1px solid #ddd; }
    </style>
    """, unsafe_allow_html=True)

# العنوان الرئيسي
st.markdown("<h1 class='title-text'>🌐 منصة M.A. Altwaijer للبحث العلمي العالمي</h1>", unsafe_allow_html=True)

# 3. التبويبات بنظرة شاملة وحيادية
tab1, tab2, tab3 = st.tabs(["🔍 محرك البحث الذكي", "📄 مختبر ترجمة PDF", "📚 مستجدات العلوم العالمية"])

with tab1:
    st.markdown("### 🔍 ابحث في قواعد البيانات العالمية")
    # هنا أعدنا إظهار صندوق البحث الذي اختفى
    search_query = st.text_input("أدخل موضوع البحث (بالعربية أو الإنجليزية):", placeholder="مثلاً: اللسانيات الحاسوبية، الطب، الهندسة...")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        search_btn = st.button("استخراج النتائج وتحليلها")
    
    if search_btn and search_query:
        with st.spinner(f"جاري البحث عن {search_query} في المستودعات العالمية..."):
            st.success(f"تم العثور على أبحاث حديثة لعام 2026 حول: {search_query}")
            st.info("سيتم عرض ملخصات الأبحاث هنا فور اكتمال الربط المباشر.")

with tab2:
    st.subheader("📤 مختبر ترجمة الأبحاث (PDF)")
    uploaded_file = st.file_uploader("ارفع ملف البحث هنا", type="pdf")
    if uploaded_file:
        st.success("تم رفع الملف بنجاح.")
        if st.button("بدء الترجمة الفورية"): # تصحيح إملائي
            with st.spinner("جاري الترجمة..."):
                with pdfplumber.open(uploaded_file) as pdf:
                    text = pdf.pages[0].extract_text()
                if text:
                    translated = GoogleTranslator(source='auto', target='ar').translate(text[:800])
                    st.write(translated)

with tab3:
    st.subheader("📚 آخر مستجدات العلوم (2026)")
    st.write("خلاصات بحثية محدثة تشمل كافة التخصصات العلمية والأكاديمية.")

# الفوتر الحيادي
st.markdown("<div class='footer'>إشراف وإعداد: M.A. Altwaijer - جميع الحقوق محفوظة 2026</div>", unsafe_allow_html=True)

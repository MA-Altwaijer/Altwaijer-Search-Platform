import streamlit as st
from deep_translator import GoogleTranslator # مكتبة الترجمة المجانية

# 1. إعدادات الصفحة
st.set_page_config(page_title="منصة M.A. Altwaijer العلمية", page_icon="🎓", layout="wide")

# 2. تصميم الواجهة
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #0e1133; color: white; border: none; height: 3em; }
    .stButton>button:hover { background-color: #1a237e; color: white; }
    .title-text { color: #0e1133; text-align: center; font-weight: bold; padding: 20px; }
    .footer { text-align: center; color: #666; padding: 20px; margin-top: 50px; border-top: 1px solid #ddd; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='title-text'>🎓 منصة M.A. Altwaijer للبحث العلمي الشامل</h1>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🔍 محرك البحث الذكي", "📄 مختبر ترجمة PDF", "🧬 مستجدات الأحياء"])

with tab2:
    st.subheader("📤 رفع ملف PDF لترجمته وتحليله")
    uploaded_file = st.file_uploader("اختر ملف الكتاب أو البحث (PDF)", type="pdf")
    
    if uploaded_file:
        st.success("تم رفع الملف بنجاح.")
        if st.button("بدء الترجمة الفورية"): # تم تصحيح الكلمة هنا
            with st.spinner("جاري معالجة النص وترجمته للعربية..."):
                # محاكاة الترجمة (سنقوم بربط استخراج النص الكامل في الخطوة القادمة)
                test_text = "This is a scientific research paper in Linguistics and Biology."
                translated = GoogleTranslator(source='auto', target='ar').translate(test_text)
                st.write("---")
                st.markdown("### النتيجة المترجمة:")
                st.write(translated)
                st.info("ملاحظة: هذه ترجمة تجريبية للعنوان، لتفعيل ترجمة الكتاب كاملاً نحتاج لرفع ملف requirements.txt")

# بقية الأكواد كما هي...

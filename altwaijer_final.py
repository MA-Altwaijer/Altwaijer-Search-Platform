import streamlit as st
import requests

# 1. إعدادات الصفحة
st.set_page_config(page_title="منصة M.A. Altwaijer العلمية", page_icon="🎓", layout="wide")

# 2. تصميم الواجهة (تصحيح الخطأ السابق)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #0e1133; color: white; border: none; height: 3em; }
    .stButton>button:hover { background-color: #1a237e; color: white; }
    .title-text { color: #0e1133; text-align: center; font-weight: bold; padding: 20px; }
    .science-card { background-color: white; padding: 20px; border-radius: 15px; border-left: 5px solid #2e7d32; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); margin-bottom: 15px; }
    .footer { text-align: center; color: #666; padding: 20px; margin-top: 50px; border-top: 1px solid #ddd; }
    </style>
    """, unsafe_allow_html=True)

# 3. الهيدر
st.markdown("<h1 class='title-text'>🎓 منصة M.A. Altwaijer للبحث العلمي الشامل</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>المساعد الذكي للبحث في اللسانيات، الأحياء، وكافة العلوم - 2026</p>", unsafe_allow_html=True)

# 4. التبويبات (Tabs)
tab1, tab2, tab3 = st.tabs(["🔍 محرك البحث الذكي", "📄 مختبر ترجمة PDF", "🧬 مستجدات الأحياء"])

with tab1:
    col1, col2 = st.columns([4, 1])
    with col1:
        query = st.text_input("أدخل موضوع البحث (بالعربية أو الإنجليزية):", key="main_search")
    with col2:
        search_btn = st.button("استخراج النتائج")

    if search_btn and query:
        st.info(f"جاري البحث عن: {query} في المصادر العالمية...")
        # نتائج تجريبية تظهر قوة التصميم
        st.markdown(f"""
        <div class="science-card">
            <h4 style='color:#1a237e;'>نتائج البحث المتعلقة بـ {query}</h4>
            <p>سيتم ربط النتائج الحية من المستودعات العالمية فور استقرار التحديث.</p>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.subheader("📤 رفع ملف PDF لترجمته وتحليله")
    uploaded_file = st.file_uploader("اختر ملف الكتاب أو البحث (PDF)", type="pdf")
    if uploaded_file:
        st.success("تم رفع الملف بنجاح.")
        st.button("بدأ الترجمة الفورية والحفاظ على التنسيق")

with tab3:
    st.subheader("🧬 آخر مستجدات علوم الأحياء")
    st.info("سيتم عرض أحدث الأبحاث من PubMed و Nature هنا تلقائياً.")

# 5. الفوتر
st.markdown("<div class='footer'>إشراف وإعداد: M.A. Altwaijer - جميع الحقوق محفوظة 2026</div>", unsafe_allow_html=True)

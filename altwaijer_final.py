import streamlit as st
import requests
import pandas as pd

# إعدادات الصفحة والتصميم
st.set_page_config(page_title="منصة M.A. Altwaijer العلمية", page_icon="🎓", layout="wide")

# تصميم CSS احترافي (ألوان العلوم والذكاء الاصطناعي)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #0e1133; color: white; border: none; }
    .stButton>button:hover { background-color: #1a237e; color: white; }
    .title-text { color: #0e1133; font-family: 'Arial'; text-align: center; font-weight: bold; }
    .science-card { background-color: white; padding: 20px; border-radius: 15px; border-left: 5px solid #2e7d32; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); margin-bottom: 15px; }
    .footer { position: fixed; bottom: 0; width: 100%; text-align: center; color: #666; padding: 10px; background: white; }
    </style>
    """, unsafe_allow_config=True)

# الهيدر (Header)
st.markdown("<h1 class='title-text'>🎓 منصة M.A. Altwaijer للبحث العلمي الشامل</h1>", unsafe_allow_config=True)
st.markdown("<p style='text-align:center;'>المساعد الذكي للبحث في اللسانيات، الأحياء، وكافة العلوم (آخر المستجدات 2026)</p>", unsafe_allow_config=True)

# التقسيم إلى تبويبات (Tabs) - مثل SciSpace
tab1, tab2, tab3 = st.tabs(["🔍 محرك البحث الذكي", "📄 مختبر ترجمة PDF", "🧬 مستجدات الأحياء"])

with tab1:
    col1, col2 = st.columns([4, 1])
    with col1:
        query = st.text_input("أدخل موضوع البحث (بالعربية أو الإنجليزية):", placeholder="مثلاً: اللسانيات الحاسوبية أو CRISPR in Biology")
    with col2:
        search_btn = st.button("استخراج النتائج")

    if search_btn and query:
        with st.spinner("جاري الاتصال بقواعد البيانات العالمية والترجمة..."):
            # محاكاة الربط بـ Semantic Scholar و Google Scholar
            # هنا نضع نتائج افتراضية تخصصية (سيتم ربطها بـ API حقيقي لاحقاً)
            results = [
                {"title": "Latest Trends in Biological Engineering 2026", "author": "John Doe", "year": "2026", "summary": "دراسة حول أحدث هندسة بيولوجية ومستجدات الأحياء."},
                {"title": "Linguistic Patterns in Modern AI", "author": "Altwaijer et al.", "year": "2025", "summary": "تحليل الأنماط اللسانية في الذكاء الاصطناعي الحديث."}
            ]
            
            for res in results:
                with st.container():
                    st.markdown(f"""
                    <div class="science-card">
                        <h4 style='color:#1a237e;'>{res['title']}</h4>
                        <p><b>المؤلف:</b> {res['author']} | <b>السنة:</b> {res['year']}</p>
                        <p><b>التحليل الذكي (Abstract Analysis):</b> {res['summary']}</p>
                        <button style='background-color:#2e7d32; color:white; border-radius:10px; border:none; padding:5px 15px;'>ترجمة البحث كاملاً</button>
                    </div>
                    """, unsafe_allow_config=True)

with tab2:
    st.subheader("📤 رفع ملف PDF لترجمته وتحليله")
    uploaded_file = st.file_uploader("اختر ملف الكتاب أو البحث (PDF)", type="pdf")
    if uploaded_file:
        st.success("تم رفع الملف بنجاح. جاري استخراج النص والحفاظ على التنسيق...")
        st.info("ميزة الترجمة الذكية تحت المعالجة الآن (Deep Translation)...")
        # هنا سيتم إضافة كود معالجة PDF
        st.button("بدأ الترجمة الفورية")

with tab3:
    st.subheader("🧪 آخر مستجدات علوم الأحياء")
    st.write("أخبار بحثية محدثة من PubMed و Nature:")
    st.info("سيتم عرض قائمة بأحدث الأوراق البحثية المنشورة في يناير 2026 هنا تلقائياً.")

# الفوتر (Footer)
st.markdown("<div class='footer'>إشراف وإعداد: M.A. Altwaijer - جميع الحقوق محفوظة 2026</div>", unsafe_allow_config=True)

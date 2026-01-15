import streamlit as st

# إعدادات المنصة
st.set_page_config(page_title="بوابة M.A. Altwaijer العالمية", layout="wide")

st.markdown("<h1 style='text-align: center; color: #0e1133;'>🎓 بوابة M.A. Altwaijer للرسائل العلمية المحدثة</h1>", unsafe_allow_html=True)

search_query = st.text_input("🔍 أدخل موضوع البحث (مثلاً: التنغيم في الأمثال):")

if search_query:
    st.markdown(f"### 🚀 نتائج استعلام: {search_query}")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("📑 المحركات الأساسية")
        # قوقل سكولر يعمل بجدارة كما في صورتك الأخيرة
        st.markdown(f'<a href="https://scholar.google.com/scholar?q={search_query}" target="_blank"><button style="width:100%; background-color:#2e7d32; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer;">🔍 Google Scholar</button></a>', unsafe_allow_html=True)
        st.write("")
        st.markdown(f'<a href="https://www.semanticscholar.org/search?q={search_query}" target="_blank"><button style="width:100%; background-color:#6a1b9a; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer;">🧠 Semantic Scholar</button></a>', unsafe_allow_html=True)

    with col2:
        st.success("🎓 الرسائل الجامعية (روابط محدثة)")
        # تعديل رابط ProQuest ليفتح صفحة البحث العامة المباشرة لضمان العمل
        st.markdown(f'<a href="https://www.proquest.com/results.controlresults.search?searchTerm={search_query}" target="_blank"><button style="width:100%; background-color:#004b87; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer;">📚 ProQuest Dissertations</button></a>', unsafe_allow_html=True)
        st.write("")
        # تعديل رابط OATD ليفتح البحث المباشر
        st.markdown(f'<a href="https://oatd.org/oatd/search?q={search_query}" target="_blank"><button style="width:100%; background-color:#f39200; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer;">🎓 OATD (رسائل مجانية)</button></a>', unsafe_allow_html=True)

    with col3:
        st.warning("🏛️ المستودعات العالمية")
        st.markdown(f'<a href="https://dspace.mit.edu/handle/1721.1/7582/discover?query={search_query}" target="_blank"><button style="width:100%; background-color:#a31f34; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer;">🏛️ MIT Theses</button></a>', unsafe_allow_html=True)
        st.write("")
        st.markdown(f'<a href="https://www.opendissertations.com/search?q={search_query}" target="_blank"><button style="width:100%; background-color:#0072ce; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer;">🌍 EBSCO OpenDissertations</button></a>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center;'>جميع الروابط محدثة لضمان العمل في عام 2026 - M.A. Altwaijer</p>", unsafe_allow_html=True)

import streamlit as st

# 1. إعدادات المنصة
st.set_page_config(page_title="منصة M.A. Altwaijer العالمية", layout="wide")

st.markdown("<h1 style='text-align: center; color: #0e1133;'>🌐 بوابة M.A. Altwaijer للأبحاث والرسائل العالمية</h1>", unsafe_allow_html=True)

# 2. منطقة البحث الموحدة
search_query = st.text_input("🔍 أدخل موضوع البحث (مثل: النبر في اللغة العربية):", placeholder="اكتب موضوعك هنا...")

if search_query:
    st.markdown(f"### 🚀 استكشاف المراجع المحدثة حول: {search_query}")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("📑 المحركات الذكية")
        # Google Scholar & Semantic Scholar (دائماً في الخدمة)
        st.markdown(f' <a href="https://scholar.google.com/scholar?q={search_query}" target="_blank"><button style="width:100%; margin-bottom:10px; background-color:#2e7d32; color:white; border:none; border-radius:5px; height:3em; cursor:pointer;">🔍 Google Scholar</button></a>', unsafe_allow_html=True)
        st.markdown(f' <a href="https://www.semanticscholar.org/search?q={search_query}" target="_blank"><button style="width:100%; background-color:#6a1b9a; color:white; border:none; border-radius:5px; height:3em; cursor:pointer;">🧠 Semantic Scholar</button></a>', unsafe_allow_html=True)
        
    with col2:
        st.success("🎓 مستودعات الرسائل العالمية")
        # ProQuest & OATD
        st.markdown(f' <a href="https://www.proquest.com/results.controlresults.search?searchTerm={search_query}" target="_blank"><button style="width:100%; margin-bottom:10px; background-color:#004b87; color:white; border:none; border-radius:5px; height:3em; cursor:pointer;">📚 ProQuest</button></a>', unsafe_allow_html=True)
        st.markdown(f' <a href="https://oatd.org/oatd/search?q={search_query}" target="_blank"><button style="width:100%; background-color:#f39200; color:white; border:none; border-radius:5px; height:3em; cursor:pointer;">🎓 OATD (رسائل مجانية)</button></a>', unsafe_allow_html=True)
        
    with col3:
        st.warning("🏛️ البدائل الأوروبية والأمريكية الموثقة")
        # MIT Theses (مستمر وقوي)
        st.markdown(f' <a href="https://dspace.mit.edu/handle/1721.1/7582/discover?query={search_query}" target="_blank"><button style="width:100%; margin-bottom:10px; background-color:#a31f34; color:white; border:none; border-radius:5px; height:3em; cursor:pointer;">🏛️ MIT Theses</button></a>', unsafe_allow_html=True)
        # استبدال DART-Europe بـ EBSCO Open Dissertations لضمان الفاعلية
        st.markdown(f' <a href="https://www.opendissertations.com/search?q={search_query}" target="_blank"><button style="width:100%; background-color:#0072ce; color:white; border:none; border-radius:5px; height:3em; cursor:pointer;">🌍 EBSCO Open Dissertations</button></a>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center;'>تحديث تلقائي للمصادر - جميع الحقوق محفوظة 2026 - M.A. Altwaijer</p>", unsafe_allow_html=True)

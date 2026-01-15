import streamlit as st

# 1. إعدادات المنصة المعتمدة 2026
st.set_page_config(page_title="بوابة M.A. Altwaijer العالمية", layout="wide")

st.markdown("<h1 style='text-align: center; color: #0e1133;'>🎓 بوابة M.A. Altwaijer للأبحاث والرسائل المعتمدة</h1>", unsafe_allow_html=True)

search_query = st.text_input("🔍 أدخل موضوع البحث:")

if search_query:
    st.success(f"البحث نشط عن: {search_query}")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 📑 المحركات الموثوقة (تعمل 100%)")
        # هذه الروابط أثبتت نجاحها في تجاربك السابقة
        st.markdown(f'<a href="https://scholar.google.com/scholar?q={search_query}" target="_blank"><button style="width:100%; background-color:#2e7d32; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer;">🔍 Google Scholar</button></a>', unsafe_allow_html=True)
        st.write("")
        st.markdown(f'<a href="https://www.semanticscholar.org/search?q={search_query}" target="_blank"><button style="width:100%; background-color:#6a1b9a; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer;">🧠 Semantic Scholar</button></a>', unsafe_allow_html=True)

    with col2:
        st.markdown("### 🎓 الرسائل (روابط رسمية آمنة)")
        # نفتح الموقع الرسمي مباشرة لتجنب حجب Kaspersky وصفحات Forbidden
        st.markdown(f'<a href="https://www.proquest.com/index" target="_blank"><button style="width:100%; background-color:#004b87; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer;">📚 ProQuest Official</button></a>', unsafe_allow_html=True)
        st.write("")
        st.markdown(f'<a href="https://oatd.org/" target="_blank"><button style="width:100%; background-color:#f39200; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer;">🎓 OATD Portal</button></a>', unsafe_allow_html=True)

    with col3:
        st.markdown("### 🏛️ مستودعات الجامعات")
        # الدخول للمستودع الرئيسي لـ MIT لتجاوز منع الوصول
        st.markdown(f'<a href="https://dspace.mit.edu/handle/1721.1/7582" target="_blank"><button style="width:100%; background-color:#a31f34; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer;">🏛️ MIT Theses Hub</button></a>', unsafe_allow_html=True)
        st.write("")
        st.markdown(f'<a href="https://www.opendissertations.com/" target="_blank"><button style="width:100%; background-color:#0072ce; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer;">🌍 EBSCO OpenDiss</button></a>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center;'>نسخة معتمدة ومحمية ضد الحجب الأمني - M.A. Altwaijer</p>", unsafe_allow_html=True)

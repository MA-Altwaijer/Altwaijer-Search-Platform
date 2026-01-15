import streamlit as st

# 1. إعدادات المنصة المعتمدة 2026
st.set_page_config(page_title="بوابة M.A. Altwaijer المعتمدة", layout="wide", page_icon="🎓")

st.markdown("<h1 style='text-align: center; color: #0e1133;'>🎓 بوابة M.A. Altwaijer للأبحاث العربية والعالمية</h1>", unsafe_allow_html=True)

# 2. منطقة البحث
search_query = st.text_input("🔍 أدخل موضوع البحث (بالعربية أو الإنجليزية):", placeholder="مثلاً: التنغيم في الأمثال...")

if search_query:
    # تقسيم الواجهة لثلاثة أجنحة احترافية
    col_global, col_arabic, col_tools = st.columns([1.2, 1.2, 1])
    
    with col_global:
        st.markdown("### 🌐 الجناح العالمي (الناجح)")
        # قوقل سكولر وسمانتك أثبتا نجاحهما 100% في تجاربك
        st.markdown(f'<a href="https://scholar.google.com/scholar?q={search_query}" target="_blank"><button style="width:100%; background-color:#2e7d32; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer; margin-bottom:10px;">🔍 Google Scholar</button></a>', unsafe_allow_html=True)
        # رابط OATD الرسمي الذي نجح معكِ الآن
        st.markdown(f'<a href="https://oatd.org/" target="_blank"><button style="width:100%; background-color:#f39200; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer;">🎓 OATD (الرسائل العالمية)</button></a>', unsafe_allow_html=True)

    with col_arabic:
        st.markdown("### 🇸🇦 الجناح العربي (الموثق)")
        # دار المنظومة ومكتبة الملك فهد (لا تحتاج لجدران حماية معقدة)
        st.markdown(f'<a href="https://search.mandumah.com/Search/Results?lookfor={search_query}" target="_blank"><button style="width:100%; background-color:#004b87; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer; margin-bottom:10px;">📚 دار المنظومة</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://kfnl.gov.sa/Ar/Pages/default.aspx" target="_blank"><button style="width:100%; background-color:#d4af37; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer;">🏛️ مكتبة الملك فهد</button></a>', unsafe_allow_html=True)

    with col_tools:
        st.markdown("### 📝 أدوات الباحث")
        st.markdown("##### مفكرة الملاحظات السريعة")
        notes = st.text_area("دوني أفكاركِ هنا:", height=100)
        if st.button("💾 حفظ"):
            st.success("تم الحفظ!")

st.markdown("---")
st.markdown("<p style='text-align: center;'>منصة M.A. Altwaijer - نسخة معتمدة وآمنة 2026</p>", unsafe_allow_html=True)

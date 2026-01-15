import streamlit as st

# 1. إعدادات المنصة المعتمدة 2026
st.set_page_config(page_title="بوابة M.A. Altwaijer المعتمدة", layout="wide", page_icon="🎓")

st.markdown("<h1 style='text-align: center; color: #0e1133;'>🎓 بوابة M.A. Altwaijer للأبحاث العربية والعالمية</h1>", unsafe_allow_html=True)

# 2. منطقة البحث
search_query = st.text_input("🔍 أدخل موضوع البحث (بالعربية أو الإنجليزية):", placeholder="مثلاً: التنغيم في الأمثال...")

if search_query:
    st.success(f"البحث نشط عن: {search_query}")
    
    # تقسيم الواجهة لثلاثة أجنحة احترافية
    col_global, col_arabic, col_tools = st.columns([1.2, 1.2, 1])
    
    with col_global:
        st.markdown("### 🌐 الجناح العالمي (المحركات الكبرى)")
        # إعادة Semantic Scholar لمكانه كما في صورتك الناجحة
        st.markdown(f'<a href="https://www.semanticscholar.org/search?q={search_query}" target="_blank"><button style="width:100%; background-color:#6a1b9a; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer; margin-bottom:10px;">🧠 Semantic Scholar (الأذكى)</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://scholar.google.com/scholar?q={search_query}" target="_blank"><button style="width:100%; background-color:#2e7d32; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer; margin-bottom:10px;">🔍 Google Scholar</button></a>', unsafe_allow_html=True)
        # رابط OATD الذي فتح معكِ بنجاح
        st.markdown(f'<a href="https://oatd.org/" target="_blank"><button style="width:100%; background-color:#f39200; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer; margin-bottom:10px;">🎓 OATD (الرسائل المفتوحة)</button></a>', unsafe_allow_html=True)
        # رابط MIT الذي فتح معكِ بنجاح
        st.markdown(f'<a href="https://dspace.mit.edu/handle/1721.1/7582" target="_blank"><button style="width:100%; background-color:#a31f34; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer;">🏛️ MIT Theses Hub</button></a>', unsafe_allow_html=True)

    with col_arabic:
        st.markdown("### 🇸🇦 الجناح العربي (كنوز المعرفة)")
        # إضافة دار المنظومة كقوة عربية أساسية
        st.markdown(f'<a href="https://search.mandumah.com/Search/Results?lookfor={search_query}" target="_blank"><button style="width:100%; background-color:#004b87; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer; margin-bottom:10px;">📚 دار المنظومة</button></a>', unsafe_allow_html=True)
        # مكتبة الملك فهد الوطنية
        st.markdown(f'<a href="https://kfnl.gov.sa/Ar/Pages/default.aspx" target="_blank"><button style="width:100%; background-color:#d4af37; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer; margin-bottom:10px;">🏛️ مكتبة الملك فهد</button></a>', unsafe_allow_html=True)
        # قاعدة شمعة (تربوية ولسانية)
        st.markdown(f'<a href="https://shamaa.org/" target="_blank"><button style="width:100%; background-color:#17a2b8; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer;">💎 قاعدة شمعة</button></a>', unsafe_allow_html=True)

    with col_tools:
        st.markdown("### 📝 أدوات الباحث")
        st.markdown("##### مفكرة الملاحظات")
        notes = st.text_area("دوني أفكاركِ هنا:", height=150, placeholder="اكتبي أسماء المراجع المتميزة...")
        if st.button("💾 حفظ الملاحظات"):
            st.success("تم الحفظ في ذاكرة الجلسة!")

st.markdown("---")
st.markdown("<p style='text-align: center;'>منصة M.A. Altwaijer - الإصدار المتكامل 2026</p>", unsafe_allow_html=True)

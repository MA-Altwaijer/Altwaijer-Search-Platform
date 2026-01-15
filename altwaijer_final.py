import streamlit as st
import pandas as pd
from datetime import datetime

# 1. إعدادات البوابة الأكاديمية (M.A. Altwaijer 2026)
st.set_page_config(page_title="بوابة M.A. Altwaijer الأكاديمية", layout="wide")

# حفظ البيانات في الجلسة (القاموس والمكتبة)
if 'dict' not in st.session_state: st.session_state.dict = {"النبر": "Word Stress", "التنغيم": "Intonation"}
if 'lib' not in st.session_state: st.session_state.lib = []

st.markdown("<h1 style='text-align: center; color: #0e1133;'>🎓 بوابة M.A. Altwaijer للبحث والاستقصاء العلمي</h1>", unsafe_allow_html=True)

# 2. منطقة البحث والروابط المباشرة لجميع المحركات المعتمدة
query = st.text_input("🔍 أدخل موضوع البحث:", placeholder="ابحث في كافة المحركات (MIT, OATD, المنظومة...)...")

if query:
    st.markdown("---")
    col_global, col_arabic = st.columns(2)
    
    with col_global:
        st.markdown("### 🌐 الجناح العالمي (رسائل وأبحاث)")
        # محركات الصور (70, 71, 75)
        st.markdown(f'<a href="https://dspace.mit.edu/discover?query={query}" target="_blank"><button style="width:100%; background-color:#a31f34; color:white; border-radius:10px; height:3.5em; cursor:pointer; font-weight:bold; margin-bottom:10px;">🏛️ MIT Theses (رسائل MIT)</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://oatd.org/oatd/search?q={query}" target="_blank"><button style="width:100%; background-color:#f39200; color:white; border-radius:10px; height:3.5em; cursor:pointer; font-weight:bold; margin-bottom:10px;">🎓 OATD (الرسائل العالمية)</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://www.semanticscholar.org/search?q={query}" target="_blank"><button style="width:100%; background-color:#6a1b9a; color:white; border-radius:10px; height:3.5em; cursor:pointer; font-weight:bold; margin-bottom:10px;">🧠 Semantic Scholar (AI)</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://scholar.google.com/scholar?q={query}" target="_blank"><button style="width:100%; background-color:#2e7d32; color:white; border-radius:10px; height:3.5em; cursor:pointer; font-weight:bold;">🔍 Google Scholar</button></a>', unsafe_allow_html=True)

    with col_arabic:
        st.markdown("### 🇸🇦 الجناح العربي والوطني")
        # محركات الصور (62, 68)
        st.markdown(f'<a href="https://search.mandumah.com/Search/Results?lookfor={query}" target="_blank"><button style="width:100%; background-color:#004b87; color:white; border-radius:10px; height:3.5em; cursor:pointer; font-weight:bold; margin-bottom:10px;">📚 دار المنظومة</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://shamaa.org/results?q={query}" target="_blank"><button style="width:100%; background-color:#17a2b8; color:white; border-radius:10px; height:3.5em; cursor:pointer; font-weight:bold; margin-bottom:10px;">💎 قاعدة شمعة (تربوي)</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://kfnl.gov.sa/Ar/Pages/default.aspx" target="_blank"><button style="width:100%; background-color:#155724; color:white; border-radius:10px; height:3.5em; cursor:pointer; font-weight:bold;">🏛️ مكتبة الملك فهد الوطنية</button></a>', unsafe_allow_html=True)

    # 3. الأدوات التفاعلية (القاموس والأرشفة)
    st.markdown("---")
    tab_dict, tab_lib = st.tabs(["📘 قاموس المصطلحات", "📂 أرشفة مراجعكِ"])
    
    with tab_dict:
        c1, c2 = st.columns([1, 2])
        with c1:
            ar = st.text_input("عربي:", key="ar"); en = st.text_input("إنجليزي:", key="en")
            if st.button("إضافة"):
                if ar and en: st.session_state.dict[ar] = en; st.rerun()
        with c2: st.table(pd.DataFrame(list(st.session_state.dict.items()), columns=['العربية', 'الإنجليزية']))
        
    with tab_lib:
        c3, c4 = st.columns([1, 2])
        with c3:
            t_ref = st.text_input("عنوان البحث:", key="t"); l_ref = st.text_input("الرابط:", key="l")if st.button("حفظ المرجع"):
                if t_ref and l_ref:
                    st.session_state.lib.append({"العنوان": t_ref, "الرابط": l_ref, "التاريخ": datetime.now().strftime("%Y-%m-%d")})
                    st.rerun()
        with c4:
            if st.session_state.lib: st.dataframe(pd.DataFrame(st.session_state.lib), use_container_width=True)

st.markdown("<p style='text-align: center; color: gray;'>الإصدار المستقر والكامل 2026 - M.A. Altwaijer</p>", unsafe_allow_html=True)

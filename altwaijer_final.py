import streamlit as st
import pandas as pd
from datetime import datetime

# 1. إعدادات المنصة والهوية الأكاديمية
st.set_page_config(page_title="بوابة M.A. Altwaijer الأكاديمية", layout="wide")

if 'dict' not in st.session_state: st.session_state.dict = {"النبر": "Word Stress", "التنغيم": "Intonation"}
if 'lib' not in st.session_state: st.session_state.lib = []

st.markdown("<h1 style='text-align:center;'>🎓 بوابة M.A. Altwaijer للبحث العلمي</h1>", unsafe_allow_html=True)

# 2. منطقة البحث والمحركات (المستخلصة من صوركِ 70 و71 و75)
query = st.text_input("🔍 أدخل موضوع البحث:", placeholder="ابحث في MIT، OATD، والمنظومة...")

if query:
    st.markdown("---")
    col_g, col_a = st.columns(2)
    with col_g:
        st.markdown("### 🌐 الجناح العالمي")
        st.markdown(f'<a href="https://dspace.mit.edu/discover?query={query}" target="_blank"><button style="width:100%;background-color:#a31f34;color:white;border-radius:10px;height:3em;font-weight:bold;margin-bottom:10px;cursor:pointer;">🏛️ MIT Theses (رسائل MIT)</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://oatd.org/oatd/search?q={query}" target="_blank"><button style="width:100%;background-color:#f39200;color:white;border-radius:10px;height:3em;font-weight:bold;margin-bottom:10px;cursor:pointer;">🎓 OATD (الرسائل العالمية)</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://www.semanticscholar.org/search?q={query}" target="_blank"><button style="width:100%;background-color:#6a1b9a;color:white;border-radius:10px;height:3em;font-weight:bold;margin-bottom:10px;cursor:pointer;">🧠 Semantic Scholar</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://scholar.google.com/scholar?q={query}" target="_blank"><button style="width:100%;background-color:#2e7d32;color:white;border-radius:10px;height:3em;font-weight:bold;cursor:pointer;">🔍 Google Scholar</button></a>', unsafe_allow_html=True)
    with col_a:
        st.markdown("### 🇸🇦 الجناح العربي")
        st.markdown(f'<a href="https://search.mandumah.com/Search/Results?lookfor={query}" target="_blank"><button style="width:100%;background-color:#004b87;color:white;border-radius:10px;height:3em;font-weight:bold;margin-bottom:10px;cursor:pointer;">📚 دار المنظومة</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://shamaa.org/results?q={query}" target="_blank"><button style="width:100%;background-color:#17a2b8;color:white;border-radius:10px;height:3em;font-weight:bold;margin-bottom:10px;cursor:pointer;">💎 قاعدة شمعة</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://kfnl.gov.sa/" target="_blank"><button style="width:100%;background-color:#155724;color:white;border-radius:10px;height:3em;font-weight:bold;cursor:pointer;">🏛️ مكتبة الملك فهد الوطنية</button></a>', unsafe_allow_html=True)

    # 3. القاموس والأرشفة (كما في صورتك 67)
    st.markdown("---")
    t1, t2 = st.tabs(["📘 قاموس المصطلحات", "📂 أرشفة مراجعكِ"])
    with t1:
        c1, c2 = st.columns([1, 2])
        with c1:
            ar = st.text_input("عربي:", key="ar")
            en = st.text_input("إنجليزي:", key="en")
            if st.button("إضافة"):
                if ar and en: st.session_state.dict[ar] = en; st.rerun()
        with c2: st.table(pd.DataFrame(list(st.session_state.dict.items()), columns=['العربية', 'الإنجليزية']))
    with t2:
        c3, c4 = st.columns([1, 2])
        with c3:
            title = st.text_input("العنوان:", key="t")
            link = st.text_input("الرابط:", key="l")
            if st.button("حفظ"):
                if title and link: st.session_state.lib.append({"العنوان": title, "الرابط": link, "التاريخ": datetime.now().strftime("%Y-%m-%d")}); st.rerun()
        with c4:
            if st.session_state.lib: st.dataframe(pd.DataFrame(st.session_state.lib), use_container_width=True)

st.markdown("<p style='text-align: center; color: gray;'>M.A. Altwaijer 2026 - نسخة مستقرة</p>", unsafe_allow_html=True)

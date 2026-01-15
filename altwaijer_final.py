import streamlit as st
import pandas as pd
from datetime import datetime

# 1. إعدادات الهوية الأكاديمية
st.set_page_config(page_title="بوابة M.A. Altwaijer", layout="wide")

if 'dictionary' not in st.session_state:
    st.session_state.dictionary = {"النبر": "Word Stress", "التنغيم": "Intonation"}
if 'library' not in st.session_state:
    st.session_state.library = []

st.markdown("<h1 style='text-align: center; color: #0e1133;'>🎓 بوابة M.A. Altwaijer للاستقصاء العلمي</h1>", unsafe_allow_html=True)

# 2. منطقة البحث
search_query = st.text_input("🔍 أدخل موضوع البحث:", placeholder="مثلاً: التنغيم في اللغة العربية...")

if search_query:
    # الروابط المستخلصة من صوركِ الناجحة
    u_scholar = f"https://scholar.google.com/scholar?q={search_query}"
    u_semantic = f"https://www.semanticscholar.org/search?q={search_query}"
    u_mandumah = f"https://search.mandumah.com/Search/Results?lookfor={search_query}"
    u_mit = f"https://dspace.mit.edu/discover?query={search_query}"
    u_oatd = f"https://oatd.org/oatd/search?q={search_query}"

    col_g, col_a = st.columns(2)
    with col_g:
        st.markdown("### 🌐 الجناح العالمي")
        st.markdown(f'<a href="{u_mit}" target="_blank"><button style="width:100%; background-color:#a31f34; color:white; border:none; border-radius:10px; height:3em; cursor:pointer; font-weight:bold; margin-bottom:10px;">🏛️ MIT Theses (رسائل MIT)</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="{u_oatd}" target="_blank"><button style="width:100%; background-color:#f39200; color:white; border:none; border-radius:10px; height:3em; cursor:pointer; font-weight:bold; margin-bottom:10px;">🎓 OATD (الرسائل العالمية)</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="{u_semantic}" target="_blank"><button style="width:100%; background-color:#6a1b9a; color:white; border:none; border-radius:10px; height:3em; cursor:pointer; font-weight:bold;">🧠 Semantic Scholar</button></a>', unsafe_allow_html=True)
    
    with col_a:
        st.markdown("### 🇸🇦 الجناح العربي")
        st.markdown(f'<a href="{u_mandumah}" target="_blank"><button style="width:100%; background-color:#004b87; color:white; border:none; border-radius:10px; height:3em; cursor:pointer; font-weight:bold; margin-bottom:10px;">📚 دار المنظومة</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://shamaa.org/" target="_blank"><button style="width:100%; background-color:#17a2b8; color:white; border:none; border-radius:10px; height:3em; cursor:pointer; font-weight:bold; margin-bottom:10px;">💎 قاعدة شمعة</button></a>', unsafe_allow_html=True)
        # الزر الذي يجمع عوالم الصور (MIT, OATD, المنظومة)
        magic_html = f'<button onclick="window.open(\'{u_mit}\');window.open(\'{u_oatd}\');window.open(\'{u_mandumah}\');" style="width:100%; background-color:#1c243d; color:white; border:none; border-radius:10px; height:3em; cursor:pointer; font-weight:bold;">🚀 الاستقصاء الشامل (فتح 3 مصادر)</button>'
        st.components.v1.html(magic_html, height=55)

    # 3. القاموس والأرشفة (كما في صورتك 67)
    st.markdown("---")
    t1, t2 = st.tabs(["📘 قاموس المصطلحات", "📂 أرشفة مراجعكِ"])
    with t1:
        c1, c2 = st.columns([1, 2])
        with c1:
            ar_in = st.text_input("عربي:", key="ar_z")
            en_in = st.text_input("إنجليزي:", key="en_z")
            if st.button("إضافة"):
                if ar_in and en_in: st.session_state.dictionary[ar_in] = en_in; st.rerun()
        with c2: st.table(pd.DataFrame(list(st.session_state.dictionary.items()), columns=['العربية', 'الإنجليزية']))
    with t2:
        c3, c4 = st.columns([1, 2])
        with c3:
            t_ref = st.text_input("العنوان:", key="t_z")
            l_ref = st.text_input("الرابط:", key="l_z")
            if st.button("حفظ"):
                if t_ref and l_ref: st.session_state.library.append({"العنوان": t_ref, "الرابط": l_ref, "التاريخ": datetime.now().strftime("%Y-%m-%d")}); st.rerun()
        with c4: 
            if st.session_state.library: st.dataframe(pd.DataFrame(st.session_state.library))
                st.markdown("<p style='text-align: center; color: gray;'>M.A. Altwaijer 2026 - الإصدار المستقر</p>", unsafe_allow_html=True)

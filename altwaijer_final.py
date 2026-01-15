import streamlit as st
import pandas as pd
from datetime import datetime

# 1. إعدادات البوابة الأكاديمية
st.set_page_config(page_title="بوابة M.A. Altwaijer الأكاديمية", layout="wide")

if 'dictionary' not in st.session_state:
    st.session_state.dictionary = {"النبر": "Word Stress", "التنغيم": "Intonation"}
if 'library' not in st.session_state:
    st.session_state.library = []

st.markdown("<h1 style='text-align: center; color: #0e1133;'>🎓 بوابة M.A. Altwaijer للأبحاث والاستقصاء العلمي</h1>", unsafe_allow_html=True)

# 2. منطقة البحث
search_query = st.text_input("🔍 أدخل موضوع البحث:", placeholder="ابحث في MIT و OATD وكافة المحركات...")

if search_query:
    st.markdown("---")
    
    # الروابط المجهزة (كما في صوركِ 70 و 71)
    u_scholar = f"https://scholar.google.com/scholar?q={search_query}"
    u_semantic = f"https://www.semanticscholar.org/search?q={search_query}"
    u_mandumah = f"https://search.mandumah.com/Search/Results?lookfor={search_query}"
    u_mit = f"https://dspace.mit.edu/discover?query={search_query}"
    u_oatd = f"https://oatd.org/oatd/search?q={search_query}"

    col_global, col_arabic = st.columns(2)
    
    with col_global:
        st.markdown("### 🌐 الجناح العالمي (المستودعات المفتوحة)")
        st.markdown(f'<a href="{u_mit}" target="_blank"><button style="width:100%; background-color:#a31f34; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer; font-weight:bold; margin-bottom:10px;">🏛️ MIT Theses (رسائل معهد ماساتشوستس)</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="{u_oatd}" target="_blank"><button style="width:100%; background-color:#f39200; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer; font-weight:bold; margin-bottom:10px;">🎓 OATD (الرسائل العالمية المفتوحة)</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="{u_semantic}" target="_blank"><button style="width:100%; background-color:#6a1b9a; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer; font-weight:bold;">🧠 Semantic Scholar (AI)</button></a>', unsafe_allow_html=True)

    with col_arabic:
        st.markdown("### 🇸🇦 الجناح العربي")
        st.markdown(f'<a href="{u_mandumah}" target="_blank"><button style="width:100%; background-color:#004b87; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer; font-weight:bold; margin-bottom:10px;">📚 دار المنظومة</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://shamaa.org/" target="_blank"><button style="width:100%; background-color:#17a2b8; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer; font-weight:bold; margin-bottom:10px;">💎 قاعدة شمعة</button></a>', unsafe_allow_html=True)
        
        # الزر المصحح للاستقصاء (يفتح المصادر العالمية والعربية معاً)
        magic_button = f"""
        <button onclick="window.open('{u_mit}'); window.open('{u_oatd}'); window.open('{u_mandumah}');" 
        style="width:100%; background-color:#1c243d; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer; font-weight:bold;">
            📂 تشغيل الاستقصاء الشامل (MIT & OATD & المنظومة)
        </button>
        """
        st.components.v1.html(magic_button, height=60)

    # 3. الأدوات التفاعلية (القاموس والأرشفة كما في صورتك 67)
    st.markdown("---")
    tab_dict, tab_lib = st.tabs(["📘 قاموس المصطلحات الأكاديمية", "📂 خزانة أرشفة المراجع"])
    
    with tab_dict:
        c1, c2 = st.columns([1, 2])
        with c1:
            n_ar = st.text_input("عربي:", key="ar")
            n_en = st.text_input("إنجليزي:", key="en")
            if st.button("حفظ"):
                if n_ar and n_en: st.session_state.dictionary[n_ar] = n_en; st.rerun()
        with c2: st.table(pd.DataFrame(list(st.session_state.dictionary.items()), columns=['العربية', 'الإنجليزية']))
           with tab_lib:
        c3, c4 = st.columns([1, 2])
        with c3:
            t_ref = st.text_input("عنوان البحث:", key="t")
            l_ref = st.text_input("الرابط:", key="l")
            if st.button("أرشفة المرجع"):
                if t_ref and l_ref:
                    st.session_state.library.append({"العنوان": t_ref, "الرابط": l_ref, "تاريخ الأرشفة": datetime.now().strftime("%Y-%m-%d")})
                    st.rerun()
        with c4:
            if st.session_state.library: st.dataframe(pd.DataFrame(st.session_state.library), use_container_width=True)

st.markdown("<p style='text-align: center; color: gray;'>M.A. Altwaijer 2026 - بوابة البحث والاستقصاء الشاملة</p>", unsafe_allow_html=True) 

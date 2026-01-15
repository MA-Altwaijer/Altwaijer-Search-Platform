import streamlit as st
import pandas as pd
from datetime import datetime

# 1. إعدادات المنصة الكلاسيكية المعتمدة 2026
st.set_page_config(page_title="بوابة M.A. Altwaijer الأكاديمية", layout="wide")

# إدارة البيانات (قاموس ومكتبة)
if 'dictionary' not in st.session_state: st.session_state.dictionary = {"النبر": "Word Stress", "التنغيم": "Intonation"}
if 'library' not in st.session_state: st.session_state.library = []

st.markdown("<h1 style='text-align: center; color: #0e1133;'>🎓 بوابة M.A. Altwaijer للبحث الأكاديمي</h1>", unsafe_allow_html=True)

# 2. منطقة البحث المركزية
search_query = st.text_input("🔍 أدخل موضوع البحث:", placeholder="اكتب هنا موضوعك للبحث...")

if search_query:
    st.markdown("---")
    # الروابط المجهزة
    u_scholar = f"https://scholar.google.com/scholar?q={search_query}"
    u_semantic = f"https://www.semanticscholar.org/search?q={search_query}"
    u_mandumah = f"https://search.mandumah.com/Search/Results?lookfor={search_query}"
    u_shamaa = f"https://shamaa.org/results?q={search_query}"
    
    # توزيع الأجنحة الكلاسيكي (عربي / عالمي)
    col_global, col_arabic = st.columns(2)
    
    with col_global:
        st.markdown("### 🌐 الجناح العالمي")
        st.markdown(f'<a href="{u_semantic}" target="_blank"><button style="width:100%; background-color:#6a1b9a; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer; margin-bottom:10px; font-weight:bold;">🧠 Semantic Scholar</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="{u_scholar}" target="_blank"><button style="width:100%; background-color:#2e7d32; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer; margin-bottom:10px; font-weight:bold;">🔍 Google Scholar</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://oatd.org/" target="_blank"><button style="width:100%; background-color:#f39200; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer; font-weight:bold;">🎓 OATD (الرسائل العالمية)</button></a>', unsafe_allow_html=True)

    with col_arabic:
        st.markdown("### 🇸🇦 الجناح العربي")
        st.markdown(f'<a href="{u_mandumah}" target="_blank"><button style="width:100%; background-color:#004b87; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer; margin-bottom:10px; font-weight:bold;">📚 دار المنظومة</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="{u_shamaa}" target="_blank"><button style="width:100%; background-color:#17a2b8; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer; margin-bottom:10px; font-weight:bold;">💎 قاعدة شمعة</button></a>', unsafe_allow_html=True)
        st.markdown(f'<button onclick="window.open(\'{u_scholar}\',\'_blank\');window.open(\'{u_semantic}\',\'_blank\');window.open(\'{u_mandumah}\',\'_blank\');" style="width:100%; background-color:#1c243d; color:white; border:none; border-radius:10px; height:3.5em; cursor:pointer; font-weight:bold;">📂 الاستقصاء الموحد (فتح 3 محركات)</button>', unsafe_allow_html=True)

    # 3. الأدوات الجانبية (تبويبات منظمة)
    st.markdown("---")
    t1, t2 = st.tabs(["📘 قاموس المصطلحات", "📂 أرشفة مراجعكِ"])
    with t1:
        c1, c2 = st.columns([1, 2])
        with c1:
            n_ar = st.text_input("عربي:")
            n_en = st.text_input("إنجليزي:")
            if st.button("إضافة للقاموس"):
                st.session_state.dictionary[n_ar] = n_en
                st.rerun()
        with c2: st.table(pd.DataFrame(list(st.session_state.dictionary.items()), columns=['العربية', 'الإنجليزية']))
    with t2:
        c3, c4 = st.columns([1, 2])
        with c3:
            t_ref = st.text_input("عنوان المرجع:")
            l_ref = st.text_input("رابط المرجع:")
            if st.button("أرشفة الآن"):
                st.session_state.library.append({"العنوان": t_ref, "الرابط": l_ref, "التاريخ": datetime.now().strftime("%Y-%m-%d")})
                st.rerun()
        with c4: st.dataframe(pd.DataFrame(st.session_state.library), use_container_width=True)st.markdown("<p style='text-align: center; color: gray;'>M.A. Altwaijer 2026 - الإصدار المستقر</p>", unsafe_allow_html=True)

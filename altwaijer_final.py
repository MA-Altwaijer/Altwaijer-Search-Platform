import streamlit as st
import pandas as pd
from datetime import datetime

# 1. إعدادات المنصة
st.set_page_config(page_title="بوابة M.A. Altwaijer الأكاديمية", layout="wide")
if 'dict' not in st.session_state: st.session_state.dict = {"النبر": "Word Stress", "التنغيم": "Intonation"}
if 'lib' not in st.session_state: st.session_state.lib = []

st.markdown("<h1 style='text-align:center;'>🎓 بوابة M.A. Altwaijer للبحث العلمي الشامل</h1>", unsafe_allow_html=True)

# 2. منطقة البحث والروابط
q = st.text_input("🔍 موضوع البحث:", placeholder="ابحث في قوقل سكولر، سيمنتك، توبقال، MIT...")

if q:
    st.markdown("---")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 🌐 الجناح العالمي (الذكاء الاصطناعي والرسائل)")
        st.markdown(f'<a href="https://scholar.google.com/scholar?q={q}" target="_blank"><button style="width:100%;background:#2e7d32;color:white;border-radius:10px;height:2.8em;font-weight:bold;margin-bottom:10px;cursor:pointer;">🔍 Google Scholar (الباحث العلمي)</button></a>', unsafe_allow_html=True)
        # إعادة محرك Semantic Scholar
        st.markdown(f'<a href="https://www.semanticscholar.org/search?q={q}" target="_blank"><button style="width:100%;background:#6a1b9a;color:white;border-radius:10px;height:2.8em;font-weight:bold;margin-bottom:10px;cursor:pointer;">🧠 Semantic Scholar (سيمنتك بالذكاء الاصطناعي)</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://dspace.mit.edu/discover?query={q}" target="_blank"><button style="width:100%;background:#a31f34;color:white;border-radius:10px;height:2.8em;font-weight:bold;margin-bottom:10px;cursor:pointer;">🏛️ MIT Theses (رسائل MIT)</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://oatd.org/oatd/search?q={q}" target="_blank"><button style="width:100%;background:#f39200;color:white;border-radius:10px;height:2.8em;font-weight:bold;cursor:pointer;">🎓 OATD (الرسائل العالمية المفتوحة)</button></a>', unsafe_allow_html=True)

    with c2:
        st.markdown("### 🏛️ الجناح العربي والإقليمي")
        st.markdown(f'<a href="https://toubkal.imist.ma/browse?type=title&query={q}" target="_blank"><button style="width:100%;background:#c1272d;color:white;border-radius:10px;height:2.8em;font-weight:bold;margin-bottom:10px;cursor:pointer;">🇲🇦 مستودع توبقال (المغرب)</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://www.iasj.net/iasj/search?query={q}" target="_blank"><button style="width:100%;background:#007a33;color:white;border-radius:10px;height:2.8em;font-weight:bold;margin-bottom:10px;cursor:pointer;">🇮🇶 المجلات الأكاديمية (العراق)</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://search.mandumah.com/Search/Results?lookfor={q}" target="_blank"><button style="width:100%;background:#004b87;color:white;border-radius:10px;height:2.8em;font-weight:bold;margin-bottom:10px;cursor:pointer;">📚 دار المنظومة (الشامل)</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://shamaa.org/results?q={q}" target="_blank"><button style="width:100%;background:#17a2b8;color:white;border-radius:10px;height:2.8em;font-weight:bold;cursor:pointer;">💎 قاعدة شمعة (بيروت)</button></a>', unsafe_allow_html=True)

    # 3. الأدوات التفاعلية
    st.markdown("---")
    t1, t2 = st.tabs(["📘 قاموس المصطلحات", "📂 أرشفة مراجعكِ"])
    with t1:
        cl1, cl2 = st.columns([1, 2])
        with cl1:
            ar = st.text_input("عربي:", key="ar"); en = st.text_input("إنجليزي:", key="en")
            if st.button("إضافة"):
                if ar and en: st.session_state.dict[ar] = en; st.rerun()
        with cl2: st.table(pd.DataFrame(list(st.session_state.dict.items()), columns=['العربية', 'الإنجليزية']))
    with t2:
        cl3, cl4 = st.columns([1, 2])
        with cl3:
            ti = st.text_input("العنوان:", key="t"); li = st.text_input("الرابط:", key="l")

if st.button("حفظ المرجع"):
                if ti and li: st.session_state.lib.append({"العنوان": ti, "الرابط": li, "التاريخ": datetime.now().strftime("%Y-%m-%d")}); st.rerun()
        with cl4:
            if st.session_state.lib: st.dataframe(pd.DataFrame(st.session_state.lib), use_container_width=True)

st.markdown("<p style='text-align: center; color: gray;'>M.A. Altwaijer 2026 - الإصدار المستقر والكامل</p>", unsafe_allow_html=True)

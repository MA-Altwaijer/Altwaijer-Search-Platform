import streamlit as st
import pandas as pd
from datetime import datetime

# 1. إعدادات الواجهة والسمة الأكاديمية
st.set_page_config(page_title="بوابة M.A. Altwaijer الدولية", layout="wide")

if 'dict' not in st.session_state: st.session_state.dict = {"النبر": "Word Stress", "التنغيم": "Intonation"}
if 'lib' not in st.session_state: st.session_state.lib = []

st.markdown("<h1 style='text-align:center;'>🎓 بوابة M.A. Altwaijer للبحث والاستقصاء العلمي</h1>", unsafe_allow_html=True)

# 2. منطقة البحث المركزي
query = st.text_input("🔍 أدخل موضوع البحث (مثلاً: التنغيم، النبر، اللسانيات...):", placeholder="ابحث في المستودعات العالمية والعربية...")

if query:
    st.markdown("---")
    col_global, col_arabic = st.columns(2)
    
    with col_global:
        st.markdown("### 🌐 الجناح العالمي (رسائل وأبحاث)")
        st.markdown(f'<a href="https://dspace.mit.edu/discover?query={query}" target="_blank"><button style="width:100%;background-color:#a31f34;color:white;border-radius:10px;height:3em;font-weight:bold;margin-bottom:10px;cursor:pointer;">🏛️ MIT Theses (رسائل MIT)</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://oatd.org/oatd/search?q={query}" target="_blank"><button style="width:100%;background-color:#f39200;color:white;border-radius:10px;height:3em;font-weight:bold;margin-bottom:10px;cursor:pointer;">🎓 OATD (الرسائل العالمية)</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://www.semanticscholar.org/search?q={query}" target="_blank"><button style="width:100%;background-color:#6a1b9a;color:white;border-radius:10px;height:3em;font-weight:bold;cursor:pointer;">🧠 Semantic Scholar (AI)</button></a>', unsafe_allow_html=True)

    with col_arabic:
        st.markdown("### 🏛️ مستودعات (المغرب، الشام، الرافدين، ليبيا)")
        # المغرب العربي (توبقال)
        st.markdown(f'<a href="https://toubkal.imist.ma/browse?type=title&query={query}" target="_blank"><button style="width:100%;background-color:#c1272d;color:white;border-radius:10px;height:3em;font-weight:bold;margin-bottom:10px;cursor:pointer;">🇲🇦 مستودع توبقال (المغرب)</button></a>', unsafe_allow_html=True)
        # العراق (IASJ)
        st.markdown(f'<a href="https://www.iasj.net/iasj/search?query={query}" target="_blank"><button style="width:100%;background-color:#007a33;color:white;border-radius:10px;height:3em;font-weight:bold;margin-bottom:10px;cursor:pointer;">🇮🇶 المجلات الأكاديمية (العراق)</button></a>', unsafe_allow_html=True)
        # دار المنظومة (تغطي سوريا، لبنان، وليبيا)
        st.markdown(f'<a href="https://search.mandumah.com/Search/Results?lookfor={query}" target="_blank"><button style="width:100%;background-color:#004b87;color:white;border-radius:10px;height:3em;font-weight:bold;margin-bottom:10px;cursor:pointer;">📚 دار المنظومة (الشام وليبيا)</button></a>', unsafe_allow_html=True)
        # قاعدة شمعة (لبنان والأردن)
        st.markdown(f'<a href="https://shamaa.org/results?q={query}" target="_blank"><button style="width:100%;background-color:#17a2b8;color:white;border-radius:10px;height:3em;font-weight:bold;cursor:pointer;">💎 قاعدة شمعة (الإنتاج اللبناني)</button></a>', unsafe_allow_html=True)

    # 3. القاموس والأرشفة الذكية
    st.markdown("---")
    t1, t2 = st.tabs(["📘 قاموس المصطلحات الأكاديمية", "📂 خزانة أرشفة المراجع"])
    with t1:
        c1, c2 = st.columns([1, 2])
        with c1:
            ar = st.text_input("عربي:", key="ar"); en = st.text_input("إنجليزي:", key="en")
            if st.button("إضافة"):
                if ar and en: st.session_state.dict[ar] = en; st.rerun()
        with c2: st.table(pd.DataFrame(list(st.session_state.dict.items()), columns=['العربية', 'الإنجليزية']))
    with t2:
        c3, c4 = st.columns([1, 2])
        with c3:
            title = st.text_input("عنوان البحث:", key="t"); link = st.text_input("الرابط:", key="l")if st.button("أرشفة الآن"):
                if title and link: st.session_state.lib.append({"العنوان": title, "الرابط": link, "التاريخ": datetime.now().strftime("%Y-%m-%d")}); st.rerun()
        with c4:
            if st.session_state.lib: st.dataframe(pd.DataFrame(st.session_state.lib), use_container_width=True)

st.markdown("<p
style='text-align: center; 
color: gray;'>M.A. Altwaijer
2026 - الإصدار الأكاديمي الشامل</p>", 
unsafe_allow_html=True)

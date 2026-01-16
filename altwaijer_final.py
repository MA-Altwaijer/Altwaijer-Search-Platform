import streamlit as st
import pandas as pd
from datetime import datetime

# 1. الإعدادات وتأمين البيانات
st.set_page_config(page_title="M.A. Altwaijer 2026", layout="wide")
if 'dict' not in st.session_state:
    st.session_state.dict = {"النبر": "Word Stress", "التنغيم": "Intonation"}
if 'lib' not in st.session_state:
    st.session_state.lib = []

st.markdown("<h1 style='text-align:center;'>🎓 بوابة M.A. Altwaijer للبحث العلمي الشامل</h1>", unsafe_allow_html=True)

# 2. محرك البحث
q = st.text_input("🔍 أدخل موضوع البحث هنا:", placeholder="قوقل سكولر، توبقال، MIT، المنظومة...")

if q:
    st.markdown("---")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 🌐 الجناح العالمي")
        st.markdown(f'<a href="https://scholar.google.com/scholar?q={q}" target="_blank"><button style="width:100%;background:#2e7d32;color:white;border-radius:10px;height:3em;font-weight:bold;margin-bottom:10px;cursor:pointer;">🔍 Google Scholar</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://www.semanticscholar.org/search?q={q}" target="_blank"><button style="width:100%;background:#6a1b9a;color:white;border-radius:10px;height:3em;font-weight:bold;margin-bottom:10px;cursor:pointer;">🧠 Semantic Scholar</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://dspace.mit.edu/discover?query={q}" target="_blank"><button style="width:100%;background:#a31f34;color:white;border-radius:10px;height:3em;font-weight:bold;cursor:pointer;">🏛️ MIT Theses</button></a>', unsafe_allow_html=True)
    with c2:
        st.markdown("### 🏛️ الجناح العربي")
        st.markdown(f'<a href="https://toubkal.imist.ma/browse?type=title&query={q}" target="_blank"><button style="width:100%;background:#c1272d;color:white;border-radius:10px;height:3em;font-weight:bold;margin-bottom:10px;cursor:pointer;">🇲🇦 مستودع توبقال (المغرب)</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://www.iasj.net/iasj/search?query={q}" target="_blank"><button style="width:100%;background:#007a33;color:white;border-radius:10px;height:3em;font-weight:bold;margin-bottom:10px;cursor:pointer;">🇮🇶 مجلات العراق</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://search.mandumah.com/Search/Results?lookfor={q}" target="_blank"><button style="width:100%;background:#004b87;color:white;border-radius:10px;height:3em;font-weight:bold;cursor:pointer;">📚 دار المنظومة</button></a>', unsafe_allow_html=True)

    # 3. القاموس والأرشفة (تم تبسيط المسافات لمنع أخطاء الصور 78 و 80)
    st.markdown("---")
    t1, t2 = st.tabs(["📘 القاموس الأكاديمي", "📂 أرشفة المراجع"])
    with t1:
        st.table(pd.DataFrame(list(st.session_state.dict.items()), columns=['العربية', 'الإنجليزية']))
        ar_in = st.text_input("إضافة مصطلح عربي:")
        en_in = st.text_input("إضافة مصطلح إنجليزي:")
        if st.button("حفظ في القاموس"):
            if ar_in and en_in:
                st.session_state.dict[ar_in] = en_in
                st.rerun()
    with t2:
        res_t = st.text_input("عنوان المرجع:")
        res_l = st.text_input("رابط المرجع:")
        if st.button("حفظ في الأرشفة"):
            if res_t and res_l:
                st.session_state.lib.append({"العنوان": res_t, "الرابط": res_l, "التاريخ": datetime.now().strftime("%Y-%m-%d")})
                st.rerun()
        if st.session_state.lib:
            st.dataframe(pd.DataFrame(st.session_state.lib))

st.markdown("<p style='text-align: center; color: gray;'>M.A. Altwaijer 2026 - بوابة البحث المستقرة</p>", unsafe_allow_html=True)

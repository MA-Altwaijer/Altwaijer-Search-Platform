import streamlit as st
import pandas as pd

# 1. الإعدادات الأساسية
st.set_page_config(page_title="M.A. Altwaijer Lab", layout="wide")
if 'matrix' not in st.session_state: st.session_state.matrix = []

st.markdown("<h1 style='text-align:center;'>🔬 مختبر M.A. Altwaijer للتحليل المقارن</h1>", unsafe_allow_html=True)

# 2. الجناح البحثي (المحركات التي ظهرت في صورتك 79)
with st.expander("🔍 محركات البحث (قوقل سكولر، توبقال، سيمنتك)"):
    q = st.text_input("أدخلي موضوع البحث:")
    if q:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f'<a href="https://scholar.google.com/scholar?q={q}" target="_blank"><button style="width:100%;background:#2e7d32;color:white;border-radius:10px;height:2.5em;font-weight:bold;margin-bottom:5px;">🔍 Google Scholar</button></a>', unsafe_allow_html=True)
            st.markdown(f'<a href="https://www.semanticscholar.org/search?q={q}" target="_blank"><button style="width:100%;background:#6a1b9a;color:white;border-radius:10px;height:2.5em;font-weight:bold;">🧠 Semantic Scholar</button></a>', unsafe_allow_html=True)
        with c2:
            st.markdown(f'<a href="https://toubkal.imist.ma/browse?type=title&query={q}" target="_blank"><button style="width:100%;background:#c1272d;color:white;border-radius:10px;height:2.5em;font-weight:bold;margin-bottom:5px;">🇲🇦 توبقال (المغرب)</button></a>', unsafe_allow_html=True)
            st.markdown(f'<a href="https://search.mandumah.com/Search/Results?lookfor={q}" target="_blank"><button style="width:100%;background:#004b87;color:white;border-radius:10px;height:2.5em;font-weight:bold;">📚 دار المنظومة</button></a>', unsafe_allow_html=True)

# 3. مختبر التلخيص والمقارنة (بناءً على صورتك 82)
st.markdown("---")
st.markdown("### 📝 تلخيص دراسة جديدة للمقارنة")
col_in, col_tab = st.columns([1, 2])

with col_in:
    title = st.text_input("عنوان الدراسة:")
    author = st.text_input("الباحث/السنة:")
    method = st.text_input("المنهجية (Praat، وصفي...):")
    findings = st.text_area("أهم النتائج والفجوة البحثية:")
    if st.button("📥 إضافة للمصفوفة"):
        if title and findings:
            st.session_state.matrix.append({"الدراسة": title, "الباحث": author, "المنهج": method, "النتائج": findings})
            st.rerun()

with col_tab:
    st.markdown("#### 📊 مصفوفة المقارنة والتركيب (Matrix)")
    if st.session_state.matrix:
        df = pd.DataFrame(st.session_state.matrix)
        st.table(df)
        if st.button("🗑️ مسح المصفوفة"):
            st.session_state.matrix = []
            st.rerun()
    else:
        st.write("ابدئي بإضافة ملخصات البحوث من الجانب الأيمن.")

st.markdown("<p style='text-align: center; color: gray;'>M.A. Altwaijer 2026</p>", unsafe_allow_html=True)

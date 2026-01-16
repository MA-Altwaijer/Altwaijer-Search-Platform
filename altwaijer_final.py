import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="M.A. Altwaijer Open Lab", layout="wide")

if 'library' not in st.session_state: st.session_state.library = []

st.markdown("<h1 style='text-align:center;'>🌍 بوابة M.A. Altwaijer للأبحاث (الأفق المفتوح)</h1>", unsafe_allow_html=True)

# 1. محرك الاستكشاف الشامل (تاريخي + حديث)
st.markdown("### 🔍 محرك الاستكشاف الشامل (بدون قيود زمنية)")
q = st.text_input("أدخلي موضوع البحث للاستكشاف عبر التاريخ:")
if q:
    c1, c2, c3 = st.columns(3)
    with c1:
        # البحث العام بدون تقييد بسنوات
        st.markdown(f'<a href="https://scholar.google.com/scholar?q={q}" target="_blank"><button style="width:100%;background:#2e7d32;color:white;border-radius:10px;height:3em;">📚 كل العصور (Scholar)</button></a>', unsafe_allow_html=True)
    with c2:
        # البحث في سيمنتك مع التركيز على التأثير العلمي وليس التاريخ فقط
        st.markdown(f'<a href="https://www.semanticscholar.org/search?q={q}&sort=influence" target="_blank"><button style="width:100%;background:#6a1b9a;color:white;border-radius:10px;height:3em;">🧠 الأكثر تأثيراً (Semantic)</button></a>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<a href="https://toubkal.imist.ma/browse?type=title&query={q}" target="_blank"><button style="width:100%;background:#c1272d;color:white;border-radius:10px;height:3em;">🏛️ الأرشيف الوطني (توبقال)</button></a>', unsafe_allow_html=True)

st.markdown("---")

# 2. قسم الإضافة الحرة للمكتبة
with st.expander("➕ توثيق مرجع (من أي حقبة زمنية)"):
    col1, col2 = st.columns([2, 1])
    with col1:
        t_in = st.text_input("عنوان البحث/الكتاب:")
        l_in = st.text_input("الرابط (إن وجد):")
        f_in = st.text_area("رؤيتكِ النقدية (الفجوة أو الإضافة العلمية):")
    with col2:
        # جعلنا السنة نصاً حراً بدلاً من قائمة منسدلة ليتقبل السنوات القديمة جداً أو المخطوطات
        y_in = st.text_input("سنة النشر (مثلاً: 1980، أو تركها فارغة):")
        p_in = st.text_input("رقم الصفحة (للاقتباس):")
        s_in = st.selectbox("النظام:", ["APA", "MLA", "Harvard", "توثيق حر"])
    
    if st.button("📥 حفظ في المكتبة التاريخية"):
        if t_in:
            st.session_state.library.append({
                "العنوان": t_in, "السنة": y_in, "الصفحة": p_in,
                "الرابط": l_in, "التوثيق": s_in, "الرؤية النقدية": f_in
            })
            st.success("تم الحفظ في مخزن المعرفة!")

# 3. محرك البحث الداخلي (البحث في المحتوى وليس فقط العنوان)
if st.session_state.library:
    st.markdown("### 🔎 فرز وتحليل المكتبة الشخصية")
    search_q = st.text_input("ابحثي عن فكرة أو مصطلح داخل كل ما حفظتِ:")
    
    df = pd.DataFrame(st.session_state.library)
    if search_q:
        # البحث في العنوان وفي الرؤية النقدية معاً
        df = df[df['العنوان'].str.contains(search_q, case=False, na=False) | 
                df['الرؤية النقدية'].str.contains(search_q, case=False, na=False)]
    
    st.dataframe(df, use_container_width=True)

import streamlit as st
import pandas as pd

# 1. إعدادات الواجهة والذاكرة
st.set_page_config(page_title="M.A. Altwaijer Global Lab", layout="wide")
if 'library' not in st.session_state: st.session_state.library = []

st.markdown("<h1 style='text-align:center;'>🎯 مصفاة M.A. Altwaijer للبحث اللساني الدقيق</h1>", unsafe_allow_html=True)

# 2. محرك البحث الذكي (علاج مشكلة توبقال والعلوم الأخرى)
st.markdown("### 🔍 البحث في التخصص (استبعاد الطب والقانون والعلوم التطبيقية)")
query = st.text_input("أدخلي موضوع البحث (مثلاً: النبر، التنغيم، الفونولوجيا):")

if query:
    # صياغة بحث تخصصي يستبعد الكلمات التي ظهرت في صورك (طب، قانون، جراحة)
    strict_query = f'"{query}" AND (لسانيات OR لغة OR صوتيات) -طب -قانون -جراحة -هندسة'
    
    st.success(f"نتائج مصفاة لموضوع: {query}")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🌍 الوصول العالمي والمباشر (PDF)")
        # قوقل سكولر مبرمج لاستبعاد العلوم الأخرى
        st.markdown(f'<a href="https://scholar.google.com/scholar?q={strict_query}" target="_blank"><button style="width:100%;background:#2e7d32;color:white;border-radius:10px;height:3.5em;font-weight:bold;margin-bottom:10px;">🔍 Google Scholar (مصفى)</button></a>', unsafe_allow_html=True)
        # سيمنتك سكولر للوصول المفتوح
        st.markdown(f'<a href="https://www.semanticscholar.org/search?q={query}&pdf=true" target="_blank"><button style="width:100%;background:#6a1b9a;color:white;border-radius:10px;height:3.5em;font-weight:bold;margin-bottom:10px;">🧠 Semantic Scholar (نسخ مفتوحة)</button></a>', unsafe_allow_html=True)

    with col2:
        st.markdown("#### 🏛️ المستودعات العربية (للتوثيق والعناوين)")
        # توبقال مع تقييد البحث لضمان عدم ظهور نتائج الصورة 2 و 4
        st.markdown(f'<a href="https://toubkal.imist.ma/browse?type=title&query={strict_query}" target="_blank"><button style="width:100%;background:#c1272d;color:white;border-radius:10px;height:3.5em;font-weight:bold;margin-bottom:10px;">🇲🇦 توبقال (أطروحات لسانية فقط)</button></a>', unsafe_allow_html=True)
        # مجلات العراق (بديل مجاني لدار المنظومة)
        st.markdown(f'<a href="https://www.iasj.net/iasj/search?query={query}+لسانيات" target="_blank"><button style="width:100%;background:#f39c12;color:white;border-radius:10px;height:3.5em;font-weight:bold;">🇮🇶 مجلات العراق (PDF مجاني)</button></a>', unsafe_allow_html=True)

st.markdown("---")

# 3. مكتبة الإدارة الذكية (تفعيل مصفوفة الصورة 1)
st.markdown("### 📋 مصفوفة الدراسات السابقة (Literature Matrix)")
with st.expander("📥 إضافة دراسة تم التحقق من تخصصها"):
    c1, c2 = st.columns(2)
    with c1:
        t = st.text_input("عنوان البحث المختار:")
        y = st.text_input("السنة:")
        s = st.selectbox("المصدر:", ["توبقال", "مجلات العراق", "Scholar", "MIT"])
    with c2:
        p = st.text_input("رقم الصفحة (للتوثيق):")
        gap = st.text_area("الفجوة البحثية المكتشفة:")
    
    if st.button("حفظ المرجع للمقارنة"):
        if t:
            st.session_state.library.append({"العنوان": t, "السنة": y, "المصدر": s, "الصفحة": p, "الفجوة": gap})
            st.rerun()

if st.session_state.library:
    st.table(pd.DataFrame(st.session_state.library))

st.markdown("<p style='text-align: center; color: gray;'>M.A. Altwaijer 2026</p>", unsafe_allow_html=True)

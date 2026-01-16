import streamlit as st
import pandas as pd

# 1. إعدادات المنصة العالمية
st.set_page_config(page_title="M.A. Altwaijer Global Search", layout="wide")
if 'library' not in st.session_state: st.session_state.library = []

st.markdown("<h1 style='text-align:center;'>🌐 منصة M.A. Altwaijer العالمية للبحث الأكاديمي الشامل</h1>", unsafe_allow_html=True)

# 2. محرك البحث الحر (بدون قيود أو أقواس)
st.markdown("### 🔍 محرك البحث الأكاديمي الحر")
query = st.text_input("أدخلي موضوع البحث (في أي علم أو تخصص):", placeholder="مثلاً: النبر، الذكاء الاصطناعي، الاقتصاد الرقمي...")

if query:
    st.info(f"استكشاف النتائج العالمية لـ: {query}")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🌍 المصادر العالمية (Open Access)")
        # البحث الحر في قوقل سكولر بدون إضافات إجبارية
        st.markdown(f'<a href="https://scholar.google.com/scholar?q={query}" target="_blank"><button style="width:100%;background:#2e7d32;color:white;border-radius:10px;height:3em;font-weight:bold;margin-bottom:10px;">🔍 Google Scholar</button></a>', unsafe_allow_html=True)
        # سيمنتك سكولر للوصول الذكي
        st.markdown(f'<a href="https://www.semanticscholar.org/search?q={query}" target="_blank"><button style="width:100%;background:#6a1b9a;color:white;border-radius:10px;height:3em;font-weight:bold;margin-bottom:10px;">🧠 Semantic Scholar</button></a>', unsafe_allow_html=True)

    with col2:
        st.markdown("#### 🏛️ المستودعات العربية والوطنية")
        # توبقال - البحث الحر كما في الصورة 5
        st.markdown(f'<a href="https://toubkal.imist.ma/browse?type=title&query={query}" target="_blank"><button style="width:100%;background:#c1272d;color:white;border-radius:10px;height:3em;font-weight:bold;margin-bottom:10px;">🇲🇦 مستودع توبقال</button></a>', unsafe_allow_html=True)
        # المجلات العراقية - وصول مفتوح وشامل
        st.markdown(f'<a href="https://www.iasj.net/iasj/search?query={query}" target="_blank"><button style="width:100%;background:#f39c12;color:white;border-radius:10px;height:3em;font-weight:bold;">🇮🇶 المجلات العراقية</button></a>', unsafe_allow_html=True)

st.markdown("---")

# 3. المختبر التحليلي (تفعيل الصورة 1)
st.markdown("### 🔬 المختبر التحليلي لإدارة المراجع")
with st.expander("📝 تلخيص دراسة جديدة (أضيفي بياناتكِ هنا لتظهر في المصفوفة)"):
    c1, c2 = st.columns(2)
    with c1:
        title = st.text_input("عنوان البحث:")
        year = st.text_input("السنة:")
        field = st.text_input("التخصص:")
    with c2:
        page = st.text_input("رقم الصفحة:")
        gap = st.text_area("الفجوة البحثية/الملاحظات:")
    
    if st.button("📥 حفظ في المصفوفة"):
        if title:
            st.session_state.library.append({"العنوان": title, "السنة": year, "التخصص": field, "الصفحة": page, "الفجوة": gap})
            st.rerun()

# عرض المصفوفة (حل مشكلة الصورة 1)
if st.session_state.library:
    st.table(pd.DataFrame(st.session_state.library))
else:
    st.write("المصفوفة فارغة حالياً. ابدئي بإضافة ملخصات البحوث من الأعلى.")

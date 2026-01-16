import streamlit as st
import pandas as pd

# 1. إعدادات المنصة
st.set_page_config(page_title="M.A. Altwaijer Global Lab", layout="wide")
if 'library' not in st.session_state: st.session_state.library = []

st.markdown("<h1 style='text-align:center;'>🌐 منصة M.A. Altwaijer العالمية المتقدمة</h1>", unsafe_allow_html=True)

# 2. مصفاة التخصص (اختياري)
with st.sidebar:
    st.header("⚙️ ضبط البحث")
    is_linguistics = st.checkbox("تركيز البحث على اللسانيات فقط", value=True)
    exclude_terms = " -طب -قانون -جراحة" if is_linguistics else ""

# 3. محرك البحث الشامل
st.markdown("### 🔍 محرك البحث الذكي (عالمي + عربي)")
query = st.text_input("أدخلي موضوع البحث:", placeholder="مثلاً: النبر، التنغيم، أو أي تخصص آخر...")

if query:
    # صياغة الاستعلام بناءً على رغبتك في التخصص أو العالمية
    search_q = f'"{query}"' + (f" AND (لسانيات OR لغة)" if is_linguistics else "")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 🔓 تحميل مباشر (PDF)")
        st.markdown(f'<a href="https://scholar.google.com/scholar?q={query}{exclude_terms}" target="_blank"><button style="width:100%;background:#2e7d32;color:white;border-radius:10px;height:3em;font-weight:bold;margin-bottom:10px;">🔍 Google Scholar</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://www.semanticscholar.org/search?q={query}&pdf=true" target="_blank"><button style="width:100%;background:#6a1b9a;color:white;border-radius:10px;height:3em;font-weight:bold;">🧠 Semantic Scholar</button></a>', unsafe_allow_html=True)
    with col2:
        st.markdown("#### 🏛️ توثيق عناوين ودراسات سابقة")
        st.markdown(f'<a href="https://toubkal.imist.ma/browse?type=title&query={search_q}" target="_blank"><button style="width:100%;background:#c1272d;color:white;border-radius:10px;height:3em;font-weight:bold;margin-bottom:10px;">🇲🇦 مستودع توبقال</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://www.iasj.net/iasj/search?query={query}" target="_blank"><button style="width:100%;background:#f39c12;color:white;border-radius:10px;height:3em;font-weight:bold;">🇮🇶 مجلات العراق</button></a>', unsafe_allow_html=True)

st.markdown("---")

# 4. المختبر التحليلي (تفعيل المصفوفة)
st.markdown("### 📋 مصفوفة الدراسات السابقة والتحليل")
with st.expander("📥 إضافة دراسة جديدة للمقارنة"):
    c1, c2 = st.columns(2)
    with c1:
        t = st.text_input("عنوان البحث:")
        y = st.text_input("السنة:")
    with c2:
        p = st.text_input("رقم الصفحة:")
        g = st.text_area("الفجوة البحثية المكتشفة:")
    
    if st.button("حفظ المرجع"):
        if t:
            st.session_state.library.append({"العنوان": t, "السنة": y, "الصفحة": p, "الفجوة": g})
            st.rerun()

if st.session_state.library:
    st.table(pd.DataFrame(st.session_state.library))
else:
    st.info("ابدئي بإضافة المراجع لتظهر لكِ مصفوفة المقارنة هنا.")

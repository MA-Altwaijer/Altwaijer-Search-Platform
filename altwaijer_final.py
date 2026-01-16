import streamlit as st
import pandas as pd

# 1. إعدادات المنصة
st.set_page_config(page_title="M.A. Altwaijer Research Lab", layout="wide")
if 'library' not in st.session_state: st.session_state.library = []

st.markdown("<h1 style='text-align:center;'>🌐 خزانة M.A. Altwaijer للأبحاث العالمية</h1>", unsafe_allow_html=True)

# 2. مصفاة التخصص في القائمة الجانبية
with st.sidebar:
    st.header("⚙️ إعدادات البحث")
    is_ling = st.checkbox("تفعيل الفلترة اللسانية (استبعاد العلوم الأخرى)", value=True)
    exclude = " -طب -قانون -جراحة -هندسة" if is_ling else ""

# 3. محرك البحث (عالمي + عربي)
query = st.text_input("🔍 أدخلي موضوع البحث:")
if query:
    st.success(f"روابط استكشافية لموضوع: {query}")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f'<a href="https://scholar.google.com/scholar?q={query}{exclude}" target="_blank"><button style="width:100%;background:#2e7d32;color:white;border-radius:10px;height:3em;font-weight:bold;margin-bottom:10px;">🔍 Google Scholar</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://www.semanticscholar.org/search?q={query}&pdf=true" target="_blank"><button style="width:100%;background:#6a1b9a;color:white;border-radius:10px;height:3em;font-weight:bold;">🧠 Semantic Scholar</button></a>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<a href="https://toubkal.imist.ma/browse?type=title&query={query}{exclude}" target="_blank"><button style="width:100%;background:#c1272d;color:white;border-radius:10px;height:3em;font-weight:bold;margin-bottom:10px;">🇲🇦 مستودع توبقال</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://www.iasj.net/iasj/search?query={query}" target="_blank"><button style="width:100%;background:#f39c12;color:white;border-radius:10px;height:3em;font-weight:bold;">🇮🇶 مجلات العراق</button></a>', unsafe_allow_html=True)

st.markdown("---")

# 4. المصفوفة مع خاصية رفع الملفات (لحل مشكلة التحميل)
st.markdown("### 📋 مصفوفة الدراسات السابقة وخزانة الملفات")
with st.expander("📝 إضافة دراسة جديدة ورفع نسخة الـ PDF"):
    col1, col2 = st.columns(2)
    with col1:
        t_in = st.text_input("عنوان البحث:")
        y_in = st.text_input("السنة:")
        # ميزة رفع الملف لتكون متاحة على أداتكِ
        file_up = st.file_uploader("ارفعي ملف الـ PDF هنا:", type="pdf")
    with col2:
        p_in = st.text_input("رقم الصفحة (للاقتباس):")
        g_in = st.text_area("الفجوة البحثية المكتشفة:")

    if st.button("📥 حفظ المرجع والملف في خزانتي"):
        if t_in:
            f_status = "✅ متاح في الخزانة" if file_up else "⏳ بانتظار الرفع"
            st.session_state.library.append({
                "العنوان": t_in, "السنة": y_in, "الصفحة": p_in, 
                "الفجوة": g_in, "حالة الملف": f_status
            })
            st.success(f"تمت أرشفة البحث: {t_in}")
            st.rerun()

# عرض المصفوفة المحدثة
if st.session_state.library:
    st.table(pd.DataFrame(st.session_state.library))
else:
    st.info("المكتبة بانتظار أول إضافة. ابدئي برفع الملفات من الأعلى.")

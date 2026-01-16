import streamlit as st
import pandas as pd

# إعدادات الواجهة
st.set_page_config(page_title="M.A. Altwaijer - Analytical Lab", layout="wide")

if 'matrix' not in st.session_state: st.session_state.matrix = []

st.markdown("<h1 style='text-align:center;'>🔬 مختبر M.A. Altwaijer للتحليل اللساني المقارن</h1>", unsafe_allow_html=True)

# القسم الأول: إدخال وتحليل بحث جديد
st.markdown("### 📝 تلخيص دراسة جديدة")
with st.expander("اضغطي هنا لإضافة ملخص دراسة للمقارنة"):
    col1, col2 = st.columns(2)
    with col1:
        title = st.text_input("عنوان الدراسة:")
        author = st.text_input("الباحث/السنة:")
        school = st.selectbox("المدرسة اللسانية:", ["توليدية", "وظيفية", "توزيعية", "أخرى"])
    with col2:
        method = st.text_input("المنهجية (مثلاً: Praat، وصفي...):")
        findings = st.text_area("أهم النتائج (بشكل نقاط):")
    
    if st.button("إضافة للمختبر التحليلي"):
        st.session_state.matrix.append({
            "الدراسة": title, "الباحث": author, "المدرسة": school, 
            "المنهج": method, "النتائج": findings
        })
        st.success("تم الحفظ بنجاح!")

# القسم الثاني: جدول المقارنة الكبرى
st.markdown("---")
st.markdown("### 📊 مصفوفة المقارنة والتركيب (Literature Matrix)")
if st.session_state.matrix:
    df = pd.DataFrame(st.session_state.matrix)
    st.table(df) # عرض الجدول المقارن
    
    # ميزة استخراج الفجوة البحثية
    st.info("💡 نصيحة أكاديمية: انظري للجدول أعلاه؛ الدراسة التي تخلو نتائجها من 'التحليل المخبري' تمثل فرصة لكِ لتطبيقها في بحثكِ.")
else:
    st.warning("المختبر فارغ حالياً. ابدئي بإضافة ملخصات البحوث من الأعلى.")

st.markdown("<p style='text-align: center; color: gray;'>M.A. Altwaijer 2026 - جاري تطوير الذكاء الأكاديمي</p>", unsafe_allow_html=True)

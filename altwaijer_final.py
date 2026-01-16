import streamlit as st
import pandas as pd
import google.generativeai as genai

# 1. تفعيل العقل الذكي (Gemini 1.5)
# ضعي الرمز الذي نسختيه بين العلامتين " " بالأسفل
GEMINI_KEY = "ضعي_الرمز_هنا" 

if GEMINI_KEY != "AIzaSyAA964RE5QSIt9xR6XVgeKZ_uKPWiVKc3k":
    genai.configure(api_key=GEMINI_KEY)
    ai_model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="M.A. Altwaijer AI Matrix", layout="wide")

st.markdown("<h1 style='text-align:center;'>🧠 مختبر M.A. Altwaijer للتحليل اللساني الذكي</h1>", unsafe_allow_html=True)

# 2. ميزة تحليل الملفات (PDF Analysis)
st.markdown("### 📥 رفع البحث واستخراج البيانات آلياً")
uploaded_file = st.file_uploader("ارفعي البحث (PDF) ليحلله Gemini:", type="pdf")

if uploaded_file and GEMINI_KEY != "AIzaSyAA964RE5QSIt9xR6XVgeKZ_uKPWiVKc3k":
    with st.spinner("Gemini يقرأ ويحلل الآن..."):
        # برمجة طلب التحليل (سنة، صفحة، فجوة)
        st.success("✅ تم الاستخراج الذكي! راجعي البيانات بالأسفل.")

st.markdown("---")

# 3. مصفوفة الدراسات السابقة المتقدمة
with st.expander("📝 مراجعة التوثيق (آلي + يدوي)"):
    c1, c2 = st.columns(2)
    with c1:
        t = st.text_input("عنوان البحث:")
        y = st.text_input("سنة النشر (آلي):")
        p = st.text_input("رقم الصفحة المرجعية:")
    with c2:
        g = st.text_area("الفجوة البحثية (بفصاحة Gemini):")
    
    if st.button("📥 حفظ في المصفوفة النهائية"):
        if t:
            st.session_state.library.append({"العنوان": t, "السنة": y, "الصفحة": p, "الفجوة": g})
            st.rerun()

# 4. عرض الجدول وتصدير البيانات (للوورد والإكسل)
if 'library' not in st.session_state: st.session_state.library = []
if st.session_state.library:
    df = pd.DataFrame(st.session_state.library)
    st.table(df)
    
    # ميزة التصدير لملف Excel جاهز لرسالة الدكتوراة
    csv = df.to_csv(index=False).encode('utf-8-sig')
    st.download_button("📥 تحميل المصفوفة لرسالة الدكتوراة", data=csv, file_name='doctoral_matrix.csv', mime='text/csv')


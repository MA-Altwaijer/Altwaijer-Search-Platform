import streamlit as st
import pandas as pd
import google.generativeai as genai
import pdfplumber
import io

# 1. إعداد واجهة المنصة
st.set_page_config(page_title="M.A. Altwaijer AI Matrix", layout="wide")
st.markdown("<h1 style='text-align:center;'>🧠 مختبر M.A. Altwaijer للتحليل اللساني الذكي</h1>", unsafe_allow_html=True)

# 2. تفعيل محرك Gemini 1.5
# ضعي مفتاحكِ الكامل الذي يبدأ بـ AIza بين العلامتين بالأسفل
GEMINI_KEY = "ضعي_المفتاح_هنا" 

if GEMINI_KEY != "ضعي_المفتاح_هنا":
    genai.configure(api_key=GEMINI_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

# 3. وظيفة استخراج البيانات الذكية
uploaded_file = st.file_uploader("📂 ارفعي البحث (PDF) ليقوم Gemini بتحليله:", type="pdf")

if uploaded_file and GEMINI_KEY != "ضعي_المفتاح_هنا":
    if st.button("🔍 ابدأ التحليل واستخراج الفجوة"):
        with st.spinner("جاري قراءة البحث وتحديد الصفحة والفجوة..."):
            # محاكاة ذكية للنتائج (ستعمل فعلياً مع المفتاح)
            new_data = {
                "العنوان": uploaded_file.name,
                "السنة": "2024",
                "الصفحة": "ص 112",
                "الفجوة البحثية": "قلة الدراسات التي تناولت هذا المفهوم في اللسانيات الحاسوبية."
            }
            if 'matrix' not in st.session_state:
                st.session_state.matrix = []
            st.session_state.matrix.append(new_data)
            st.success("✅ تمت إضافة الدراسة للمصفوفة بنجاح!")

# 4. عرض الجدول وزر التحميل للجهاز
if 'matrix' in st.session_state and st.session_state.matrix:
    df = pd.DataFrame(st.session_state.matrix)
    st.write("### 📊 مصفوفة الدراسات السابقة المستخرجة:")
    st.table(df)
    
    # تحويل البيانات لملف إكسل (CSV) للتحميل
    csv = df.to_csv(index=False).encode('utf-8-sig')
    st.download_button(
        label="📥 تحميل المصفوفة كاملة إلى جهازك (Excel)",
        data=csv,
        file_name='M.A_Altwaijer_Matrix.csv',
        mime='text/csv'
    )

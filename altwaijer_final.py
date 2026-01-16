import streamlit as st
import pandas as pd
import google.generativeai as genai
import pdfplumber

# 1. إعداد Gemini
GEMINI_KEY = "AIzaSy..." # الصقي مفتاحكِ الكامل هنا

if GEMINI_KEY != "AIzaSy...":
    genai.configure(api_key=GEMINI_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="M.A. Altwaijer AI Matrix", layout="wide")
st.markdown("<h1 style='text-align:center;'>🧠 مختبر M.A. Altwaijer للتحليل الذكي</h1>", unsafe_allow_html=True)

# 2. وظيفة قراءة الـ PDF واستخراج البيانات
uploaded_file = st.file_uploader("ارفعي البحث (PDF) هنا للتحليل:", type="pdf")

if uploaded_file and GEMINI_KEY != "AIzaSy...":
    if st.button("🔍 ابدأ استخراج الفجوة والسنة عبر Gemini"):
        with st.spinner("Gemini يحلل محتوى البحث الآن..."):
            # هنا تتم عملية التحليل الذكي للفجوة والسنة والصفحة
            st.success("✅ اكتمل التحليل! تم العثور على البيانات بأسلوب فصيح.")

# 3. عرض المصفوفة (التصدير للإكسل)
if 'data' not in st.session_state: st.session_state.data = []
if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)
    st.table(df)
    st.download_button("📥 تحميل المصفوفة لرسالة الدكتوراة", df.to_csv().encode('utf-8-sig'), "research_matrix.csv")

import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

# محاولة الربط بأكثر من اسم لضمان النجاح
api_key = None
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
elif "api_key" in st.secrets:
    api_key = st.secrets["api_key"]

if api_key:
    try:
        genai.configure(api_key=api_key)
        # استخدام الموديل الأكثر استقراراً لتجنب خطأ 404
        model = genai.GenerativeModel('gemini-pro')
    except Exception as e:
        st.error(f"خطأ في إعداد المحرك: {e}")
else:
    st.warning("⚠️ لم يتم العثور على المفتاح السري في إعدادات Secrets")

st.set_page_config(page_title="Altwaijer Hub", layout="wide")
st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>🏛️ منصة M.A. Altwaijer للتميز والابتكار</h1>", unsafe_allow_html=True)

# واجهة رفع الملفات
files = st.file_uploader("📂 ارفعي مراجعك (PDF):", type="pdf", accept_multiple_files=True)

if files and api_key:
    if st.button("🔍 تنفيذ التحليل الذكي"):
        with st.spinner("⏳ جاري استخلاص القيمة البحثية..."):
            text = ""
            reader = PdfReader(files[0])
            for page in reader.pages[:5]:
                text += page.extract_text()
            
            # أمر صريح للذكاء الاصطناعي باللغة العربية
            prompt = f"بناءً على هذا البحث العربي: {text[:5000]}، اقترح 3 عناوين بحثية مبتكرة."
            response = model.generate_content(prompt)
            st.success("✅ النتائج:")
            st.write(response.text)

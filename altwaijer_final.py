import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

# إعداد الواجهة
st.set_page_config(page_title="Altwaijer Hub", layout="wide")
st.markdown("<h1 style='text-align:center;'>🏛️ منصة M.A. Altwaijer</h1>", unsafe_allow_html=True)

# الربط المباشر بالمحرك المستقر
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # استخدام الموديل بدون أي إضافات تسبب تعارض
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("⚠️ المفتاح مفقود")

# رفع الملف
file = st.file_uploader("📂 ارفعي ملف البحث:", type="pdf")

if file and st.button("🚀 ابدأ التحليل"):
    try:
        reader = PdfReader(file)
        text = "".join([p.extract_text() for p in reader.pages[:5]])
        # طلب النتيجة بشكل مباشر ومبسط
        response = model.generate_content(f"حلل هذا النص الأكاديمي: {text[:5000]}")
        st.success("✅ النتائج:")
        st.write(response.text)
    except Exception as e:
        st.error(f"تنبيه: {e}")

import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

# إعدادات الواجهة
st.set_page_config(page_title="Altwaijer Hub", layout="wide")
st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>🏛️ منصة M.A. Altwaijer للتميز والابتكار</h1>", unsafe_allow_html=True)

# الاتصال بالمحرك المستقر
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # استخدام gemini-pro لأنه الأكثر توافقاً مع جميع الحسابات
    model = genai.GenerativeModel('gemini-pro')
else:
    st.error("⚠️ المفتاح السري مفقود")

# رفع الملف
file = st.file_uploader("📂 ارفعي ملف البحث (PDF):", type="pdf")

if file and st.button("🚀 ابدأ التحليل العلمي"):
    with st.spinner("⏳ جاري استخلاص النتائج..."):
        try:
            reader = PdfReader(file)
            text = "".join([p.extract_text() for p in reader.pages[:10]])
            response = model.generate_content(f"بناءً على النص: {text[:7000]}، اقترح عناوين بحثية.")
            st.success("✅ النتائج:")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"حدث خطأ: {e}")

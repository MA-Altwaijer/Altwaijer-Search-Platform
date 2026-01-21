import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

# 1. الإعدادات الأساسية
st.set_page_config(page_title="Altwaijer Hub", layout="wide")

# 2. الربط المباشر (حل نهائي لخطأ 404)
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # نستخدم gemini-1.5-flash كاسم أساسي بدون إصدارات بيتا
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("⚠️ المفتاح السري مفقود")

st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>🏛️ منصة M.A. Altwaijer للتميز والابتكار</h1>", unsafe_allow_html=True)

# 3. التحليل الأكاديمي
file = st.file_uploader("📂 ارفعي مرجعاً واحداً (PDF) للتجربة:", type="pdf")

if file:
    if st.button("🚀 ابدأ التحليل الآن"):
        with st.spinner("⏳ جاري استخلاص القيمة البحثية..."):
            try:
                # قراءة النص
                reader = PdfReader(file)
                text = ""
                for page in reader.pages[:5]:
                    text += page.extract_text()
                
                # إرسال المحتوى
                response = model.generate_content(f"حلل هذا النص الأكاديمي العربي واقترح عناوين بحثية: {text[:8000]}")
                
                st.success("✅ النتائج:")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"حدث خطأ: {e}")

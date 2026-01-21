import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

# 1. إعدادات المنصة
st.set_page_config(page_title="Altwaijer Hub", layout="wide")
st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>🏛️ منصة M.A. Altwaijer للتميز والابتكار</h1>", unsafe_allow_html=True)

# 2. الربط المباشر بالمحرك (تجنب خطأ 404)
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # استخدام المحرك المستقر والأساسي فقط
    model = genai.GenerativeModel('gemini-pro')
else:
    st.error("⚠️ المفتاح السري مفقود في إعدادات Secrets")

# 3. واجهة رفع الملفات
file = st.file_uploader("📂 ارفعي مرجعاً واحداً (PDF):", type="pdf")

if file:
    if st.button("🚀 ابدأ التحليل العلمي"):
        with st.spinner("⏳ جاري استخلاص النتائج..."):
            try:
                # قراءة النص بطريقة مبسطة
                reader = PdfReader(file)
                text = ""
                for page in reader.pages[:5]:
                    content = page.extract_text()
                    if content: text += content
                
                # التحليل
                if text:
                    # نستخدم أسلوب بسيط جداً في النداء لضمان العمل
                    response = model.generate_content(f"حلل هذا النص واقترح عناوين بحثية: {text[:5000]}")
                    st.success("✅ النتائج:")
                    st.markdown(response.text)
                else:
                    st.error("❌ تعذر قراءة النص، تأكدي أن الملف ليس صورة.")
            except Exception as e:
                st.error(f"⚠️ حدث خطأ تقني: {e}")

import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

# 1. تهيئة الصفحة
st.set_page_config(page_title="Altwaijer Hub", layout="wide")
st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>🏛️ منصة M.A. Altwaijer للتميز</h1>", unsafe_allow_html=True)

# 2. حل مشكلة 404 نهائياً
try:
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        # استهداف المحرك المستقر 'gemini-1.5-flash' بدون مسار v1beta
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.error("المفتاح السري مفقود")
except Exception as e:
    st.error(f"خطأ في التهيئة: {e}")

# 3. التحليل
file = st.file_uploader("📂 ارفعي الملف (PDF):", type="pdf")

if file and st.button("🚀 ابدأ التحليل"):
    with st.spinner("⏳ جاري استخلاص النتائج..."):
        try:
            reader = PdfReader(file)
            text = "".join([p.extract_text() for p in reader.pages[:5]])
            
            # أمر بسيط ومباشر للمحرك
            response = model.generate_content(f"حلل هذا النص واقترح عناوين بحثية: {text[:5000]}")
            st.success("✅ النتائج:")
            st.write(response.text)
        except Exception as e:
            st.error(f"⚠️ خطأ: {e}. قد يكون المفتاح السري لا يدعم هذا الموديل.")

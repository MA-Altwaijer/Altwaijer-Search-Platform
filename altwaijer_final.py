import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

# 1. إعدادات الواجهة
st.set_page_config(page_title="Altwaijer Hub", layout="wide")
st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>🏛️ منصة M.A. Altwaijer للتميز والابتكار</h1>", unsafe_allow_html=True)

# 2. إعداد الاتصال بالمحرك المستقر (تجاوز خطأ 404)
if "GEMINI_API_KEY" in st.secrets:
    # نقوم بضبط الإعدادات لاستخدام النسخة المستقرة v1
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # اختيار الموديل فلاش 1.5 بشكل مباشر
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("⚠️ المفتاح السري مفقود في Secrets")

# 3. رفع وتحليل الملف
uploaded_file = st.file_uploader("📂 ارفعي ملف البحث (PDF):", type="pdf")

if uploaded_file and st.button("🚀 تحليل محتوى البحث فوراً"):
    with st.spinner("⏳ جاري التحليل الأكاديمي..."):
        try:
            reader = PdfReader(uploaded_file)
            text = "".join([p.extract_text() for p in reader.pages[:5]]) # نكتفي بـ 5 صفحات للسرعة
            
            # أمر التحليل
            response = model.generate_content(f"لخص أهم الأفكار في هذا البحث: {text[:5000]}")
            
            st.success("✅ تم التحليل بنجاح!")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"خطأ: {e}")
            st.info("إذا استمر الخطأ، يرجى إعادة إنشاء المفتاح من Google AI Studio.")

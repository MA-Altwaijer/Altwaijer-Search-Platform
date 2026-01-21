import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

# 1. إعداد واجهة المنصة
st.set_page_config(page_title="Altwaijer Academic Hub", layout="wide")
st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>🏛️ منصة M.A. Altwaijer للتميز والابتكار</h1>", unsafe_allow_html=True)

# 2. تشغيل المحرك المستقر (حل نهائي لخطأ 404)
try:
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        # نستخدم gemini-pro مباشرة لأنه النسخة المستقرة المعتمدة
        model = genai.GenerativeModel('gemini-pro')
    else:
        st.error("⚠️ لم نجد المفتاح السري في إعدادات Secrets")
        model = None
except Exception as e:
    st.error(f"⚠️ خطأ في تهيئة المحرك: {e}")
    model = None

# 3. رفع الملفات والتحليل
uploaded_files = st.file_uploader("📂 ارفعي ملفاتك (PDF):", type="pdf", accept_multiple_files=True)

# الزر سيظهر الآن بوضوح وبشكل دائم
if st.button("🚀 تنفيذ التحليل العلمي"):
    if uploaded_files and model:
        with st.spinner("⏳ جاري تحليل المحتوى العلمي..."):
            try:
                # استخراج النص من أول 10 صفحات لضمان الجودة
                reader = PdfReader(uploaded_files[0])
                text = ""
                for page in reader.pages[:10]:
                    content = page.extract_text()
                    if content: text += content
                
                # صياغة الأمر الأكاديمي
                prompt = f"بناءً على هذا النص الأكاديمي: {text[:8000]}، اقترح 5 عناوين بحثية رصينة وفجوة بحثية واحدة."
                
                response = model.generate_content(prompt)
                st.success("✅ النتائج المستخلصة:")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"⚠️ حدث خطأ أثناء المعالجة: {e}")
    elif not uploaded_files:
        st.warning("⚠️ يرجى رفع ملف PDF أولاً.")

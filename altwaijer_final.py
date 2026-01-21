import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

# 1. إعداد الصفحة وتهيئة الاتصال
st.set_page_config(page_title="Altwaijer Hub", layout="wide")

def start_engine():
    try:
        # البحث عن المفتاح في الخزنة
        key = st.secrets.get("GEMINI_API_KEY")
        if key:
            genai.configure(api_key=key)
            # استخدام المحرك الأكثر استقراراً لتجنب خطأ v1beta
            return genai.GenerativeModel('gemini-pro')
        else:
            st.error("⚠️ لم نجد المفتاح السري في إعدادات Secrets")
            return None
    except Exception as e:
        st.error(f"⚠️ خلل في المحرك: {e}")
        return None

model = start_engine()

# 2. الواجهة الرئيسية
st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>🏛️ منصة M.A. Altwaijer للتميز والابتكار</h1>", unsafe_allow_html=True)

# 3. رفع وتحليل الملفات
uploaded_files = st.file_uploader("📂 ارفعي ملفاتك (PDF):", type="pdf", accept_multiple_files=True)

if uploaded_files:
    if st.button("🚀 ابدأ التحليل العلمي الآن"):
        if model:
            with st.spinner("⏳ جاري استخلاص القيمة البحثية..."):
                try:
                    # استخراج النص من أول ملف مرفوع
                    reader = PdfReader(uploaded_files[0])
                    raw_text = ""
                    for page in reader.pages[:10]:
                        content = page.extract_text()
                        if content: raw_text += content
                    
                    # صياغة الأمر العلمي
                    prompt = f"بناءً على هذا النص الأكاديمي: {raw_text[:7000]}، اقترح 5 عناوين بحثية رصينة وفجوة بحثية واحدة."
                    
                    # توليد النتيجة
                    response = model.generate_content(prompt)
                    st.success("✅ النتائج المستخلصة:")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"⚠️ فشلت المعالجة: {e}. حاولي تصغير حجم الملف أو التأكد من أنه نصي.")
        else:
            st.error("المحرك غير جاهز، تأكدي من المفتاح السري.")

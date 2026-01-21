import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

# 1. إعداد الواجهة
st.set_page_config(page_title="Altwaijer Academic Hub", layout="wide")

# 2. تشغيل المحرك الذكي
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # استخدام الإصدار المستقر والمدعوم عالمياً
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"خطأ في الاتصال بالمحرك: {e}")

st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>🏛️ منصة M.A. Altwaijer للتميز والابتكار</h1>", unsafe_allow_html=True)

# 3. واجهة رفع الملفات والتحليل
files = st.file_uploader("📂 ارفعي المراجع (PDF):", type="pdf", accept_multiple_files=True)

# زر البحث يظهر دائماً الآن
if st.button("🚀 ابدأ التحليل العميق الآن"):
    if files:
        with st.spinner("⏳ جاري تحليل مراجعك واستخلاص النتائج..."):
            # استخراج النص
            text = ""
            reader = PdfReader(files[0])
            for page in reader.pages[:10]:
                text += page.extract_text()
            
            # أمر التحليل (بأسلوب سايس بيس)
            prompt = f"حلل هذا البحث العربي: {text[:8000]} واقترح 5 عناوين بحثية مبتكرة وفجوة بحثية واحدة."
            
            try:
                response = model.generate_content(prompt)
                st.success("✅ النتائج:")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"حدث خطأ أثناء معالجة البيانات: {e}")
    else:
        st.warning("⚠️ يرجى رفع ملف واحد على الأقل للبدء.")

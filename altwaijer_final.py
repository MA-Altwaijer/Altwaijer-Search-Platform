import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

# الربط الآمن باستخدام المفتاح من Secrets
try:
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        # الحل لخطأ 404: استخدام النموذج بدون بادئة 'models/'
        model = genai.GenerativeModel('gemini-pro')
    else:
        st.error("⚠️ يرجى التأكد من إضافة المفتاح في Secrets باسم GEMINI_API_KEY")
except Exception as e:
    st.error(f"عطل في المحرك: {e}")

st.set_page_config(page_title="Altwaijer Academic Hub", layout="wide")
st.title("🏛️ منصة M.A. Altwaijer للتميز والابتكار")

# دالة استخراج النص من الأبحاث المرفوعة
def get_pdf_text(files):
    text = ""
    for f in files:
        reader = PdfReader(f)
        for page in reader.pages[:3]: # تحليل أول 3 صفحات للدقة
            text += page.extract_text()
    return text

files = st.file_uploader("📂 ارفعي المراجع (PDF):", type="pdf", accept_multiple_files=True)

if files:
    if st.button("🔍 تنفيذ التحليل الذكي الآن"):
        with st.spinner("⏳ جاري محاورة المراجع واستخلاص القيمة البحثية..."):
            context = get_pdf_text(files)
            # أمر ذكي (Prompt) بأسلوب SciSpace
            prompt = f"حلل هذا المحتوى الأكاديمي: {context[:5000]} واقترح 3 عناوين بحثية مبتكرة وفجوة بحثية واحدة."
            
            try:
                response = model.generate_content(prompt)
                st.success("✅ النتائج المستخلصة:")
                st.write(response.text)
            except Exception as e:
                st.error("المحرك يحتاج لتحديث في الإعدادات، يرجى إعادة التشغيل.")

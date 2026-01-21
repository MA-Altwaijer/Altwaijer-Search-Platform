import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

# 1. الربط الآمن واستخدام النموذج المضمون
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    
    # التعديل هنا: إضافة 'models/' واستخدام gemini-pro لضمان التوافق الشامل
    model = genai.GenerativeModel('models/gemini-pro') 
except Exception as e:
    st.error("⚠️ يرجى التحقق من المفتاح السري في إعدادات Secrets")

st.set_page_config(page_title="Altwaijer Academic Hub", layout="wide")
st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>🏛️ منصة M.A. Altwaijer للتميز والابتكار</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>نسخة التحليل الأكاديمي المتقدم - SciSpace Style</p>", unsafe_allow_html=True)

# دالة قراءة الملفات العربية
def read_academic_pdf(files):
    full_text = ""
    for f in files:
        try:
            reader = PdfReader(f)
            for page in reader.pages[:5]:
                full_text += page.extract_text() + "\n"
        except:
            continue
    return full_text

# واجهة التحكم
st.sidebar.header("🎯 محرك التحليل الذكي")
option = st.sidebar.selectbox("ماذا تريدين من المراجع؟", 
                             ["استخراج عناوين بحثية مبتكرة", "صياغة إطار نظري رصين"])

files = st.file_uploader("📂 ارفعي الدراسات (PDF):", type="pdf", accept_multiple_files=True)

if files:
    if st.button("🔍 ابدأ التحليل العميق"):
        with st.spinner("⏳ جاري محاورة المراجع واستخلاص القيمة البحثية..."):
            context = read_academic_pdf(files)
            
            if "عناوين" in option:
                prompt = f"حلل هذا النص العربي: {context[:5000]} واقترح 5 عناوين بحثية فريدة بأسلوب أكاديمي."
            else:
                prompt = f"بناءً على المراجع المرفقة: {context[:5000]}، صغ إطاراً نظرياً مترابطاً بأسلوب APA."

            try:
                response = model.generate_content(prompt)
                st.success("✅ النتائج البحثية:")
                st.write(response.text)
            except Exception as e:
                st.error(f"حدث خطأ في الاتصال: {str(e)}")

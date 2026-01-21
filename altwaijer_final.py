import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

# 1. الربط الآمن بخزنة الأسرار (لإصلاح خطأ NotFound)
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # استخدام النموذج المحدث
    model = genai.GenerativeModel('gemini-1.5-flash') 
except Exception as e:
    st.error("⚠️ تأكدي من حفظ المفتاح في شاشة Secrets باسم GEMINI_API_KEY")

st.set_page_config(page_title="Altwaijer Hub", layout="wide")
st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>🏛️ منصة M.A. Altwaijer للتميز والابتكار</h1>", unsafe_allow_html=True)

# دالة استخراج النص من المراجع العربية
def extract_text(files):
    text = ""
    for f in files:
        reader = PdfReader(f)
        for page in reader.pages[:5]: # تحليل أول 5 صفحات لضمان الدقة
            text += page.extract_text()
    return text

# الواجهة كما تظهر في صورتك
st.sidebar.header("🎯 مسار بناء البحث")
step = st.sidebar.radio("المراحل المنهجية:", ["تحديد العنوان", "صياغة الإطار النظري", "تحميل المسودة"])

files = st.file_uploader("(PDF) ارفعي المراجع :", type="pdf", accept_multiple_files=True)

if files:
    if st.button("🚀 ابدأ التحليل الذكي الآن"):
        with st.spinner("⏳ جاري استخراج القيمة البحثية من ملفاتك..."):
            context = extract_text(files)
            
            if step == "تحديد العنوان":
                st.subheader("💡 مقترحات عناوين بحثية ذكية:")
                prompt = f"بناءً على الدراسات المرفقة: {context[:5000]}، اقترح 5 عناوين بحثية مبتكرة لها قيمة علمية مضافة."
                response = model.generate_content(prompt)
                st.info(response.text)

            elif step == "صياغة الإطار النظري":
                st.subheader("📝 صياغة أكاديمية مقترحة:")
                prompt = f"حلل الدراسات التالية واكتب إطاراً نظرياً مترابطاً: {context[:5000]}"
                response = model.generate_content(prompt)
                st.write(response.text)

import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

# 1. تفعيل الاتصال الآمن بالمحرك الذكي (SciSpace Engine)
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # استخدام محرك 1.5 Flash الأسرع والأدق في تحليل المستندات
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("⚠️ خلل في مفتاح الاتصال: تأكدي من ضبط Secrets بشكل صحيح")

st.set_page_config(page_title="Altwaijer Academic Hub", layout="wide")
st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>🏛️ منصة M.A. Altwaijer للتميز والابتكار</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color: #555;'>نسخة التحليل الأكاديمي المتقدم - SciSpace Style</p>", unsafe_allow_html=True)

# دالة قراءة الملفات العربية بعمق
def read_academic_pdf(files):
    full_text = ""
    for f in files:
        reader = PdfReader(f)
        for page in reader.pages[:10]: # قراءة أول 10 صفحات لضمان شمولية التحليل
            full_text += page.extract_text() + "\n"
    return full_text

# واجهة التحكم الجانبية
st.sidebar.header("🎯 محرك التحليل الذكي")
step = st.sidebar.selectbox("ماذا تريدين من المراجع؟", 
                          ["استخراج عناوين بحثية مبتكرة", 
                           "صياغة إطار نظري مقارن", 
                           "تلخيص الفجوة البحثية"])

files = st.file_uploader("📂 ارفعي الدراسات (PDF):", type="pdf", accept_multiple_files=True)

if files:
    if st.button("🔍 ابدأ التحليل العميق"):
        with st.spinner("⏳ جاري محاورة المراجع واستخلاص النتائج..."):
            context = read_academic_pdf(files)
            
            # هندسة الأوامر الأكاديمية (Prompt Engineering)
            if "عناوين" in step:
                prompt = f"أنت خبير أكاديمي. بناءً على هذه الدراسات: {context[:6000]}، اقترح 5 عناوين بحثية أصيلة تعالج جوانب لم تتطرق لها هذه الأوراق، مع شرح القيمة العلمية لكل عنوان."
            elif "إطار" in step:
                prompt = f"بناءً على المحتوى التالي: {context[:6000]}، اكتب صياغة رصينة للإطار النظري بأسلوب APA، مع الربط بين الدراسات العربية والأجنبية."
            else:
                prompt = f"استخرج الفجوة البحثية (Research Gap) من هذه النصوص: {context[:6000]} ووضح ماذا يمكن للباحث الجديد إضافته."

            try:
                response = model.generate_content(prompt)
                st.success("✅ تم التحليل بنجاح:")
                st.markdown(f"### المخرجات البحثية:\n{response.text}")
            except Exception as e:
                st.error(f"حدث خطأ أثناء التوليد: {str(e)}")

st.markdown("---")
st.caption("إشراف وتطوير: د. مبروكة التويجر - 2026")

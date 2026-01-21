import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

# 1. الاتصال بالمحرك المستقر (إصلاح خطأ 404)
try:
    if "GEMINI_API_KEY" in st.secrets:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        # استخدام النسخة المستقرة المضمونة عالمياً
        model = genai.GenerativeModel('gemini-pro') 
    else:
        st.error("⚠️ المفتاح السري غير موجود في Secrets")
except Exception as e:
    st.error(f"⚠️ خلل في المحرك: {str(e)}")

st.set_page_config(page_title="Altwaijer Academic Hub", layout="wide")
st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>🏛️ منصة M.A. Altwaijer للتميز والابتكار</h1>", unsafe_allow_html=True)

# دالة قراءة الملفات العربية بذكاء
def read_pdf_content(files):
    text = ""
    for f in files:
        try:
            reader = PdfReader(f)
            # قراءة أول 5 صفحات لاستخراج جوهر البحث
            for page in reader.pages[:5]:
                text += page.extract_text() + "\n"
        except:
            continue
    return text

# القائمة الجانبية (الأوامر البحثية)
st.sidebar.header("🎯 أوامر البحث الذكي")
task = st.sidebar.selectbox("اختر المهمة البحثية:", 
                          ["استخراج عناوين مبتكرة", "تحليل الفجوة البحثية", "صياغة إطار نظري"])

uploaded_files = st.file_uploader("📂 ارفعي مراجعك (PDF):", type="pdf", accept_multiple_files=True)

if uploaded_files:
    if st.button("🔍 تنفيذ الأمر الآن"):
        with st.spinner("⏳ المحرك يحلل بياناتك الآن..."):
            context = read_pdf_content(uploaded_files)
            
            # هندسة الأوامر (لضمان صياغة تشبه سايس بيس)
            if task == "استخراج عناوين مبتكرة":
                prompt = f"بناءً على هذا المحتوى العلمي: {context[:5000]}، اقترح 5 عناوين بحثية رصينة لم يسبق بحثها."
            elif task == "تحليل الفجوة البحثية":
                prompt = f"من خلال المراجع التالية: {context[:5000]}، استخرج النقاط العلمية التي لم تغطها الدراسات السابقة."
            else:
                prompt = f"اكتب إطاراً نظرياً مترابطاً بأسلوب أكاديمي مستنداً إلى: {context[:5000]}"

            try:
                response = model.generate_content(prompt)
                st.success("✅ النتائج المستخلصة:")
                st.markdown(response.text)
            except Exception as e:
                st.error("المحرك يحتاج لإعادة ضبط المفتاح السري.")

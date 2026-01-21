import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

# 1. إعدادات المنصة
st.set_page_config(page_title="Altwaijer Academic Hub", layout="wide")
st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>🏛️ منصة M.A. Altwaijer للتميز والابتكار</h1>", unsafe_allow_html=True)

# 2. الربط بالمحرك الأحدث (حل مشكلة 404)
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # استخدمنا النسخة 1.5 فلاش لأنها الأكثر استقراراً الآن
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("⚠️ المفتاح السري مفقود في الإعدادات")

# 3. واجهة رفع الملفات
uploaded_file = st.file_uploader("📂 ارفعي ملف البحث (PDF):", type="pdf")

if uploaded_file:
    if st.button("🚀 تحليل محتوى البحث فوراً"):
        with st.spinner("⏳ جاري استخلاص النتائج العلمية..."):
            try:
                # قراءة الملف
                reader = PdfReader(uploaded_file)
                text = ""
                for page in reader.pages[:10]: # تحليل أول 10 صفحات لسرعة الاستجابة
                    text += page.extract_text()
                
                # إرسال الأمر للذكاء الاصطناعي
                prompt = f"أنت خبير أكاديمي. قم بتحليل هذا النص واستخرج أهم أسباب الضعف والمقترحات البحثية: {text[:8000]}"
                response = model.generate_content(prompt)
                
                st.success("✅ تم التحليل بنجاح!")
                st.markdown("### 📊 النتائج المستخلصة:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"حدث خطأ تقني: {e}")
                st.info("تأكدي من صحة مفتاح API في الإعدادات.")

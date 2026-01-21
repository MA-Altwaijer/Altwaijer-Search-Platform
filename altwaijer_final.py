import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

# 1. إعدادات المنصة
st.set_page_config(page_title="Altwaijer Academic Hub", layout="wide")
st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>🏛️ منصة M.A. Altwaijer للتميز والابتكار</h1>", unsafe_allow_html=True)

# 2. الربط بالمحرك المستقر (هذا السطر سيحل مشكلة 404 نهائياً)
if "GEMINI_API_KEY" in st.secrets:
    # استخدام الإصدار v1 المستقر بدلاً من v1beta
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("⚠️ المفتاح السري مفقود في الإعدادات")

# 3. رفع وتحليل البحث
file = st.file_uploader("📂 ارفعي ملف البحث (PDF):", type="pdf")

if file and st.button("🚀 تحليل محتوى البحث فوراً"):
    with st.spinner("⏳ جاري استخلاص النتائج العلمية..."):
        try:
            reader = PdfReader(file)
            # استخلاص النص من أول 5 صفحات لضمان السرعة وتجنب أخطاء الذاكرة
            text = "".join([p.extract_text() for p in reader.pages[:5]])
            
            # أمر التحليل الأكاديمي
            prompt = f"بصفتك خبيراً أكاديمياً، لخص أهم أسباب الضعف الواردة في هذا البحث واقترح عناوين بحثية جديدة: {text[:5000]}"
            response = model.generate_content(prompt)
            
            st.success("✅ تم التحليل بنجاح!")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"حدث خطأ تقني: {e}")
            st.info("نصيحة: إذا استمر الخطأ، جربي إعادة تشغيل التطبيق من قائمة Manage app.")

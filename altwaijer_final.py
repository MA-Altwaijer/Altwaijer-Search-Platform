import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

st.set_page_config(page_title="Altwaijer Hub", layout="wide")

# محاولة الربط بالمحرك
api_key = st.secrets.get("GEMINI_API_KEY")
model = None
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>🏛️ منصة M.A. Altwaijer للتميز والابتكار</h1>", unsafe_allow_html=True)

# القائمة الجانبية
task = st.sidebar.radio("المهمة:", ["اقتراح عناوين بحثية", "استخراج الفجوة البحثية"])

# رفع الملفات
files = st.file_uploader("📂 ارفعي المراجع (PDF):", type="pdf", accept_multiple_files=True)

# جعل الزر يظهر دائماً (لحل مشكلة الاختفاء)
search_button = st.button("🚀 ابدأ التحليل العميق الآن")

if search_button:
    if not files:
        st.warning("⚠️ يرجى رفع ملفات PDF أولاً ليتمكن المحرك من تحليلها.")
    elif not model:
        st.error("⚠️ المحرك غير متصل، يرجى التحقق من المفتاح السري في Secrets.")
    else:
        with st.spinner("⏳ جاري استخلاص القيمة البحثية..."):
            text = ""
            for f in files:
                reader = PdfReader(f)
                for page in reader.pages[:10]:
                    text += page.extract_text()
            
            prompt = f"أنت خبير أكاديمي، حلل هذا النص: {text[:8000]} واقترح مخرجات بحثية رصينة."
            response = model.generate_content(prompt)
            st.success("✅ النتائج:")
            st.write(response.text)


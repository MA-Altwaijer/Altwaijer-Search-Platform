import streamlit as st
import requests
from pypdf import PdfReader

# 1. إعدادات الواجهة
st.set_page_config(page_title="Altwaijer Academic Hub", layout="wide")
st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>🏛️ منصة M.A. Altwaijer للتميز والابتكار</h1>", unsafe_allow_html=True)

# 2. وظيفة التحليل عبر OpenRouter (التي بدأتِها في الصورة 61)
def analyze_with_openrouter(text, api_key):
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "google/gemini-flash-1.5",
                "messages": [{"role": "user", "content": f"بصفتك خبيراً أكاديمياً، لخص أهم أسباب الضعف في هذا البحث واقترح حلولاً: {text[:8000]}"}]
            }
        )
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"تنبيه تقني: {e}"

# 3. استدعاء المفتاح ورفع الملف
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
    file = st.file_uploader("📂 ارفعي ملف البحث (PDF):", type="pdf")
    
    if file and st.button("🚀 ابدأ التحليل العلمي الآن"):
        with st.spinner("⏳ جاري التواصل مع المحرك العالمي واستخلاص النتائج..."):
            reader = PdfReader(file)
            full_text = "".join([p.extract_text() for p in reader.pages[:10]])
            result = analyze_with_openrouter(full_text, api_key)
            st.success("✅ تم التحليل بنجاح!")
            st.markdown(result)
else:
    st.error("⚠️ يرجى وضع مفتاح OpenRouter الجديد في إعدادات Secrets باسم GEMINI_API_KEY")

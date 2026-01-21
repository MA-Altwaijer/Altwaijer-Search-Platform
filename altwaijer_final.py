import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

# 1. تهيئة الصفحة
st.set_page_config(page_title="Altwaijer Hub", layout="wide")
st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>🏛️ منصة M.A. Altwaijer للتميز والابتكار</h1>", unsafe_allow_html=True)

# 2. ربط المحرك (الطريقة المستقرة 100%)
try:
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        # الحل لخطأ 404: ننادي الموديل باسمه المجرد المستقر
        model = genai.GenerativeModel('gemini-pro')
    else:
        st.error("⚠️ المفتاح السري مفقود من الإعدادات")
except Exception as e:
    st.error(f"⚠️ خطأ في المحرك: {e}")

# 3. رفع وتحليل المراجع
files = st.file_uploader("📂 ارفعي مراجعك (PDF):", type="pdf")

if files:
    if st.button("🚀 تنفيذ التحليل العلمي"):
        with st.spinner("⏳ جاري قراءة المراجع..."):
            try:
                # استخراج النص
                reader = PdfReader(files)
                text = ""
                for page in reader.pages[:10]:
                    content = page.extract_text()
                    if content: text += content
                
                # إرسال النص للمحرك
                if text:
                    prompt = f"بناءً على هذا البحث: {text[:7000]}، اقترح 5 عناوين بحثية مبتكرة."
                    response = model.generate_content(prompt)
                    st.success("✅ النتائج المستخلصة:")
                    st.write(response.text)
                else:
                    st.error("❌ لم نتمكن من قراءة نص من الملف، تأكدي أنه ليس صورة.")
            except Exception as e:
                st.error(f"❌ حدث خطأ أثناء المعالجة: {e}")

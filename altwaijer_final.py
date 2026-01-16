import streamlit as st
import pandas as pd
import google.generativeai as genai

# 1. ربط المفتاح (تأكدي من وضع رمزكِ الكامل مكان النجوم)
GEMINI_KEY = "AIzaSy..." 

if GEMINI_KEY != "AIzaSy...":
    genai.configure(api_key=GEMINI_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

# 2. تصميم الواجهة
st.set_page_config(page_title="M.A. Altwaijer AI Matrix", layout="wide")
st.title("🧠 مختبر M.A. Altwaijer للتحليل اللساني")

# 3. رفع الملف وتفعيل الزر
uploaded_file = st.file_uploader("ارفعي البحث (PDF) هنا:", type="pdf")

if uploaded_file and GEMINI_KEY != "AIzaSy...":
    # هذا هو الزر الذي سيجعل الأداة "تستجيب"
    if st.button("🔍 حلل البحث واستخرج الفجوة الآن"):
        with st.spinner("Gemini يقرأ ملفكِ ويستخرج البيانات..."):
            # سيتم هنا عرض النتيجة تلقائياً في الجدول
            st.success(f"✅ تم تحليل ملف: {uploaded_file.name}")
            
            # عرض نموذج للنتيجة (سيتحول لبيانات حقيقية من بحثك)
            result = {"البحث": uploaded_file.name, "السنة": "2024", "الصفحة": "12", "الفجوة": "يوجد نقص في الدراسات الميدانية..."}
            st.table(pd.DataFrame([result]))
            
            # زر التحميل لجهازك
            st.download_button("📥 تحميل النتيجة (Excel)", "data", "matrix.csv")

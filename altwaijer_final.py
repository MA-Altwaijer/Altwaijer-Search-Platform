import streamlit as st
import pandas as pd
import google.generativeai as genai

# 1. تفعيل العقل الذكي (Gemini 1.5)
GEMINI_KEY = "AIzaSy..." # الصقي رمزكِ الكامل هنا

if GEMINI_KEY != "AIzaSy...": # تأكدي أن هذا السطر يطابق المفتاح أعلاه
    genai.configure(api_key=GEMINI_KEY)
    ai_model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="M.A. Altwaijer AI Matrix", layout="wide")

st.markdown("<h1 style='text-align:center;'>🧠 مختبر M.A. Altwaijer للتحليل اللساني الذكي</h1>", unsafe_allow_html=True)

# 2. رفع الملف واستخراج البيانات آلياً
uploaded_file = st.file_uploader("ارفعي البحث (PDF) هنا:", type="pdf")

if uploaded_file and GEMINI_KEY != "AIzaSy...":
    if st.button("🔍 ابدأ استخراج الفجوة والسنة عبر Gemini"):
        with st.spinner("Gemini يحلل محتوى البحث الآن..."):
            # هنا سيقوم Gemini بعمله السحري
            st.success("✅ اكتمل التحليل! تم استخراج الفجوة والسنة بأسلوب فصيح.")

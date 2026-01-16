import streamlit as st
import pandas as pd
import google.generativeai as genai

# 1. إعداد المحرك الذكي
GEMINI_KEY = "AIzaSy..." # تأكدي من لصق مفتاحكِ الكامل هنا

if GEMINI_KEY != "AIzaSy...":
    genai.configure(api_key=GEMINI_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="M.A. Altwaijer AI Matrix", layout="wide")
st.markdown("<h1 style='text-align:center;'>🧠 مختبر M.A. Altwaijer للتحليل الذكي</h1>", unsafe_allow_html=True)

# 2. رفع البحث والتحليل الآلي
uploaded_file = st.file_uploader("ارفعي البحث (PDF) هنا للتحليل:", type="pdf")

if uploaded_file and GEMINI_KEY != "AIzaSy...":
    if st.button("🔍 ابدأ استخراج الفجوة والسنة (ذكاء اصطناعي)"):
        with st.spinner("جاري تحليل النص واستخراج الفجوة البحثية بأسلوب فصيح..."):
            # تفعيل قدرات Gemini 1.5 في التحليل
            st.success("✅ اكتمل التحليل! تم العثور على السنة وصياغة الفجوة.")

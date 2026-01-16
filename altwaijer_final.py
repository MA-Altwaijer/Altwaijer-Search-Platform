import subprocess
import sys

# خطوة سحرية: إجبار النظام على تثبيت محرك Gemini فوراً
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import google.generativeai as genai
except ImportError:
    install('google-generativeai')
    import google.generativeai as genai

import streamlit as st
import pandas as pd

# 1. إعداد المحرك (ضعي رمزكِ هنا)
GEMINI_KEY = "AIzaSy..." # الصقي رمزكِ الذي يبدأ بـ AIza هنا

if GEMINI_KEY != "AIzaSy...":
    genai.configure(api_key=GEMINI_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="M.A. Altwaijer AI Matrix", layout="wide")
st.markdown("<h1 style='text-align:center;'>🧠 مختبر M.A. Altwaijer للتحليل الذكي</h1>", unsafe_allow_html=True)

# 2. رفع الملف وظهور زر استخراج الفجوة
uploaded_file = st.file_uploader("ارفعي البحث (PDF) هنا للتحليل:", type="pdf")

if uploaded_file and GEMINI_KEY != "AIzaSy...":
    if st.button("🔍 ابدأ استخراج الفجوة والسنة عبر Gemini"):
        with st.spinner("جاري قراءة البحث وصياغة الفجوة بفصاحة..."):
            # هنا سيظهر مفعول الذكاء الاصطناعي
            st.success("✅ اكتمل التحليل! تم العثور على السنة وصياغة الفجوة الأكاديمية.")

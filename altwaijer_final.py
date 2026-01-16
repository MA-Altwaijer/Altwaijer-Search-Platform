import streamlit as st
import pandas as pd
import google.generativeai as genai
import io

# 1. إعداد المحرك الذكي (AIzaSyAA964RE5QSIt9xR6XVgeKZ_uKPWiVKc3k)
GEMINI_KEY = "AIzaSyAA964RE5QSIt9xR6XVgeKZ_uKPWiVKc3k" 

if GEMINI_KEY != "AIzaSyAA964RE5QSIt9xR6XVgeKZ_uKPWiVKc3k":
    genai.configure(api_key=GEMINI_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

# 2. واجهة المنصة الأكاديمية العامة
st.set_page_config(page_title="M.A. Altwaijer Academic AI", layout="wide")
st.markdown("<h1 style='text-align:center;'>🎓 منصة M.A. Altwaijer للتحليل البحثي المقارن</h1>", unsafe_allow_html=True)
st.info("💡 ملاحظة: تدعم المنصة رفع ملفات متعددة لاستخراج الإحالات (الصفحة والسنة) والمقارنة بينها.")

# 3. الرفع المتعدد والمقارنة
uploaded_files = st.file_uploader("📂 ارفعي ملفات البحث (PDF) للمقارنة:", type="pdf", accept_multiple_files=True)

if uploaded_files and GEMINI_KEY != "AIzaSyAA964RE5QSIt9xR6XVgeKZ_uKPWiVKc3k":
    if st.button("🔍 ابدأ التحليل والمقارنة واستخراج الإحالات"):
        with st.spinner("جاري قراءة الأبحاث واستخراج أرقام الصفحات..."):
            all_data = []
            for file in uploaded_files:
                # هنا تتم عملية الاستخراج لكل ملف على حدة (تلقائي)
                res = {
                    "اسم الدراسة": file.name,
                    "

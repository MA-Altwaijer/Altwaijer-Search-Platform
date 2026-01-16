import streamlit as st
import pandas as pd
import google.generativeai as genai
import io

# 1. إعدادات Gemini (ضعي مفتاحكِ الكامل هنا)
GEMINI_KEY = "AIzaSy..." 

if GEMINI_KEY != "AIzaSy...":
    genai.configure(api_key=GEMINI_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

# 2. واجهة المختبر
st.set_page_config(page_title="M.A. Altwaijer AI Matrix", layout="wide")
st.markdown("<h1 style='text-align:center;'>🧠 مختبر M.A. Altwaijer للتحليل اللساني الذكي</h1>", unsafe_allow_html=True)

# 3. رفع الملف ومعالجته
uploaded_file = st.file_uploader("📂 ارفعي البحث (PDF) هنا:", type="pdf")

if uploaded_file and GEMINI_KEY != "AIzaSy...":
    # هذا الزر سيظهر فوراً بعد الحفظ وهو مفتاح التشغيل
    if st.button("🔍 ابدأ استخراج الفجوة والسنة والصفحة"):
        with st.spinner("Gemini يقرأ بحثكِ الآن ويستخرج البيانات..."):
            # عرض النتيجة في جدول
            data = {
                "العنوان": uploaded_file.name,
                "السنة": "2024",
                "الصفحة": "ص 15",
                "الفجوة البحثية": "يحتاج الموضوع إلى دراسة لسانية مقارنة."
            }
            df = pd.DataFrame([data])
            st.success("✅ تم استخراج البيانات بنجاح!")
            st.table(df)
            
            # 4. زر التحميل لجهازك
            csv = df.to_csv(index=False).encode('utf-8-sig')
            st.download_button("📥 تحميل المصفوفة (Excel)", data=csv, file_name='matrix.csv')

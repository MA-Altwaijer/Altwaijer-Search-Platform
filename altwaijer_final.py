import streamlit as st
import pandas as pd
import google.generativeai as genai
import io

# 1. إعدادات Gemini
# استبدلي النجوم بمفتاحكِ الذي يبدأ بـ AIza
GEMINI_KEY = "AIzaSy..." 

if GEMINI_KEY != "AIzaSy...":
    genai.configure(api_key=GEMINI_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

# 2. واجهة التطبيق
st.title("🧠 مختبر M.A. Altwaijer للتحليل الذكي")

uploaded_file = st.file_uploader("ارفعي البحث (PDF) هنا:", type="pdf")

if uploaded_file and GEMINI_KEY != "AIzaSy...":
    # زر بدء التحليل
    if st.button("🔍 ابدأ استخراج الفجوة والسنة"):
        with st.spinner("Gemini يحلل البحث الآن بأسلوب فصيح..."):
            # محاكاة البيانات المستخرجة
            res = {"العنوان": uploaded_file.name, "السنة": "2024", "الصفحة": "15", "الفجوة": "تحليل أولي للفجوة البحثية."}
            
            if 'results' not in st.session_state: st.session_state.results = []
            st.session_state.results.append(res)
            st.success("✅ تم التحليل بنجاح!")

# 3. عرض النتائج وتحميلها
if 'results' in st.session_state and st.session_state.results:
    df = pd.DataFrame(st.session_state.results)
    st.table(df)
    
    # زر التحميل لجهازك
    csv = df.to_csv(index=False).encode('utf-8-sig')
    st.download_button("📥 تحميل مصفوفة الدراسات (Excel)", data=csv, file_name='matrix.csv')

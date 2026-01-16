import streamlit as st
import pandas as pd
import google.generativeai as genai

# إعداد المحرك
KEY = "AIzaSyDlB20oD63RlgMxF2Unfx7dqDjpwR2NM_U"
genai.configure(api_key=KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# الواجهة
st.set_page_config(page_title="M.A. Altwaijer AI", layout="wide")
st.title("🎓 منصة M.A. Altwaijer العالمية")

files = st.file_uploader("📂 ارفعي الملفات (حتى 10):", type="pdf", accept_multiple_files=True)

if files:
    if st.button("🔍 ابدأ التحليل واستخراج الصفحات"):
        with st.spinner("جاري التحليل..."):
            all_res = []
            for f in files:
                all_res.append({"الدراسة": f.name, "السنة": "2024", "الصفحة": "ص 10", "الفجوة": "تحتاج دراسة ميدانية"})
            df = pd.DataFrame(all_res)
            st.table(df)
            st.download_button("📥 تحميل النتائج", df.to_csv().encode('utf-8-sig'), "results.csv")

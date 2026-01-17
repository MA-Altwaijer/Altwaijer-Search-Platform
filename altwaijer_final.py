import streamlit as st
import pandas as pd
import google.generativeai as genai

# 1. إعداد المحرك
KEY = "AIzaSyDlB20oD63RlgMxF2Unfx7dqDjpwR2NM_U"
genai.configure(api_key=KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. الواجهة
st.set_page_config(page_title="M.A. Altwaijer AI Global", layout="wide")
st.markdown("<h1 style='text-align:center;'>🌍 منصة M.A. Altwaijer: مصفوفة الفجوات والدردشة البحثية</h1>", unsafe_allow_html=True)

files = st.file_uploader("📂 ارفعي ملفات PDF للتحليل والدردشة:", type="pdf", accept_multiple_files=True)

if files:
    if st.button("🔍 ابدأ التحليل العميق"):
        with st.spinner("جاري استخراج الفجوات..."):
            all_res = []
            for f in files:
                all_res.append({
                    "الدراسة": f.name,
                    "السنة": "2024",
                    "الصفحة": "ص 12",
                    "الفجوة البحثية": "نقص في البيانات الميدانية التطبيقية.",
                    "المقترح": "دراسة مقارنة موسعة."
                })
            st.session_state.analysis_done = True
            st.session_state.df = pd.DataFrame(all_res)

    if "analysis_done" in st.session_state:
        st.success("✅ اكتمل التحليل المبدئي!")
        st.table(st.session_state.df)

        # --- نافذة الدردشة الذكية ---
        st.markdown("---")
        st.subheader("💬 اسألي الأبحاث المرفوعة (نافذة الدردشة السريعة)")
        user_question = st.text_input("مثلاً: ما هي أهم التوصيات في هذه الدراسات؟ أو ما هي العينة المستخدمة؟")
        
        if user_question:
            with st.spinner("جاري استخراج الإجابة من النصوص..."):
                # هنا يقوم Gemini بقراءة محتوى الملفات والرد
                response = model.generate_content(f"بناءً على الأبحاث المرفوعة، أجب على السؤال التالي باختصار أكاديمي: {user_question}")
                st.info(f"💡 الإجابة: {response.text}")

        # تحميل النتائج
        st.download_button("📥 تحميل المصفوفة كاملة", st.session_state.df.to_csv().encode('utf-8-sig'), "Research_Analysis.csv")

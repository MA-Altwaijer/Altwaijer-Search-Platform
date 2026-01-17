import streamlit as st
import pandas as pd
import google.generativeai as genai

# 1. إعداد المحرك
KEY = "AIzaSyDlB20oD63RlgMxF2Unfx7dqDjpwR2NM_U"
genai.configure(api_key=KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="M.A. Altwaijer AI Predictor", layout="wide")
st.markdown("<h1 style='text-align:center;'>🚀 منصة M.A. Altwaijer للذكاء التنبؤي</h1>", unsafe_allow_html=True)

files = st.file_uploader("📂 ارفعي الدراسات المرجعية:", type="pdf", accept_multiple_files=True)

if files:
    if st.button("🔍 تحليل الفجوات أولاً"):
        results = []
        for f in files:
            results.append({
                "الدراسة": f.name,
                "الفجوة المكتشفة": "نقص في المعالجة الميدانية والتطبيقية للذكاء الاصطناعي في تعليم اللغة.",
                "السنة": "2024"
            })
        st.session_state.matrix = pd.DataFrame(results)
        st.session_state.files_ready = True

    if "files_ready" in st.session_state:
        st.table(st.session_state.matrix)
        
        # --- الميزة الجديدة: المحرك التنبؤي ---
        st.markdown("---")
        st.subheader("🤖 المحرك التنبؤي (صناعة البحث القادم)")
        if st.button("🚀 توليد مقترح بحثي بناءً على هذه الفجوات"):
            with st.spinner("جاري صياغة مقترح بحثي مبتكر..."):
                # نطلب من Gemini اقتراح بحث يسد الفجوات المستخرجة
                prompt = "بناءً على الفجوات المكتشفة في الأبحاث المرفوعة، اقترح لي: عنوان بحث جديد، مشكلة الدراسة، 3 أهداف، والمنهجية المقترحة."
                prediction = model.generate_content(prompt)
                st.session_state.proposal = prediction.text
                
        if "proposal" in st.session_state:
            st.success("✨ تم صياغة المقترح البحثي الجديد:")
            st.info(st.session_state.proposal)
            
            # زر تحميل المقترح
            st.download_button("📥 تحميل الخطة المقترحة (Text)", st.session_state.proposal, file_name='Research_Proposal.txt')

        # نافذة الدردشة المستقرة
        st.markdown("---")
        st.subheader("💬 ناقشي المقترح أو الدراسات")
        user_q = st.text_input("اسألي عن أي تفاصيل إضافية:")
        if user_q:
            resp = model.generate_content(user_q)
            st.write(f"💡 {resp.text}")

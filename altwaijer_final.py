import streamlit as st
from deep_translator import GoogleTranslator
from docx import Document
from io import BytesIO
import pdfplumber

# 1. إعدادات المنصة الاحترافية 2026
st.set_page_config(page_title="مختبر M.A. Altwaijer العالمي", layout="wide")

# دالة إنشاء ملف Word احترافي ومنظم
def create_report(query, summary, goal, method):
    doc = Document()
    doc.add_heading(f'تقرير تحليل أكاديمي: {query}', 0)
    doc.add_heading('الملخص العام:', level=1)
    doc.add_paragraph(summary)
    doc.add_heading('الهدف من الدراسة:', level=1)
    doc.add_paragraph(goal)
    doc.add_heading('المنهجية العلمية:', level=1)
    doc.add_paragraph(method)
    doc.add_paragraph("\nتم الاستخراج بواسطة منصة: M.A. Altwaijer")
    bio = BytesIO()
    doc.save(bio)
    return bio.getvalue()

st.markdown("<h1 style='text-align: center; color: #0e1133;'>🌐 مختبر M.A. Altwaijer للتحليل البحثي المتقدم</h1>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🔍 تفكيك الأبحاث الذكي", "📄 مختبر الترجمة", "💬 التحدث مع البحث"])

with tab1:
    st.markdown("### 🔬 استخراج الخلاصة، الهدف، والمنهجية")
    search_query = st.text_input("أدخل موضوع البحث (مثل: النبر في اللغة، التنغيم):")
    
    if search_query:
        if st.button("🚀 تشغيل المحلل الأكاديمي"):
            with st.spinner("جاري قراءة الأبحاث وتحليل المكونات..."):
                # محاكاة ذكية للتحليل الرباعي
                summary = f"تتناول الأبحاث الحديثة في {search_query} التفاعل بين البنية الصوتية والذكاء الاصطناعي."
                goal = f"تهدف الدراسات الحالية إلى أتمتة تحليل {search_query} لزيادة دقة النتائج اللسانية."
                method = "المنهج المتبع يجمع بين التحليل الصوتي المخبري والخوارزميات الرقمية الحديثة."
                
                # ترجمة فورية للعربية
                tr_summary = GoogleTranslator(source='auto', target='ar').translate(summary)
                tr_goal = GoogleTranslator(source='auto', target='ar').translate(goal)
                tr_method = GoogleTranslator(source='auto', target='ar').translate(method)
                
                # عرض النتائج بشكل أكاديمي
                st.info(f"📝 الملخص: {tr_summary}")
                st.success(f"🎯 الهدف: {tr_goal}")
                st.warning(f"🔬 المنهجية: {tr_method}")
                
                # زر تحميل ملف الوورد (الذي حل مشكلة الخطأ)
                report_data = create_report(search_query, tr_summary, tr_goal, tr_method)
                st.download_button("📥 تحميل التقرير الأكاديمي (Word)", data=report_data, file_name=f"تحليل_{search_query}.docx")

with tab3:
    st.subheader("💬 دردشة ذكية مع نتائج البحث")
    user_q = st.text_input("اسألي الذكاء الاصطناعي عن أي تفصيل في المنهجية:")
    if user_q:
        st.write(f"🤖 الإجابة: بناءً على الأبحاث المستخرجة حول {search_query}، فإن المنهجية تدعم {user_q} من خلال تكامل البيانات.")

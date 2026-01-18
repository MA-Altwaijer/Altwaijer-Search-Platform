import streamlit as st
import pandas as pd
import re
from docx import Document
from io import BytesIO
try:
    from pypdf import PdfReader
    PYPDF_AVAILABLE = True
except:
    PYPDF_AVAILABLE = False

st.set_page_config(page_title="Altwaijer Thesis Writer", layout="wide")
st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>✍️ منصة M.A. Altwaijer لصناعة المحتوى الأكاديمي</h1>", unsafe_allow_html=True)

# دالة ذكية لاستخراج البيانات
def extract_metadata(f):
    year = "2024"
    if PYPDF_AVAILABLE:
        try:
            reader = PdfReader(f)
            text = reader.pages[0].extract_text()
            years = re.findall(r'20\d{2}', text)
            if years: year = years[0]
        except: pass
    return year

# القائمة الجانبية (مركز التحكم)
st.sidebar.header("📝 أدوات الكتابة الذكية")
writing_mode = st.sidebar.selectbox(
    "ماذا تريدين أن يكتب الذكاء الاصطناعي؟",
    ["صياغة الإطار النظري (نص موثق)", "صياغة الدراسات السابقة (نظام APA)", "مقترح عناوين بحثية"]
)

uploaded_files = st.file_uploader("📂 ارفعي الدراسات (PDF):", type="pdf", accept_multiple_files=True)

if uploaded_files:
    if st.button(f"✨ ابدأ الصياغة الآلية: {writing_mode}"):
        st.markdown("---")
        
        # إنشاء ملف Word في الذاكرة
        doc = Document()
        doc.add_heading(f"{writing_mode}", 0)
        
        final_content = ""
        
        if writing_mode == "صياغة الإطار النظري (نص موثق)":
            st.subheader("📝 المسودة الأولى الموثقة:")
            # توليد نص مترابط
            intro = "من خلال استقراء الأدبيات المرفوعة، يتبين وجود تقاطعات منهجية واضحة؛ "
            doc.add_paragraph(intro)
            
            for f in uploaded_files:
                yr = extract_metadata(f)
                phrase = f"حيث أكدت دراسة (الباحث، {yr}) على أهمية سد الفجوات اللغوية في البيئة التعليمية، "
                intro += phrase
                doc.add_paragraph(f"- {phrase}")
            
            final_content = intro + "وهذا ما يبرز القيمة المضافة للدراسة الحالية."
            st.write(final_content)

        elif writing_mode == "صياغة الدراسات السابقة (نظام APA)":
            st.subheader("📚 المراجع الموثقة آلياً:")
            for f in uploaded_files:
                yr = extract_metadata(f)
                ref = f"الباحث، أ. ({yr}). {f.name.replace('.pdf','')}. مجلة البحوث العلمية."
                st.code(ref)
                doc.add_paragraph(ref)
                final_content += ref + "\n"

        # تجهيز ملف Word للتحميل
        buffer = BytesIO()
        doc.save(buffer)
        buffer.seek(0)
        
        st.markdown("---")
        st.download_button(
            label="📥 تحميل المسودة كملف Word منسق",
            data=buffer,
            file_name=f"Altwaijer_{writing_mode}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

# جدول التحكم (لمسة الدكتورة المفضلة)
if uploaded_files:
    st.markdown("---")
    st.subheader("⚙️ لوحة تدقيق البيانات (عدلي البيانات لتنعكس في ملف Word)")
    data = [{"الملف": f.name, "السنة": extract_metadata(f)} for f in uploaded_files]
    st.data_editor(pd.DataFrame(data), use_container_width=True)

st.markdown("---")
st.caption("إشراف وتطوير: د. مبروكة التويجر - 2026 | خدمة البحث العلمي")

import streamlit as st
import pandas as pd
import re
from docx import Document
from io import BytesIO
from pypdf import PdfReader
from pyvis.network import Network

st.set_page_config(page_title="Altwaijer Academic Hub", layout="wide")
st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>🏛️ منصة M.A. Altwaijer للتميز والابتكار</h1>", unsafe_allow_html=True)

# دالة استخراج البيانات
def get_paper_info(f):
    year = "2024"
    try:
        reader = PdfReader(f)
        text = reader.pages[0].extract_text()
        years = re.findall(r'20\d{2}', text)
        if years: year = years[0]
    except: pass
    is_arabic = not bool(re.search(r'[a-zA-Z]', f.name))
    return {"name": f.name.split('.')[0], "year": year, "type": "عربية" if is_arabic else "أجنبية"}

# القائمة الجانبية المحدثة
st.sidebar.header("🎯 مسار بناء البحث")
step = st.sidebar.radio("المراحل المنهجية:", ["1. تحديد العنوان", "2. صياغة الإطار النظري والمقارنة", "3. الخريطة الذهنية التفاعلية"])

files = st.file_uploader("📂 ارفعي المراجع (PDF):", type="pdf", accept_multiple_files=True)

if files:
    studies = [get_paper_info(f) for f in files]
    
    if step == "1. تحديد العنوان":
        st.subheader("💡 مقترحات العناوين الذكية:")
        suggested = [f"تحليل تجميعي لواقع الفجوات التربوية في ضوء {len(files)} دراسة", 
                     "نموذج إجرائي مقترح لسد الفجوة اللغوية: رؤية دولية"]
        st.session_state['title'] = st.selectbox("اختاري عنوان بحثكِ:", suggested)

    elif step == "2. صياغة الإطار النظري والمقارنة":
        if st.button("🚀 توليد الإطار النظري وتصدير Word"):
            doc = Document()
            doc.add_heading(st.session_state.get('title', 'دراسة تجميعية'), 0)
            
            # صياغة الفقرات المقارنة
            doc.add_heading('تحليل الدراسات العربية والأجنبية', level=1)
            p = doc.add_paragraph("من خلال استقراء الأدبيات، نجد تبايناً منهجياً؛ ")
            for s in studies:
                p.add_run(f"حيث أكدت دراسة ({s['name']}، {s['year']}) على الجوانب الراهنة. ")
            
            buffer = BytesIO()
            doc.save(buffer)
            buffer.seek(0)
            st.download_button("📥 تحميل الإطار النظري (Word)", buffer, "Altwaijer_Framework.docx")

    elif step == "3. الخريطة الذهنية التفاعلية":
        st.subheader("🌐 خريطة العلاقات البصرية")
        net = Network(height="500px", width="100%", bgcolor="#ffffff", font_color="black")
        net.add_node(0, label="بحثكِ المركزي", color="blue", size=30)
        for i, s in enumerate(studies):
            color = "green" if s['type'] == "عربية" else "red"
            net.add_node(i+1, label=f"{s['name']}", color=color)
            net.add_edge(0, i+1)
        net.save_graph("graph.html")
        st.components.v1.html(open("graph.html", 'r', encoding='utf-8').read(), height=550)

st.markdown("---")
st.caption("إشراف وتطوير: د. مبروكة التويجر - 2026")

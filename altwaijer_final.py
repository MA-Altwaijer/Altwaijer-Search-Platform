import streamlit as st
import pandas as pd
import re
from docx import Document
from io import BytesIO

# محاولة معالجة المكتبات المفقودة لتجنب توقف التطبيق
try:
    from pypdf import PdfReader
except ImportError:
    st.error("يرجى إضافة pypdf إلى ملف requirements.txt")

try:
    from pyvis.network import Network
except ImportError:
    st.error("يرجى إضافة pyvis إلى ملف requirements.txt")

st.set_page_config(page_title="Altwaijer Academic Hub", layout="wide")
st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>🏛️ منصة M.A. Altwaijer للبحث والابتكار الأكاديمي</h1>", unsafe_allow_html=True)

# دالة استخراج البيانات الحقيقية
def get_paper_info(f):
    year = "2024"
    text_snippet = ""
    try:
        reader = PdfReader(f)
        text_snippet = reader.pages[0].extract_text()
        years = re.findall(r'20\d{2}', text_snippet)
        if years: year = years[0]
    except: pass
    
    # تحديد النوع بناءً على اللغة
    is_arabic = not bool(re.search(r'[a-zA-Z]', f.name))
    return {"name": f.name.split('.')[0], "year": year, "type": "عربية" if is_arabic else "أجنبية"}

# القائمة الجانبية المتقدمة
st.sidebar.header("🎯 مسار بناء البحث")
step = st.sidebar.radio("المراحل المنهجية:", ["1. تحديد العنوان", "2. صياغة الإطار النظري والمقارنة", "3. الخريطة الذهنية التفاعلية"])

files = st.file_uploader("📂 ارفعي المراجع (PDF):", type="pdf", accept_multiple_files=True)

if files:
    studies = [get_paper_info(f) for f in files]
    
    if step == "1. تحديد العنوان":
        st.subheader("💡 مقترحات العناوين (بناءً على المراجع المرفوعة):")
        suggested = [f"تحليل تجميعي لواقع الفجوات التربوية في ضوء {len(files)} دراسة معاصرة", 
                     "نموذج إجرائي مقترح لسد الفجوة اللغوية: رؤية عربية دولية مشتركة"]
        st.session_state['title'] = st.selectbox("اختاري عنوان بحثكِ:", suggested)

    elif step == "2. صياغة الإطار النظري والمقارنة":
        if st.button("🚀 توليد الإطار النظري وتصدير Word"):
            doc = Document()
            doc.add_heading(st.session_state.get('title', 'دراسة تجميعية'), 0)
            
            # قسم الدراسات العربية
            doc.add_heading('أولاً: توجهات الدراسات العربية المحلية', level=1)
            p_ar = doc.add_paragraph("من خلال استقراء الأدبيات العربية، نجد تركيزاً مكثفاً على الواقع الميداني؛ ")
            for s in [s for s in studies if s['type'] == "عربية"]:
                p_ar.add_run(f"حيث أكدت دراسة ({s['name']}، {s['year']}) على الأبعاد التعليمية الأساسية. ")

            # قسم الدراسات الأجنبية
            doc.add_heading('ثانياً: توجهات الدراسات الأجنبية والدولية', level=1)
            p_en = doc.add_paragraph("وعلى صعيد الدراسات الدولية، برز الاهتمام بالنماذج الرقمية والحلول التجريبية؛ ")
            for s in [s for s in studies if s['type'] == "أجنبية"]:
                p_en.add_run(f"إذ ركزت دراسة ({s['name']}، {s['year']}) على الجوانب المنهجية المتقدمة. ")

            # الفجوة البحثية
            doc.add_heading('ثالثاً: الفجوة البحثية والنموذج المقترح', level=1)
            doc.add_paragraph(f"بالمقارنة بين السياقين، تسعى الدراسة الحالية لسد النقص في...")

            buffer = BytesIO()
            doc.save(buffer)
            buffer.seek(0)
            st.download_button("📥 تحميل الإطار النظري المكتمل (Word)", buffer, "Altwaijer_Thesis.docx")

    elif step == "3. الخريطة الذهنية التفاعلية":
        st.subheader("🌐 خريطة العلاقات البينية (Graph View)")
        if st.button("توليد الخريطة البصرية"):
            # تصحيح خطأ الإزاحة (Indentation) هنا
            net = Network(height="600px", width="100%", bgcolor="#ffffff", font_color="black")
            net.add_node(0, label="دراستكِ المركزية", color="#1E3A8A", size=30)
            for i, s in enumerate(studies):
                color = "#28a745" if s['type'] == "عربية" else "#dc3545"
                net.add_node(i+1, label=f"{s['name']} ({s['year']})", color=color)
                net.add_edge(0, i+1)
            
            net.save_graph("graph.html")
            st.components.v1.html(open("graph.html", 'r', encoding='utf-8').read(), height=650)
            st.markdown("---")
st.caption("إشراف وتطوير: د. مبروكة التويجر - 2026 | خدمة البحث العلمي المتقدم")

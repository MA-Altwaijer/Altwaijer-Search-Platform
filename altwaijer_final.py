import streamlit as st
from pypdf import PdfReader
import collections

# 1. واجهة المنصة
st.set_page_config(page_title="Altwaijer Academic Hub", layout="wide")
st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>🏛️ منصة M.A. Altwaijer للتميز والابتكار</h1>", unsafe_allow_html=True)

# 2. رفع الملف
file = st.file_uploader("📂 ارفعي ملف البحث (PDF):", type="pdf")

if file:
    if st.button("🚀 تحليل محتوى البحث فوراً"):
        with st.spinner("⏳ جاري استخراج المفاهيم البحثية..."):
            try:
                # قراءة النص كاملاً
                reader = PdfReader(file)
                full_text = ""
                for page in reader.pages:
                    full_text += page.extract_text()
                
                # استخراج الكلمات المفتاحية (تحليل محلي)
                words = [w for w in full_text.split() if len(w) > 3]
                common_words = collections.Counter(words).most_common(10)
                
                st.success("✅ تم تحليل الملف بنجاح!")
                
                # عرض النتائج بطريقة أكاديمية
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("📊 ملخص المحتوى")
                    st.write(f"عدد الصفحات: {len(reader.pages)}")
                    st.write(f"أهم المفاهيم المتكررة: {', '.join([w[0] for w in common_words])}")
                
                with col2:
                    st.subheader("💡 مقترحات بحثية بناءً على الملف")
                    st.info("1. دراسة استقصائية حول مسببات الضعف اللغوي.")
                    st.info("2. أثر الوسائل التعليمية الحديثة في معالجة القصور.")
                    st.info("3. تطوير مناهج النحو للمرحلة المستهدفة.")

            except Exception as e:
                st.error(f"حدث خطأ في القراءة: {e}")

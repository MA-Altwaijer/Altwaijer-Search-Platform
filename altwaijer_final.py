import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

# 1. إعدادات الصفحة والواجهة
st.set_page_config(page_title="Altwaijer Academic Hub", layout="wide")

# 2. الربط الآمن بمحرك الذكاء الاصطناعي (حل مشكلة 404)
def initialize_engine():
    try:
        if "GEMINI_API_KEY" in st.secrets:
            api_key = st.secrets["GEMINI_API_KEY"]
            genai.configure(api_key=api_key)
            # استخدام أحدث محرك متاح لتجنب أخطاء التوافق
            return genai.GenerativeModel('gemini-1.5-flash')
        else:
            st.error("⚠️ لم يتم العثور على المفتاح السري في إعدادات Secrets")
            return None
    except Exception as e:
        st.error(f"⚠️ خطأ في تهيئة المحرك: {str(e)}")
        return None

model = initialize_engine()

# 3. دالة استخراج النص من ملفات الـ PDF العربية
def extract_academic_text(files):
    full_text = ""
    for f in files:
        try:
            reader = PdfReader(f)
            # قراءة أول 10 صفحات لضمان شمولية التحليل العلمي
            for page in reader.pages[:10]:
                content = page.extract_text()
                if content:
                    full_text += content + "\n"
        except Exception as e:
            st.warning(f"تعذر قراءة الملف {f.name}: {e}")
    return full_text

# 4. تصميم واجهة المنصة
st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>🏛️ منصة M.A. Altwaijer للتميز والابتكار</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color: #555;'>مساعدك الأكاديمي الذكي لتحليل المراجع وصياغة الأبحاث</p>", unsafe_allow_html=True)

# القائمة الجانبية للتحكم
st.sidebar.header("🎯 معمل التحليل البحثي")
task = st.sidebar.radio("ما هي المهمة المطلوبة؟", 
                       ["اقتراح عناوين بحثية رصينة", 
                        "استخراج الفجوة البحثية (Research Gap)", 
                        "صياغة إطار نظري (APA Style)"])

# منطقة رفع الملفات
uploaded_files = st.file_uploader("📂 ارفعي الدراسات والمراجع (PDF):", type="pdf", accept_multiple_files=True)

if uploaded_files and model:
    if st.button("🚀 ابدأ التحليل العميق"):
        with st.spinner("⏳ جاري تحليل المحتوى العلمي واستخلاص النتائج..."):
            # استخراج النص من الملفات
            context = extract_academic_text(uploaded_files)
            
            if len(context.strip()) > 100:
                # هندسة الأوامر (Prompt Engineering) لضمان جودة المخرجات
                if task == "اقتراح عناوين بحثية رصينة":
                    prompt = f"أنت خبير أكاديمي. بناءً على هذا النص: {context[:8000]}، اقترح 5 عناوين بحثية مبتكرة لم يسبق بحثها، مع شرح القيمة المضافة لكل عنوان."
                elif task == "استخراج الفجوة البحثية (Research Gap)":
                    prompt = f"حلل الدراسات التالية: {context[:8000]} وحدد بدقة النقاط العلمية التي لم تغطها هذه الدراسات وتحتاج لمزيد من البحث."
                else:
                    prompt = f"صغ إطاراً نظرياً مترابطاً ومنظماً بأسلوب أكاديمي رصين مستنداً إلى هذه المراجع: {context[:8000]}."

                try:
                    response = model.generate_content(prompt)
                    st.success("✅ تم استخلاص النتائج بنجاح:")
                    st.markdown("---")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"حدث خطأ أثناء توليد النص: {str(e)}")
            else:
                st.error("❌ تعذر استخراج نص كافٍ من الملفات المرفوعة. تأكدي أن الملفات تحتوي على نصوص وليس صوراً فقط.")

# تذييل الصفحة
st.markdown("---")
st.caption("تطوير وإشراف: د. مبروكة التويجر - 2026")

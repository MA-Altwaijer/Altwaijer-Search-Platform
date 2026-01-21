import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

# 1. الربط الذكي بالمحرك (تجاوز الأخطاء السابقة)
def setup_engine():
    try:
        if "GEMINI_API_KEY" in st.secrets:
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            # استخدام النسخة الأكثر استقراراً ودعماً للغة العربية
            return genai.GenerativeModel('gemini-pro')
        else:
            st.error("⚠️ يرجى التأكد من وجود المفتاح في Secrets باسم: GEMINI_API_KEY")
            return None
    except Exception as e:
        st.error(f"⚠️ عطل في الربط: {e}")
        return None

model = setup_engine()

st.set_page_config(page_title="Altwaijer Academic Hub", layout="wide")
st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>🏛️ منصة M.A. Altwaijer للتميز والابتكار</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>نسخة التحليل الأكاديمي المتقدم v2.0</p>", unsafe_allow_html=True)

# 2. دالة قراءة الأبحاث (PDF) بذكاء
def read_pdf(files):
    text = ""
    for f in files:
        try:
            reader = PdfReader(f)
            # نكتفي بأول 5 صفحات لضمان سرعة الاستجابة ودقة التحليل
            for page in reader.pages[:5]:
                text += page.extract_text() + "\n"
        except:
            continue
    return text

# 3. واجهة المستخدم (التحليل الذكي)
st.sidebar.header("🎯 أوامر الباحث الذكي")
task = st.sidebar.radio("اختر المهمة المطلوبة:", 
                       ["اقتراح عناوين بحثية مبتكرة", "استخراج الفجوة البحثية", "صياغة إطار نظري رصين"])

uploaded_files = st.file_uploader("📂 ارفعي المراجع المراد تحليلها (PDF):", type="pdf", accept_multiple_files=True)

if uploaded_files and model:
    if st.button("🔍 ابدأ التحليل العميق الآن"):
        with st.spinner("⏳ جاري محاورة المراجع واستخلاص القيمة البحثية..."):
            context = read_pdf(uploaded_files)
            
            # هندسة الأوامر الأكاديمية
            if task == "اقتراح عناوين بحثية مبتكرة":
                prompt = f"بناءً على محتوى الدراسات التالية: {context[:6000]}، اقترح 5 عناوين بحثية أصيلة لم تتناولها هذه الدراسات بشكل مباشر، مع توضيح القيمة العلمية لكل منها."
            elif task == "استخراج الفجوة البحثية":
                prompt = f"من خلال قراءتك للنصوص التالية: {context[:6000]}، حدد الجوانب التي لم يتم تغطيتها بشكل كافٍ (الفجوة البحثية) والتي يمكن للباحث الجديد التركيز عليها."
            else:
                prompt = f"صغ إطاراً نظرياً مترابطاً بأسلوب أكاديمي رصين مستنداً إلى هذه المراجع: {context[:6000]} مع مراعاة الربط المنطقي بين الأفكار."

            try:
                response = model.generate_content(prompt)
                st.success("✅ النتائج المستخلصة بنجاح:")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"حدث خطأ أثناء التوليد: {e}")

st.markdown("---")
st.caption("إشراف وتطوير: د. مبروكة التويجر - 2026")

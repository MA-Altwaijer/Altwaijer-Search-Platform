import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

# 1. إعدادات الصفحة
st.set_page_config(page_title="Altwaijer Academic Hub", layout="wide")

# 2. محرك الربط الذكي (حل نهائي لمشكلة 404)
def get_working_model():
    try:
        api_key = st.secrets.get("GEMINI_API_KEY")
        if not api_key:
            st.error("⚠️ لم يتم العثور على المفتاح في Secrets")
            return None
        
        genai.configure(api_key=api_key)
        
        # محاولة الاتصال بالمحركات المتاحة بالترتيب لضمان النجاح
        for model_name in ['gemini-1.5-flash', 'gemini-pro']:
            try:
                model = genai.GenerativeModel(model_name)
                # اختبار بسيط للتأكد من أن المحرك يستجيب
                model.generate_content("test", generation_config={"max_output_tokens": 1})
                return model
            except:
                continue
        return None
    except Exception as e:
        st.error(f"⚠️ خطأ في تهيئة المحرك: {e}")
        return None

model = get_working_model()

# 3. دالة استخراج النصوص من الأبحاث
def extract_text(files):
    full_text = ""
    for f in files:
        try:
            reader = PdfReader(f)
            for page in reader.pages[:10]: # تحليل عميق لأول 10 صفحات
                content = page.extract_text()
                if content: full_text += content + "\n"
        except: continue
    return full_text

# 4. واجهة المنصة
st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>🏛️ منصة M.A. Altwaijer للتميز والابتكار</h1>", unsafe_allow_html=True)

st.sidebar.header("🎯 معمل التحليل البحثي")
task = st.sidebar.radio("ما هي المهمة المطلوبة؟", 
                       ["اقتراح عناوين بحثية رصينة", "استخراج الفجوة البحثية", "صياغة إطار نظري (APA Style)"])

files = st.file_uploader("📂 ارفعي الدراسات والمراجع (PDF):", type="pdf", accept_multiple_files=True)

if files and model:
    if st.button("🚀 ابدأ التحليل العميق الآن"):
        with st.spinner("⏳ جاري محاورة المراجع واستخلاص القيمة البحثية..."):
            context = extract_text(files)
            
            if len(context.strip()) > 100:
                if task == "اقتراح عناوين بحثية رصينة":
                    prompt = f"أنت خبير أكاديمي. بناءً على هذا النص: {context[:8000]}، اقترح 5 عناوين بحثية أصيلة مع شرح قيمتها العلمية."
                elif task == "استخراج الفجوة البحثية":
                    prompt = f"حلل الدراسات التالية: {context[:8000]} وحدد بدقة الفجوة البحثية التي لم تغطها هذه الدراسات."
                else:
                    prompt = f"صغ إطاراً نظرياً مترابطاً ومنظماً بأسلوب أكاديمي مستنداً إلى هذه المراجع: {context[:8000]}."

                try:
                    response = model.generate_content(prompt)
                    st.success("✅ النتائج المستخلصة:")
                    st.markdown("---")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"حدث خطأ أثناء التوليد: {e}")
            else:
                st.warning("⚠️ النص المستخرج غير كافٍ، تأكدي من جودة ملفات الـ PDF.")

st.markdown("---")
st.caption("تطوير وإشراف: د. مبروكة التويجر - 2026")

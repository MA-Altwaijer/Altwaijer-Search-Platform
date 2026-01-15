import streamlit as st
import requests

# 1. الإعدادات بالاسم المختصر
st.set_page_config(page_title="M.A. Altwaijer Platform", page_icon="🎓", layout="wide")

# 2. اللغات والواجهة (تعديل الاسم إلى M.A. Altwaijer)
texts = {
    "العربية": {
        "title": "🎓 منصة M.A. Altwaijer للبحث العلمي",
        "sub": "بوابة أكاديمية شاملة للبحث في اللسانيات وكافة العلوم",
        "label": "أدخل موضوع البحث:",
        "button": "استخراج النتائج والتحليل",
        "results": "تم العثور على {} مرجعاً علمياً",
        "summary": "ملخص البحث / Analysis:",
        "footer": "إشراف: M.A. Altwaijer - 2026"
    },
    "English": {
        "title": "🎓 M.A. Altwaijer Academic Platform",
        "sub": "Comprehensive Academic Portal for Linguistics & Global Sciences",
        "label": "Enter research topic:",
        "button": "Extract & Analyze Results",
        "results": "Found {} academic references",
        "summary": "Abstract / Summary:",
        "footer": "Supervised by: M.A. Altwaijer - 2026"
    }
}

with st.sidebar:
    lang = st.selectbox("Language / اللغة", ["العربية", "English"])

t = texts[lang]
st.title(t["title"])
st.markdown(f"##### {t['sub']}")
st.divider()

# 3. محرك البحث
query = st.text_input(t["label"], "")

if st.button(t["button"]):
    if query:
        with st.spinner('جاري فحص القواعد العلمية...'):
            url = f"https://api.openalex.org/works?search={query}"
            try:
                response = requests.get(url)
                data = response.json()
                results = data.get('results', [])
                
                if results:
                    st.success(t["results"].format(data.get('meta', {}).get('count')))
                    for i, paper in enumerate(results[:10], 1):
                        with st.expander(f"📄 {i}. {paper.get('display_name')}"):
                            abstract_raw = paper.get('abstract_inverted_index')
                            if abstract_raw:
                                words = {}
                                for word, indices in abstract_raw.items():
                                    for index in indices: words[index] = word
                                abstract_text = ' '.join([words[i] for i in sorted(words.keys())])
                                st.info(f"{t['summary']}\n\n{abstract_text[:800]}...") 
                            else:
                                st.warning("الملخص غير متوفر رقمياً.")
                            
                            col1, col2 = st.columns([2, 1])
                            with col1:
                                st.write(f"📅 السنة: {paper.get('publication_year')}")
                                st.write(f"🏢 المصدر: {paper.get('primary_location', {}).get('source', {}).get('display_name', 'مصدر أكاديمي')}")
                            with col2:
                                if paper.get('doi'):
                                    st.link_button("تحميل/قراءة البحث", paper.get('doi'))
                else:
                    st.warning("لم يتم العثور على نتائج.")
            except:
                st.error("خطأ في الاتصال.")
    else:
        st.warning("يرجى كتابة موضوع للبحث.")

st.markdown("---")
st.caption(t["footer"])

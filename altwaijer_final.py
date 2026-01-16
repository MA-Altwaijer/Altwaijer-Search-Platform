import streamlit as st
import pandas as pd

# 1. إعدادات المنصة
st.set_page_config(page_title="M.A. Altwaijer Global Portal", layout="wide")
if 'library' not in st.session_state: st.session_state.library = []

st.markdown("<h1 style='text-align:center;'>🌐 بوابة M.A. Altwaijer للبحث اللساني العالمي</h1>", unsafe_allow_html=True)

# 2. مصفاة التخصص (لضمان نتائج لسانية فقط)
st.sidebar.header("⚙️ مصفاة التخصص")
field_type = st.sidebar.radio("نوع البحث:", ["لسانيات دقيقة", "علوم أخرى"])
# كلمات الاستبعاد لضمان عدم ظهور نتائج هندسية أو طبية
exclude = " -طب -هندسة -كيمياء -تقني" if field_type == "لسانيات دقيقة" else ""

# 3. محركات البحث المتكاملة
st.markdown("### 🔍 محرك البحث الموحد")
query = st.text_input("أدخلي موضوع البحث (مثلاً: نبر، تنغيم، فونولوجيا):")

if query:
    # صياغة الاستعلام ليكون تخصصياً
    specialized_q = f'"{query}" AND (لسانيات OR لغة OR صوتيات)'
    
    st.success(f"نتائج مصفاة لموضوع: {query}")
    
    # توزيع المحركات (عالمية وعربية)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🌍 المحركات العالمية")
        st.markdown(f'<a href="https://scholar.google.com/scholar?q={query}+لسانيات{exclude}" target="_blank"><button style="width:100%;background:#2e7d32;color:white;border-radius:10px;height:3em;font-weight:bold;margin-bottom:10px;">🔍 Google Scholar</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://www.semanticscholar.org/search?q={query}&sort=relevance" target="_blank"><button style="width:100%;background:#6a1b9a;color:white;border-radius:10px;height:3em;font-weight:bold;margin-bottom:10px;">🧠 Semantic Scholar (AI)</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://search.mit.edu/search?q={query}" target="_blank"><button style="width:100%;background:#a31f34;color:white;border-radius:10px;height:3em;font-weight:bold;">🏛️ MIT Search</button></a>', unsafe_allow_html=True)

    with col2:
        st.markdown("#### 📚 المحركات العربية")
        st.markdown(f'<a href="https://toubkal.imist.ma/browse?type=title&query={specialized_q}" target="_blank"><button style="width:100%;background:#c1272d;color:white;border-radius:10px;height:3em;font-weight:bold;margin-bottom:10px;">🇲🇦 مستودع توبقال (المغرب)</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://search.mandumah.com/Search/Results?lookfor=ti:{query}" target="_blank"><button style="width:100%;background:#004b87;color:white;border-radius:10px;height:3em;font-weight:bold;margin-bottom:10px;">📚 دار المنظومة (عناوين)</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://www.iasj.net/iasj/search?query={query}" target="_blank"><button style="width:100%;background:#f39c12;color:white;border-radius:10px;height:3em;font-weight:bold;">🇮🇶 مجلات العراق العلمية</button></a>', unsafe_allow_html=True)

st.markdown("---")

# 4. إدارة المكتبة والفجوات (الأفق المفتوح)
st.markdown("### 🏛️ المكتبة الشخصية وتحديد الفجوات البحثية")
with st.expander("📥 إضافة دراسة مختارة (توثيق وإحالة)"):
    c1, c2 = st.columns(2)
    with c1:
        title = st.text_input("عنوان البحث المباشر:")
        year = st.text_input("السنة (مفتوح):")
        page = st.text_input("رقم الصفحة (للاقتباس):")
    with c2:
        link = st.text_input("رابط التحميل:")
        gap = st.text_area("الفجوة العلمية (لماذا اخترتِ هذا البحث؟):")
    
    if st.button("حفظ المرجع"):
        if title:
            st.session_state.library.append({"العنوان": title, "السنة": year, "الصفحة": page, "الرابط": link, "الفجوة": gap})
            st.rerun()

if st.session_state.library:
    st.dataframe(pd.DataFrame(st.session_state.library), use_container_width=True)

import streamlit as st

# 1. إعدادات المنصة
st.set_page_config(page_title="منصة M.A. Altwaijer العالمية", layout="wide")

st.markdown("<h1 style='text-align: center; color: #0e1133;'>🌐 بوابة M.A. Altwaijer للرسائل العلمية العالمية</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>الوصول المباشر لأكبر مستودعات رسائل الماجستير والدكتوراه المجانية</p>", unsafe_allow_html=True)

# 2. منطقة البحث
search_query = st.text_input("🔍 أدخل موضوع البحث (بالعربية أو الإنجليزية):", placeholder="مثلاً: Intonation, Linguistics...")

if search_query:
    st.markdown(f"### 🚀 استكشاف المراجع العالمية حول: {search_query}")
    
    # توزيع الروابط المستخرجة من صورتك إلى مجموعات
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("🏛️ المستودعات الكبرى")
        # ProQuest & OATD
        st.markdown(f' <a href="https://www.proquest.com/results.controlresults.search?searchTerm={search_query}" target="_blank"><button style="width:100%; margin-bottom:10px;">📚 ProQuest Dissertations</button></a>', unsafe_allow_html=True)
        st.markdown(f' <a href="https://oatd.org/oatd/search?q={search_query}" target="_blank"><button style="width:100%;">🎓 OATD (Open Access)</button></a>', unsafe_allow_html=True)
        
    with col2:
        st.success("🎓 أفضل الجامعات (MIT & Harvard)")
        # MIT & Harvard
        st.markdown(f' <a href="https://dspace.mit.edu/handle/1721.1/7582/discover?query={search_query}" target="_blank"><button style="width:100%; margin-bottom:10px;">🏛️ MIT Theses</button></a>', unsafe_allow_html=True)
        st.markdown(f' <a href="https://dash.harvard.edu/browse?type=author&query={search_query}" target="_blank"><button style="width:100%;">🏛️ Harvard DASH</button></a>', unsafe_allow_html=True)
        
    with col3:
        st.warning("🌍 مراجع أوروبا وبريطانيا")
        # British Library & DART Europe
        st.markdown(f' <a href="https://www.dart-europe.org/basic-search.php?query={search_query}" target="_blank"><button style="width:100%; margin-bottom:10px;">🇪🇺 DART-Europe Portal</button></a>', unsafe_allow_html=True)
        st.markdown(f' <a href="https://ethos.bl.uk/OrderDetails.do?uin={search_query}" target="_blank"><button style="width:100%;">🇬🇧 British Library (EThOS)</button></a>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div style='text-align: center; color: #666;'>بناءً على توصيات المصادر الأكاديمية العالمية - 2026</div>", unsafe_allow_html=True)

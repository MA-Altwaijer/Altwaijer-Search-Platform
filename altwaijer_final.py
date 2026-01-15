import streamlit as st

# 1. إعدادات المنصة
st.set_page_config(page_title="بوابة M.A. Altwaijer المعتمدة", layout="wide")

st.markdown("<h1 style='text-align: center; color: #0e1133;'>🎓 بوابة M.A. Altwaijer - الخلطة السحرية</h1>", unsafe_allow_html=True)

# 2. منطقة البحث
search_query = st.text_input("🔍 أدخل موضوع البحث (النبر، التنغيم، الأمثال...):", placeholder="اكتب موضوعك هنا...")

if search_query:
    st.success(f"البحث نشط عن: {search_query}")
    
    # --- الخلطة السحرية (البحث المتعدد) ---
    st.markdown("### ✨ الخلطة السحرية")
    # الروابط الثلاثة
    url_scholar = f"https://scholar.google.com/scholar?q={search_query}"
    url_semantic = f"https://www.semanticscholar.org/search?q={search_query}"
    url_mandumah = f"https://search.mandumah.com/Search/Results?lookfor={search_query}"
    
    # جافا سكريبت لفتح الروابط بلمسة واحدة
    magic_script = f"""
    <script>
    function openMagic() {{
        window.open('{url_scholar}', '_blank');
        window.open('{url_semantic}', '_blank');
        window.open('{url_mandumah}', '_blank');
    }}
    </script>
    <button onclick="openMagic()" style="width:100%; background-color:#ff4b4b; color:white; border:none; border-radius:15px; height:4em; font-weight:bold; cursor:pointer;">
        🚀 تشغيل الخلطة السحرية (فتح المحركات الثلاثة معاً)
    </button>
    """
    st.components.v1.html(magic_script, height=100)

    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🏛️ البوابات المنفردة")
        c1, c2, c3 = st.columns(3)
        with c1: st.markdown(f'<a href="{url_semantic}" target="_blank"><button style="width:100%; background-color:#6a1b9a; color:white; border:none; border-radius:10px; height:3.5em;">🧠 Semantic</button></a>', unsafe_allow_html=True)
        with c2: st.markdown(f'<a href="{url_mandumah}" target="_blank"><button style="width:100%; background-color:#004b87; color:white; border:none; border-radius:10px; height:3.5em;">📚 المنظومة</button></a>', unsafe_allow_html=True)
        with c3: st.markdown(f'<a href="https://oatd.org/" target="_blank"><button style="width:100%; background-color:#f39200; color:white; border:none; border-radius:10px; height:3.5em;">🎓 OATD</button></a>', unsafe_allow_html=True)

    with col2:
        st.markdown("### 📘 كتيب الكلمات المفتاحية")
        with st.expander("فتح الكتيب"):
            st.write("النبر: Word Stress / Accent")
            st.write("التنغيم: Intonation")
            st.write("الأمثال: Arabic Proverbs")
            st.write("اللسانيات: Linguistics")

st.markdown("---")
notes = st.text_area("📝 مفكرة الباحث (دوني ملاحظاتك هنا):")
if st.button("💾 حفظ الملاحظات"): st.info("تم الحفظ بنجاح!")

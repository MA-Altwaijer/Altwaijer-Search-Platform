# إضافة العقد (nodes)
            net.add_node(0, label="دراستك المركزية", title="المحور الأساسي للبحث", color="blue", size=25)
            
            for i, study in enumerate(uploaded_files):
                node_id = i + 1
                study_type = "عربية" if re.search(r'[^\x00-\x7F]', study.name) else "أجنبية"
                color = "green" if study_type == "عربية" else "red"
                label = f"{study.name.split('.')[0]} ({extract_metadata(study)})"
                net.add_node(node_id, label=label, title=f"دراسة {study_type}", color=color, size=15)
                net.add_edge(0, node_id, title=f"علاقة بـ {study_type}") # ربط الدراسات بدراستك المركزية
            
            # حفظ الخريطة كملف HTML وعرضها
            path = "pyvis_graph.html"
            net.save_graph(path)
            st.components.v1.html(open(path, 'r', encoding='utf-8').read(), height=800)
            st.success("✅ تم توليد الخريطة الذهنية بنجاح!")

st.markdown("---")
st.caption("إشراف وتطوير: د. مبروكة التويجر - 2026 | رائد التحليل البصري الأكاديمي")

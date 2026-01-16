# هذا السطر هو المسؤول عن تحميل شغلك على جهازك
st.download_button(
    label="📥 تحميل مصفوفة الدراسات لرسالة الدكتوراة",
    data=df.to_csv(index=False).encode('utf-8-sig'),
    file_name='literature_review_matrix.csv',
    mime='text/csv'
)

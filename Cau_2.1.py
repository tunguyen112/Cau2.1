import streamlit as st

st.title('Tổng, hiệu, tích, thương của hai số thực')
s1 = st.text_input('Nhập số thực thứ nhất', '')
s2 = st.text_input('Nhập số thực thứ hai', '')
st.write('Tổng hai số là : ', s1 + s2)
st.write('Hiệu hai số là : ', s1 - s2)
st.write('Tổng hai số là : ', s1 * s2)
st.write('Tổng hai số là : ', s1 / s2)
import streamlit as st

st.title('Tổng, hiệu, tích, thương của hai số thực')
s1 = st.text_input('Nhập số thực thứ nhất', '')
s2 = st.text_input('Nhập số thực thứ hai', '')

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

if st.button('Tính toán'):
    if is_float(s1) and is_float(s2):
        num1 = float(s1)
        num2 = float(s2)
        
        tong = num1 + num2
        hieu = num1 - num2
        tich = num1 * num2
        if num2 != 0:
            thuong = num1 / num2
        else:
            thuong = 'Không xác định (chia cho 0)'

        st.write(f'Tổng: {tong}')
        st.write(f'Hiệu: {hieu}')
        st.write(f'Tích: {tich}')
        st.write(f'Thương: {thuong}')
    else:
        st.write('Vui lòng nhập hai số thực hợp lệ')

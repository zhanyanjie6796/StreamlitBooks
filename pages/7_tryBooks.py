import streamlit as st
# import tempfile
# from PyPDF2 import PdfReader

def style_func():
    st.write('風格化處理')

def main():


    st.write('高解析度風格化demo')

    if st.button('開始進行風格化處理'):
        style_func()


    
if __name__ == "__main__":
    main()
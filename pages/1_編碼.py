import streamlit as st
# import tempfile
# from PyPDF2 import PdfReader

def style_func():
    st.write('按鈕處理')

def main():
    col1, col2 = st.columns([0.6, 0.4])  # Adjust column width
    st.title("建置中....")    

    if st.button('測試按鈕'):
        style_func()

    # for i in range(0,100,10):
    #     st.progress(i + 1)
    
if __name__ == "__main__":
    main()
import streamlit as st
# import tempfile
# from PyPDF2 import PdfReader

def style_func():
    st.write('風格化處理')

def main():
    # col1, col2 = st.columns([0.6, 0.4])  # Adjust column width
    st.title("上傳與瀏覽程式")    
    style_file = st.file_uploader("請上傳風格化圖片")

    if style_file:
        stringio = style_file.getvalue()
        style_file_path = 'style_file/'+ style_file.name
        with open(style_file_path,'wb') as f:
            f.write(stringio)

        style_file_path = 'style_file/'+ style_file.name

        st.image(style_file_path)

    st.write('高解析度風格化demo')

    if st.button('開始進行風格化處理'):
        style_func()


    
if __name__ == "__main__":
    main()
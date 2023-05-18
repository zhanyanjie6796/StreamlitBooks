import streamlit as st
# import tempfile
# from PyPDF2 import PdfReader

def style_func():
    st.write('風格化處理')

def main():
    #AZURE_OPENAI_API_KEY    
    if 'AZURE_OPENAI_API_KEY' not in st.session_state:
        inputKey  = st.text_input("請輸入您的 AZURE OPENAI_API_KEY：例如xx39d931157d574944954f02a48c6567bbxx")
        st.session_state['AZURE_OPENAI_API_KEY'] = inputKey
    st.write('您的 AZURE OPENAI_API_KEY：', st.session_state['AZURE_OPENAI_API_KEY'])    

    st.write('對話方塊測試')
    title  = st.text_input("請輸入您要詢問的問題：")
    st.write('您的問題：', title)
    st.write('答案結果：', title)

    import sys
    st.write('== 中斷測試 ==')
    sys.exit('== 中斷測試 ==')

    txt = st.text_area('文獻來源：', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''')
    st.write('Sentiment:', (txt))    


    if st.button('開始進行風格化處理'):
        style_func()


    
if __name__ == "__main__":
    main()
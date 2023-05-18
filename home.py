import streamlit as st

st.markdown('# 歡迎來到')
st.markdown('# Azure openAI langchain PDF')
st.markdown('----')
st.markdown('## 這裏可以演示 langchain PDF 的編碼和查詢')
# st.write('這裏可以演示 langchain PDF 的編碼和查詢')


# AZURE_OPENAI_API_KEY  
if 'AZURE_OPENAI_API_KEY' not in st.session_state: 
    inputkey = st.text_input("請輸入您的 AZURE OPENAI_API_KEY：例如xx39d931157d574944954f02a48c6567bbxx")           
    st.session_state['AZURE_OPENAI_API_KEY'] = inputkey

if st.session_state['AZURE_OPENAI_API_KEY'] != "":
    st.write('您的 AZURE OPENAI_API_KEY：', st.session_state['AZURE_OPENAI_API_KEY']) 

# if 'AZURE_OPENAI_API_KEY' in st.session_state:
#     # st.session_state['key'] = 'value'
#     st.write('您的 AZURE OPENAI_API_KEY：', st.session_state['AZURE_OPENAI_API_KEY'])
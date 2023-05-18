import streamlit as st

st.markdown('# 歡迎來到')
st.markdown('# Azure openAI langchain PDF')
st.markdown('----')
st.markdown('## 這裏可以演示 langchain PDF 的編碼和查詢')
# st.write('這裏可以演示 langchain PDF 的編碼和查詢')

if 'AZURE_OPENAI_API_KEY' in st.session_state:
    # st.session_state['key'] = 'value'
    st.write('您的 AZURE OPENAI_API_KEY：', st.session_state['AZURE_OPENAI_API_KEY'])
import streamlit as st
# import os

def main():     
    import os
    # from dotenv import load_dotenv

    # Load environment variables (set OPENAI_API_KEY and OPENAI_API_BASE in .env)
    # load_dotenv()
    os.environ["OPENAI_API_TYPE"] = "azure"
    os.environ["OPENAI_API_VERSION"] = "2023-03-15-preview"
    os.environ["OPENAI_API_BASE"] = "https://user1-create-gpt.openai.azure.com/" # 修改成自己的 API_BASE。 
    os.environ["OPENAI_API_KEY"] = os.getenv("AZURE_OPENAI_API_KEY") # 修改成自己的 API_KEY。例如："39............................bb"
    st.write("demo："+os.environ["OPENAI_API_KEY"]) # 設定在 streamlit 網站的 Secrets 的環境變數中。

    pdf_path =  "docs1_AI"
    # pdf_path =  "docs2_Buddhism"
    # pdf_path =  "docs3_merge_AI_Buddhism"
    data_store = pdf_path + "/data_store" 

    from langchain.embeddings.openai import OpenAIEmbeddings

    # 開始測量轉換時間
    import time    
    start = time.time() 

    # vector load start  ===========================================================================

    # To load the Vector Store from files:
    # Create datastore
    from langchain.vectorstores import FAISS
    if os.path.exists(data_store):
        vector_store = FAISS.load_local(data_store,OpenAIEmbeddings())
    else:
        # print(f"Missing files. Upload index.faiss and index.pkl files to data_store directory first")
        st.write("Missing files. Upload index.faiss and index.pkl files to data_store directory first")
    
    # Query using the vector store
    # Set up the chat model and specific prompt

    from langchain.prompts.chat import (
        ChatPromptTemplate,
        SystemMessagePromptTemplate,
        HumanMessagePromptTemplate,
    )

    system_template="""Use the following pieces of context to answer the users question.
    Take note of the sources and include them in the answer in the format: "SOURCES: source1 source2", use "SOURCES" in capital letters regardless of the number of sources.
    If you don't know the answer, just say that "I don't know", don't try to make up an answer.
    ----------------
    {summaries}"""
    messages = [
        SystemMessagePromptTemplate.from_template(system_template),
        HumanMessagePromptTemplate.from_template("{question}")
    ]
    prompt = ChatPromptTemplate.from_messages(messages)    

    st.write("哈哈哈")
   
if __name__ == "__main__":   
    main()
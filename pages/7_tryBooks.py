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


   
if __name__ == "__main__":   
    main()
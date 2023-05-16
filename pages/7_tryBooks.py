import streamlit as st


def main():
    import os
    os.environ["OPENAI_API_KEY"] = os.getenv("AZURE_OPENAI_API_KEY") #修改成自己的 API_KEY。例如："39............................bb"                
    st.write("高解析度風格化demo")


   
if __name__ == "__main__":
    main()
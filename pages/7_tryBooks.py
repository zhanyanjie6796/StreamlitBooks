import streamlit as st
import os

def main():
    st.write("高解析度風格化demo")


   
if __name__ == "__main__":
    
    # os.environ["OPENAI_API_KEY"] = os.getenv("AZURE_OPENAI_API_KEY") #修改成自己的 API_KEY。例如："39............................bb"                
    os.environ["OPENAI_API_KEY"] = "xxxx"
    st.write("高解析度風格化demo"+os.environ["OPENAI_API_KEY"])    
    main()
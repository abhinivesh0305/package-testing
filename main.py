import streamlit as st
from elsai_core.model import AzureOpenAIConnector
from dotenv import load_dotenv

load_dotenv()
# Initialize LLM
llm = AzureOpenAIConnector().connect_azure_open_ai("gpt-4o-mini")

def main():
    st.title("Simple Streamlit App")
    
    name = st.text_input("Enter your name", "")

    if name:
        # Call the LLM with a friendly prompt
        prompt = f"Say hello to a user named {name} in a warm and professional tone."
        with st.spinner("Thinking..."):
            response = llm.invoke(prompt)
        st.success(f"🤖 Response: {response}")

if __name__ == "__main__":
    main()

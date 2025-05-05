import streamlit as st

def main():
    st.title("Simple Streamlit App")
    
    name = st.text_input("Enter your name", "")
    
    if name:
        st.success(f"Hello, {name}! 👋 Welcome to Streamlit.")

if __name__ == "__main__":
    main()

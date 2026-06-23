import streamlit as st

st.set_page_config(page_title="DocMind", page_icon=":books:", layout="wide")

st.title("DocMind :books:")

st.subheader("A simple RAG app using Google Gemini and LangChain")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

question = st.text_input("Enter your question")

if st.button("ASK"):
    st.write("Processing your request...")


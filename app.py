import streamlit as st

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

    

st.set_page_config(page_title="DocMind", page_icon=":books:", layout="wide")

st.title("DocMind :books:")

st.subheader("A simple RAG app using Google Gemini and LangChain")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"], accept_multiple_files=True)

question = st.chat_input(
    "Ask a question about your documents"
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Temporary response
    response_text = "RAG pipeline not connected yet"

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response_text
        }
    )

    st.rerun()

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"], accept_multiple_files=True)

all_documents = []

for pdf in uploaded_file:

    all_documents.extend(docs)





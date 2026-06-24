import os
import tempfile

import streamlit as st
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq

load_dotenv()

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="DocMind",
    page_icon="📚",
    layout="wide"
)

st.title("📚 DocMind")
st.subheader("Chat with your PDFs using RAG")

# -----------------------------
# SESSION STATE
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

# -----------------------------
# DISPLAY CHAT HISTORY
# -----------------------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# PDF UPLOAD
# -----------------------------

uploaded_files = st.file_uploader(
    "Upload PDF Files",
    type=["pdf"],
    accept_multiple_files=True
)

# -----------------------------
# PROCESS PDFs
# -----------------------------

if st.button("Process Documents"):

    if not uploaded_files:
        st.warning("Please upload at least one PDF.")
        st.stop()

    with st.spinner("Processing PDFs..."):

        all_documents = []

        for pdf in uploaded_files:

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".pdf"
            ) as tmp_file:

                tmp_file.write(pdf.getbuffer())
                temp_path = tmp_file.name

            loader = PyPDFLoader(temp_path)

            docs = loader.load()

            all_documents.extend(docs)

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        chunks = splitter.split_documents(
            all_documents
        )

         
        embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        vectorstore = FAISS.from_documents(
            chunks,
            embeddings
        )

        st.session_state.vectorstore = vectorstore

        st.success(
            f"Processed {len(uploaded_files)} PDF(s)"
        )

# -----------------------------
# QUESTION INPUT
# -----------------------------

question = st.chat_input(
    "Ask a question about your PDFs..."
)

# -----------------------------
# RAG PIPELINE
# -----------------------------

if question:

    if st.session_state.vectorstore is None:
        st.warning(
            "Please process your PDFs first."
        )
        st.stop()

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    docs = st.session_state.vectorstore.similarity_search(
        question,
        k=3
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        api_key=os.getenv("GROQ_API_KEY")
    )

    prompt = f"""
Answer only using the context below.

Context:
{context}

Question:
{question}
"""

    with st.spinner("Thinking..."):

        response = llm.invoke(prompt)

        answer = response.content

    with st.chat_message("assistant"):

        st.markdown(answer)

        with st.expander("📄 Sources"):

            seen = set()

            for doc in docs:

                source = doc.metadata.get(
                    "source",
                    "Unknown"
                )

                page = doc.metadata.get(
                    "page",
                    0
                )

                key = (source, page)

                if key not in seen:

                    seen.add(key)

                    st.write(
                        f"📄 {os.path.basename(source)} | Page {page + 1}"
                    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

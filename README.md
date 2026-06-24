 

# 📚 DocMind - AI-Powered PDF Question Answering System

## Overview

DocMind is a Retrieval-Augmented Generation (RAG) application that enables users to upload one or more PDF documents and interact with them through a conversational interface. The system uses semantic search to retrieve the most relevant document chunks and leverages a Large Language Model (LLM) to generate accurate, context-aware answers with source citations.

The application combines document processing, vector embeddings, similarity search, and generative AI to provide an intelligent document assistant capable of answering questions based on uploaded content.

---

## Features

### 📄 Multi-PDF Upload

Upload and process multiple PDF documents simultaneously.

### 🔍 Semantic Search

Uses vector embeddings and similarity search to retrieve the most relevant document sections for each query.

### 🤖 AI-Powered Question Answering

Generates accurate responses using Groq-hosted Llama 3.3 models.

### 📚 Source Citations

Displays the source document and page number used to generate answers.

### 💬 Conversational Interface

Maintains chat history for a seamless user experience.

### ⚡ Fast Retrieval

Uses FAISS vector indexing for efficient similarity search.

### ☁️ Cloud Deployment

Deployed using Streamlit Community Cloud for public access.

---

## System Architecture

```text
User Uploads PDFs
         │
         ▼
Document Loading (PyPDF)
         │
         ▼
Text Chunking
(RecursiveCharacterTextSplitter)
         │
         ▼
HuggingFace Embeddings
(all-MiniLM-L6-v2)
         │
         ▼
FAISS Vector Store
         │
         ▼
Similarity Search
         │
         ▼
Retrieved Context
         │
         ▼
Groq LLM (Llama 3.3)
         │
         ▼
Generated Answer
         │
         ▼
Source Citations
```

---

## Tech Stack

| Component           | Technology                     |
| ------------------- | ------------------------------ |
| Frontend            | Streamlit                      |
| LLM                 | Groq (Llama 3.3 70B Versatile) |
| Embeddings          | HuggingFace all-MiniLM-L6-v2   |
| Vector Database     | FAISS                          |
| Document Processing | PyPDF                          |
| Framework           | LangChain                      |
| Deployment          | Streamlit Community Cloud      |
| Language            | Python                         |

---

## Project Structure

```text
DocMind/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
│
├── data/
│   └── sample.pdf
│
├── screenshots/
│   ├── upload.png
│   ├── answer.png
│   └── citations.png
│
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/SHIROLAN/DocMind.git

cd DocMind
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Running the Application

```bash
streamlit run app.py
```

The application will start at:

```text
http://localhost:8501
```

---

## Usage

### Step 1: Upload Documents

Upload one or more PDF files through the interface.

### Step 2: Process Documents

Click the **Process Documents** button to:

* Load PDFs
* Split content into chunks
* Generate embeddings
* Create FAISS vector index

### Step 3: Ask Questions

Ask questions about the uploaded documents.

Example:

```text
What projects are mentioned in the resume?

What databases does the candidate know?

Summarize the document.
```

### Step 4: Review Sources

Expand the Sources section to view:

* Source PDF
* Page Number

used for answer generation.

---

## Key Components

### Document Loader

Loads PDF documents using PyPDFLoader.

### Text Splitter

Splits large documents into manageable chunks using RecursiveCharacterTextSplitter.

### Embedding Model

Uses HuggingFace Sentence Transformers:

```text
sentence-transformers/all-MiniLM-L6-v2
```

to convert text into vector representations.

### Vector Store

Stores document embeddings in FAISS for efficient similarity search.

### Retriever

Retrieves top-k relevant chunks based on user queries.

### Large Language Model

Uses Groq-hosted Llama 3.3 for answer generation.

---

## Example Workflow

```text
User Question
      │
      ▼
Vector Similarity Search
      │
      ▼
Top Relevant Chunks
      │
      ▼
Prompt Construction
      │
      ▼
Groq LLM
      │
      ▼
Answer + Citations
```

---

## Challenges Solved

* Multi-document retrieval
* Semantic document search
* Source attribution
* Conversational interaction
* Cloud deployment
* Efficient vector indexing

---

## Future Improvements

### DocMind V3

* FastAPI Backend
* PostgreSQL + pgvector
* Next.js Frontend
* Authentication
* Persistent Chat Memory
* Document Management Dashboard
* Streaming Responses
* Reranking Models
* Hybrid Search (Keyword + Vector)
* Docker Deployment

---

## Live Demo

Add your deployed Streamlit URL here:

 < https://docmind-z8slyvhplls9z4zzc3hutu.streamlit.app/>

---

## Author

K

Aspiring AI Engineer focused on:

* Retrieval-Augmented Generation (RAG)
* AI Agents
* LLM Applications
* Generative AI Engineering
* Full Stack AI Systems

---

## License

This project is licensed under the MIT License.


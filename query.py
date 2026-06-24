import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI,
)

from langchain_community.vectorstores import FAISS

load_dotenv()

print("Loading vector database...")

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

db = FAISS.load_local("vectorstore", embeddings, allow_dangerous_deserialization=True)

question = input("Enter your question: ")

dcos = db.similarity_search(question, k=3)

print("\nRetrieved documents:\n")

for i, doc in enumerate(dcos, start=1):
    print(f"Document {i}:")
    print(doc.page_content[:300])
    print("\n---\n")\
    
context = "\n\n".join([doc.page_content for doc in dcos])

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

prompt = f"""
Answer only using the context below.

context:
{context}

Question:
{question}
"""

response = llm.invoke(prompt)

print("\nSources:\n")

seen = set()

for doc in dcos:
    source = doc.metadata.get("source", "Unknown")
    page = doc.metadata.get("page", 0)

    key = (source, page)

    if key not in seen:
        seen.add(key)

        print(
            f"📄 {os.path.basename(source)} | Page {page + 1}"
        )

print("\nAnswer:\n")
print(response.content)




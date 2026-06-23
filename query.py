import os
from dotenv import load_dotenv

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

llm=ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
)

prompt = f"""
Answer only using the context below.

context:
{context}

Question:
{question}
"""

response = llm.invoke(prompt)

print("\nAnswer:\n")
print(response.content)




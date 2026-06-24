import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq


load_dotenv()

client = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
)

models = client.models.list()

for model in models:
    print(model.id)



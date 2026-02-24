from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

import os

DATA_PATH = "data"
DB_PATH = "vector_db"

documents = []

for file in os.listdir(DATA_PATH):
    path = os.path.join(DATA_PATH, file)
    if file.endswith(".pdf"):
        loader = PyPDFLoader(path)
    elif file.endswith(".txt"):
        loader = TextLoader(path)
    else:
        continue
    documents.extend(loader.load())

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(documents)

embeddings = OllamaEmbeddings(model="nomic-embed-text")

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=DB_PATH
)

print("✅ Documents ingested successfully!")
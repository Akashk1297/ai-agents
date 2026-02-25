<!-- AI Agent to understand internal documentation using Llama (Meta’s LLM) can be done locally on both Linux and Windows using tools like Ollama, LangChain, and a vector database.
Your AI Agent will work like this:
📄 Load Internal Docs (PDF, DOCX, TXT, MD)
✂️ Split into chunks
🔎 Convert to embeddings
🗄 Store in Vector DB (Chroma)
🤖 Use Llama to answer questions
💬 Chat interface (CLI or Web)
This approach is called RAG (Retrieval-Augmented Generation).
-->

# Install Python (if not installed)
```sudo apt install python3 python3-pip
```

# Create Virtual Environment
```python -m venv venv
source venv/scripts/activate
```

# Install Required Libraries
```pip install langchain chromadb pypdf python-docx sentence-transformers langchain-community langchain-text-splitters langchain-ollama langchain-chroma chromadb
```

# Pull & run the model
```
ollama pull llama3
ollama pull nomic-embed-text
ollama run llama3
```

# Create Project Structure
```
ai-doc-agent/
│
├── data/               # Put internal docs here
├── ingest.py           # Loads + embeds docs
├── agent.py            # Chat agent
├── ReadMe.md
├── vector_db          

```

# Create ingest.py
<!--
This script:
- Loads documents
- Splits into chunks
- Creates embeddings
- Stores in Chroma
-->
```
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
```
# run ingestion:
```python ingest.py```

# Create agent.py (Chat AI Agent)
```
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

DB_PATH = "vector_db"

# Embeddings
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# Load Vector DB
vectorstore = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever()

# LLM
llm = OllamaLLM(model="llama3")

# Prompt Template
prompt = ChatPromptTemplate.from_template("""
You are an AI assistant answering questions based only on the provided context.

Context:
{context}

Question:
{question}

Answer clearly and concisely.
""")

# RAG Chain
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

print("🤖 AI Agent Ready! Type 'exit' to quit.\n")

while True:
    query = input("You: ")
    if query.lower() == "exit":
        break

    docs = retriever.invoke(query)
    context = format_docs(docs)

    chain = prompt | llm | StrOutputParser()

    response = chain.invoke({
        "context": context,
        "question": query
    })

    print("\nAI:", response)
```

# run the agent:
```python agent.py```
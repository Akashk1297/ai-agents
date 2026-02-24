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
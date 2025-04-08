# movie_bot.py

import os
from dotenv import load_dotenv
from langchain_community.document_loaders import CSVLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain.chains import RetrievalQA

# Load environment variables (if needed)
load_dotenv()

# Load movie data from CSV
loader = CSVLoader(file_path="movies.csv")
documents = loader.load()
print(f"Loaded {len(documents)} movie descriptions.")

# Use HuggingFace embeddings (local, free)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Create vector store
db = FAISS.from_documents(documents, embeddings)

# Set up retriever and local LLM (Gemma 2B)
retriever = db.as_retriever()
llm = ChatOllama(model="gemma:2b", temperature=0.5)

# Create QA Chain
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# Chat loop
while True:
    query = input("\nAsk something about movies (or type 'exit'): ")

    # Exit early before retrieval
    if query.lower() == 'exit':
        print("👋 Exiting the movie assistant. See you!")
        break

    # Show retrieved documents
    docs = retriever.invoke(query)
    print("\n Retrieved context:")
    for i, doc in enumerate(docs, 1):
        print(f"{i}. {doc.page_content}")

    # Get response
    response = qa_chain.invoke(query)

    # Print only the final result (clean)
    print("\n🤖 Recommendation:", response['result'])



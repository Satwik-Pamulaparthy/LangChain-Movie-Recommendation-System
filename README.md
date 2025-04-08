# LangChain - Movie Recommendation System

LangChain is a powerful open-source framework designed to help developers build LLM-powered applications quickly and efficiently. It allows for chaining multiple steps, managing conversation context, integrating with vector databases, and building intelligent agents.

##  Features
-  Uses vector similarity to retrieve movie info from a CSV file
-  Processes natural language questions using a local LLM (via Ollama)
-  Vector storage powered by FAISS
-  Embeddings generated using HuggingFace (`all-MiniLM-L6-v2`)
-  No internet required

##  Getting Started
Clone this repo
```bash
git clone [https://github.com/Satwik-Pamulaparthy/langchain-movie-recommender.git]
cd langchain-movie-recommender
```
## Install Dependencies:
``` bash
pip install -r requirements.txt
```
## Download the model:
``` bash
ollama pull gemma:2b
```
## Run the Assistant:
``` bash
python .\langchain_movie_recommender.py
```
## Sample Prompt:
``` bash
Ask something about movies (or type 'exit'): Suggest a time-travel movie
```
## Sample Output:
``` bash
Retrieved context:
1. Tenet, "A secret agent manipulates time..."
2. Interstellar, "A team travels through a wormhole..."
🤖 Recommendation: The context describes movies about time travel...
```



Feel free to fork, contribute, or customize it for your own movie assistant project!
- Satwik Pamulaparthy

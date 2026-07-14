
# Steps to run the local AI agent

## Install Python, recommend version 3.10 and 3.13
```
sudo apt install python3 python3-pip
```

## Create Virtual Environment
```
python -m venv venv
source venv/bin/activate
```

## Install Required Libraries
```
pip install langchain chromadb pypdf python-docx sentence-transformers ollama
```

## Run ai agent python script
```
./agent_ollama1.py #prompt is hardcoded
```

```
./agent_ollama2.py #promt has to be given as user input during runtime
```

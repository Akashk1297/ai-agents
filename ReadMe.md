
  # Ensure version is between 3.10 and 3.13
python3 --version
pip install virtualenv

python -m venv .ai_sandbox
source .ai_sandbox/Scripts/activate

pip install crewai

git clone https://github.com/joaomdmoura/crewAI.git
cd crewAI/examples/metaquest_knowledge
locate metaquest_knowledge

mv "/c/Users/akash/Downloads/9 A- B - Chemistry - Lesson 14 - Oxides of carbon ( part 1).pdf" ./knowledge


####

# Install Python (if not installed)
sudo apt install python3 python3-pip

# Create Virtual Environment
python -m venv venv
source venv/bin/activate

# STEP 3: Install Required Libraries
pip install langchain chromadb pypdf python-docx sentence-transformers ollama


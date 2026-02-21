from strands import Agent
from strands.models.ollama import OllamaModel

ollama_model = OllamaModel(
    host="http://localhost:11434",
    model_id="llama3.1:latest"
)

agent=Agent(model=ollama_model)
agent("Hello how are u?")

# Ask the agent a question
result = Agent("What operating system am I using?")

# Print only the last response
print(result)
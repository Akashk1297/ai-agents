from strands import Agent
from strands.models.ollama import OllamaModel
from strands_tools import http_request

# local llm
ollama_model = OllamaModel(
    host="http://localhost:11434",
    model_id="llama3.1:latest",
    tools=[http_request]
)

system_prompt = "Answer in a polite and respectful tone"
agent=Agent(model=ollama_model,system_prompt=system_prompt,tools=[http_request])

# Ask the agent a question
user_input=input("You: ")

# Print only the last response
agent(user_input)
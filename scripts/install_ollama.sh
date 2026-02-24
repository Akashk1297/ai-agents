#!/bin/bash

OS_NAME=$(uname -s)
case "${OS_NAME}" in
    Linux*)
        if [ $(uname -r | grep -q "Microsoft")$? -eq 0 ]; then
            echo "Running on Windows Subsystem for Linux (WSL)";
        else
            echo "Running on native Linux";
            linux_configure
        fi
        ;;
    Darwin*)
        echo "Running on Mac";
        ;;
    CYGWIN*|MINGW*|MSYS_NT*)
        echo "Running on Windows (Cygwin/Git Bash/MSYS)";
        echo "This script is currently designed for Ubuntu Linux";
        ;;
    *)
        echo "Unknown OS: ${OS_NAME}";
        ;;
esac

linux_configure () {
    # Install python
    sudo apt update
    sudo apt install python3

    #Install strands sdk & tools
    apt install -y python3.12-venv
    python -m venv .venv
    apt install -y pipx
    pipx install strands-agents
    pip install strands-agents-tools strands-agents-builder

    #Installing and starting Ollama model
    pipx install 'strands-agents[ollama]' strands-agents-tools
    curl -fsSL https://ollama.com/install.sh | sh
    ollama pull llama3.1
    ollama serve
    docker pull ollama/ollama
    ollama list
    docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
    docker exec -it ollama ollama pull llama3.1
    curl http://localhost:11434/api/tags
}
from autogen import ConversableAgent
from openai import OpenAI
import os

# Carrega a chave da API e # verifica se o carregamento deu certo
api_key = os.getenv("OPENAI_API_KEY").strip()  # Remove qualquer caractere extra
if not api_key:
    print("Erro: chave da API não encontrada.")
    exit(1)


# LLM config
llm_config = {
    "model": "gpt-3.5-turbo",
    "api_key": api_key
}


directCommunicationAgent = ConversableAgent(
    name = "DirectCommunication",
    llm_config = llm_config,
    system_message = 
        "You are a communicator." +
        "You operate in a sports betting system." +
        "You receive messages and forward them to the user."
)
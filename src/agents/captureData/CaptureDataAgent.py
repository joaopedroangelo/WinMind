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


captureDataAgent = ConversableAgent(
    name = "CaptureData",
    llm_config = llm_config,
    system_message = 
        "You operate in a sports betting system" +
        "Its responsibility is to collect user data and pass it on to the monitor for analysis."
)
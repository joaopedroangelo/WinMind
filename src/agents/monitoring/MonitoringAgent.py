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


monitoringAgent = ConversableAgent(
    name = "Monitor",
    llm_config = llm_config,
    system_message = 
        "You monitor a sports betting system." +
        "Based on the data you receive, you should identify cases of compulsive gambling." +
        "You also pass some data to the feedback agent."
)
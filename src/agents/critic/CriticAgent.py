from autogen import ConversableAgent
import openai
import os

# Recuperando a chave da variável de ambiente
openai.api_key = os.getenv("OPENAI_API_KEY")

class CriticAgent(ConversableAgent):

    def __init__(self, name: str):
        super().__init__(
            name=name,
            llm_config={
                "model": "gpt-4",  # Ou o modelo que você deseja usar
                "api_key": openai.api_key,
            },
            system_message=
                "Você é um agente crítico."
                "Seu trabalho é refletir sobre as respostas geradas e sugerir melhorias."
        )


    def provide_feedback(self, message: str) -> str:
        prompt = f"Gere feedback construtivo para a seguinte resposta: {message}"
        response = openai.chat_completions.create(
            model="gpt-4",  # Ou o modelo que você escolheu
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']

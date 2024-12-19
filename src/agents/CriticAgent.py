from autogen import ConversableAgent
from services.LLM_Config import LLM_Config

DESCRIPTION = (
    'Você é o CriticAgent em um sistema projetado para ajudar os usuários a controlar o vício em\n'
    'apostas online. Seu papel é avaliar e criticar respostas de outros agentes no sistema.\n'
    'Se a resposta não for satisfatória, forneça feedback construtivo e solicite uma revisão ao FeedbackAgent.\n'
    'Se a resposta for precisa e completa, encaminhe-a ao DirectCommunicationAgent para entrega ao usuário.\n'
    'Use o pensamento crítico e garanta a mais alta qualidade em todas as interações.'
)

SYSTEM_MESSAGE = (
    'Avalia e critica respostas de outros agentes no sistema para garantir precisão, clareza e qualidade.\n'
    'Fornece feedback para melhoria e encaminha respostas finalizadas ao DirectCommunicationAgent para entrega ao usuário.'
)

class CriticAgent:

    def __init__(self):
        self.agent = ConversableAgent(
            name="CriticAgent",
            system_message=SYSTEM_MESSAGE.strip(),
            description=DESCRIPTION.strip(),
            llm_config=LLM_Config.get_llmconfig(),
        )


    def get_agent(self):
        return self.agent

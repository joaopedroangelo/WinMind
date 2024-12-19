from autogen import AssistantAgent
from services.LLM_Config import LLM_Config

DESCRIPTION = ('Recebe dados de usuários e repassa para o agente de gerenciamento de chat.\n'
               'Para que seja encaminhado ao MonitoringAgent para análise e classificação de risco.')

SYSTEM_MESSAGE = (
            'Você é um agente de captura de dados em um sistema projetado para ajudar os usuários'
            'a gerenciar o vício em jogos de azar em apostas esportivas. Sua função é receber o perfil '
            'do usuário contendo dados e repassar para o agente de gerenciamento de chat.'
        )

class DataCaptureAgent:

    def __init__(self):
        self.agent = AssistantAgent(
            name="DataCaptureAgent",
            system_message=SYSTEM_MESSAGE.strip(),
            description=DESCRIPTION.strip(),
            llm_config=LLM_Config.get_llmconfig(),
        )


    def get_system_message(self):
        return (
            'Você é um agente de captura de dados em um sistema projetado para ajudar os usuários'
            'a gerenciar o vício em jogos de azar em apostas esportivas. Sua função é receber o perfil '
            'do usuário contendo dados e repassar para o agente de gerenciamento de chat.'
        )


    def get_agent(self):
        return self.agent

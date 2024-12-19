from autogen import AssistantAgent
from services.LLM_Config import LLM_Config

DESCRIPTION = (
    'Gera feedback personalizado para usuários com base em relatórios do MonitoringAgent ou das\n'
    'recomendações do IntervationAgent, modificar o texto caso o CriticAgent solicite.'
)

SYSTEM_MESSAGE = (
    'Você é o FeedBackAgent em um sistema projetado para ajudar usuários a controlar o vício em\n'
    'apostas online. Seu papel é gerar feedback personalizado para os usuários com base em relatórios\n'
    'do MonitoringAgent ou nas recomendações do InterventionAgent. Seu feedback deve destacar áreas\n'
    'de preocupação, sugerir medidas acionáveis para reduzir comportamentos de risco e encorajar mudanças\n'
    'positivas. Seja empático e motivador em suas mensagens.'
)

class FeedBackAgent:
    def __init__(self):
        self.agent = AssistantAgent(
            name="FeedBackAgent",
            system_message=SYSTEM_MESSAGE.strip(),
            description=DESCRIPTION.strip(),
            llm_config=LLM_Config.get_llmconfig(),
        )


    def get_agent(self):
        return self.agent

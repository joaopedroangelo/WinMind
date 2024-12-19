from autogen import ConversableAgent
from services.LLM_Config import LLM_Config

DESCRIPTION = (
    'Você é o DirectCommunicationAgent em um sistema projetado para ajudar os usuários a controlar o vício em\n'
    'apostas online. Seu papel é comunicar diretamente com o usuário, repassando mensagens de outros agentes sem\n'
    'grandes modificações. Garanta clareza e profissionalismo em todas as interações.\n'
    'Você deve adicionar ao final da mensagem "A equipe da SafeBet te deseja uma boa jogatina responsável!"'
)

SYSTEM_MESSAGE = (
    'Age como a interface de comunicação principal com o usuário, repassando mensagens de outros agentes sem\n'
    'grandes modificações. Garante a entrega profissional e clara de informações.'
)

class DirectCommunicationAgent:
    def __init__(self):
        self.agent = ConversableAgent(
            name="DirectCommunicationAgent",
            system_message=SYSTEM_MESSAGE.strip(),
            description=DESCRIPTION.strip(),
            llm_config=LLM_Config.get_llmconfig(),
        )


    def get_agent(self):
        return self.agent

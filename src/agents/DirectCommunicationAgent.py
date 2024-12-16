from autogen import ConversableAgent
from services.LLM_Config import LLM_Config

class DirectCommunicationAgent:
    
    def __init__(self):
        self.system_message = """
        You are the DirectCommunicationAgent in a system designed to help users manage gambling addiction in sports betting.
        Your role is to directly communicate with the user, relaying messages from other agents without modification.
        You must ensure clarity and professionalism in all interactions.
        """
        self.name = "DirectCommunicationAgent"
        self.llm_config = LLM_Config.get_llmconfig()
        # Criando a instância de ConversableAgent no momento da inicialização
        self.agentConversable = self.get_agent()


    def get_agent(self):
        return ConversableAgent(name=self.name,
                              system_message=self.system_message,
                              llm_config=self.get_llmconfig
                              )

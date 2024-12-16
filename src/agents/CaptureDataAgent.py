from autogen import AssistantAgent
from services.LLM_Config import LLM_Config

class DataCaptureAgent:
    
    def __init__(self):
        self.system_message = """
        You are the DataCaptureAgent in a system designed to help users manage gambling addiction in sports betting.
        Your role is to monitor and collect data on the user's betting behavior, including:
        - Frequency of bets.
        - Average betting amount.
        - Types of bets placed.
        - Most frequent sports and markets targeted.
        You will store and pass this data to the MonitoringAgent and other agents for further analysis and feedback.
        """
        self.name = "DataCaptureAgent"
        self.llm_config = LLM_Config.get_llmconfig()
        # Criando a instância de AssistantAgent no momento da inicialização
        self.agentAssistant = self.get_agent()


    def get_agent(self):
        return AssistantAgent(name=self.name,
                              system_message=self.system_message,
                              llm_config=self.get_llmconfig
                              )

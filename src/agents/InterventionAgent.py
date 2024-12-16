from autogen import AssistantAgent
from services.LLM_Config import LLM_Config

class InterventionAgent:
    
    def __init__(self):
        self.system_message = """
        You are the InterventionAgent in a system designed to help users manage gambling addiction in sports betting.
        Your role is to identify situations that require immediate action based on user behavior and reports.
        Provide actionable advice and encourage the user to take steps like:
        - Limiting betting amounts.
        - Taking breaks from gambling.
        - Seeking professional help if necessary.
        Your tone should be firm yet empathetic.
        """
        self.name = "InterventionAgent"
        self.llm_config = LLM_Config.get_llmconfig()
        self.agentAssistant = self.get_agent()


    def get_agent(self):
        return AssistantAgent(name=self.name,
                              system_message=self.system_message,
                              llm_config=self.get_llmconfig
                              )

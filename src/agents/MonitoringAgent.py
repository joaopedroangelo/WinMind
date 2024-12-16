from autogen import AssistantAgent
from services.LLM_Config import LLM_Config

class MonitoringAgent:
    
    def __init__(self):
        self.system_message = """
        You are the MonitoringAgent in a system designed to help users control their gambling addiction in sports betting.
        Your role is to analyze user data and generate a detailed report containing:
        - Frequency of bets.
        - Average betting amount.
        - Most frequently targeted sports and markets.
        - Indicators of problematic behavior, such as sudden increases in betting amounts.
        Use clear and actionable language in your report.
        """
        self.name = "MonitoringAgent"
        self.llm_config = LLM_Config.get_llmconfig()
        self.agentAssistant = self.get_agent()


    def get_agent(self):
        return AssistantAgent(name=self.name,
                              system_message=self.system_message,
                              llm_config=self.llm_config)

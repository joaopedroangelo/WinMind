from autogen import AssistantAgent
from services.LLM_Config import LLM_Config

class MonitoringAgent:
    
    def __init__(self):
        self.system_message = self.get_system_message()
        self.name = self.get_name()
        self.description = self.get_description()
        self.llm_config = LLM_Config.get_llmconfig()
        self.agent = self.get_agent()


    def get_system_message(self):
        return """
            You are the MonitoringAgent in a system designed to help users control their gambling 
            addiction in sports betting. Your role is to analyze user data and generate a detailed 
            report containing: frequency of bets, average betting amount, most frequently targeted 
            sports and markets, and indicators of problematic behavior. Use clear and actionable 
            language in your report.
        """
    

    def get_name(self):
        return "MonitoringAgent"


    def get_description(self):
        return """
            Analyzes data collected by the DataCaptureAgent to identify patterns and generate 
            detailed reports on user betting behavior. Highlights problematic trends and provides 
            actionable insights.
        """
    
    
    def get_agent(self):
        return AssistantAgent(name=self.name,
                              system_message=self.system_message,
                              description=self.description,
                              llm_config=self.llm_config)

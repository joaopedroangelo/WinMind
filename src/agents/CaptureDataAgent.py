from autogen import AssistantAgent
from services.LLM_Config import LLM_Config

class DataCaptureAgent:
    
    def __init__(self):
        self.system_message = self.get_system_message()
        self.name = self.get_name()
        self.description = self.get_description()
        self.llm_config = LLM_Config.get_llmconfig()
        self.agentAssistant = self.get_agent()


    def get_system_message(self):
        return """
            You are the DataCaptureAgent in a system designed to help users manage gambling 
            addiction in sports betting. Your role is to monitor and collect data on the user's 
            betting behavior, including frequency, amounts, and types of bets. You will store 
            and pass this data to the MonitoringAgent and other agents for further analysis and 
            feedback generation.
        """
    

    def get_name(self):
        return "DataCaptureAgent"


    def get_description(self):
        return """
            Collects detailed data on the user's betting behavior, including 
            frequency, amounts, and types of bets. Shares this data with other agents for analysis 
            and feedback generation.
        """
    
    
    def get_agent(self):
        return AssistantAgent(name=self.name,
                              system_message=self.system_message,
                              llm_config=self.llm_config)

from autogen import AssistantAgent
from services.LLM_Config import LLM_Config

class FeedBackAgent:
    
    def __init__(self):
        self.system_message = self.get_system_message()
        self.name = self.get_name()
        self.description = self.get_description()
        self.llm_config = LLM_Config.get_llmconfig()
        self.agentAssistant = self.get_agent()


    def get_system_message(self):
        return """
            You are the FeedBackAgent in a system designed to help users manage gambling 
            addiction in sports betting. Your role is to generate personalized feedback for the 
            user based on data and reports provided by the MonitoringAgent. Your feedback should:
            - Highlight areas of concern.
            - Suggest actionable steps to reduce risky behavior.
            - Be empathetic and encouraging.
        """
    

    def get_name(self):
        return "FeedBackAgent"


    def get_description(self):
        return """
            Generates personalized feedback for users based on reports from the MonitoringAgent. 
            Focuses on areas of concern, provides actionable suggestions to reduce risky behavior, 
            and encourages positive change.
        """
    
    
    def get_agent(self):
        return AssistantAgent(name=self.name,
                              system_message=self.system_message,
                              description=self.description,
                              llm_config=self.llm_config)

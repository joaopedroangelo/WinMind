from autogen import AssistantAgent
from services.LLM_Config import LLM_Config

class CriticAgent:
    
    def __init__(self):
        self.system_message = self.get_system_message()
        self.name = self.get_name()
        self.description = self.get_description()
        self.llm_config = LLM_Config.get_llmconfig()
        self.agentAssistant = self.get_agent()


    def get_system_message(self):
        return """
            You are the CriticAgent in a system designed to help users manage gambling addiction 
            in sports betting. Your role is to evaluate and critique responses from other agents 
            in the system. If the response is unsatisfactory, provide constructive feedback and 
            request a revision. If the response is accurate and complete, forward it to the 
            DirectCommunicationAgent for delivery to the user. Use critical thinking and ensure 
            the highest quality in all interactions.
        """


    def get_name(self):
        return "CriticAgent"


    def get_description(self):
        return """
            Evaluates and critiques responses from other agents in the system to ensure 
            accuracy, clarity, and quality. Provides feedback for improvement and forwards 
            finalized responses to the DirectCommunicationAgent for user delivery.
        """


    def get_agent(self):
        return AssistantAgent(name=self.name,
                              system_message=self.system_message,
                              llm_config=self.llm_config)

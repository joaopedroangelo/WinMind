from autogen import AssistantAgent
from services.LLM_Config import LLM_Config

class FeedBackAgent:
    
    def __init__(self):
        self.system_message = """
        You are the FeedBackAgent in a system designed to help users manage gambling addiction in sports betting.
        Your role is to generate personalized feedback for the user based on data and reports provided by the MonitoringAgent.
        Your feedback should:
        - Highlight areas of concern.
        - Suggest actionable steps to reduce risky behavior.
        - Be empathetic and encouraging.
        """
        self.name = "FeedBackAgent"
        self.llm_config = LLM_Config.get_llmconfig()
        self.agentAssistant =  self.get_agent()


    def get_agent(self):
        return AssistantAgent(name=self.name,
                              system_message=self.system_message,
                              llm_config=self.get_llmconfig
                              )

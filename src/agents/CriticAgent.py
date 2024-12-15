from autogen import AssistantAgent
import os

class CriticAgent:
    
    def __init__(self):
        self.system_message = """
        You are the CriticAgent in a system designed to help users manage gambling addiction in sports betting.
        Your role is to evaluate and critique responses from other agents in the system. 
        If the response is unsatisfactory, provide constructive feedback and request a revision. 
        If the response is accurate and complete, forward it to the DirectCommunicationAgent for delivery to the user.
        Use critical thinking and ensure the highest quality in all interactions.
        """


    @staticmethod
    def get_llmconfig():
        api_key = os.getenv("OPENAI_API_KEY").strip()
        if not api_key:
            print("Error: API key not found.")
            exit(1)
        llm_config = {
            "model": "gpt-3.5-turbo",
            "api_key": api_key
        }
        return llm_config


    def get_agent(self):
        return AssistantAgent(name="CriticAgent",
                              system_message=self.system_message,
                              llm_config=self.get_llmconfig
                              )

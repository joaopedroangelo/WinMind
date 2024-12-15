from autogen import AssistantAgent
import os

class DirectCommunicationAgent:
    def __init__(self):
        self.system_message = """
        You are the DirectCommunicationAgent in a system designed to help users manage gambling addiction in sports betting.
        Your role is to directly communicate with the user, relaying messages from other agents without modification.
        You must ensure clarity and professionalism in all interactions.
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
        return AssistantAgent(name="DirectCommunicationAgent",
                              system_message=self.system_message,
                              llm_config=self.get_llmconfig
                              )

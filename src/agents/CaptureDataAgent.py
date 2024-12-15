from autogen import AssistantAgent
import os

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
        return AssistantAgent(name="DataCaptureAgent",
                              system_message=self.system_message,
                              llm_config=self.get_llmconfig
                              )

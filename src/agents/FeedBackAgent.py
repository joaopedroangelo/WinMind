from autogen import AssistantAgent
import os

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
        return AssistantAgent(name="FeedBackAgent",
                              system_message=self.system_message,
                              llm_config=self.get_llmconfig
                              )

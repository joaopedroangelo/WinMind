from autogen import AssistantAgent
import os

class InterventionAgent:
    def __init__(self):
        self.system_message = """
        You are the InterventionAgent in a system designed to help users manage gambling addiction in sports betting.
        Your role is to identify situations that require immediate action based on user behavior and reports.
        Provide actionable advice and encourage the user to take steps like:
        - Limiting betting amounts.
        - Taking breaks from gambling.
        - Seeking professional help if necessary.
        Your tone should be firm yet empathetic.
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
        return AssistantAgent(name="InterventionAgent",
                              system_message=self.system_message,
                              llm_config=self.get_llmconfig
                              )

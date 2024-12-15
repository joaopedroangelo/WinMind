from autogen import AssistantAgent
import os

class MonitoringAgent:
    def __init__(self):
        self.system_message = """
        You are the MonitoringAgent in a system designed to help users control their gambling addiction in sports betting.
        Your role is to analyze user data and generate a detailed report containing:
        - Frequency of bets.
        - Average betting amount.
        - Most frequently targeted sports and markets.
        - Indicators of problematic behavior, such as sudden increases in betting amounts.
        Use clear and actionable language in your report.
        """


    @staticmethod
    def get_llmconfig():
        api_key = os.getenv("OPENAI_API_KEY").strip()
        if not api_key:
            print("Erro: chave da API não encontrada.")
            exit(1)
        llm_config = {
            "model": "gpt-3.5-turbo",
            "api_key": api_key
        }
        return llm_config



    def get_agent(self):
        return AssistantAgent(name="MonitoringAgent",
                              system_message=self.system_message,
                              llm_config=self.get_llmconfig
                              )
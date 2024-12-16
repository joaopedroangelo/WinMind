from autogen import AssistantAgent
from services.LLM_Config import LLM_Config

class InterventionAgent:
    
    def __init__(self):
        self.system_message = self.get_system_message
        self.name = self.get_name
        self.description = self.get_description
        self.llm_config = LLM_Config.get_llmconfig()
        self.agentAssistant = self.get_agent()


    def get_system_message():
        return """
            You are the InterventionAgent in a system designed to help users manage 
            gambling addiction in sports betting.
            Your role is to identify situations that require immediate action based on user 
            behavior and reports.
            Provide actionable advice and encourage the user to take steps like:
            - Limiting betting amounts.
            - Taking breaks from gambling.
            - Seeking professional help if necessary.
            Your tone should be firm yet empathetic.
        """


    def get_name():
        return "InterventionAgent"

    def get_description():
        return """
            Identifies situations requiring immediate action based on user behavior and monitoring
            reports.
            Delivers firm yet empathetic advice to help users take steps such as setting limits or
            seeking professional help.
        """


    def get_agent(self):
        return AssistantAgent(name=self.name,
                              system_message=self.system_message,
                              llm_config=self.get_llmconfig
                              )

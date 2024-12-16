from autogen import ConversableAgent
from services.LLM_Config import LLM_Config

class DirectCommunicationAgent:
    
    def __init__(self):
        self.system_message = self.get_system_message()
        self.name = self.get_name()
        self.description = self.get_description()
        self.llm_config = LLM_Config.get_llmconfig()
        self.agent = self.get_agent()


    def get_system_message(self):
        return """
            You are the DirectCommunicationAgent in a system designed to help users manage 
            gambling addiction in sports betting. Your role is to directly communicate with 
            the user, relaying messages from other agents without modification. You must ensure 
            clarity and professionalism in all interactions.
        """


    def get_name(self):
        return "DirectCommunicationAgent"


    def get_description(self):
        return """
            Acts as the primary communication interface with the user, relaying messages from 
            other agents without modification. Ensures professional and clear delivery of information.
        """

    
    def get_agent(self):
        return ConversableAgent(name=self.name,
                                system_message=self.system_message,
                                description=self.description,
                                llm_config=self.llm_config)


    def send_direct(self, message):
        print(message)
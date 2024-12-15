class DirectCommunicationService:

    def __init__(self, direct_communication_agent):
        self.direct_communication_agent = direct_communication_agent
    

    def deliver_message(self, message):
        # Envia a mensagem para o DirectCommunicationAgent entregar ao usuário
        if not message:
            print("Error: No message to deliver.")
            return None    
        self.direct_communication_agent.generate_message(message)

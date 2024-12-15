class CritiqueService:

    def __init__(self, critic_agent):
        self.critic_agent = critic_agent
    

    def critique_responses(self, feedback):
        # Envia o feedback para o CriticAgent avaliar
        if not feedback:
            print("Error: No feedback to critique.")
            return None    
        critique = self.critic_agent.generate_message(feedback)
        # Validar a crítica gerada
        if not critique:
            print("Error: No critique generated.")
            return None
        return critique

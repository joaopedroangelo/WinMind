class FeedbackService:
    
    def __init__(self, feedback_agent):
        self.feedback_agent = feedback_agent
    

    def generate_feedback(self, monitoring_report):
        # Envia o relatório para o FeedBackAgent para gerar feedback
        if not monitoring_report:
            print("Error: No monitoring report to generate feedback.")
            return None    
        feedback = self.feedback_agent.generate_message(monitoring_report)
        # Validar o feedback gerado
        if not feedback:
            print("Error: No feedback generated.")
            return None
        return feedback

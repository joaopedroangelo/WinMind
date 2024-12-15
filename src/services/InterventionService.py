class InterventionService:
    
    def __init__(self, intervention_agent):
        self.intervention_agent = intervention_agent
    

    def suggest_intervention(self, monitoring_report):
        # Envia o relatório para o InterventionAgent para sugerir intervenções
        if not monitoring_report:
            print("Error: No monitoring report to suggest intervention.")
            return None    
        intervention = self.intervention_agent.generate_message(monitoring_report)
        # Validar a sugestão de intervenção
        if not intervention:
            print("Error: No intervention suggested.")
            return None
        return intervention

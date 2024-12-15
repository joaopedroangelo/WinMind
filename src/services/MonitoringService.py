class MonitoringService:
    
    def __init__(self, monitoring_agent):
        self.monitoring_agent = monitoring_agent
    

    def analyze_data(self, data):
        # Envia os dados para o agente de monitoramento para gerar o relatório
        if not data:
            print("Error: No data to analyze.")
            return None    
        monitoring_report = self.monitoring_agent.generate_message(data)
        # Validar o relatório gerado
        if not monitoring_report:
            print("Error: No monitoring report generated.")
            return None
        return monitoring_report

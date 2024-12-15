class DataCaptureService:
    
    def __init__(self, data_capture_agent):
        self.data_capture_agent = data_capture_agent
    

    def collect_data(self):
        # Aqui você pode implementar a lógica de coleta de dados
        # Chama o agente para coletar os dados do usuário
        data = self.data_capture_agent.generate_message("Collect user data for analysis.")    
        # Valida os dados coletados (se necessário)
        if not data:
            print("Error: No data collected.")
            return None
        return data

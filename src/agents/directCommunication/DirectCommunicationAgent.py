import time
from autogen import Agent, Message

class DirectCommunicationAgent(Agent):

    # Construtor
    def __init__(self, name):
        super().__init__(name)
    

    def process_message(self, message: Message):
        """
        Método para processar mensagens recebidas de outros agentes
        e enviá-las para o usuário. Este método pode ser chamado
        quando o agente recebe uma mensagem de qualquer outro agente.
        """
        # Aqui, você pode personalizar como processar as mensagens.
        # Vamos assumir que a mensagem possui um conteúdo textual.
        print(f"{self.name} recebeu uma mensagem: {message.content}")
        
        # Envia a mensagem para o usuário (no caso, imprimindo-a)
        self.send_to_user(message.content)


    def send_to_user(self, message_content):
        """
        Método para enviar a mensagem para o usuário.
        Aqui, você pode integrar com qualquer sistema de interface com o usuário.
        No exemplo, apenas imprimimos a mensagem.
        """
        print(f"Enviando mensagem para o usuário: {message_content}")
        # Adicionar lógica de envio real aqui (e.g., API de interface com o usuário)


    def run(self):
        """
        Método que mantém o agente em execução, esperando por novas mensagens.
        """
        while True:
            # Aqui o agente ficaria aguardando por novas mensagens.
            # Este é um exemplo simples; o AutoGen tem seus próprios métodos para receber mensagens.
            time.sleep(5)  # Aguardar 5 segundos antes de verificar por novas mensagens.

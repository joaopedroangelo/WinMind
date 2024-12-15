# Classe utilitária para calcular o custo dos tokens usados
class TokenCostCalculator:

    def __init__(self):
        """
        Inicializa a classe com valores padrão para o custo por token e quantidade de tokens.
        """
        # Definindo o custo por token baseado nos preços padrão da OpenAI (exemplo fictício)
        self.cost_per_token = 0.0004  # Exemplo de custo por token


    def calculate_cost(self, tokens_used: int) -> float:
        """
        Método auxiliar para calcular o custo com base no número de tokens usados.
        :param tokens_used: O número total de tokens usados.
        :return: O custo total em moeda.
        """
        return tokens_used * self.cost_per_token


    def get_cost_breakdown(self, token_usage: dict) -> dict:
        """
        Método que recebe o dicionário de uso de tokens e calcula os custos para cada parte.
        :param token_usage: Um dicionário contendo o número de tokens usados no prompt e na resposta.
        :return: Um dicionário com os custos para cada parte e o total.
        """
        cost_prompt = self.calculate_cost(token_usage['prompt_tokens'])
        cost_response = self.calculate_cost(token_usage['completion_tokens'])
        total_cost = self.calculate_cost(token_usage['total_tokens'])
        return {
            'cost_prompt': cost_prompt,
            'cost_response': cost_response,
            'total_cost': total_cost
        }


    def calculate_cost_from_conversation(self, conversation: list) -> dict:
        """
        Método que recebe uma conversa (lista de mensagens) e calcula os custos.
        :param conversation: Uma lista de mensagens trocadas entre os agentes.
        :return: Um dicionário com o custo detalhado por parte da conversa.
        """
        # Calculando os tokens utilizados na conversa
        prompt_tokens = sum(len(message['content'].split()) for message in conversation if message['role'] == 'user')
        completion_tokens = sum(len(message['content'].split()) for message in conversation if message['role'] == 'assistant')
        total_tokens = prompt_tokens + completion_tokens
        # Criando o dicionário com os tokens usados na conversa
        token_usage = {
            'total_tokens': total_tokens,
            'prompt_tokens': prompt_tokens,
            'completion_tokens': completion_tokens
        }
        # Retornando a breakdown do custo baseado na conversa
        return self.get_cost_breakdown(token_usage)


    def calculate_cost_from_tokens(self, prompt_tokens: int, completion_tokens: int) -> dict:
        """
        Método que recebe diretamente o número de tokens usados no prompt e na resposta, e calcula os custos.
        :param prompt_tokens: O número de tokens usados no prompt.
        :param completion_tokens: O número de tokens usados na resposta.
        :return: Um dicionário com o custo detalhado para prompt, resposta e total.
        """
        total_tokens = prompt_tokens + completion_tokens
        token_usage = {
            'total_tokens': total_tokens,
            'prompt_tokens': prompt_tokens,
            'completion_tokens': completion_tokens
        }
        return self.get_cost_breakdown(token_usage)

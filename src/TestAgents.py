from agents.CriticAgent import CriticAgent

critic_agent = CriticAgent()
message = "The user has a problem with gambling, and we should just tell them to stop betting."
review = critic_agent.generate_review(message)
print(review)

# Enviar a mensagem para o DirectCommunicationAgent
critic_agent.forward_to_direct_communication("OPA")

# O resultado esperado é que o DirectCommunicationAgent imprima a mensagem recebida.

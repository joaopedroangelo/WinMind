from agents.CriticAgent import CriticAgent

critic_agent = CriticAgent()
message = "The user has a problem with gambling, and we should just tell them to stop betting."
review = critic_agent.generate_review(message)
print(review)

# Guia de Apresentação do WinMind

> Slides: https://www.canva.com/design/DAGZYZspJIY/oklmQeol3FR3ev468I-Zgw/edit?ui=eyJFIjp7IkE_IjoiTiIsIlMiOiJBQUZTM2R6a0NVVSIsIlQiOjd9fQ

---
### Slide 01 e 02 *(1 minuto)*
Realizar uma apresentação abrangente sobre o sistema **WinMind**, destacando o potencial do framework **AutoGen** e sua evolução com o **AG2**,
seguida por uma análise do problema do vício em apostas e como o WinMind o aborda.

---
### Slide 03 *(2 minutos)*

**O que é AutoGen?**<br>
O AutoGen é um framework projetado para simplificar a criação de sistemas multiagentes colaborativos utilizando Modelos de Linguagem (LLMs).

Ele fornece ferramentas para:
- **Programação Conversacional**: Defina facilmente como os agentes interagem.
- **Reflexão e Revisão**: Suporte a ciclos iterativos de feedback.
- **Integração com Ferramentas**: Conecte APIs externas e sistemas sem complicações.

> Abaixo, detalho melhor as características acima.

---
### Slide 04 e 05 *(3 minutos)* 
Como o próprio nome sugere, a programação conversacional permite que os desenvolvedores definam de forma eficiente como os agentes se comunicam, trocam informações
e tomam decisões em um sistema orientado por diálogos.

**Definição de Interações Dinâmicas**: 
A programação conversacional permitem a interação direta entre pessoas e máquinas, tendo uma interação natural.<br>
Um recurso de pesquisa por voz é um exemplo de interface conversacional, pois permite a interação entre humanos e máquinas por meio da conversa.<br>
O autogen permite que o contexto de cada agente seja definido por meio da conversação. Basta escrever, de forma natural, o que o agente deve fazer e em qual contexto
ele atual.

**Exemplo em Código**:
```python
class CriticAgent:
    
    def __init__(self):
        self.system_message = self.get_system_message()
        self.name = self.get_name()
        self.description = self.get_description()
        self.llm_config = LLM_Config.get_llmconfig()
        self.agent = self.get_agent()
        self.direct_communication_agent = DirectCommunicationAgent()


    def get_system_message(self):
        return """
            You are the CriticAgent in a system designed to help users manage gambling addiction 
            in sports betting. Your role is to evaluate and critique responses from other agents 
            in the system. If the response is unsatisfactory, provide constructive feedback and 
            request a revision. If the response is accurate and complete, forward it to the 
            DirectCommunicationAgent for delivery to the user. Use critical thinking and ensure 
            the highest quality in all interactions.
        """


    def get_name(self):
        return "CriticAgent"
```

---
### Slide 06 e 07 *(4 minutos)*
O processo de reflexão refere-se à capacidade do agente reformular a sua resposta, baseado nas sugestões de melhorias feitas por outro agente (crítico).

**Como funciona o processo?**
1. Recebimento da Mensagem Inicial (crítico recebe mensagem inicial do agente de origem)
2. Análise e Crítica (crítico analisa e critica)
3. Geração de Sugestões (a crítica é enviada para o agente de origem)
4. Reformulação pelo Agente de Origem (resposta mais adequada é feita, com base na crítica)
5. Envio Final

---
### Slide 08 e 09 *(2 minutos)*

---
### Slide 10 e 11 *(2 minutos)*

---
### Slide 12 e 13 *(2 minutos)*

---
### Slide 14 *(2 minutos)*

---
### Slide 15 *(3 minutos)*

---
### Slide 16 *(1 minuto)*

---
### Slide 17 e Site do AG2 *(4 minutos)*

---
### Slide 18 e Começo da Problemática - Contexto *(4 minutos)*

---
### Aplicação - Definição dos Agentes e Arquitetura *(4 minutos)*

---
### Aplicação - O que é um usuário viciado *(3 minutos)*

---
### Aplicação - Explicação da comunicação entre agentes *(5 minutos)*

---
### Aplicação - Execução *(5 minutos)*

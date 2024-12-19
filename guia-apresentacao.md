# Guia de Apresentação do WinMind

---
### Objetivo *(1 minuto)*
Realizar uma apresentação abrangente sobre o sistema **WinMind**, destacando o potencial do framework **AutoGen** e sua evolução com o **AG2**,
seguida por uma análise do problema do vício em apostas e como o WinMind o aborda.

---
### Introdução ao AutoGen *(2 minutos)*

**O que é AutoGen?**<br>
O AutoGen é um framework projetado para simplificar a criação de sistemas multiagentes colaborativos utilizando Modelos de Linguagem (LLMs).

Ele fornece ferramentas para:
- **Programação Conversacional**: Defina facilmente como os agentes interagem.
- **Reflexão e Revisão**: Suporte a ciclos iterativos de feedback.
- **Integração com Ferramentas**: Conecte APIs externas e sistemas sem complicações.

> Abaixo, detalho melhor as características acima.

---
### Programação Conversacional *(3 minutos)* 
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
### Reflexão e Revisão *(5 minutos)*
O processo de reflexão refere-se à capacidade do agente reformular a sua resposta, baseado nas sugestões de melhorias feitas por outro agente (crítico).

**Como funciona o processo?**
1. Recebimento da Mensagem Inicial (crítico recebe mensagem inicial do agente de origem)
2. Análise e Crítica (crítico analisa e critica)
3. Geração de Sugestões (a crítica é enviada para o agente de origem)
4. Reformulação pelo Agente de Origem (resposta mais adequada é feita, com base na crítica)
5. Envio Final

**Exemplo em Código**:
```python
# Função de Reflexão Simples
def reflection_message(recipient, sender):
    # Pega a última mensagem enviada pelo Agente Escritor
    last_message = recipient.chat_messages_for_summary(sender)[-1]["content"]
    # Retorna uma instrução para criticar essa mensagem
    return f"Analyze and critique the following message: \n\n{last_message}"

# Configuração da fila de reflexão
nested_chat_queue = [
    {
        "recipient": reflection_agent,  # Agente de Reflexão recebe a mensagem
        "message": reflection_message,  # Gera a mensagem para reflexão
        "max_turns": 2,  # Limita a 2 turnos de reflexão
    },
]

# Registro do fluxo de reflexão no User Proxy
user_proxy.register_nested_chats(
    nested_chat_queue,
    trigger=writing_agent,  # A reflexão será acionada pelo Agente Escritor
)

# Mensagem Inicial: Escrever um blogpost
user_proxy.initiate_chat(
    writing_agent,
    message="Write a short, engaging blogpost about AI advancements.",
    max_turns=1,
)
```

> O exemplo apresentado ilustra como o AutoGen utiliza um fluxo de reflexão em um sistema multiagente para melhorar a qualidade de mensagens ou respostas geradas por agentes.

**Passo a Passo da Execução**:
1. O WritingAgent recebe a tarefa de criar uma pequena frase sobre IA.
2. Mensagem Inicial do WritingAgent: "A IA está transformando indústrias, criando soluções mais inteligentes para saúde, finanças e educação."
3. Após o WritingAgent enviar a mensagem, o ReflectionAgent é acionado e reflete.
4. Reflexão: "Refletindo...  A mensagem é concisa, mas carece de exemplos Considere adicionar um caso específico, como o uso de IA no diagnóstico de doenças. 
5. O WritingAgent reformula a resposta.
6. Reformulação: "A IA está transformando indústrias. Por exemplo, na saúde, diagnósticos auxiliados por IA estão ajudando médicos a detectar doenças de forma mais rápida e precisa."
7. Caso o limite de turnos seja 1, a mensagem já é enviada ao usuário.

---
### Integração com Ferramentas *(1 minuto)*
```python
import os

class LLM_Config:

    @staticmethod
    def get_llmconfig():
        api_key = os.getenv("OPENAI_API_KEY").strip()
        if not api_key:
            print("Error: API key not found.")
            exit(1)
        llm_config = {
            "model": "gpt-3.5-turbo",
            "api_key": api_key
        }
        return llm_config
```

```python
from services.LLM_Config import LLM_Config

def __init__(self):
        self.llm_config = LLM_Config.get_llmconfig()
```

---
### Tipos de Agentes - AssistantAgent *(3 minutos)*

---
### Tipos de Agentes - ConversableAgent *(3 minutos)*

---
### Fluxo de Conversa - send/receive/generate_reply *(3 minutos)*

---
### Atualizações - AutoGen 2.0, 4.0 e AG2 *(4 minutos)*

---
### Contexto do Problema: Vício em Apostas** *(5 minutos)*
#### **O Problema**
- O vício em apostas, especialmente em apostas esportivas, é um problema crescente.
- Impactos incluem perdas financeiras, relacionamentos abalados e problemas de saúde mental.

#### **A Necessidade de uma Solução**
O WinMind aborda isso por meio de:
- Identificação de padrões de apostas de risco.
- Fornecimento de feedback personalizado.
- Oferecimento de intervenções para mitigar comportamentos compulsivos.

---
### Visão Geral do Sistema WinMind** *(15 minutos)*

#### **Arquitetura**
```
        +-------------------+
        | CaptureDataAgent  |
        +-------------------+
                  |
                  v
  +-------------------+   +-------------------+   +-------------------+
  | InterventionAgent |   | MonitoringAgent   |   |  FeedbackAgent    |
  +-------------------+   +-------------------+   +-------------------+
                  \                 |                  /
                   \                |                 /
                    +---------------+----------------+
                                    |
                                    v
                         +-------------------+
                         |    CriticAgent    |
                         +-------------------+
                                    |
                                    v
                         +-------------------+
                         | DirectCommunication|
                         +-------------------+
                                    |
                                    v
                         +-------------------+
                         |      Usuário      |
                         +-------------------+
```

#### **Responsabilidades dos Agentes**
- **CaptureDataAgent**:
  - Coleta dados do usuário, como padrões de apostas e comportamento.
  - Fornece entradas para outros agentes.

- **MonitoringAgent**:
  - Monitora o comportamento de apostas em tempo real.
  - Detecta potenciais riscos e sinaliza padrões preocupantes.

- **InterventionAgent**:
  - Propõe ações imediatas durante cenários de risco.
  - Encoraja apostas responsáveis.

- **FeedbackAgent**:
  - Processa dados do CaptureDataAgent.
  - Envia feedback ao CriticAgent e refina respostas com base na crítica.

- **CriticAgent**:
  - Avalia respostas de outros agentes.
  - Fornece feedback construtivo ou aprovação final.

- **DirectCommunicationAgent**:
  - Repassa mensagens finais ao usuário.
  - Garante clareza e profissionalismo.

#### **Demonstração de Código** *(5 minutos)*
1. **CriticAgent**:
   - Mostre o método `generate_review` usando LLMs para crítica.

   ```python
   def generate_review(self, message):
       messages = [
           {"role": "system", "content": self.system_message},
           {"role": "assistant", "content": message}
       ]
       response = self.agent.generate_reply(messages=messages)
       return response
   ```

2. **DirectCommunicationAgent**:
   - Destaque a simplicidade de repassar mensagens:

   ```python
   def send_direct(self, message):
       print(f"Mensagem final para o usuário: {message}")
   ```

3. **Integração**:
   - Simule o fluxo de dados de CaptureDataAgent → FeedbackAgent → CriticAgent → DirectCommunicationAgent.

#### **Demonstração** *(5 minutos)*
Execute o sistema:
1. CaptureDataAgent coleta dados fictícios.
2. FeedbackAgent processa os dados e envia feedback ao CriticAgent.
3. CriticAgent critica e refina a mensagem.
4. DirectCommunicationAgent entrega a mensagem final no console.

---

### **4. Conclusão e Trabalhos Futuros** *(10 minutos)*
#### **Benefícios do WinMind** *(3 minutos)*
- Arquitetura modular permite fácil escalabilidade.
- Cada agente é especializado em um papel, garantindo alta eficiência.
- Combina monitoramento em tempo real com feedback amigável ao usuário.

#### **Melhorias Futuras** *(2 minutos)*
- **Modelos de IA Avançados**: Use LLMs mais sofisticados para detecção de comportamentos complexos.
- **Personalização**: Adapte o feedback com base em perfis de usuários.
- **Escalabilidade**: Expanda para lidar com uma base maior de usuários.

#### **Considerações Finais** *(2 minutos)*
- "O WinMind demonstra o poder da colaboração orientada por IA para abordar desafios sociais complexos. Por meio de agentes modulares e feedback iterativo, o sistema cria uma estrutura robusta para o gerenciamento responsável de apostas."

#### **Perguntas e Respostas** *(3 minutos)*
- Convide perguntas e feedback da audiência.

---

> **Dica**: Pratique o tempo de cada seção para garantir que você permaneça dentro do limite de 40 minutos.

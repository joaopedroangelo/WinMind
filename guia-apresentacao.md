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
Agente de Conversa: Essa classe é uma abstração que facilita a definição de agentes que interagem entre si ou com sistemas externos por meio de mensagens estruturadas.

A classe ConversableAgent encapsula o mecanismo de envio e recepção de mensagens, permitindo que os agentes troquem informações de maneira eficiente.
Suporta mensagens em diferentes formatos e protocolos definidos pelo desenvolvedor, como JSON, texto estruturado ou até representações personalizadas.
Projetada como uma superclasse genérica, pode ser herdada para implementar agentes com comportamentos específicos.
Os agentes baseados em ConversableAgent podem se conectar a APIs de modelos de linguagem (como OpenAI GPT).
Inclui mecanismos para rastrear o estado de uma conversa ou interação.

1. send_message(target, content): Envia uma mensagem a outro agente ou sistema externo. O parâmetro target indica o destinatário, e content representa o conteúdo da mensagem.
2. receive_message(content): Processa uma mensagem recebida. Este método pode ser sobrescrito para incluir lógicas específicas de processamento ou resposta.
3. start_chat(): Um método interativo para iniciar sessões de conversa estruturadas, seja entre agentes, seja com usuários.
4. add_to_context(message): Adiciona uma mensagem ao contexto da conversa, permitindo que o agente mantenha informações históricas relevantes.

1. Abstração poderosa: Simplifica a implementação de agentes, fornecendo um ponto de partida robusto e genérico.
2. Modularidade: Cada agente pode ser especializado sem a necessidade de reimplementar funcionalidades básicas de comunicação.
3. Integração com fluxos modernos: A arquitetura facilita a integração de IA em sistemas já existentes, incluindo pipelines automatizados.

---
### Slide 10 e 11 *(2 minutos)*
Sobre o agente assistente:<br>
São agentes orientados a tarefas que auxiliam em tarefas específicas, frequentemente fornecendo conhecimento especializado ou realizando ações com base em solicitações do usuário. Eles são bem adequados para suporte técnico, assistência em pesquisa ou qualquer tarefa que exija conhecimento especializado.

---
### Slide 12, 13, 14, 15 *(6 minutos)*
O AutoGen oferece diferentes padrões de interação entre agentes e usuários, que variam de interações simples a fluxos mais complexos envolvendo múltiplos agentes.
Entre os principais padrões estão: Two-Agent Chat, Sequential Chat e Group Chat.

1. Two-Agent Chat
Descrição: Um agente conversa diretamente com outro agente, trocando mensagens para resolver problemas ou realizar tarefas.
Funcionamento:
Um agente atua como solicitante (Requester), enviando consultas ou tarefas.
O outro agente é o executante (Responder), que processa a solicitação e retorna uma resposta.
Exemplo de Uso:
Um agente de planejamento solicita informações a um agente de dados para criar um relatório.
Vantagem: Simples e eficiente para resolver problemas específicos com interação direta entre dois agentes.

2. Sequential Chat
Descrição: Os agentes se comunicam em sequência, com o fluxo de conversa passando de um agente para outro, seguindo uma ordem definida.
Funcionamento:
Cada agente contribui com uma parte do processo ou tarefa antes de passar o controle para o próximo agente.
Útil para tarefas que podem ser divididas em etapas lógicas.
Exemplo de Uso:
Um agente coleta dados do usuário, outro analisa as informações e um terceiro fornece a resposta final.
Vantagem: Estrutura modular e escalável para lidar com fluxos complexos.

3. Group Chat
Descrição: Múltiplos agentes interagem simultaneamente em um único ambiente de conversa, colaborando para resolver uma tarefa em tempo real.
Funcionamento:
Cada agente pode contribuir com base em sua especialidade, enquanto acompanha as interações dos demais.
Há um controle central que organiza as mensagens e evita sobreposição de respostas.
Exemplo de Uso:
Em um sistema de suporte técnico, diferentes agentes (diagnóstico, solução e atendimento ao cliente) colaboram para solucionar o problema do usuário.
Vantagem: Promove colaboração entre agentes com diferentes habilidades e conhecimentos, aumentando a eficiência e a qualidade das respostas.

---
### Slide 16 *(2 minutos)*
Problemas Comuns:
Restrições na modificação de padrões de interação.
Dificuldade em integrar lógicas complexas ou comportamentos personalizados em agentes.
Limitações na adaptação a situações em tempo real, onde o comportamento dos agentes precisa ser altamente dinâmico.

À medida que o número de agentes, usuários ou interações simultâneas cresce, a capacidade do AutoGen de gerenciar essas conexões de forma eficiente[ pode ser comprometida.

A depuração de fluxos de conversa baseados em agentes pode ser um processo desafiador devido à natureza não determinística dos modelos de linguagem e à falta de ferramentas específicas para análise.

---
### Slide 17 e 18 *(5 minutos)*
Semelhanças: 
São escritos em Python
São projetados para criar agentes de IA
Suportam conversas multiagentes
Podem integrar com LLMs locais
Permitem entrada humana durante a execução

CrewAI:
Dois recursos notáveis ​​do crewAI: o primeiro, saída esperada, que trata da especificação de uma saída para uma tarefa (por exemplo, lista com marcadores em vez de parágrafo), garantindo os resultados desejados; e o segundo, delegação, onde os agentes transferem tarefas para outros quando eles estão mais aptos a lidar com elas.

LangGraph:
LangGraph é um framework construído sobre a biblioteca Langchain e usa suas muitas funções e ferramentas. LangGraph utiliza gráficos para criar uma estrutura multiagente ou de agente único. O gráfico representa o fluxo geral da arquitetura. LangGraph é uma ferramenta projetada para visualizar e gerenciar relacionamentos e fluxos de trabalho complexos envolvendo modelos de linguagem, criando uma representação semelhante a um gráfico de interações de componentes.

For Software Development: LangGraph — Best suited for tasks involving code generation and complex multi-agent coding workflows.

Best for Newbies: CrewAI — User-friendly, making it ideal for those new to multi-agent AI without complex setup requirements.

Best for Complex Tasks: LangGraph — Offers high flexibility and is built for advanced users, allowing custom logic and orchestration.

Open-Source LLMs: LangGraph — Integrates well with open-source LLMs and supports various APIs, unlike some other frameworks. Even CrewAI is fine.

Best community support: AutoGen has decent community support helping you with out-of-the-way issues

---
### Slide 19 *(1 minuto)*

---
### Slide 20 e Site do AG2 *(4 minutos)*

---
### Slide 21 e Começo da Problemática - Contexto *(4 minutos)*

---
### Aplicação - Definição dos Agentes e Arquitetura *(4 minutos)*

---
### Aplicação - O que é um usuário viciado *(3 minutos)*

---
### Aplicação - Explicação da comunicação entre agentes *(5 minutos)*

---
### Aplicação - Execução *(5 minutos)*

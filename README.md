# WinMind Project

![Beige and Dark Brown Simple Minimalist Bookstore Circle Logo](https://github.com/user-attachments/assets/2534df5e-5581-4aad-8520-094d413ae04e)

> WinMind is a multi-agent system designed to assist individuals in managing gambling addiction, specifically in the context of sports betting. 

---
## Multi-Agent Architecture

> The system is built on a modular multi-agent framework that promotes collaboration and specialization.
> Each agent has a clearly defined role, ensuring streamlined functionality and efficiency.

```lua
        +-------------------+
        | CaptureDataAgent  | -------|
        +-------------------+        |                       
                                     |                       
                                     v                       
  +-------------------+   +-------------------+    +-------------------+
  | InterventionAgent | <-|  MonitoringAgent  | -> |  FeedbackAgent    |
  +-------------------+   +-------------------+    +-------------------+
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


---
## Agents
- **CaptureDataAgent**:
  - Collects user data, including betting patterns and behavioral indicators.
  - Provides data to other agents for analysis.

- **FeedbackAgent**:
  - Provides feedback to the user, based on their behavior on the betting platform

- **CriticAgent**:
  - Critiques responses from other agents to ensure quality and accuracy.
  - Provides constructive feedback or approval for finalized responses.

- **DirectCommunicationAgent**:
  - Serves as the primary communication interface with the user.

- **MonitoringAgent**:
  - Monitors user activity in real-time.
  - Detects patterns indicative of high-risk behavior and triggers interventions when needed.

- **InterventionAgent**:
  - If the monitoring agent detects compulsive behavior, the intervener is activated.
  - Engages with users during high-risk scenarios to encourage self-control.

---
## Technologies
- **Python**:
  - System implementation is primarily in Python.

- **AutoGen**:
  - Uses the AutoGen framework for managing agent communication.

- **LLM Integration**:
  - Leverages Large Language Models (LLMs) for natural language processing and decision-making.

---
## Credits
- João Pedro Carneiro Angelo (carneiroangelojoaopedro@gmail.com)
- Lucas Raniere (github.com/lucasraniere)

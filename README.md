# WinMind Project

---
## Overview
WinMind is a multi-agent system designed to assist individuals in managing gambling addiction, specifically in the context of sports betting. 


---
## Key Features

### 1. **Multi-Agent Architecture**
The system is built on a modular multi-agent framework that promotes collaboration and specialization. Each agent has a clearly defined role, ensuring streamlined functionality and efficiency.

### 2. **Core Agents**
WinMind comprises the following core agents:

- **CaptureDataAgent**:
  - Collects user data, including betting patterns and behavioral indicators.
  - Provides data to other agents for analysis.

- **FeedbackAgent**:
  - Processes data from the CaptureDataAgent.
  - Sends feedback to the CriticAgent for evaluation.
  - Revises responses based on CriticAgent input and ensures quality feedback delivery.

- **CriticAgent**:
  - Critiques responses from other agents to ensure quality and accuracy.
  - Provides constructive feedback or approval for finalized responses.
  - Forwards approved messages to the DirectCommunicationAgent.

- **DirectCommunicationAgent**:
  - Serves as the primary communication interface with the user.
  - Relays messages from the CriticAgent to the user in a clear and professional manner.

- **MonitoringAgent**:
  - Monitors user activity in real-time.
  - Detects patterns indicative of high-risk behavior and triggers interventions when needed.

- **InterventionAgent**:
  - Implements strategies to guide users away from problematic gambling behavior.
  - Engages with users during high-risk scenarios to encourage self-control.


---
### 3. **Key Technologies**
- **Python Framework**:
  - System implementation is primarily in Python.
  - Uses the AutoGen framework for managing agent communication.

- **LLM Integration**:
  - Leverages Large Language Models (LLMs) for natural language processing and decision-making.
  - Each agent utilizes customized prompts and configurations to align with its role.


---
### 4. **Communication Workflow**
- Data flows seamlessly between agents using the AutoGen methods (`send`, `receive`, `generate_reply`).
- The CriticAgent ensures the quality of messages before they are relayed to the user.

  
---
### 5. **User Interaction**
- The user receives messages exclusively via the DirectCommunicationAgent.
- Communication focuses on clarity, support, and professionalism.

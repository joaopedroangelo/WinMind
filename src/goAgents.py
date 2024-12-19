from services.LLM_Config import LLM_Config
from agents import MonitoringAgent
from agents import InterventionAgent
from agents import CaptureDataAgent
from agents import FeedBackAgent
from agents import DirectCommunicationAgent
from agents import CriticAgent

from autogen import GroupChat
from autogen import GroupChatManager

def run(user):
    user_profile = user.get_user_profile()

    data_agent = CaptureDataAgent.DataCaptureAgent().get_agent()
    data_agent.description = data_agent.description.strip()
    reply = data_agent.generate_reply(messages=[{"content": user_profile, "role": "user"}])

    monitoring_agent = MonitoringAgent.MonitoringAgent().get_agent()
    monitoring_agent.description = monitoring_agent.description.strip()

    intervention_agent = InterventionAgent.InterventionAgent().get_agent()
    intervention_agent.description = intervention_agent.description.strip()

    feedback_agent = FeedBackAgent.FeedBackAgent().get_agent()
    feedback_agent.description = feedback_agent.description.strip()

    critic_agent = CriticAgent.CriticAgent().get_agent()
    critic_agent.description = critic_agent.description.strip()

    direct_communication_agent = DirectCommunicationAgent.DirectCommunicationAgent().get_agent()
    direct_communication_agent.description = direct_communication_agent.description.strip()

    allowed_transitions = {
        data_agent: [monitoring_agent],
        monitoring_agent: [monitoring_agent, intervention_agent, feedback_agent],
        intervention_agent: [feedback_agent],
        feedback_agent: [critic_agent],
        critic_agent: [feedback_agent, direct_communication_agent]
    }

    group_chat = GroupChat(
        agents=[data_agent, monitoring_agent, intervention_agent, feedback_agent, critic_agent, direct_communication_agent],
        messages=[],
        allowed_or_disallowed_speaker_transitions=allowed_transitions,
        speaker_transitions_type="allowed",
        speaker_selection_method="auto",
        send_introductions=True,
    )
    group_chat_manager = GroupChatManager(
        groupchat=group_chat,
        llm_config=LLM_Config.get_llmconfig(),
    )
    chat_result = data_agent.initiate_chat(
        group_chat_manager,
        message=reply,
        summary_method="reflection_with_llm",
    )


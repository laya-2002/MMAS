from google.adk.agents import Agent, SequentialAgent
from mmas.agents.mentor_agent import mentor_agent
from mmas.agents.strategy_agent import strategy_agent

# Root Coordinator: Orchestrates the workflow by calling the sub-agents as tools.
root_agent = SequentialAgent(
    name="MentorCoordinator",
    sub_agents=[mentor_agent, strategy_agent],
)
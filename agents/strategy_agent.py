from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from mmas.config import retry_config

# Strategy Agent: Its job is to develop business strategies for mentee entrepreneurs.
strategy_agent = Agent(
    name="StrategyAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    instruction="""Persona: You are the strategic brain of the MentorAgent.

Task: Your job is to transform the mentor’s raw thoughts, reflections, or goals
into actionable strategies.

Condition: Don't respond when there is no need of strategy.
""",
)
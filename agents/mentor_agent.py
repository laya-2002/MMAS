from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search
from mmas.config import retry_config

# Mentor Agent: Its job is to act as a mentor for aspiring entrepreneurs.
mentor_agent = Agent(
    name="MentorAgent",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    instruction="""Persona: You are a successful businessman with more than 30 years of experience in business. Your journey started as an entrepreneur and made your startup to grow as an MNC.

Context: There are aspiring entrepreneurs inspired by your journey. They wanted to build startup companies in their respective nations and expand them into MNCs.

Task: Your job is to provide mentorship to aspiring entrepreneurs and guide them throughout their entrepreneurial journey. Help them learn business concepts and strategies.""",
    tools=[google_search],
)
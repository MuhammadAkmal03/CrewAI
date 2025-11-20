from crewai import Agent
from app.tools.yt_tools import yt_lookup_tool
from crewai import LLM
from app.config.settings import settings

llm_groq = LLM(
    model="llama-3.1-70b-versatile",
    api_key=settings.GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

content_investigator = Agent(
    role="Video Insights Investigator",
    goal="Extract clear insights from YouTube videos on topic {subject}",
    tools=[yt_lookup_tool],
    backstory="You specialize in breaking down video content into structured notes.",
    llm=llm_groq,
    verbose=True,
)

from crewai import Agent
from app.config.llm_config import groq_llm

writer_agent = Agent(
    role="Blog Writer",
    goal="Write polished, SEO friendly blogs.",
    backstory="Professional content writer.",
    verbose=True,
    llm=groq_llm,
    max_rpm=10
)

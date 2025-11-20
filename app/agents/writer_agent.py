from crewai import Agent
from crewai import LLM
from app.config.settings import settings

llm_groq = LLM(
    model="llama-3.1-70b-versatile",
    api_key=settings.GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

blog_creator = Agent(
    role="Technical Blog Composer",
    goal="Write a high-quality blog post about {subject}.",
    backstory="You turn technical insights into friendly, readable blog content.",
    tools=[],   
    llm=llm_groq,
    verbose=True,
)

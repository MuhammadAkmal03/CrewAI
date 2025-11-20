from crewai import Agent
from app.tools.yt_transcript_tool import youtube_tool
from app.config.llm_config import groq_llm

transcript_agent = Agent(
    role="Transcript Extractor",
    goal="Extract and summarize transcripts concisely.",
    backstory=(
        "Expert at summarizing YouTube videos into short, structured summaries."
    ),
    tools=[youtube_tool],
    verbose=True,
    llm=groq_llm,
    max_rpm=10
)

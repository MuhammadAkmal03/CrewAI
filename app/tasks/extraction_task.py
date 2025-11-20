from crewai import Task
from app.agents.transcript_agent import transcript_agent

task_extraction = Task(
    description=(
        "Use the YouTube Transcript Retriever tool to fetch the transcript for {video_url}. "
        "Produce: 1) A short summary (2–3 paragraphs), "
        "2) Five key takeaways (bullet points), "
        "3) Three blog title ideas."
    ),
    agent=transcript_agent,
    expected_output=(
        "Summary, 5 takeaways, 3 blog title options."
    )
)

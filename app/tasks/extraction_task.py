from crewai import Task
from app.agents.transcript_agent import transcript_agent

YOUTUBE_URL = "https://www.youtube.com/watch?v=6H5gQXzN6vQ"

task_extraction = Task(
    description=(
        f"Use transcript tool to extract the transcript from: {YOUTUBE_URL}. "
        "Output: 1) Short summary (2-3 paragraphs). "
        "2) 5 Key Takeaways. 3) 3 Blog title options."
    ),
    agent=transcript_agent,
    expected_output="Short summary, takeaways, and 3 blog titles.",
    input={"video_url": YOUTUBE_URL},
)

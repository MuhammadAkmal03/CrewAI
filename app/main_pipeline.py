from crewai import Crew, Process
from app.tasks.extraction_task import task_extraction
from app.tasks.writing_task import create_writing_task
from app.agents.transcript_agent import transcript_agent
from app.agents.writer_agent import writer_agent

def run_pipeline(video_url: str, blog_length: str = "Medium", include_faq: bool = False):
    # Create writing task with dynamic parameters
    task_writing = create_writing_task(blog_length, include_faq)
    
    crew = Crew(
        agents=[transcript_agent, writer_agent],
        tasks=[task_extraction, task_writing],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff(inputs={"video_url": video_url})
    # Convert CrewOutput to string for easier handling
    return str(result)

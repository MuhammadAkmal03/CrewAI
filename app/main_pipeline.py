from crewai import Crew, Process
from app.tasks.extraction_task import task_extraction
from app.tasks.writing_task import task_writing
from app.agents.transcript_agent import transcript_agent
from app.agents.writer_agent import writer_agent

def run_pipeline():
    crew = Crew(
        agents=[transcript_agent, writer_agent],
        tasks=[task_extraction, task_writing],
        process=Process.sequential,
        verbose=True
    )

    print("Starting pipeline...\n")
    result = crew.kickoff()
    print(result)
    return result

if __name__ == "__main__":
    run_pipeline()

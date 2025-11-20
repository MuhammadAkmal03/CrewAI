from crewai import Crew, Process
from app.tasks.analysis_task import analysis_task
from app.tasks.writing_task import writing_task
from app.agents.analysis_agent import content_investigator
from app.agents.writing_agent import blog_creator

pipeline = Crew(
    agents=[content_investigator, blog_creator],
    tasks=[analysis_task, writing_task],
    process=Process.sequential
)

def generate_blog(subject: str):
    result = pipeline.kickoff(inputs={"subject": subject})
    return result

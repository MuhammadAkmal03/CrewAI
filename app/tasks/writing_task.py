from crewai import Task
from app.agents.writer_agent import writer_agent
from app.tasks.extraction_task import task_extraction

task_writing = Task(
    description=(
        "Write a full 700–1000 word blog based on the extracted summary. "
        "Use markdown formatting, add headings, intro, conclusion."
    ),
    agent=writer_agent,
    context=[task_extraction],
    expected_output="A full blog post in Markdown."
)

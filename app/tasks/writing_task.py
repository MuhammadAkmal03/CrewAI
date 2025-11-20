from crewai import Task
from app.agents.writing_agent import blog_creator

writing_task = Task(
    description="Create a complete blog article using the video insights.",
    expected_output="A polished blog article written in markdown.",
    agent=blog_creator,
    output_file="final_blog.md"
)

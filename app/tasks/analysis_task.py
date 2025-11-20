from crewai import Task
from app.agents.analysis_agent import content_investigator
from app.tools.yt_tools import yt_lookup_tool

analysis_task = Task(
    description="Analyze YouTube videos and extract useful content about {subject}.",
    expected_output="A structured summary of insights from relevant YouTube videos.",
    tools=[yt_lookup_tool],
    agent=content_investigator,
)

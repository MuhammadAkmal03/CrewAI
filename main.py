import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
# CORRECTED IMPORT: Targeting the specific base_tool module file to avoid namespace issues
from crewai.tools.base_tool import BaseTool
from youtube_transcript_api import YouTubeTranscriptApi
from typing import Type
from pydantic import BaseModel, Field

# Load environment variables from .env file
# Ensure your .env file has GEMINI_API_KEY="YOUR_KEY"
load_dotenv()

# --- 1. Configure Groq LLM ---
# Retrieve API key and model name from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL_NAME", "groq/llama-3.1-70b-versatile")

# Check for API key presence
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found. Please set it in your .env file.")

# Initialize the LLM object using the CrewAI LLM class
groq_llm = LLM(
    model="groq/llama-3.3-70b-versatile",      # or groq/llama-3.1-8b-instant, etc.
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY"),       # your real Groq key
    temperature=0.3
)

print(f"LLM configured to use: {GROQ_MODEL}")

# --- 2. Custom Tool for YouTube Transcript Retrieval ---

# Pydantic model for tool input validation
class YouTubeTranscriptInput(BaseModel):
    """Input schema for YouTubeTranscriptTool."""
    video_url: str = Field(description="The full URL of the YouTube video (e.g., https://www.youtube.com/watch?v=...)")

class YouTubeTranscriptTool(BaseTool):
    name: str = "YouTube Transcript Retriever"
    description: str = "A tool to retrieve the full, unedited transcript of a YouTube video given its full URL."
    args_schema: Type[BaseModel] = YouTubeTranscriptInput

    def _run(self, video_url: str) -> str:
        try:
            # Extract video ID from URL (robustly handles various formats)
            if "youtu.be" in video_url:
                video_id = video_url.split('/')[-1].split('?')[0]
            elif "v=" in video_url:
                video_id = video_url.split('v=')[1].split('&')[0]
            else:
                return "Error: Invalid YouTube URL format. Could not find video ID."
            
            # Fetch the transcript
            # Note: Tries English first, or falls back to auto-generated if available
            transcript_api = YouTubeTranscriptApi()
            fetched_transcript = transcript_api.fetch(
                video_id,
                languages=['en', 'en-US']
            )
            
            # Concatenate all parts into a single string
            transcript = " ".join([snippet.text for snippet in fetched_transcript])
            
            return transcript
        except Exception as e:
            return f"Error retrieving transcript: {e}"

# Instantiate the custom tool
youtube_tool = YouTubeTranscriptTool()

# --- 3. Define Agents ---

transcript_agent = Agent(
    role='Transcript Extractor and Summarizer',
    goal='Extract a concise, user-friendly summary and key takeaways from the video transcript for the writer. Keep summaries brief and focused.',
    backstory=("Expert in video analysis and summarization, capable of accurately retrieving YouTube transcripts "
               "and condensing the core information into concise, easy-to-read summaries. You excel at distilling "
               "complex content into brief, user-friendly formats. You MUST use the provided tool."),
    tools=[youtube_tool],
    verbose=True,
    llm=groq_llm,
    max_rpm=10
)

writer_agent = Agent(
    role='Professional Blog Post Writer',
    goal='Turn the provided summary and key points into an engaging, well-structured, SEO-friendly blog post of 700-1000 words.',
    backstory=("A seasoned content writer with a focus on SEO and converting raw data into high-quality, "
               "reader-friendly blog articles with excellent flow and Markdown formatting."),
    verbose=True,
    llm=groq_llm,
    max_rpm=10
)

# --- 4. Define Tasks ---

# !!! IMPORTANT: REPLACE THIS URL WITH A REAL YOUTUBE VIDEO URL !!!
# Example URL: "https://www.youtube.com/watch?v=kYJzN_N4oXU" (a short, transcript-heavy video works best)
YOUTUBE_URL = "https://www.youtube.com/watch?v=6H5gQXzN6vQ" 

task_extraction = Task(
    description=(
        f"Use the YouTube Transcript Retriever tool to get the full transcript for this URL: {YOUTUBE_URL}. "
        "Analyze the content and output a structured, concise summary that includes: "
        "1) A brief summary (2-3 paragraphs maximum, keep it user-friendly and easy to read), "
        "2) Top 5 Key Takeaways (bulleted list, one line each), and "
        "3) Three highly engaging blog post titles (numbered list) suitable for the content. "
        "Keep the summary concise and focused on the main points - avoid lengthy explanations."
    ),
    agent=transcript_agent,
    expected_output="A concise structured summary including: 1. Brief Summary (2-3 paragraphs), 2. Top 5 Key Takeaways (one line each), and 3. Three Blog Titles (numbered).",
    # Pass the URL input to the tool via the task's input
    input={"video_url": YOUTUBE_URL} 
)

task_writing = Task(
    description=(
        "Using the structured summary and key takeaways from the previous task, write a complete, professional blog post (700-1000 words). "
        "The post must include an engaging title (choose the best one), a brief introduction, "
        "multiple main sections corresponding to the key takeaways (using Markdown headings like '##'), and a conclusion/call to action. "
        "**Format the final output entirely in Markdown.**"
    ),
    agent=writer_agent,
    context=[task_extraction], # Dependency on the extraction task's output
    expected_output="A full blog post in clean Markdown format, ready for publication."
)

# --- 5. Create and Run the Crew ---

crew = Crew(
    agents=[transcript_agent, writer_agent],
    tasks=[task_extraction, task_writing],
    process=Process.sequential,
    verbose=True # Enable detailed agent thoughts and tool usage
)

# Quick standalone test (remove after confirming it works)
print("Testing YouTube tool...")
tool = YouTubeTranscriptTool()
test_transcript = tool._run(YOUTUBE_URL)
print(f"Test Result: {test_transcript[:200]}...")  # First 200 chars

print("Starting the YouTube to Blog Crew with Groq...")
print(f"Targeting URL: {YOUTUBE_URL}\n")
result = crew.kickoff()

print("\n\n######################################")
print("## CREW JOB FINISHED")
print("######################################\n")
print(result)
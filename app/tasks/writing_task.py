from crewai import Task
from app.agents.writer_agent import writer_agent
from app.tasks.extraction_task import task_extraction

def create_writing_task(blog_length: str = "Medium", include_faq: bool = False):
    """Create a writing task with configurable blog length and FAQ section."""
    
    # Define word count based on blog length
    word_counts = {
        "Short": "400–600 words",
        "Medium": "700–1000 words",
        "Long": "1200–1500 words"
    }
    word_count = word_counts.get(blog_length, "700–1000 words")
    
    # Build description
    description = (
        f"Write a full {word_count} blog post based on the extracted summary. "
        "Use markdown formatting with proper headings (## for main sections, ### for subsections), "
        "an engaging introduction, well-structured body sections, and a strong conclusion with call to action. "
    )
    
    if include_faq:
        description += (
            "**IMPORTANT: Include a FAQ section at the end with 5-7 common questions and answers "
            "related to the video content. Format it as '## FAQ' followed by questions as '### Q: ...' "
            "and answers as regular paragraphs below each question.**"
        )
    
    return Task(
        description=description,
        agent=writer_agent,
        context=[task_extraction],
        expected_output="A full blog post in Markdown format with proper headings and formatting."
    )

# Default task for backward compatibility
task_writing = create_writing_task()

import os
from crewai.tools.base_tool import BaseTool
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import GenericProxyConfig
from typing import Type
from pydantic import BaseModel, Field

class YouTubeTranscriptInput(BaseModel):
    video_url: str = Field(
        description="Full YouTube URL such as https://www.youtube.com/watch?v=abc123"
    )

class YouTubeTranscriptTool(BaseTool):
    name: str = "YouTube Transcript Retriever"
    description: str = "Fetches complete transcript from any given YouTube URL."
    args_schema: Type[BaseModel] = YouTubeTranscriptInput

    def _run(self, video_url: str) -> str:
        try:
            if "youtu.be" in video_url:
                video_id = video_url.split('/')[-1].split('?')[0]
            elif "v=" in video_url:
                video_id = video_url.split("v=")[1].split("&")[0]
            else:
                return "Invalid YouTube URL"

            proxies = None
            proxy_url = os.getenv("YOUTUBE_PROXY")
            if proxy_url:
                proxies = GenericProxyConfig(http_url=proxy_url, https_url=proxy_url)

            # Use the class instantiation method which supports proxy_config
            transcript_api = YouTubeTranscriptApi(proxy_config=proxies)
            transcript_data = transcript_api.fetch(
                video_id,
                languages=["en", "en-US"]
            )

            transcript = " ".join([segment.text for segment in transcript_data])
            return transcript

        except Exception as e:
            return f"Transcript Error: {e}"

youtube_tool = YouTubeTranscriptTool()

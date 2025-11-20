from youtube_transcript_api import YouTubeTranscriptApi
import re
from urllib.parse import urlparse, parse_qs

def _get_video_id(youtube_url: str) -> str:
    """Extract video id from a YouTube URL."""
    # Handle common url forms
    parsed = urlparse(youtube_url)
    if parsed.hostname in ("www.youtube.com", "youtube.com"):
        qs = parse_qs(parsed.query)
        return qs.get("v", [None])[0]
    if parsed.hostname == "youtu.be":
        return parsed.path.lstrip('/')
    # fallback: assume last part
    return youtube_url.split('v=')[-1]

def get_youtube_transcript(youtube_url: str) -> str:
    """Fetch transcript using youtube_transcript_api.
    Returns a plain text transcript (joined segments).
    """
    video_id = _get_video_id(youtube_url)
    if not video_id:
        raise ValueError("Could not parse YouTube video id from URL")

    raw = YouTubeTranscriptApi.get_transcript(video_id)
    text = "\n\n".join([seg['text'].strip() for seg in raw if seg.get('text')])

    # basic cleaning: remove repeated whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text
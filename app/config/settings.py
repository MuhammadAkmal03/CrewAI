from pydantic import BaseSettings

class AppSettings(BaseSettings):
    GROQ_API_KEY: str

    class Config:
        env_file = ".env"

settings = AppSettings()
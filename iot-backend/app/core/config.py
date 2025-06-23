from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI"
    SECRET_KEY: str = "your-super-secret-key-here"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str = "postgresql+asyncpg://ammar:ammar@db:5432/mydatabase-pgresql"
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"
        extra = "ignore"  # Ignore extra fields in environment variables

settings = Settings()

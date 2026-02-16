from pydantic_settings import BaseSettings
from typing import Optional 

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite+aiosqlite:///./blog.db"
    SECRET_KEY: str = "your-secret-key-change-in-prod"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 1440
    DEBUG: Optional[bool] = False  # добавьте это

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()

import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Application settings
    PROJECT_NAME: str = "Markdown Analysis Service"
    VERSION: str = "0.0.1"
    API_PREFIX: str = "/api"

    # Database settings
    # <to-do> ES

    # Security settings
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Email settings
    MAIL_USERNAME: str = os.getenv("MAIL_USERNAME", "your_email@gmail.com")
    MAIL_PASSWORD: str = os.getenv("MAIL_PASSWORD", "your_email_password")
    MAIL_FROM: str = os.getenv("MAIL_FROM", "your_email@gmail.com")
    MAIL_PORT: int = os.getenv("MAIL_PORT", 587)
    MAIL_SERVER: str = os.getenv("MAIL_SERVER", "smtp.gmail.com")

    # OAuth settings
    GOOGLE_CLIENT_ID: str = os.getenv("GOOGLE_CLIENT_ID", "your-google-client-id")
    GOOGLE_CLIENT_SECRET: str = os.getenv("GOOGLE_CLIENT_SECRET", "your-google-client-secret")

    # Redis settings
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", 6379))

    # Other settings
    SLACK_WEBHOOK_URL: str = os.getenv("SLACK_WEBHOOK_URL", "")
    ALLOWED_ORIGINS: list = ["http://localhost", "http://localhost:3000"]

    # Environment mode
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Instantiate settings
settings = Settings()

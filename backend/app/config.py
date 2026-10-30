from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_env: str = "development"
    database_url: str = "sqlite:///./agentguard.db"
    openai_api_key: str | None = None
    openai_model: str = "gpt-4o-mini"
    aws_region: str = "eu-west-2"
    aws_bedrock_model_id: str | None = None
    cors_origins: str = "http://localhost:5173"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()

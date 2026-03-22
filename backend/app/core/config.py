from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    apollo_api_key: str = ""
    snov_client_id: str = ""
    snov_client_secret: str = ""
    instantly_api_key: str = ""
    database_url: str = "sqlite:///./pipeline.db"

    class Config:
        env_file = ".env"


settings = Settings()

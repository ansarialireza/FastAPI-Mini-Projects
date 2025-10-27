from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    app_name = str = "FastAPI Project"
    version: str = "0.1.0"
    database_url: str
    secret_key: str
    debug: bool = False
    allowed_hosts: list[str]
    log_level: str = "INFO"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

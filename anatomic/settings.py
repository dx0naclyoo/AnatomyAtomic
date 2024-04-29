import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class DatabaseSettings(BaseSettings):
    postgres_url: str = os.getenv("POSTGRESQL_URL")
    echo: bool = False
    redis_url: str = os.getenv("REDIS_URL")
    redis_default_expire: int = 3600


class AppSettings(BaseSettings):
    port: int = 9871
    host: str = "127.0.0.1"


class Settings(DatabaseSettings, AppSettings):
    database: DatabaseSettings = DatabaseSettings()
    app: AppSettings = AppSettings()


settings = Settings()

import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class DatabaseSettings(BaseSettings):
    url: str = os.getenv("POSTGRESQL_URL")
    echo: bool = False


class AppSettings(BaseSettings):
    port: int = 9871
    host: str = "127.0.0.1"


class Settings(DatabaseSettings, AppSettings):
    database: DatabaseSettings = DatabaseSettings()
    app: AppSettings = AppSettings()


settings = Settings()

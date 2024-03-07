import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    MYSQL_USER: str = os.environ.get("MYSQL_USER", )
    MYSQL_PASSWORD: str = os.environ.get("MYSQL_PASSWORD")
    MYSQL_SERVER: str = os.environ.get("MYSQL_SERVER")
    MYSQL_PORT: int = int(os.environ.get("MYSQL_PORT", 3306))
    MYSQL_DB: str = os.environ.get("MYSQL_DB")


settings = Settings()

from pydantic import BaseSettings
from os import environ as env


class Settings(BaseSettings):
    redis_host: str = env.get("REDIS_HOST", "localhost")


settings = Settings()

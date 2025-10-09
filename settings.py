# settings.py
from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    SECRET: str

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value):
        # prepare validator that will check whether the value of ENVIRONMENT is in (dev, test, prod)
        allowed_envs = ["dev", "test", "prod"]
        if value not in allowed_envs:
            raise ValueError(f"Environment must be one of {allowed_envs}")
        return value

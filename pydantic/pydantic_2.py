from typing import Optional

from pydantic import ValidationError, BaseSettings


class NestedSettings(BaseSettings):
    optional_nested_value: int


class Settings(BaseSettings):
    value1: str
    value2: int
    nested_settings: Optional[int] = None

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


def read_env_settings():
    try:
        env_settings = Settings()
        return env_settings
    except ValidationError as error:
        print(error.json())


if __name__ == "__main__":
    env_settings = read_env_settings()
    if env_settings:
        print(env_settings.json())

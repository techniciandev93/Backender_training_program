from typing import Optional

from environs import Env
from pydantic import ValidationError, BaseModel


class NestedSettings(BaseModel):
    optional_nested_value: int


class Settings(BaseModel):
    value1: str
    value2: int
    nested_settings: Optional[int] = None


def read_env_settings():
    env = Env()
    env.read_env()

    try:
        value1 = env.str('VALUE1')
        value2 = env.int('VALUE2')
        nested_settings = env.str('NESTED_SETTINGS')
        settings = Settings(value1=value1, value2=value2, nested_settings=nested_settings)
        return settings
    except ValidationError as error:
        print(error.json())


if __name__ == "__main__":
    env_settings = read_env_settings()
    if env_settings:
        print(env_settings.json())

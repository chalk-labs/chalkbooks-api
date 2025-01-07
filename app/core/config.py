import secrets
import warnings
from pydantic import (
    AnyUrl,
    BeforeValidator,
    HttpUrl,
    PostgresDsn,
    computed_field,
    model_validator,
)
from pydantic_core import MultiHostUrl
from typing_extensions import Self


class Settings():
    API_V1_STR: str = "/api/v1"


settings = Settings()  # type: ignore
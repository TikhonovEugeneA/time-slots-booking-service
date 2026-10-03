from pathlib import Path

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class DataBaseConfig(BaseModel):
    url: str
    echo: bool
    echo_pool: bool
    pool_size: int
    max_overflow: int
    pool_pre_ping: bool
    pool_recycle: int
    pool_timeout: int


class UrlPrefix(BaseModel):
    prefix: str = ""


class AppConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(
            BASE_DIR / ".env.example",
            BASE_DIR / ".env",
            BASE_DIR / ".env.local",
        ),
        env_prefix="APP_CONFIG__",
        env_nested_delimiter="__",
        extra="ignore",
    )

    database: DataBaseConfig
    url: UrlPrefix = Field(default_factory=UrlPrefix)
    app: AppConfig = Field(default_factory=AppConfig)


settings = Settings()

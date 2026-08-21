from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


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
    prefix: str


class AppConfig(BaseModel):
    host: str
    port: int


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(BASE_DIR / ".env", BASE_DIR / ".env.example"),
        env_prefix="APP_CONFIG__",
        env_nested_delimiter="__",
        extra="ignore",
    )
    database: DataBaseConfig
    url: UrlPrefix = UrlPrefix()
    app: AppConfig = AppConfig()

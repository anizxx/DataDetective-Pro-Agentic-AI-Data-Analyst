from functools import lru_cache
from pathlib import Path
from pydantic import Field
from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = Field(default="DataDetective Pro", alias="APP_NAME")
    debug: bool = Field(default=True, alias="DEBUG")
    database_url: str = Field(default="sqlite:///./datadetective.db", alias="DATABASE_URL")
    openai_api_key: str = Field(default="", alias="OPENAI_API_KEY")
    openai_model: str = Field(default="", alias="OPENAI_MODEL")
    embedding_model: str = Field(default="", alias="EMBEDDING_MODEL")
    max_upload_size_mb: int = Field(default=20, alias="MAX_UPLOAD_SIZE_MB")
    frontend_url: str = Field(default="http://localhost:5173", alias="FRONTEND_URL")

    model_config = SettingsConfigDict(env_file=".env", populate_by_name=True, extra="ignore")

    @field_validator("debug", mode="before")
    @classmethod
    def parse_debug(cls, value):
        if isinstance(value, str) and value.lower() in {"release", "prod", "production"}:
            return False
        return value


ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "data"
UPLOAD_DIR = DATA_DIR / "uploads"
DOCUMENT_DIR = ROOT_DIR / "documents"
REPORT_DIR = ROOT_DIR / "reports"
STORAGE_DIR = ROOT_DIR / "backend" / "storage"


@lru_cache
def get_settings() -> Settings:
    for folder in (DATA_DIR, UPLOAD_DIR, DOCUMENT_DIR, REPORT_DIR, STORAGE_DIR):
        folder.mkdir(parents=True, exist_ok=True)
    return Settings()

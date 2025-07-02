from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class TranslationAPIConfig(BaseModel):
    base_url: str


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = True


class LoggingConfig(BaseModel):
    log_format: str = "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"


class CorsConfig(BaseModel):
    allowed_origins: list[str]
    allow_credentials: bool = True
    allowed_methods: list[str] = ["GET", "POST", "PATCH"]
    allowed_headers: list[str] = ["*"]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="APP_CONFIG__",
        env_nested_delimiter="__",
        case_sensitive=False,
    )

    api_title: str = "Docx Translator API"

    cors: CorsConfig

    translation_api: TranslationAPIConfig

    log: LoggingConfig = LoggingConfig()

    run: RunConfig = RunConfig()


settings = Settings()

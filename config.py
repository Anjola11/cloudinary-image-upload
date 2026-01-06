from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    CLOUDINARY_CLOUD_NAME:str
    CLOUDINARY_API_KEY:str
    CLOUDINARY_API_SECRET:str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


Config = Settings()
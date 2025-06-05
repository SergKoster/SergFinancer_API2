from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    
    PROJECT_NAME: str = "SergFinancer_API2"
    API_V1_STR: str = "/api"
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30 
    ALGORITHM: str = "HS256"

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str = "db"
    POSTGRES_PORT: str = "5432"

    class Config:
        env_file = ".env"

settings = Settings()

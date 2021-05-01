from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    db_name: str = Field(..., env="DB_NAME")
    user: str = Field(..., env="DB_USER")
    password: str = Field(..., env="PASSWORD")
    host: str = Field(..., env="HOST")
    port: str = Field(..., env="PORT")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings(_env_file="../.env")

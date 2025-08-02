import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str

def get_settings() -> Settings:
    if os.getenv("RENDER") == "true":
        # Render環境：.envは使わず直接環境変数
        class Config:
            env_file = None
        return Settings(_env_file=None)
    else:
        # ローカル：.envを読み込む
        env_path = os.path.join(os.path.dirname(__file__), "../../.env")
        return Settings(_env_file=env_path)

settings = get_settings()

import os

from pydantic_settings import BaseSettings


# デフォルトは環境変数から読み込み db_host -> DB_HOSTという環境変数の値がバインドされる
class Settings(BaseSettings):
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str


def get_settings() -> Settings:
    if os.getenv("RENDER") == "true":
        return Settings()
    else:
        return Settings(
            db_host="localhost",
            db_port=5435,
            db_name="free_autofill_db",
            db_user="user",
            db_password="password",
        )


settings = get_settings()

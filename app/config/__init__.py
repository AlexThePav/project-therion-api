from pydantic_settings import BaseSettings
from os.path import abspath, dirname

app_path = abspath(dirname(dirname(__file__)))


class Settings(BaseSettings):
    database_url: str = f"sqlite:///{app_path}/database/db/therion.db"


settings = Settings()



if __name__ == "__main__":
    ...

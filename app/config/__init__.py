from pydantic_settings import BaseSettings
from os.path import abspath, dirname

app_path = abspath(dirname(dirname(__file__)))


class Settings(BaseSettings):
    database_url: str = (
        f"sqlite:///{app_path}/database/db/therion.db?"
        f"check_same_thread=true&timeout=10&mode=ro&nolock=1&uri=true"
    )


settings = Settings()



if __name__ == "__main__":
    ...

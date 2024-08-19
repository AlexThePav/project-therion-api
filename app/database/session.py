import contextlib
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.exceptions.exceptions import ServiceError


class DatabaseManager:
    def __init__(self, db_url: str):
        self.engine: Engine | None = create_engine(db_url)
        self._sessionmaker: sessionmaker = sessionmaker(
            bind=self.engine,
        )

    def close(self):
        if self.engine is None:
            raise ServiceError
        self.engine.dispose()
        self.engine = None
        self._sessionmaker = None


db_manager = DatabaseManager(settings.database_url)

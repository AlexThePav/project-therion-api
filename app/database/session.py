from sqlalchemy import create_engine, text
from app.config import settings

engine = create_engine(
    f"{settings.database_url}"
    "check_same_thread=true&timeout=10&mode=ro&nolock=1&uri=true"
)

if __name__ == "__main__":
    with engine.connect() as conn:
        result = conn.execute(text("select 'hello world'"))
        print(result.all())

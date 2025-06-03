from sqlalchemy.orm import sessionmaker
from health_simplified.db.database import get_engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=get_engine())

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

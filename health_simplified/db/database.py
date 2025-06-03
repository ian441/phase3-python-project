import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}"

Base = declarative_base()

def get_engine():
    return create_engine(DATABASE_URL)
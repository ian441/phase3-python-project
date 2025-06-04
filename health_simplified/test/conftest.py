"""Pytest configuration for Health Simplified tests."""
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from health_simplified.db.database import Base
from health_simplified.models.user import User

@pytest.fixture
def db_session():
    """Fixture for creating a database session for tests."""

    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    session_factory = sessionmaker(bind=engine)
    session = session_factory()
    
    try:
        # Create test data
        user = User(name="Test User")
        session.add(user)
        session.commit()
        yield session
    finally:
        session.close()
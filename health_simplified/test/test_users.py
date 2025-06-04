import pytest
from services.user_service import UserService

@pytest.fixture
def user_service():
    return UserService()

def test_create_user(user_service):
    user_service.create_user("Test User")
    users = user_service.list_users()
    assert any(user.name == "Test User" for user in users)

def test_list_users(user_service):
    user_service.create_user("Another User")
    users = user_service.list_users()
    assert len(users) >= 2

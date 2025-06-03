import pytest
from services.food_service import FoodService

@pytest.fixture
def food_service():
    return FoodService()

def test_add_food_entry(food_service):
    food_service.add_food_entry("Test User", "Apple", 95, "2023-10-01")
    entries = food_service.list_food_entries(user="Test User")
    assert any(entry.food == "Apple" for entry in entries)

def test_list_food_entries(food_service):
    food_service.add_food_entry("Test User", "Banana", 105, "2023-10-01")
    entries = food_service.list_food_entries(user="Test User")
    assert len(entries) >= 2

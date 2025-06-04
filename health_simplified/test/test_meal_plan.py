import pytest
from health_simplified.services.meal_plan_service import MealPlanService

@pytest.fixture
def meal_plan_service():
    return MealPlanService()

def test_create_meal_plan(meal_plan_service):
    meal_plan_service.create_meal_plan("Test User", 1)
    plans = meal_plan_service.list_meal_plans("Test User")
    assert any(plan.week == 1 for plan in plans)

def test_list_meal_plans(meal_plan_service):
    meal_plan_service.create_meal_plan("Test User", 2)
    plans = meal_plan_service.list_meal_plans("Test User")
    assert len(plans) >= 2

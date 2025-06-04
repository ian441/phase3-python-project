import pytest
from services.goal_service import GoalService

@pytest.fixture
def goal_service():
    return GoalService()

def test_set_goal(goal_service):
    goal_service.set_goal("Test User", 2000, 14000)
    goals = goal_service.list_goals("Test User")
    assert any(goal.daily == 2000 for goal in goals)

def test_list_goals(goal_service):
    goal_service.set_goal("Test User", 2500, 17500)
    goals = goal_service.list_goals("Test User")
    assert len(goals) >= 2

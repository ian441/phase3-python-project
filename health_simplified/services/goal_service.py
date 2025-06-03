from health_simplified.db.session import get_db
from health_simplified.models.nutrition_goals import NutritionGoal
from sqlalchemy.orm import Session
from health_simplified.models.user import User

class GoalService:
    def set_goal(self, user: str, daily: int, weekly: int):
        db: Session = next(get_db())
        user_obj = db.query(User).filter(User.name == user).first()
        if user_obj:
            goal = NutritionGoal(user_id=user_obj.id, daily=daily, weekly=weekly)
            db.add(goal)
            db.commit()
            db.refresh(goal)
            return goal
        else:
            raise ValueError("User not found")

    def list_goals(self, user: str):
        db: Session = next(get_db())
        user_obj = db.query(User).filter(User.name == user).first()
        if user_obj:
            return db.query(NutritionGoal).filter(NutritionGoal.user_id == user_obj.id).all()
        else:
            raise ValueError("User not found")

from health_simplified.db.session import get_db
from health_simplified.models.meal_plan import MealPlan
from health_simplified.models.user import User  
from sqlalchemy.orm import Session

class MealPlanService:
    def create_meal_plan(self, user: str, week: int):
        db: Session = next(get_db())
        user_obj = db.query(User).filter(User.name == user).first()
        if user_obj:
            meal_plan = MealPlan(user_id=user_obj.id, week=week, details="Meal plan details here")
            db.add(meal_plan)
            db.commit()
            db.refresh(meal_plan)
            return meal_plan
        else:
            raise ValueError("User not found")

    def list_meal_plans(self, user: str):
        db: Session = next(get_db())
        user_obj = db.query(User).filter(User.name == user).first()
        if user_obj:
            return db.query(MealPlan).filter(MealPlan.user_id == user_obj.id).all()
        else:
            raise ValueError("User not found")

    def delete_meal_plan(self, id: int):
        db: Session = next(get_db())
        meal_plan = db.query(MealPlan).filter(MealPlan.id == id).first()
        if meal_plan:
            db.delete(meal_plan)
            db.commit()
        else:
            raise ValueError("Meal plan not found")

    def update_meal_plan(self, id: int, details: str = None, week: int = None):
        db: Session = next(get_db())
        meal_plan = db.query(MealPlan).filter(MealPlan.id == id).first()
        if not meal_plan:
            raise ValueError("Meal plan not found")
        if details is not None:
            meal_plan.details = details
        if week is not None:
            meal_plan.week = week
        db.commit()
        db.refresh(meal_plan)
        return meal_plan
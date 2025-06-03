from health_simplified.db.database import get_engine, Base
from health_simplified.models.user import User 
from health_simplified.models.nutrition_goals import  NutritionGoal
from health_simplified.models.meal_plan import MealPlan
from health_simplified.models.food_entry import FoodEntry  

def init():
    engine = get_engine()
    Base.metadata.create_all(bind=engine)
    print("Database tables created.")

if __name__ == "__main__":
    init()
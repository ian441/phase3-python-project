from health_simplified.db.database import get_engine, Base
from health_simplified.models.user import User 
from health_simplified.models.nutrition_goals import  NutritionGoal
from health_simplified.models.meal_plan import MealPlan
from health_simplified.models.food_entry import FoodEntry  

def init():
    engine = get_engine()
    confirm = input("This will recreate all tables. Continue? (y/n): ")
    if confirm.lower() == 'y':
        Base.metadata.create_all(bind=engine)
        print("Database tables created.")
    else:
        print("Cancelled.")
        
if __name__ == "__main__":
    init()
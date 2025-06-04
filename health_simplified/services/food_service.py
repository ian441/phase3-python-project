from health_simplified.db.session import get_db
from sqlalchemy.orm import Session
from datetime import datetime
from health_simplified.models.user import User
from health_simplified.models.food_entry import FoodEntry

class FoodService:
    def add_food_entry(self, user: str, food: str, calories: int, date: str):
        db: Session = next(get_db())
        user_obj = db.query(User).filter(User.name == user).first()
        if user_obj:
            food_entry = FoodEntry(user_id=user_obj.id, food=food, calories=calories, date=datetime.strptime(date, '%Y-%m-%d').date())
            db.add(food_entry)
            db.commit()
            db.refresh(food_entry)
            return food_entry
        else:
            raise ValueError("User not found")

    def list_food_entries(self, user: str = None, date: str = None):
        db: Session = next(get_db())
        query = db.query(FoodEntry)
        if user:
            user_obj = db.query(User).filter(User.name == user).first()
            if user_obj:
                query = query.filter(FoodEntry.user_id == user_obj.id)
        if date:
            query = query.filter(FoodEntry.date == datetime.strptime(date, '%Y-%m-%d').date())
        return query.all()

    def update_food_entry(self, id: int, food: str = None, calories: int = None):
        db: Session = next(get_db())
        food_entry = db.query(FoodEntry).filter(FoodEntry.id == id).first()
        if food_entry:
            if food:
                food_entry.food = food
            if calories is not None:
                food_entry.calories = calories
            db.commit()
            db.refresh(food_entry)
            return food_entry
        else:
            raise ValueError("Food entry not found")

    def delete_food_entry(self, id: int):
        db: Session = next(get_db())
        food_entry = db.query(FoodEntry).filter(FoodEntry.id == id).first()
        if food_entry:
            db.delete(food_entry)
            db.commit()
        else:
            raise ValueError("Food entry not found")

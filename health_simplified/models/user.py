from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from health_simplified.db.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    
    food_entries = relationship("FoodEntry", back_populates="user")
    goals = relationship("NutritionGoal", back_populates="user") 
    meal_plans = relationship("MealPlan", back_populates="user")
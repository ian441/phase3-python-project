from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class MealPlan(Base):
    """Meal plan model for weekly meal planning"""
    __tablename__ = "meal_plans"

    id = Column(Integer, primary_key=True, index=True)
    week_number = Column(Integer, nullable=False)
    plan_details = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relationship
    user = relationship("User", back_populates="meal_plans")

    def __repr__(self):
        return f"<MealPlan(id={self.id}, week={self.week_number}, user_id={self.user_id})>"
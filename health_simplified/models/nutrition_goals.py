from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class NutritionGoal(Base):
    """Nutrition goals model for tracking daily/weekly targets"""
    __tablename__ = "nutrition_goals"

    id = Column(Integer, primary_key=True, index=True)
    daily_calories = Column(Integer, nullable=False)
    weekly_calories = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)

    # Relationship
    user = relationship("User", back_populates="nutrition_goal")

    def __repr__(self):
        return f"<NutritionGoal(id={self.id}, daily={self.daily_calories}, weekly={self.weekly_calories})>"
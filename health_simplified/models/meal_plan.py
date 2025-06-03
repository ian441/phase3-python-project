from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from health_simplified.db.database import Base

class MealPlan(Base):
    __tablename__ = 'meal_plans'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    week = Column(Integer)
    details = Column(String)

    user = relationship("User", back_populates="meal_plans")

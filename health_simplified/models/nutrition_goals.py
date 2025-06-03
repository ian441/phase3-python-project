from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from health_simplified.db.database import Base


class NutritionGoal(Base):
    __tablename__ = 'nutrition_goals'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    daily = Column(Integer)
    weekly = Column(Integer)

    user = relationship("User", back_populates="goals")

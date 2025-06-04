from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from health_simplified.db.database import Base

class FoodEntry(Base):
    __tablename__ = 'food_entries'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    food = Column(String)
    calories = Column(Integer)
    date = Column(Date)

    user = relationship("User", back_populates="food_entries")

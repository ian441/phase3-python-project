from pydantic import BaseModel
from datetime import date

class FoodEntryBase(BaseModel):
    food: str
    calories: int
    date: date

class FoodEntryCreate(FoodEntryBase):
    user_id: int

class FoodEntry(FoodEntryBase):
    id: int

    class Config:
        orm_mode = True

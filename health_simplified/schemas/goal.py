from pydantic import BaseModel

class GoalBase(BaseModel):
    daily: int
    weekly: int

class GoalCreate(GoalBase):
    user_id: int

class Goal(GoalBase):
    id: int

    class Config:
        orm_mode = True

from pydantic import BaseModel

class MealPlanBase(BaseModel):
    week: int
    details: str

class MealPlanCreate(MealPlanBase):
    user_id: int

class MealPlan(MealPlanBase):
    id: int

    class Config:
        orm_mode = True

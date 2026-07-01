from pydantic import BaseModel


class PlanRequest(BaseModel):
    level: str
    goal: str
    weeks: int
    daily_minutes: int


class ExerciseRequest(BaseModel):
    level: str
    goal: str
    weeks: int
    daily_minutes: int
    current_week: int


class EvaluateRequest(BaseModel):
    level: str
    goal: str
    weeks: int
    daily_minutes: int
    current_week: int
    user_answer: str
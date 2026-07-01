from fastapi import FastAPI

from app.schemas import PlanRequest, ExerciseRequest, EvaluateRequest
from app.agents import (
    goal_agent,
    curriculum_agent,
    practice_agent,
    orchestrator_agent,
)


app = FastAPI(title="AI Piano Coach")


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/plan")
def create_plan(request: PlanRequest):
    profile = goal_agent(
        level=request.level,
        goal=request.goal,
        weeks=request.weeks,
        daily_minutes=request.daily_minutes,
    )

    curriculum_plan = curriculum_agent(profile)

    return {
        "profile": profile,
        "curriculum_plan": curriculum_plan,
    }


@app.post("/exercise")
def create_exercise(request: ExerciseRequest):
    profile = goal_agent(
        level=request.level,
        goal=request.goal,
        weeks=request.weeks,
        daily_minutes=request.daily_minutes,
    )

    curriculum_plan = curriculum_agent(profile)

    exercise = practice_agent(
        curriculum_plan=curriculum_plan,
        week_number=request.current_week,
    )

    return {
        "exercise": exercise,
    }


@app.post("/evaluate")
def evaluate(request: EvaluateRequest):
    result = orchestrator_agent(
        level=request.level,
        goal=request.goal,
        weeks=request.weeks,
        daily_minutes=request.daily_minutes,
        current_week=request.current_week,
        user_answer=request.user_answer,
    )

    return result
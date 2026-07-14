from fastapi import FastAPI
from dotenv import load_dotenv
from pathlib import Path
from app.schemas import PlanRequest, ExerciseRequest, EvaluateRequest

from app.agents import (
    goal,
    curriculum,
    practice_agent,
    orchestrator_agent,
)

ROOT_DIR = Path(__file__).resolve().parent
load_dotenv(ROOT_DIR / ".env")


app = FastAPI(title="AI Piano Coach")


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/plan")
def create_plan(request: PlanRequest):
    profile = goal(
        level=request.level,
        goal=request.goal,
        weeks=request.weeks,
        daily_minutes=request.daily_minutes,
    )

    curriculum_plan = curriculum(profile)

    return {
        "profile": profile,
        "curriculum_plan": curriculum_plan,
    }


@app.post("/exercise")
def create_exercise(request: ExerciseRequest):
    profile = goal(
        level=request.level,
        goal=request.goal,
        weeks=request.weeks,
        daily_minutes=request.daily_minutes,
    )

    curriculum_plan = curriculum(profile)

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
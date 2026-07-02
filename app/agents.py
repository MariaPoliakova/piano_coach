from app.tools import load_curriculum, find_week, calculate_accuracy
from app.llm import ask_llm

def goal_agent(level: str, goal: str, weeks: int, daily_minutes: int) -> dict:
    return {
        "level": level,
        "goal": goal,
        "weeks": weeks,
        "daily_minutes": daily_minutes,
    }


def curriculum_agent(profile: dict) -> dict:
    curriculum = load_curriculum(profile["level"])

    selected_weeks = [
        week for week in curriculum["weeks"]
        if week["week"] <= profile["weeks"]
    ]

    return {
        "level": profile["level"],
        "goal": profile["goal"],
        "daily_minutes": profile["daily_minutes"],
        "weeks": selected_weeks,
    }


def practice_agent(curriculum_plan: dict, week_number: int) -> dict:
    selected_week = find_week(
        {"weeks": curriculum_plan["weeks"]},
        week_number
    )

    if selected_week is None:
        return {"error": f"Week {week_number} not found"}

    topic = selected_week["topics"][0]

    prompt = f"""
    You are an experienced piano teacher.

    Student profile:
    - Level: {curriculum_plan["level"]}
    - Goal: {curriculum_plan["goal"]}
    - Daily practice time: {curriculum_plan["daily_minutes"]} minutes

    Current lesson:
    - Week: {selected_week["week"]}
    - Title: {selected_week["title"]}
    - Topic: {topic}

    Create one beginner-friendly piano lesson.

    Return the answer in Markdown with these sections:

    ## Objective
    ## Exercise
    ## Practice Tips
    ## Common Mistakes
    ## Homework

    Keep it short and practical.
    """

    generated_lesson = ask_llm(prompt)


    return {
        "exercise_id": f"week_{week_number}_topic_1",
        "week": week_number,
        "title": selected_week["title"],
        "topic": topic,
        "type": "reflection",
        "question": f"What is the main focus of this exercise: '{topic}'?",
        "expected_answer": topic,
        "hint": "Look at the topic name and explain it in your own words.",
        "generated_lesson": generated_lesson,
    }


def feedback_agent(user_answer: str, expected_answer: str) -> dict:
    normalized_user = user_answer.strip().lower()
    normalized_expected = expected_answer.strip().lower()

    is_correct = normalized_expected in normalized_user or normalized_user in normalized_expected

    return {
        "correct": is_correct,
        "score": 1.0 if is_correct else 0.0,
        "feedback": (
            "Good answer. You understood the exercise focus."
            if is_correct
            else f"Not quite. The expected focus was: {expected_answer}"
        ),
    }


def progress_agent(previous_progress: dict, feedback: dict) -> dict:
    total = previous_progress.get("total_answers", 0) + 1
    correct = previous_progress.get("correct_answers", 0)

    if feedback["correct"]:
        correct += 1

    return {
        "total_answers": total,
        "correct_answers": correct,
        "accuracy": calculate_accuracy(correct, total),
        "current_level": previous_progress.get("current_level", "beginner"),
    }


def motivation_agent(progress: dict) -> str:
    if progress["accuracy"] >= 80:
        return "Great work. You are progressing well — keep practicing consistently."
    if progress["accuracy"] >= 50:
        return "Good start. Focus on repeating the basics slowly and carefully."
    return "Do not worry. Piano learning takes repetition. Start slow and stay consistent."


def orchestrator_agent(
    level: str,
    goal: str,
    weeks: int,
    daily_minutes: int,
    current_week: int,
    user_answer: str,
    previous_progress: dict | None = None,
) -> dict:
    if previous_progress is None:
        previous_progress = {
            "total_answers": 0,
            "correct_answers": 0,
            "accuracy": 0.0,
            "current_level": level,
        }

    profile = goal_agent(level, goal, weeks, daily_minutes)
    curriculum_plan = curriculum_agent(profile)
    exercise = practice_agent(curriculum_plan, current_week)
    feedback = feedback_agent(user_answer, exercise["expected_answer"])
    progress = progress_agent(previous_progress, feedback)
    motivation = motivation_agent(progress)

    return {
        "agent_flow": [
            "GoalAgent",
            "CurriculumAgent",
            "PracticeAgent",
            "FeedbackAgent",
            "ProgressAgent",
            "MotivationAgent",
        ],
        "profile": profile,
        "curriculum_plan": curriculum_plan,
        "exercise": exercise,
        "feedback": feedback,
        "progress": progress,
        "motivation": motivation,
    }
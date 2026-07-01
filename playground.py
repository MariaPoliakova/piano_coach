from pprint import pprint

from app.agents import (
    goal_agent,
    curriculum_agent,
    practice_agent,
    feedback_agent,
    progress_agent,
    motivation_agent,
    orchestrator_agent,
)


print("\n--- 1. Goal Agent ---")
profile = goal_agent(
    level="beginner",
    goal="play Happy Birthday",
    weeks=4,
    daily_minutes=20,
)
pprint(profile)


print("\n--- 2. Curriculum Agent ---")
curriculum_plan = curriculum_agent(profile)
for week in curriculum_plan["weeks"]:
    print(f"Week {week['week']}: {week['title']}")


print("\n--- 3. Practice Agent ---")
exercise = practice_agent(curriculum_plan, week_number=1)
pprint(exercise)


print("\n--- 4. Feedback Agent ---")
user_answer = "Correct hand position and posture"
feedback = feedback_agent(
    user_answer=user_answer,
    expected_answer=exercise["expected_answer"],
)
pprint(feedback)


print("\n--- 5. Progress Agent ---")
previous_progress = {
    "total_answers": 0,
    "correct_answers": 0,
    "accuracy": 0.0,
    "current_level": "beginner",
}
progress = progress_agent(previous_progress, feedback)
pprint(progress)


print("\n--- 6. Motivation Agent ---")
motivation = motivation_agent(progress)
print(motivation)


print("\n--- 7. Orchestrator Agent ---")
result = orchestrator_agent(
    level="beginner",
    goal="play Happy Birthday",
    weeks=4,
    daily_minutes=20,
    current_week=1,
    user_answer="Correct hand position and posture",
)
pprint(result)
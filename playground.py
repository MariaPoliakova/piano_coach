from pprint import pprint
from app.agents import goal_agent, curriculum_agent, practice_agent

profile = goal_agent(
    level="beginner",
    goal="play Happy Birthday",
    weeks=4,
    daily_minutes=20,
)

curriculum_plan = curriculum_agent(profile)

exercise = practice_agent(
    curriculum_plan=curriculum_plan,
    week_number=1,
)

pprint(exercise)
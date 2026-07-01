import json
from pathlib import Path


def load_curriculum(level: str) -> dict:
    file_path = Path("data") / f"{level}.json"

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def find_week(curriculum: dict, week_number: int):
    """
    Return the curriculum for a specific week.
    """

    for week in curriculum["weeks"]:
        if week["week"] == week_number:
            return week

    return None


def calculate_accuracy(correct_answers: int, total_answers: int):
    """
    Calculate the user's accuracy in percent.
    """

    if total_answers == 0:
        return 0.0

    return round(correct_answers / total_answers * 100, 2)
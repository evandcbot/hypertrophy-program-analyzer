from hypertrophy_analyzer import (
    calculate_muscle_sets,
    calculate_muscle_days,
    organize_workout_day,
    analyze_workout,
)


sample_exercises = [
    {
        "name": "Bench Press",
        "muscle": "Chest",
        "day": "Monday",
        "sets": 3,
        "reps": 8,
        "weight": 100,
    },
    {
        "name": "Cable Fly",
        "muscle": "Chest",
        "day": "Thursday",
        "sets": 2,
        "reps": 10,
        "weight": 40,
    },
    {
        "name": "Cable Row",
        "muscle": "Back",
        "day": "Monday",
        "sets": 4,
        "reps": 10,
        "weight": 80,
    },
]


muscle_sets = calculate_muscle_sets(sample_exercises)

assert muscle_sets["Chest"] == 5
assert muscle_sets["Back"] == 4


muscle_days = calculate_muscle_days(sample_exercises)

assert muscle_days["Chest"] == {"Monday", "Thursday"}
assert muscle_days["Back"] == {"Monday"}


workout_days = organize_workout_day(sample_exercises)

assert len(workout_days["Monday"]) == 2
assert len(workout_days["Thursday"]) == 1


analysis = analyze_workout(sample_exercises)

assert analysis["training_days"] == 2
assert analysis["weekly_sets"] == 9
assert analysis["busiest_day"] == "Monday"


assert calculate_muscle_sets([]) == {}
assert analyze_workout([]) is None


print("All tests passed!")
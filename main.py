exercises = [
# ==================== DAY 1 - UPPER ====================

    {
        "name": "Incline Bench Press",
        "muscle": "Chest",
        "day": "Monday",
        "sets": 2,
        "reps": 8,
        "weight": 75
    },
    {
        "name": "Cable Lateral Raise",
        "muscle": "Shoulders",
        "day": "Monday",
        "sets": 2,
        "reps": 6,
        "weight": 15
    },
    {
        "name": "Wide-Grip Lat Pulldown",
        "muscle": "Back",
        "day": "Monday",
        "sets": 2,
        "reps": 8,
        "weight": 100
    },
    {
        "name": "High-to-Low Cable Fly",
        "muscle": "Chest",
        "day": "Monday",
        "sets": 2,
        "reps": 10,
        "weight": 100
    },
    {
        "name": "Seated Cable Row",
        "muscle": "Back",
        "day": "Monday",
        "sets": 2,
        "reps": 10,
        "weight": 100
    },
    {
        "name": "Incline Dumbbell Curl",
        "muscle": "Biceps",
        "day": "Monday",
        "sets": 2,
        "reps": 10,
        "weight": 100
    },
    {
        "name": "Single-Arm Tricep Extension",
        "muscle": "Triceps",
        "day": "Monday",
        "sets": 2,
        "reps": 10,
        "weight": 100
    },


    # ==================== DAY 2 - LOWER ====================

    {
        "name": "Hack Squat",
        "muscle": "Quads",
        "day": "Tuesday",
        "sets": 2,
        "reps": 10,
        "weight": 100
    },
    {
        "name": "Seated Hamstring Curl",
        "muscle": "Hamstrings",
        "day": "Tuesday",
        "sets": 2,
        "reps": 10,
        "weight": 100
    },
    {
        "name": "Leg Extension",
        "muscle": "Quads",
        "day": "Tuesday",
        "sets": 2,
        "reps": 10,
        "weight": 100
    },
    {
        "name": "Standing Calf Raise",
        "muscle": "Calves",
        "day": "Tuesday",
        "sets": 2,
        "reps": 10,
        "weight": 100
    },
    {
        "name": "Hip Abduction Machine",
        "muscle": "Glutes",
        "day": "Tuesday",
        "sets": 2,
        "reps": 10,
        "weight": 100
    },
    {
        "name": "Back Extension",
        "muscle": "Lower Back",
        "day": "Tuesday",
        "sets": 2,
        "reps": 10,
        "weight": 100
    },


    # ==================== DAY 3 - UPPER ====================

    {
        "name": "Pec Deck",
        "muscle": "Chest",
        "day": "Thursday",
        "sets": 2,
        "reps": 10,
        "weight": 100
    },
    {
        "name": "Low-to-High Cable Fly",
        "muscle": "Chest",
        "day": "Thursday",
        "sets": 2,
        "reps": 10,
        "weight": 100
    },
    {
        "name": "Cable Rear Delt Fly",
        "muscle": "Rear Delts",
        "day": "Thursday",
        "sets": 2,
        "reps": 10,
        "weight": 100
    },
    {
        "name": "Preacher Curl",
        "muscle": "Biceps",
        "day": "Thursday",
        "sets": 2,
        "reps": 10,
        "weight": 100
    },
    {
        "name": "Reverse Cable Curl",
        "muscle": "Forearms",
        "day": "Thursday",
        "sets": 2,
        "reps": 10,
        "weight": 100
    },
    {
        "name": "Machine Dips",
        "muscle": "Triceps",
        "day": "Thursday",
        "sets": 2,
        "reps": 10,
        "weight": 100
    },
    {
        "name": "Hammer Curl",
        "muscle": "Biceps",
        "day": "Thursday",
        "sets": 2,
        "reps": 10,
        "weight": 100
    },


    # ==================== DAY 4 - LOWER ====================

    {
        "name": "Stiff-Leg Deadlift",
        "muscle": "Hamstrings",
        "day": "Friday",
        "sets": 2,
        "reps": 10,
        "weight": 100
    },
    {
        "name": "Bulgarian Split Squat",
        "muscle": "Quads",
        "day": "Friday",
        "sets": 2,
        "reps": 10,
        "weight": 100
    },
    {
        "name": "Hamstring Curl",
        "muscle": "Hamstrings",
        "day": "Friday",
        "sets": 2,
        "reps": 10,
        "weight": 100
    },
    {
        "name": "Leg Extension",
        "muscle": "Quads",
        "day": "Friday",
        "sets": 2,
        "reps": 10,
        "weight": 100
    },
    {
        "name": "Hip Adduction Machine",
        "muscle": "Adductors",
        "day": "Friday",
        "sets": 2,
        "reps": 10,
        "weight": 100
    }
]

for exercise in exercises:
    print(f"{exercise['name']}, {exercise['muscle']}: {exercise['sets']} sets of {exercise['reps']} reps at {exercise['weight']} lbs")

muscle_sets = {}
for exercise in exercises:
    muscle = exercise["muscle"]
    if muscle not in muscle_sets:
        muscle_sets[muscle] = 0
    muscle_sets[muscle] += exercise["sets"]

muscle_days = {}

for exercise in exercises:
    muscle = exercise["muscle"]
    day = exercise["day"]
    if muscle not in muscle_days:
        muscle_days[muscle] = set()
    muscle_days[muscle].add(day)



for muscle in muscle_sets:
    print(f"{muscle}: {muscle_sets[muscle]} sets over {len(muscle_days[muscle])} days")

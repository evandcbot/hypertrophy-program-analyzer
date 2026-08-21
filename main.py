bench_press = {"name": "Bench Press", "muscle": "Chest", "sets": 3, "reps": 10, "weight": 135}
incline_bench_press = {"name": "Incline Bench Press", "muscle": "Chest", "sets": 3, "reps": 10, "weight": 115}
incline_dumbbell_press = {"name": "Incline Dumbbell Press", "muscle": "Chest", "sets": 3, "reps": 10, "weight": 40}

exercises = [bench_press, incline_bench_press, incline_dumbbell_press]
for exercise in exercises:
    print(f"{exercise['name']}, {exercise['muscle']}: {exercise['sets']} sets of {exercise['reps']} reps at {exercise['weight']} lbs")

muscle_sets = {}
for exercise in exercises:
    muscle = exercise["muscle"]
    if muscle not in muscle_sets:
        muscle_sets[muscle] = 0
    muscle_sets[muscle] += exercise["sets"]



for muscle in muscle_sets:
    print(f"{muscle}: {muscle_sets[muscle]} sets")

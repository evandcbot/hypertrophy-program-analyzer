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

#calculates how many sets per week each muscle group gets worked
def calculate_muscle_sets(exercises):
    muscle_sets = {}
    for exercise in exercises:
        muscle = exercise["muscle"]
        if muscle not in muscle_sets:
            muscle_sets[muscle] = 0
        muscle_sets[muscle] += exercise["sets"]
    return muscle_sets



#calculates what day each muscle is exercised
def calculate_muscle_days(exercises):
    muscle_days = {}

    for exercise in exercises:
        muscle = exercise["muscle"]
        day = exercise["day"]
        if muscle not in muscle_days:
            muscle_days[muscle] = set()
        muscle_days[muscle].add(day)
    return muscle_days


#calculates ALL of the muscles hit each day
def calculate_day_muscles(exercises):
    day_muscles = {}

    for exercise in exercises:
        muscle = exercise["muscle"]
        day = exercise["day"]
        if day not in day_muscles:
            day_muscles[day] = set()
        day_muscles[day].add(muscle)
    return day_muscles

day_muscles = calculate_day_muscles(exercises)
#print(day_muscles)

#organizes above information into one easily readable section
def organize_workout_day(exercises):
    workout_day = {}
    for exercise in exercises:
        day = exercise["day"]
        if day not in workout_day:
            workout_day[day] = []
        workout_day[day].append(exercise)
    return workout_day

def display_workout(workout_day):
    for key in workout_day:
        print(f'{key}:\n')
        for exercise in workout_day[key]:
            name = exercise["name"]
            sets = exercise["sets"]
            reps = exercise["reps"]
            weight = exercise["weight"]
            print(f'{name}: {sets} sets of {reps} reps at {weight} lbs')
        print()

#prints weekly workout summary

def workout_summary(muscle_sets, muscle_days):
    print(f'WEEKLY WORKOUT SUMMARY:\n')
    for muscle in muscle_sets:
        sets = muscle_sets[muscle]
        days = len(muscle_days[muscle])
        print(f'{muscle}: {sets} sets across {days} days ')

def add_exercise(exercises):
    name = input("Exercise name: ").capitalize()
    muscle = input("Muscle worked: ").capitalize()
    days = input("Day(s) worked, separated by commas: ").split(",")
    while True:
        try:
            sets = int(input("Sets done: "))
            if sets <= 0:
                print("Sets must be greater than 0")
            else:
                break
        except ValueError:
            print("Sets must be a whole number")
    while True:
        try:
            reps = int(input("Reps worked: "))
            if reps <= 0:
                print("Reps must be greater than 0")
            else:
                break
        except ValueError:
            print("Reps must be a whole number")
    while True:
        try:
            weight = int(input("Weighted lifted: "))
            if weight <= 0:
                print("Weight must be greater than 0")
            else:
                break
        except ValueError:
            print("Weight must be a whole number")

    for day in days:
        day = day.strip().capitalize()
        new_exercise = {
            "name": name,
            "muscle": muscle,
            "day": day,
            "sets": sets,
            "reps": reps,
            "weight": weight
        }
        exercises.append(new_exercise)
        print(f'{new_exercise} added succesfully')


def view_workout(exercises):
    workout_day = organize_workout_day(exercises)
    display_workout(workout_day)

def view_summary(exercises):
    muscle_sets = calculate_muscle_sets(exercises)
    muscle_days = calculate_muscle_days(exercises)
    workout_summary(muscle_sets, muscle_days)

while True:
    print("HYPERTROPHY TRAINING PROGRAM")
    print()
    print("1. View workout")
    print("2. View weekly muscle summary")
    print("3. Add exercise")
    print("4. Exit")

    choice = input("choose option: ")
    if choice == "1":
        view_workout(exercises)
    elif choice == "2":
        view_summary(exercises)
    elif choice == "3":
        input("Please fill in the following information (press 'Enter' to continue): ")
        add_exercise(exercises)
    elif choice == "4":
        print("Program Closed")
        break
    else:
        print("Error: Invalid option")
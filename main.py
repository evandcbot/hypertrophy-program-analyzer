import json
from pathlib import Path

project_folder = Path(__file__).parent
exercise_file = project_folder / 'exercises.json'

def load_exercises():
    try:
        with open(exercise_file, 'r') as file:
            exercises = json.load(file)
        if isinstance(exercises, list):
            return exercises
        else:
            print("Error: JSON data must be stored as a list.")
            return []
    except FileNotFoundError:
        print("No exercises file found. Starting with an empty workout.")
        return []
    except json.JSONDecodeError:
        print("Error: exercises.json contains invalid JSON.")
        return []

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
    name = input("Exercise name: ").strip()
    muscle = input("Muscle worked: ").strip().title()
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
            weight = int(input("Weight lifted: "))
            if weight <= 0:
                print("Weight must be greater than 0")
            else:
                break
        except ValueError:
            print("Weight must be a whole number")

    for day in days:
        day = day.strip().title()
        new_exercise = {
            "name": name,
            "muscle": muscle,
            "day": day,
            "sets": sets,
            "reps": reps,
            "weight": weight
        }
        exercises.append(new_exercise)
        print(f'{name} added to {day} succesfully!')

    save_exercises(exercises)


def view_workout(exercises):
    workout_day = organize_workout_day(exercises)
    display_workout(workout_day)

def view_summary(exercises):
    muscle_sets = calculate_muscle_sets(exercises)
    muscle_days = calculate_muscle_days(exercises)
    workout_summary(muscle_sets, muscle_days)

def save_exercises(exercises):
    with open(exercise_file, "w") as file:
        json.dump(exercises, file, indent=4)

def delete_exercises(exercises):
    if not exercises:
        print("No exercises to delete")
        return
    for number, exercise in enumerate(exercises, start=1):
        print(number, exercise["name"], exercise["day"])

    while True:
        try:
            choice = int(input("Pick a number: "))
            if choice < 1 or choice > len(exercises):
                print("invalid option: must choose a numbered exercise")
                continue
            exercise = exercises[choice - 1]
            print(f'Are you sure you wish to delete {exercise["name"]} from your schedule on {exercise["day"]}?')
            confirmation = input("yes/no: ").strip().lower()
            if confirmation == "yes":
                exercises.pop(choice - 1)
                save_exercises(exercises)
                print("Exercise deleted successfully!")
            elif confirmation == "no":
                break
            else:
                print("Error: Invalid Option")
            break
        except ValueError:
            print("Error: Must be a number")

def edit_exercises(exercises):
    if not exercises:
        print("No exercises to edit")
        return

    for number, exercise in enumerate(exercises, start=1):
        print(number, exercise["name"], exercise["day"])

    while True:
        try:
            choice = int(input("Which exercise would you like to edit?: "))
            if 1 <= choice <= len(exercises):
                break
            print("Invalid option: must choose a numbered exercise")
        except ValueError:
            print("Error: enter a valid exercise number")

    exercise = exercises[choice - 1]
    print("\nSelected exercise:")
    editable_fields = ["name", "muscle", "day", "sets", "reps", "weight"]
    for number, field in enumerate(editable_fields, start=1):
        print(f"{number}. {field.capitalize()}: {exercise[field]}")

    while True:
        field_choice = input("Enter the field number or name to edit: ").strip().lower()
        if field_choice.isdigit():
            field_number = int(field_choice)
            if 1 <= field_number <= len(editable_fields):
                selected_field = editable_fields[field_number - 1]
                break
        elif field_choice in editable_fields:
            selected_field = field_choice
            break
        print("Invalid option: choose a listed field")

    while True:
        new_value = input(f"Please type the new value for {selected_field}: ").strip()
        if not new_value:
            print("Value cannot be empty")
            continue
        if selected_field in ["sets", "reps", "weight"]:
            try:
                new_value = int(new_value)
            except ValueError:
                print("Error: enter a whole number")
                continue
            if new_value <= 0:
                print("Value must be greater than 0")
                continue
        elif selected_field == ["name"]:
            pass
        elif selected_field in ["muscle", "day"]:
            new_value = new_value.title()
        break

    print(f'Are you sure you want to change {exercise["name"]} '
          f'{selected_field} to {new_value}?')
    confirmation = input("yes/no: ").strip().lower()
    if confirmation == "yes":
        exercise[selected_field] = new_value
        save_exercises(exercises)
        print("Exercise updated successfully!")
    else:
        print("Exercise was not changed")

def analyze_workout(exercises):
    if not exercises:
        return None
    muscle_sets = calculate_muscle_sets(exercises)
    muscle_days = calculate_muscle_days(exercises)

    day_sets = {}
    weekly_sets = 0
    for exercise in exercises:
        day = exercise["day"]
        sets = exercise["sets"]
        weekly_sets += sets
        if day not in day_sets:
            day_sets[day] = 0
        day_sets[day] += sets
    training_days = len(day_sets)
    exercises_length = len(exercises)
    avg_sets_per_day = weekly_sets / training_days
    highest_volume_muscle = max(muscle_sets, key=muscle_sets.get)
    lowest_volume_muscle = min(muscle_sets, key=muscle_sets.get)
    busiest_day = max(day_sets, key=day_sets.get)

    once_weekly = []
    for muscle in muscle_days:
        if len(muscle_days[muscle]) == 1:
            once_weekly.append(muscle)
    return {
        "training_days": training_days,
        "exercise_entries": exercises_length,
        "weekly_sets": weekly_sets,
        "average_sets_per_day": avg_sets_per_day,
        "highest_volume_muscle": highest_volume_muscle,
        "highest_volume_sets": muscle_sets[highest_volume_muscle],
        "lowest_volume_muscle": lowest_volume_muscle,
        "lowest_volume_sets": muscle_sets[lowest_volume_muscle],
        "busiest_day": busiest_day,
        "busiest_day_sets": day_sets[busiest_day],
        "trained_once_weekly": once_weekly
    }

def display_analysis(analysis):
    if analysis is None:
        print("No exercises available.")
        return
    print("\n PROGRAM ANALYSIS \n")
    print(f'Training Days: {analysis["training_days"]}')
    print(f'Exercise Entries: {analysis["exercise_entries"]}')
    print(f'Weekly Sets: {analysis["weekly_sets"]}')
    print(f'Average Sets Per Day: {analysis["average_sets_per_day"]}:.1f')
    print(f'Highest Volume Muscle: {analysis["highest_volume_muscle"]} --- {analysis["highest_volume_sets"]} sets')
    print(f'Lowest Volume Muscle: {analysis["lowest_volume_muscle"]} --- {analysis["lowest_volume_sets"]} sets')
    print(f'Busiest Day: {analysis["busiest_day"]} --- {analysis["busiest_day_sets"]} sets')
    print("Muscles Trained Once Weekly: ")
    if analysis["trained_once_weekly"]:
        for muscle in analysis["trained_once_weekly"]:
            print(f'- {muscle}')
    else:
        print(" - None")

def view_analysis(exercises):
    analysis = analyze_workout(exercises)
    display_analysis(analysis)

def main():
    exercises = load_exercises()
    while True:
        print("HYPERTROPHY TRAINING PROGRAM")
        print()
        print("1. View workout")
        print("2. View weekly muscle summary")
        print("3. Add exercise")
        print("4. Delete exercise")
        print("5. Edit exercise")
        print("6. View program analysis")
        print("7. Exit")

        choice = input("\nChoose an option: ").strip()
        if choice == "1":
            view_workout(exercises)
        elif choice == "2":
            view_summary(exercises)
        elif choice == "3":
            input("Please fill in the following information (press 'Enter' to continue): ")
            add_exercise(exercises)
        elif choice == "4":
            delete_exercises(exercises)
        elif choice == "5":
            edit_exercises(exercises)
        elif choice == "6":
            view_analysis(exercises)
        elif choice == "7":
            print("Program Closed")
            break
        else:
            print("Error: Invalid option")

if __name__ == "__main__":
    main()
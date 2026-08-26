# Hypertrophy Program Analyzer

A command-line Python application for creating, managing, and analyzing resistance-training programs.

The Hypertrophy Program Analyzer turns workout data into a clear weekly summary. Users can add, edit, view, and delete exercises while the program calculates training volume, frequency, and schedule statistics. Workout data is saved locally so changes remain available between sessions.

I built this as my first independent Python project after completing the free Futurecoder course. The project gave me practical experience with Python data structures, functions, input validation, file handling, automated testing, and Git.

## Features

* View exercises organized by training day
* Add exercises to one or more days
* Edit existing exercise information
* Delete exercises with confirmation
* Calculate weekly sets for each muscle group
* Calculate how many days each muscle is trained
* Identify the highest- and lowest-volume muscle groups
* Identify the busiest training day
* List muscles trained only once per week
* Save workout data between sessions using JSON
* Validate menu choices and exercise information
* Handle missing, empty, or invalid data files
* Run automated tests for core calculations

## Example Analysis

```text
PROGRAM ANALYSIS

Training Days: 4
Exercise Entries: 26
Weekly Sets: 52
Average Sets Per Day: 13.0
Highest Volume Muscle: Chest — 8 sets
Lowest Volume Muscle: Shoulders — 2 sets
Busiest Day: Thursday — 16 sets

Muscles Trained Once Weekly:
- Shoulders
- Calves
- Glutes
- Lower Back
- Rear Delts
- Forearms
- Adductors
```

## Technologies Used

* Python
* JSON
* `pathlib`
* Git
* GitHub

No external Python packages are required.

## Installation

1. Download or clone this repository.
2. Make sure Python 3 is installed.
3. Open a terminal in the project folder.
4. Run the application:

```bash
python hypertrophy_analyzer.py
```

On Windows, you may need to use:

```powershell
py hypertrophy_analyzer.py
```

Follow the numbered instructions displayed in the terminal.

## Data Storage

Workout information is stored locally in `exercises.json`. Each exercise is represented as a JSON object containing its name, primary muscle group, training day, sets, reps, and weight.

An example workout is included so the program can be explored immediately. Changes made through the application are automatically saved to the JSON file.

Example entry:

```json
{
    "name": "Bench Press",
    "muscle": "Chest",
    "day": "Monday",
    "sets": 3,
    "reps": 8,
    "weight": 135
}
```

## Running the Tests

The project includes automated tests for its core calculation and organization functions.

Run them with:

```bash
python test_analyzer.py
```

On Windows, you may need to use:

```powershell
py test_analyzer.py
```

A successful test run displays:

```text
All tests passed!
```

## Current Limitations

* The program runs entirely in the terminal.
* Workout data is stored in one local JSON file.
* Each exercise currently records one primary muscle group.
* Sets are treated equally and are not adjusted for effort, exercise selection, or indirect muscle involvement.
* The analysis is descriptive and does not yet provide research-based training recommendations.
* The program does not currently support separate user profiles.

## Future Plans

* Add evidence-based volume and frequency recommendations
* Support secondary muscles and indirect training volume
* Add a graphical user interface
* Support multiple workout programs and user profiles
* Track workout performance over time
* Add charts and progress reports
* Generate workout suggestions based on user goals
* Explore optional AI-assisted program feedback
* Expand the automated test suite

## What I Learned

This was my first independent Python project after completing the free Futurecoder course. Building it taught me how lists, dictionaries, sets, loops, and functions work together in a complete application rather than in isolated exercises.

I also learned how to validate user input, read and write JSON data, organize code into reusable functions, and test calculations using known inputs and expected results. One of the most challenging features was the editing system, which dynamically maps a user’s menu selection to a dictionary field while handling text and numeric values differently.

I intentionally wrote the core logic myself and used AI mainly for feedback, debugging guidance, and code review. I plan to continue developing the project because it has already made my own workout program easier to inspect, and it has room to grow into a more useful training-analysis tool.

## Disclaimer

This project is an educational software tool, not medical or professional training advice. Its current analysis describes workout data but does not determine whether a program is safe or optimal.

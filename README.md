# Rural Tele-Triage & Offline Patient Prioritization System
### (Beginner-Level Console Version)

A 100%-offline, console-based Python program that helps rural clinics and medical camps
objectively prioritize patients by clinical urgency, using a simple rule-based scoring system
inspired by the NEWS2 (National Early Warning Score) methodology.

This version is written using only **beginner-level Python**: plain functions, `if`/`elif`
statements, `for`/`while` loops, lists, and dictionaries. There are **no classes**, no external
libraries, and no advanced data structures — just the `json` module from the standard library
for saving data.

## Overview

Rural clinics often see large crowds with limited staff, no internet access, and no
specialist-grade decision support. This program:

- Asks simple, validated questions to register a patient's demographics, vital signs, and
  symptoms.
- Calculates an objective triage score and category (Critical / Urgent / Semi-Urgent /
  Non-Urgent).
- Always shows the waiting list sorted with the most urgent patient first.
- Saves everything to a local JSON file, so nothing is lost if the program is closed.
- Prints simple analytics: totals and a text-based bar chart by category.

## Features

- **Menu-driven console interface** — register patients, view the queue, call the next patient,
  mark someone as treated, and view analytics, all from one simple numbered menu.
- **Input validation** — every field (age, temperature, blood pressure, etc.) is checked with a
  loop that keeps asking until valid input is given.
- **Rule-Based Triage Scoring** — scores respiratory rate, SpO2, systolic blood pressure, heart
  rate, temperature, and consciousness level (AVPU scale); adds a small age-vulnerability point
  for very young or very old patients; and immediately flags a patient as Critical if they
  report a red-flag symptom (e.g. severe bleeding, unconsciousness, seizures).
- **Priority Queue** — implemented with a simple, readable bubble sort (no external libraries),
  ordered by category, then score, then arrival order.
- **Offline JSON Storage** — patient records are saved to `data/patients.json` using Python's
  built-in `json` module, and reloaded automatically next time the program runs.
- **Analytics** — shows total patients, current queue size, and a simple `*`-based bar chart
  per category.
- **Automated Tests** — plain `assert`-based test scripts (no testing framework needed) check
  the triage scoring, queue ordering, and validation logic.

## Technologies / Tools Used

- **Python 3** (standard library only)
- `json` — for saving and loading patient data
- `datetime` — for recording arrival times
- Plain `assert` statements for testing (no external test framework)

No external/third-party packages are required — nothing to `pip install`.

## Project Structure

```
rural-tele-triage-simple/
├── main.py                          # Program entry point (menu loop)
├── patient_functions.py             # Module 1: Patient registration
├── triage_functions.py              # Module 2: Triage scoring rules
├── queue_functions.py               # Module 3: Priority queue (bubble sort)
├── storage_functions.py             # Module 4: Save/load JSON data
├── analytics_functions.py           # Module 5: Reporting & analytics
├── validation_functions.py          # Input validation helpers
├── tests/
│   ├── test_triage_functions.py
│   ├── test_queue_functions.py
│   └── test_validation_functions.py
├── data/                            # Created automatically: patients.json
├── README.md
└── statement.md
```

## Steps to Install & Run

1. Make sure **Python 3** is installed (check with `python3 --version`).
2. Download or clone this repository.
3. No installation steps are needed — the program only uses the standard library.
4. From the project folder, run:

   ```bash
   python3 main.py
   ```

5. Follow the on-screen menu:
   ```
   1. Register a new patient
   2. View priority queue
   3. Call next patient
   4. Mark a patient as treated
   5. View analytics
   6. Save and exit
   ```

6. A `data/patients.json` file will be created automatically the first time you register a
   patient, and will be reloaded automatically the next time you run the program.

## Instructions for Testing

Each test file can be run directly and prints `PASSED:` for every check, ending with
`ALL TESTS PASSED`:

```bash
python3 tests/test_triage_functions.py
python3 tests/test_queue_functions.py
python3 tests/test_validation_functions.py
```

## Screenshots

_Run the program in your terminal and paste a screenshot of the menu, a completed registration,
and the priority queue view here._

## Future Enhancements

- Export the day's patient list to a simple CSV file to hand off to a central hospital.
- Let the clinic staff adjust the scoring thresholds for their specific region.
- Add a simple search-by-name option to look up a patient already registered today.

"""
storage_functions.py

Saves and loads the list of patients to a JSON file, so patient data is
not lost when the program is closed. JSON is used here because it is
built into Python (the `json` module) and maps naturally onto the lists
and dictionaries this program already uses.
"""

import json
import os

DATA_FOLDER = "data"
DATA_FILE = os.path.join(DATA_FOLDER, "patients.json")


def save_patients(patients_list, filename=DATA_FILE):
    """Write the patients list to a JSON file."""
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    try:
        with open(filename, "w") as file:
            json.dump(patients_list, file, indent=2)
        print(f"(Data saved to {filename})")
    except Exception as error:
        print("Something went wrong while saving data:", error)


def load_patients(filename=DATA_FILE):
    """Read the patients list back from a JSON file.
    If the file does not exist yet, just return an empty list."""
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r") as file:
            patients_list = json.load(file)
        print(f"(Loaded {len(patients_list)} patient record(s) from {filename})")
        return patients_list
    except Exception as error:
        print("Something went wrong while loading data:", error)
        return []

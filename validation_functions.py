"""
validation_functions.py

Simple functions that keep asking the user for input until they type
something valid. Each function uses a while loop and try/except so the
program never crashes just because someone typed the wrong kind of thing.
"""

VALID_GENDERS = ["Male", "Female", "Other"]
VALID_CONSCIOUSNESS = ["Alert", "Voice", "Pain", "Unresponsive"]


# ---------------------------------------------------------------------
# Pure "checker" functions (no input() calls) - these hold the actual
# validation rules, so they can be tested directly without typing
# anything. The get_valid_* functions below just repeatedly ask the
# user for input until one of these checkers says it is okay.
# ---------------------------------------------------------------------

def is_valid_name(name):
    return name.strip() != ""


def is_valid_age(age):
    return 0 <= age <= 120


def is_valid_contact_format(contact):
    if contact == "":
        return True
    for character in contact:
        if not (character.isdigit() or character in " +-()"):
            return False
    return True


def is_valid_number_in_range(value, minimum, maximum):
    return minimum <= value <= maximum


def get_valid_name():
    while True:
        name = input("Patient name: ").strip()
        if is_valid_name(name):
            return name
        else:
            print("Name cannot be empty. Please try again.")


def get_valid_age():
    while True:
        age_text = input("Age (years): ").strip()
        try:
            age = int(age_text)
        except ValueError:
            print("Age must be a whole number. Please try again.")
            continue
        if is_valid_age(age):
            return age
        else:
            print("Age must be between 0 and 120. Please try again.")


def get_valid_gender():
    while True:
        print("Gender options:", VALID_GENDERS)
        gender = input("Gender: ").strip().title()
        if gender in VALID_GENDERS:
            return gender
        else:
            print("Please type one of:", VALID_GENDERS)


def get_valid_contact():
    while True:
        contact = input("Contact number (or leave blank): ").strip()
        if is_valid_contact_format(contact):
            return contact
        else:
            print("Contact number should only contain digits, spaces, +, -, ( or ).")


def get_valid_number(prompt, minimum, maximum, is_float=False):
    """Generic helper for reading a number in a given range."""
    while True:
        text = input(prompt).strip()
        try:
            if is_float:
                value = float(text)
            else:
                value = int(text)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if is_valid_number_in_range(value, minimum, maximum):
            return value
        else:
            print(f"Value must be between {minimum} and {maximum}. Please try again.")


def get_valid_temperature():
    return get_valid_number("Temperature in Celsius (e.g. 37.0): ", 25.0, 45.0, is_float=True)


def get_valid_systolic_bp():
    return get_valid_number("Systolic blood pressure (mmHg): ", 40, 300)


def get_valid_heart_rate():
    return get_valid_number("Heart rate (beats per minute): ", 20, 250)


def get_valid_respiratory_rate():
    return get_valid_number("Respiratory rate (breaths per minute): ", 4, 70)


def get_valid_spo2():
    return get_valid_number("SpO2 / oxygen saturation (%): ", 0, 100)


def get_valid_consciousness():
    while True:
        print("Consciousness options:", VALID_CONSCIOUSNESS)
        level = input("Consciousness level: ").strip().title()
        if level in VALID_CONSCIOUSNESS:
            return level
        else:
            print("Please type one of:", VALID_CONSCIOUSNESS)


def get_valid_symptoms(common_symptoms):
    print("Common symptoms:", ", ".join(common_symptoms))
    text = input("Type symptoms separated by commas (or leave blank): ").strip()
    if text == "":
        return []
    symptoms = []
    for item in text.split(","):
        cleaned = item.strip().lower()
        if cleaned != "":
            symptoms.append(cleaned)
    return symptoms

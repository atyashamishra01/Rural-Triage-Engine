"""
patient_functions.py

Every patient is stored as a plain Python dictionary (no classes). This
module has the functions that ask the user for a new patient's details
and package them up into that dictionary.
"""

import datetime
import validation_functions as validators
import triage_functions as triage


def get_next_patient_id(patients_list):
    """Find the next free patient ID by looking at the highest one so far."""
    highest_id = 0
    for patient in patients_list:
        if patient["patient_id"] > highest_id:
            highest_id = patient["patient_id"]
    return highest_id + 1


def register_new_patient(patients_list):
    """Ask the user questions, build a patient dictionary, score it, and
    add it to the list. Returns the new patient dictionary."""

    print("\n--- Register New Patient ---")
    name = validators.get_valid_name()
    age = validators.get_valid_age()
    gender = validators.get_valid_gender()
    contact = validators.get_valid_contact()

    print("\n--- Vital Signs ---")
    temperature = validators.get_valid_temperature()
    systolic_bp = validators.get_valid_systolic_bp()
    heart_rate = validators.get_valid_heart_rate()
    respiratory_rate = validators.get_valid_respiratory_rate()
    spo2 = validators.get_valid_spo2()
    consciousness = validators.get_valid_consciousness()

    print("\n--- Symptoms ---")
    symptoms = validators.get_valid_symptoms(triage.COMMON_SYMPTOMS)

    notes = input("\nAny extra notes (optional): ").strip()

    score = triage.calculate_triage_score(
        temperature, systolic_bp, heart_rate, respiratory_rate, spo2, consciousness, age
    )
    category = triage.get_triage_category(
        score, symptoms, temperature, systolic_bp, heart_rate, respiratory_rate,
        spo2, consciousness
    )

    patient = {
        "patient_id": get_next_patient_id(patients_list),
        "name": name,
        "age": age,
        "gender": gender,
        "contact": contact,
        "temperature": temperature,
        "systolic_bp": systolic_bp,
        "heart_rate": heart_rate,
        "respiratory_rate": respiratory_rate,
        "spo2": spo2,
        "consciousness": consciousness,
        "symptoms": symptoms,
        "notes": notes,
        "arrival_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "score": score,
        "category": category,
        "status": "Waiting",
    }

    patients_list.append(patient)

    print(f"\nPatient '{name}' registered successfully.")
    print(f"Triage result -> Score: {score}, Category: {category}")

    return patient

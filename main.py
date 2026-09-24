"""
main.py

Rural Tele-Triage & Offline Patient Prioritization System
(Beginner-level console version)

Run this file with:
    python main.py

This program uses only plain functions, lists and dictionaries, and the
standard `json` module - no classes, no GUI, and no advanced libraries.
"""

import patient_functions
import queue_functions
import storage_functions
import analytics_functions


def print_menu():
    print("\n===== Rural Tele-Triage System =====")
    print("1. Register a new patient")
    print("2. View priority queue")
    print("3. Call next patient")
    print("4. Mark a patient as treated")
    print("5. View analytics")
    print("6. Save and exit")


def call_next_patient(patients_list):
    next_patient = queue_functions.get_next_patient(patients_list)
    if next_patient is None:
        print("\nThere are no waiting patients.")
        return

    print(f"\nPlease attend to: {next_patient['name']} "
          f"(ID {next_patient['patient_id']})")
    print(f"Category: {next_patient['category']}, Score: {next_patient['score']}")

    # Update the patient's status inside the main list.
    for patient in patients_list:
        if patient["patient_id"] == next_patient["patient_id"]:
            patient["status"] = "In Treatment"


def mark_patient_treated(patients_list):
    id_text = input("Enter the Patient ID to mark as treated: ").strip()
    try:
        patient_id = int(id_text)
    except ValueError:
        print("Please enter a valid whole number ID.")
        return

    found = False
    for patient in patients_list:
        if patient["patient_id"] == patient_id:
            patient["status"] = "Treated"
            found = True
            print(f"Patient {patient['name']} (ID {patient_id}) marked as treated.")

    if not found:
        print("No patient found with that ID.")


def main():
    print("Starting Rural Tele-Triage & Offline Patient Prioritization System...")
    patients_list = storage_functions.load_patients()

    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            patient_functions.register_new_patient(patients_list)
            storage_functions.save_patients(patients_list)

        elif choice == "2":
            queue_functions.print_queue(patients_list)

        elif choice == "3":
            call_next_patient(patients_list)
            storage_functions.save_patients(patients_list)

        elif choice == "4":
            mark_patient_treated(patients_list)
            storage_functions.save_patients(patients_list)

        elif choice == "5":
            analytics_functions.print_analytics(patients_list)

        elif choice == "6":
            storage_functions.save_patients(patients_list)
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()

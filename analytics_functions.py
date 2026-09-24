"""
analytics_functions.py

Simple reporting functions: counts how many patients fall into each
triage category and prints an easy-to-read summary, including a basic
bar chart made out of asterisk (*) characters.
"""

CATEGORY_ORDER = ["Critical", "Urgent", "Semi-Urgent", "Non-Urgent"]


def count_by_category(patients_list):
    """Return a dictionary like {'Critical': 2, 'Urgent': 5, ...}"""
    counts = {}
    for category in CATEGORY_ORDER:
        counts[category] = 0

    for patient in patients_list:
        category = patient["category"]
        counts[category] = counts[category] + 1

    return counts


def count_waiting(patients_list):
    total_waiting = 0
    for patient in patients_list:
        if patient["status"] == "Waiting":
            total_waiting = total_waiting + 1
    return total_waiting


def print_analytics(patients_list):
    print("\n--- Clinic Analytics ---")
    print("Total patients registered (all-time):", len(patients_list))
    print("Currently waiting:", count_waiting(patients_list))

    counts = count_by_category(patients_list)

    print("\nBreakdown by category:")
    for category in CATEGORY_ORDER:
        number_of_patients = counts[category]
        bar = "*" * number_of_patients
        print(f"{category:<14}: {bar} ({number_of_patients})")

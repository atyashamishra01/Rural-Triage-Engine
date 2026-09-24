"""
queue_functions.py

Manages the order in which waiting patients should be seen. Instead of
using an advanced data structure like a heap, this uses a simple bubble
sort that a beginner can read line by line. Bubble sort is a bit slower
for very large lists, but for a single clinic's waiting list this is
plenty fast and much easier to follow.
"""

CATEGORY_RANK = {
    "Critical": 1,
    "Urgent": 2,
    "Semi-Urgent": 3,
    "Non-Urgent": 4,
}


def get_priority_number(patient):
    """Lower number = higher priority = should be seen sooner."""
    rank = CATEGORY_RANK[patient["category"]]
    # Multiplying the rank keeps categories from overlapping, then we
    # subtract the score so a higher score (more severe) sorts earlier
    # within the same category.
    return (rank * 1000) - patient["score"]


def get_waiting_patients(patients_list):
    """Return only the patients whose status is still 'Waiting'."""
    waiting = []
    for patient in patients_list:
        if patient["status"] == "Waiting":
            waiting.append(patient)
    return waiting


def sort_patients_by_priority(patients_list):
    """
    Returns a NEW list of waiting patients sorted from most urgent to
    least urgent, using a simple (stable) bubble sort.
    """
    waiting = get_waiting_patients(patients_list)

    n = len(waiting)
    for i in range(n):
        for j in range(0, n - i - 1):
            current_priority = get_priority_number(waiting[j])
            next_priority = get_priority_number(waiting[j + 1])
            if current_priority > next_priority:
                # Swap them so the more urgent patient moves earlier.
                waiting[j], waiting[j + 1] = waiting[j + 1], waiting[j]

    return waiting


def get_next_patient(patients_list):
    """Return the single most urgent waiting patient, or None if empty."""
    sorted_queue = sort_patients_by_priority(patients_list)
    if len(sorted_queue) == 0:
        return None
    return sorted_queue[0]


def print_queue(patients_list):
    sorted_queue = sort_patients_by_priority(patients_list)

    if len(sorted_queue) == 0:
        print("\nThe waiting queue is empty.")
        return

    print("\n--- Current Priority Queue ---")
    print(f"{'#':<3}{'ID':<5}{'Name':<20}{'Age':<5}{'Category':<14}{'Score':<7}{'Arrival Time':<20}")
    position = 1
    for patient in sorted_queue:
        print(f"{position:<3}{patient['patient_id']:<5}{patient['name']:<20}"
              f"{patient['age']:<5}{patient['category']:<14}{patient['score']:<7}"
              f"{patient['arrival_time']:<20}")
        position = position + 1

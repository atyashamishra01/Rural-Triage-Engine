"""
test_queue_functions.py

Simple tests for the priority queue sorting logic, using plain `assert`
statements. Run directly with:

    python tests/test_queue_functions.py
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import queue_functions as queue


def make_patient(patient_id, category, score, status="Waiting"):
    return {
        "patient_id": patient_id,
        "name": f"Patient{patient_id}",
        "age": 30,
        "category": category,
        "score": score,
        "status": status,
        "arrival_time": "2026-01-01 00:00:00",
    }


def test_critical_comes_before_non_urgent():
    patients = [
        make_patient(1, "Non-Urgent", 0),
        make_patient(2, "Critical", 9),
    ]
    sorted_queue = queue.sort_patients_by_priority(patients)
    assert sorted_queue[0]["patient_id"] == 2
    assert sorted_queue[1]["patient_id"] == 1


def test_arrival_order_kept_for_ties():
    patients = [
        make_patient(1, "Urgent", 5),
        make_patient(2, "Urgent", 5),
    ]
    sorted_queue = queue.sort_patients_by_priority(patients)
    assert sorted_queue[0]["patient_id"] == 1
    assert sorted_queue[1]["patient_id"] == 2


def test_higher_score_wins_in_same_category():
    patients = [
        make_patient(1, "Semi-Urgent", 3),
        make_patient(2, "Semi-Urgent", 4),
    ]
    sorted_queue = queue.sort_patients_by_priority(patients)
    assert sorted_queue[0]["patient_id"] == 2


def test_treated_patients_are_excluded():
    patients = [
        make_patient(1, "Critical", 9, status="Treated"),
        make_patient(2, "Urgent", 5, status="Waiting"),
    ]
    sorted_queue = queue.sort_patients_by_priority(patients)
    assert len(sorted_queue) == 1
    assert sorted_queue[0]["patient_id"] == 2


def test_empty_queue_returns_none():
    assert queue.get_next_patient([]) is None


def run_all_tests():
    test_critical_comes_before_non_urgent()
    print("PASSED: test_critical_comes_before_non_urgent")

    test_arrival_order_kept_for_ties()
    print("PASSED: test_arrival_order_kept_for_ties")

    test_higher_score_wins_in_same_category()
    print("PASSED: test_higher_score_wins_in_same_category")

    test_treated_patients_are_excluded()
    print("PASSED: test_treated_patients_are_excluded")

    test_empty_queue_returns_none()
    print("PASSED: test_empty_queue_returns_none")

    print("\nALL TESTS PASSED")


if __name__ == "__main__":
    run_all_tests()

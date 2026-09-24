"""
test_triage_functions.py

Simple tests using plain `assert` statements instead of a testing
framework class. Run this file directly:

    python tests/test_triage_functions.py

If every assert passes, you will see "ALL TESTS PASSED".
"""

import sys
import os

# Allow this test file (inside tests/) to import modules from the project root.
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import triage_functions as triage


def test_normal_vitals_are_non_urgent():
    score = triage.calculate_triage_score(
        temperature=37.0, systolic_bp=120, heart_rate=75,
        respiratory_rate=16, spo2=98, consciousness="Alert", age=30
    )
    category = triage.get_triage_category(
        score, symptoms=[], temperature=37.0, systolic_bp=120,
        heart_rate=75, respiratory_rate=16, spo2=98, consciousness="Alert"
    )
    assert score == 0
    assert category == triage.NON_URGENT


def test_low_spo2_is_critical():
    score = triage.calculate_triage_score(
        temperature=37.0, systolic_bp=120, heart_rate=75,
        respiratory_rate=16, spo2=88, consciousness="Alert", age=30
    )
    category = triage.get_triage_category(
        score, symptoms=[], temperature=37.0, systolic_bp=120,
        heart_rate=75, respiratory_rate=16, spo2=88, consciousness="Alert"
    )
    assert category == triage.CRITICAL


def test_unconscious_patient_is_critical():
    score = triage.calculate_triage_score(
        temperature=37.0, systolic_bp=120, heart_rate=75,
        respiratory_rate=16, spo2=98, consciousness="Unresponsive", age=30
    )
    category = triage.get_triage_category(
        score, symptoms=[], temperature=37.0, systolic_bp=120,
        heart_rate=75, respiratory_rate=16, spo2=98, consciousness="Unresponsive"
    )
    assert category == triage.CRITICAL


def test_red_flag_symptom_forces_critical():
    score = triage.calculate_triage_score(
        temperature=37.0, systolic_bp=120, heart_rate=75,
        respiratory_rate=16, spo2=98, consciousness="Alert", age=30
    )
    category = triage.get_triage_category(
        score, symptoms=["severe bleeding"], temperature=37.0, systolic_bp=120,
        heart_rate=75, respiratory_rate=16, spo2=98, consciousness="Alert"
    )
    assert category == triage.CRITICAL


def test_elderly_patient_gets_extra_point():
    young_score = triage.calculate_triage_score(
        temperature=37.0, systolic_bp=120, heart_rate=75,
        respiratory_rate=16, spo2=98, consciousness="Alert", age=30
    )
    old_score = triage.calculate_triage_score(
        temperature=37.0, systolic_bp=120, heart_rate=75,
        respiratory_rate=16, spo2=98, consciousness="Alert", age=80
    )
    assert old_score == young_score + 1


def test_mild_tachycardia_is_semi_urgent():
    score = triage.calculate_triage_score(
        temperature=37.0, systolic_bp=120, heart_rate=115,
        respiratory_rate=22, spo2=98, consciousness="Alert", age=30
    )
    category = triage.get_triage_category(
        score, symptoms=[], temperature=37.0, systolic_bp=120,
        heart_rate=115, respiratory_rate=22, spo2=98, consciousness="Alert"
    )
    assert score == 4
    assert category == triage.SEMI_URGENT


def run_all_tests():
    test_normal_vitals_are_non_urgent()
    print("PASSED: test_normal_vitals_are_non_urgent")

    test_low_spo2_is_critical()
    print("PASSED: test_low_spo2_is_critical")

    test_unconscious_patient_is_critical()
    print("PASSED: test_unconscious_patient_is_critical")

    test_red_flag_symptom_forces_critical()
    print("PASSED: test_red_flag_symptom_forces_critical")

    test_elderly_patient_gets_extra_point()
    print("PASSED: test_elderly_patient_gets_extra_point")

    test_mild_tachycardia_is_semi_urgent()
    print("PASSED: test_mild_tachycardia_is_semi_urgent")

    print("\nALL TESTS PASSED")


if __name__ == "__main__":
    run_all_tests()

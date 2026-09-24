"""
test_validation_functions.py

Tests the pure "checker" functions inside validation_functions.py (the
ones that don't call input(), so they can be tested automatically).

Run directly with:
    python tests/test_validation_functions.py
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import validation_functions as validators


def test_valid_name():
    assert validators.is_valid_name("Asha Devi") is True


def test_empty_name_is_invalid():
    assert validators.is_valid_name("   ") is False


def test_valid_age():
    assert validators.is_valid_age(45) is True


def test_negative_age_is_invalid():
    assert validators.is_valid_age(-1) is False


def test_age_over_limit_is_invalid():
    assert validators.is_valid_age(150) is False


def test_valid_contact_format():
    assert validators.is_valid_contact_format("+91 98765-43210") is True


def test_blank_contact_is_allowed():
    assert validators.is_valid_contact_format("") is True


def test_contact_with_letters_is_invalid():
    assert validators.is_valid_contact_format("call-me-maybe!") is False


def test_number_in_range():
    assert validators.is_valid_number_in_range(37.5, 25.0, 45.0) is True


def test_number_out_of_range():
    assert validators.is_valid_number_in_range(150, 0, 100) is False


def run_all_tests():
    test_valid_name()
    print("PASSED: test_valid_name")

    test_empty_name_is_invalid()
    print("PASSED: test_empty_name_is_invalid")

    test_valid_age()
    print("PASSED: test_valid_age")

    test_negative_age_is_invalid()
    print("PASSED: test_negative_age_is_invalid")

    test_age_over_limit_is_invalid()
    print("PASSED: test_age_over_limit_is_invalid")

    test_valid_contact_format()
    print("PASSED: test_valid_contact_format")

    test_blank_contact_is_allowed()
    print("PASSED: test_blank_contact_is_allowed")

    test_contact_with_letters_is_invalid()
    print("PASSED: test_contact_with_letters_is_invalid")

    test_number_in_range()
    print("PASSED: test_number_in_range")

    test_number_out_of_range()
    print("PASSED: test_number_out_of_range")

    print("\nALL TESTS PASSED")


if __name__ == "__main__":
    run_all_tests()

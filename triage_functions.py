"""
triage_functions.py

Contains the rule-based triage scoring logic. This is loosely inspired by
the NEWS2 (National Early Warning Score) system used in real hospitals,
simplified for a beginner-level, offline rural clinic tool.

Each vital sign gets a small score (0 to 3) based on simple if/elif
ranges. The scores are added up to get a total triage score, which is
then turned into an easy-to-understand category.
"""

CRITICAL = "Critical"
URGENT = "Urgent"
SEMI_URGENT = "Semi-Urgent"
NON_URGENT = "Non-Urgent"

RED_FLAG_SYMPTOMS = [
    "severe bleeding",
    "unconscious",
    "seizure",
    "chest pain",
    "difficulty breathing",
    "stroke symptoms",
    "severe burns",
]

COMMON_SYMPTOMS = [
    "fever", "cough", "diarrhea", "vomiting", "headache",
    "abdominal pain", "body ache", "rash", "dizziness", "minor injury",
    "severe bleeding", "unconscious", "seizure", "chest pain",
    "difficulty breathing", "stroke symptoms", "severe burns",
]


def score_respiratory_rate(rr):
    if rr <= 8 or rr >= 25:
        return 3
    elif rr >= 21:
        return 2
    elif rr <= 11:
        return 1
    else:
        return 0


def score_spo2(spo2):
    if spo2 <= 91:
        return 3
    elif spo2 <= 93:
        return 2
    elif spo2 <= 95:
        return 1
    else:
        return 0


def score_systolic_bp(bp):
    if bp <= 90 or bp >= 220:
        return 3
    elif bp <= 100:
        return 2
    elif bp <= 110:
        return 1
    else:
        return 0


def score_heart_rate(hr):
    if hr <= 40 or hr >= 131:
        return 3
    elif hr >= 111:
        return 2
    elif hr <= 50 or hr >= 91:
        return 1
    else:
        return 0


def score_temperature(temp):
    if temp <= 35.0:
        return 3
    elif temp >= 39.1:
        return 2
    elif temp <= 36.0 or temp >= 38.1:
        return 1
    else:
        return 0


def score_consciousness(level):
    if level == "Alert":
        return 0
    else:
        return 3


def score_age(age):
    if age <= 1 or age >= 75:
        return 1
    else:
        return 0


def calculate_triage_score(temperature, systolic_bp, heart_rate,
                            respiratory_rate, spo2, consciousness, age):
    """Add up all the individual vital-sign scores into one total score."""
    total = 0
    total = total + score_respiratory_rate(respiratory_rate)
    total = total + score_spo2(spo2)
    total = total + score_systolic_bp(systolic_bp)
    total = total + score_heart_rate(heart_rate)
    total = total + score_temperature(temperature)
    total = total + score_consciousness(consciousness)
    total = total + score_age(age)
    return total


def has_red_flag_symptom(symptoms):
    """Check whether any reported symptom is a medical emergency red flag."""
    for symptom in symptoms:
        if symptom.lower() in RED_FLAG_SYMPTOMS:
            return True
    return False


def has_any_critical_vital(temperature, systolic_bp, heart_rate, respiratory_rate,
                            spo2, consciousness):
    """True if any single vital sign scored the maximum severity (3)."""
    if score_respiratory_rate(respiratory_rate) == 3:
        return True
    if score_spo2(spo2) == 3:
        return True
    if score_systolic_bp(systolic_bp) == 3:
        return True
    if score_heart_rate(heart_rate) == 3:
        return True
    if score_temperature(temperature) == 3:
        return True
    if score_consciousness(consciousness) == 3:
        return True
    return False


def get_triage_category(score, symptoms, temperature, systolic_bp,
                         heart_rate, respiratory_rate, spo2, consciousness):
    """Turn a numeric score (plus red-flag checks) into a category label."""
    if has_red_flag_symptom(symptoms):
        return CRITICAL
    if has_any_critical_vital(temperature, systolic_bp, heart_rate, respiratory_rate,
                               spo2, consciousness):
        return CRITICAL
    if score >= 7:
        return CRITICAL
    elif score >= 5:
        return URGENT
    elif score >= 3:
        return SEMI_URGENT
    else:
        return NON_URGENT

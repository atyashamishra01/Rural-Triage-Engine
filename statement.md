# Problem Statement

Rural healthcare facilities and primary health centers (PHCs) routinely experience severe
overcrowding during medical camps or routine clinic hours, while lacking specialist staff and
reliable internet connectivity. Because non-specialized nursing or community health workers
lack objective, automated decision-support tools, determining patient priority is often
subjective and inconsistent. This can create dangerous delays in identifying critical medical
emergencies (such as hypertensive crises, hypoxia, or severe tachycardia). Existing Electronic
Health Record (EHR) software typically relies on continuous internet access and cloud
databases, making it unusable in remote or connectivity-poor setups.

A lightweight, fully offline, rule-based clinical prioritization tool is required so that
front-line staff can quickly and objectively rank incoming patients by urgency, ensuring the
sickest patients are seen first regardless of arrival order or subjective judgment.

## Scope of the Project

- A simple, offline console (command-line) application, runnable on a single laptop carried to
  a rural medical camp.
- Covers patient registration, vital-sign-based triage scoring, a priority-ordered waiting
  queue, and basic clinic analytics.
- Does not cover: cloud sync, multiple connected devices, full EHR functionality, prescriptions,
  or billing.
- All data is stored locally in a plain JSON file; no patient data ever leaves the device.

## Target Users

- Community health workers and triage staff at rural PHCs or medical camps who need a simple,
  no-training-required tool.
- Visiting medical officers who want an at-a-glance, objective list of which patient to see
  next.
- Camp coordinators who need quick end-of-day numbers on patient load and severity mix.

## High-Level Features

1. **Patient Registration** — a guided, validated set of console prompts collects demographics,
   vital signs, and symptoms.
2. **Rule-Based Triage Scoring** — a simple, NEWS2-inspired scoring system built from `if`/`elif`
   checks computes an objective urgency score, with red-flag symptom overrides for emergencies
   not fully captured by vitals alone (e.g. severe bleeding, seizures).
3. **Priority Queue** — the waiting list is always shown sorted from most to least urgent, using
   a simple, easy-to-follow bubble sort.
4. **Offline JSON Storage** — all patient records are saved to a local `data/patients.json`
   file and reloaded automatically the next time the program starts.
5. **Analytics** — a menu option shows total patients seen, how many are still waiting, and a
   simple text bar chart of patients per triage category.

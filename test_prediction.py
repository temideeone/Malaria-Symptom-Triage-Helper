from src.predict import malaria_triage

sample_patient = {
    "age": 15,
    "sex": "F",
    "pregnant": False,
    "location": "Sub-Saharan Africa - Rural",
    "travel_history_endemic_area": True,
    "bed_net_use": False,
    "irs_spraying": True,
    "previous_malaria_episodes": 3,
    "fever": True,
    "chills_rigors": True,
    "headache": True,
    "night_sweats": True,
    "fatigue_malaise": True,
    "nausea_vomiting": False,
    "diarrhea": False,
    "cough": False,
    "abdominal_pain": False,
    "jaundice": False,
    "altered_consciousness": False,
    "seizures": False,
    "hemoglobin_g_dl": 10.6,
    "platelets_x10e9_l": 132,
    "wbc_x10e9_l": 5.0,
    "glucose_mg_dl": 106,
    "creatinine_mg_dl": 0.34,
    "bilirubin_mg_dl": 1.5,
    "lactate_mmol_l": 1.8
}

result = malaria_triage(sample_patient)

print(result)
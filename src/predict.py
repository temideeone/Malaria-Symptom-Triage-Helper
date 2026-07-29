import joblib
import pandas as pd

diagnosis_model = joblib.load(
    "models/malaria_diagnosis_rf.pkl"
)

severity_model = joblib.load(
    "models/malaria_severity_rf.pkl"
)

diagnosis_map = {

    0: "Malaria",
    1: "No Malaria"

}

severity_map = {

    0: "Moderate",
    1: "Severe",
    2: "Uncomplicated"

}

# predict_diagnosis function
def predict_diagnosis(patient_data):

    patient_df = pd.DataFrame(
        [patient_data]
    )

    prediction = diagnosis_model.predict(
        patient_df
    )[0]

    probability = diagnosis_model.predict_proba(
        patient_df
    )[0].max()

    return prediction, probability

# predict_severity function
def predict_severity(patient_data):

    patient_df = pd.DataFrame(
        [patient_data]
    )

    prediction = severity_model.predict(
        patient_df
    )[0]

    probability = severity_model.predict_proba(
        patient_df
    )[0].max()

    return prediction, probability


# triage function
def malaria_triage(patient_data):

    diagnosis_pred, diagnosis_prob = (
        predict_diagnosis(patient_data)
    )

    diagnosis_label = diagnosis_map[
        diagnosis_pred
    ]

    if diagnosis_label == "No Malaria":

        return {
            "Diagnosis": diagnosis_label,
            "Confidence": float(
                round(
              diagnosis_prob * 100,
            2
      )
    ), 
            "Severity": "N/A",
            "Recommendation":
                "Monitor symptoms and consult a healthcare provider if symptoms persist."
        }

    severity_pred, severity_prob = (
        predict_severity(patient_data)
    )

    severity_label = severity_map[
        severity_pred
    ]

    if severity_label == "Severe":

        recommendation = (
            "Immediate hospital admission required."
        )

    elif severity_label == "Moderate":

        recommendation = (
            "Seek medical attention within 24 hours."
        )

    else:

        recommendation = (
            "Outpatient treatment and monitoring recommended."
        )

    return {
        "Diagnosis": diagnosis_label,
        "Confidence":float( round(
            diagnosis_prob * 100,
            2
        )),
        "Severity": severity_label,
        "Recommendation": recommendation
    }
import streamlit as st
from src.predict import malaria_triage

st.title("🩺 Patient Triage")

st.write(
    "Enter patient information below to predict malaria diagnosis and severity."
)

st.header("Patient Information")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=0,
        max_value=120,
        value=25
    )

    sex = st.selectbox(
        "Sex",
        ["M", "F"]
    )

with col2:

    pregnant = st.checkbox(
        "Pregnant"
    )

    location = st.selectbox(
        "Location",
        [
            "Sub-Saharan Africa - Rural",
            "Sub-Saharan Africa - Urban",
            "Southeast Asia - Rural",
            "Southeast Asia - Urban",
            "Latin America - Urban",
            "Papua New Guinea"
        ]
    )


    st.header("Symptoms")

col1, col2 = st.columns(2)

with col1:

    fever = st.checkbox("Fever")
    chills_rigors = st.checkbox("Chills / Rigors")
    headache = st.checkbox("Headache")
    night_sweats = st.checkbox("Night Sweats")
    fatigue_malaise = st.checkbox("Fatigue / Malaise")
    nausea_vomiting = st.checkbox("Nausea / Vomiting")

with col2:

    diarrhea = st.checkbox("Diarrhea")
    cough = st.checkbox("Cough")
    abdominal_pain = st.checkbox("Abdominal Pain")
    jaundice = st.checkbox("Jaundice")
    altered_consciousness = st.checkbox("Altered Consciousness")
    seizures = st.checkbox("Seizures")



st.header("Clinical Measurements")

col1, col2 = st.columns(2)

with col1:

    hemoglobin_g_dl = st.number_input(
        "Hemoglobin (g/dL)",
        value=13.5
    )

    platelets_x10e9_l = st.number_input(
        "Platelets",
        value=250
    )

    wbc_x10e9_l = st.number_input(
        "WBC",
        value=6.5
    )

    glucose_mg_dl = st.number_input(
        "Glucose",
        value=90
    )

with col2:

    creatinine_mg_dl = st.number_input(
        "Creatinine",
        value=0.8
    )

    bilirubin_mg_dl = st.number_input(
        "Bilirubin",
        value=0.7
    )

    lactate_mmol_l = st.number_input(
        "Lactate",
        value=1.5
    )


st.header("Risk Factors")

travel_history_endemic_area = st.checkbox(
    "Travel History to Endemic Area"
)

bed_net_use = st.checkbox(
    "Uses Bed Net"
)

irs_spraying = st.checkbox(
    "Indoor Residual Spraying"
)

previous_malaria_episodes = st.number_input(
    "Previous Malaria Episodes",
    min_value=0,
    value=0
)


if st.button("Predict"):

    patient_data = {
        "age": age,
        "sex": sex,
        "pregnant": pregnant,
        "location": location,
        "travel_history_endemic_area": travel_history_endemic_area,
        "bed_net_use": bed_net_use,
        "irs_spraying": irs_spraying,
        "previous_malaria_episodes": previous_malaria_episodes,
        "fever": fever,
        "chills_rigors": chills_rigors,
        "headache": headache,
        "night_sweats": night_sweats,
        "fatigue_malaise": fatigue_malaise,
        "nausea_vomiting": nausea_vomiting,
        "diarrhea": diarrhea,
        "cough": cough,
        "abdominal_pain": abdominal_pain,
        "jaundice": jaundice,
        "altered_consciousness": altered_consciousness,
        "seizures": seizures,
        "hemoglobin_g_dl": hemoglobin_g_dl,
        "platelets_x10e9_l": platelets_x10e9_l,
        "wbc_x10e9_l": wbc_x10e9_l,
        "glucose_mg_dl": glucose_mg_dl,
        "creatinine_mg_dl": creatinine_mg_dl,
        "bilirubin_mg_dl": bilirubin_mg_dl,
        "lactate_mmol_l": lactate_mmol_l,
        "plasmodium_species": "Falciparum"
    }

    result = malaria_triage(patient_data)

    st.success("Prediction Complete")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Diagnosis", result["Diagnosis"])

    with col2:
        st.metric(
            "Confidence",
            f"{result['Confidence']}%"
        )

    with col3:
        st.metric(
            "Severity",
            result["Severity"]
        )

    st.info(result["Recommendation"])
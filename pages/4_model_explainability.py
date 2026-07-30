import streamlit as st
import pandas as pd

st.title("🔍 Model Explainability")

st.write("""
Understanding why the model makes predictions is critical
for trust and transparency in healthcare applications.
""")

st.subheader("Feature Importance")

importance_df = pd.DataFrame({

    "Feature":[
        "bilirubin_mg_dl",
        "chills_rigors",
        "fever",
        "night_sweats",
        "hemoglobin_g_dl",
        "fatigue_malaise",
        "wbc_x10e9_l",
        "platelets_x10e9_l",
        "headache",
        "nausea_vomiting"
    ],

    "Importance":[
        0.318026,
        0.161309,
        0.150203,
        0.072327,
        0.059647,
        0.055217,
        0.041542,
        0.034953,
        0.032753,
        0.009512
    ]
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

st.bar_chart(
    importance_df.set_index("Feature")
)


st.dataframe(
    importance_df,
    use_container_width=True
)

st.subheader("Interpretation")

st.info("""
The model identified bilirubin levels, chills/rigors,
fever, and night sweats as the strongest predictors
of malaria diagnosis.

This aligns with known clinical indicators of malaria,
increasing confidence in the model's predictions.
""")

st.subheader("Severity Model Insights")

severity_importance = pd.DataFrame({

    "Feature":[
        "age",
        "creatinine_mg_dl",
        "lactate_mmol_l",
        "hemoglobin_g_dl",
        "bilirubin_mg_dl",
        "glucose_mg_dl",
        "platelets_x10e9_l",
        "wbc_x10e9_l"
    ],

    "Importance":[
        0.197705,
        0.154191,
        0.153693,
        0.118993,
        0.116642,
        0.062027,
        0.027103,
        0.023461
    ]
})

st.bar_chart(
    severity_importance.set_index("Feature")
)

st.success("""
Key drivers of malaria severity include:

• Age
• Creatinine levels
• Lactate levels
• Hemoglobin
• Bilirubin

These factors are medically relevant because they
reflect organ function and disease progression.
""")

st.subheader("SHAP Explainability")

st.write("""
SHAP (SHapley Additive exPlanations) was used to
analyze how individual features contribute to
model predictions.

The SHAP analysis confirmed that bilirubin,
fever, chills/rigors, and hemoglobin are among
the most influential factors driving predictions.
""")

st.subheader("Key Takeaway")

st.warning("""
The model does not rely on a single symptom.
Instead, it combines clinical symptoms, laboratory
measurements, and patient history to make decisions.

This multi-factor approach improves robustness and
reduces the risk of relying on any one indicator.
""")
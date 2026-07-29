import streamlit as st

st.set_page_config(
    page_title="Malaria Symptom Triage Helper",
    page_icon="🦟",
    layout="wide"
)

st.title("🦟 Malaria Symptom Triage Helper")

st.markdown("""
## AI-Powered Clinical Decision Support Tool

This project uses Machine Learning to:

- Predict Malaria Diagnosis
- Assess Disease Severity
- Provide Clinical Recommendations
- Explain Model Decisions

---
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Diagnosis Accuracy",
        "99.4%"
    )

with col2:
    st.metric(
        "Severity Accuracy",
        "93%"
    )

with col3:
    st.metric(
        "Dataset Size",
        "5,000"
    )

st.header("Problem Statement")

st.write("""
Malaria remains one of the leading causes of illness and death in many regions,
particularly in Sub-Saharan Africa.

Early identification of malaria and rapid assessment of severity can improve
clinical outcomes and support healthcare professionals in decision-making.

This project applies machine learning techniques to assist in malaria triage.
""")

st.header("Project Objectives")

st.markdown("""
- Detect malaria cases
- Assess disease severity
- Recommend next clinical action
- Improve decision support
- Demonstrate explainable AI
""")
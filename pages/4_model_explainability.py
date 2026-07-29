import streamlit as st
import pandas as pd

st.title("Model Explainability")

importance = pd.DataFrame({

    "Feature":[
        "bilirubin_mg_dl",
        "chills_rigors",
        "fever",
        "night_sweats",
        "hemoglobin_g_dl"
    ],

    "Importance":[
        0.318,
        0.161,
        0.150,
        0.072,
        0.060
    ]
})

st.bar_chart(
    importance.set_index("Feature")
)

st.write("""
Most important factors influencing malaria diagnosis:

1. Bilirubin
2. Chills/Rigors
3. Fever
4. Night Sweats
5. Hemoglobin
""")
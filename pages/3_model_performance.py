import streamlit as st
import pandas as pd

st.title("Model Performance")

results = pd.DataFrame({

    "Model":[
        "Random Forest",
        "Logistic Regression",
        "Decision Tree",
        "SVM",
        "KNN"
    ],

    "Accuracy":[
        0.994,
        0.990,
        0.990,
        0.988,
        0.975
    ],

    "F1":[
        0.995696,
        0.992826,
        0.992816,
        0.991392,
        0.982282
    ]
})

st.dataframe(
    results,
    use_container_width=True
)
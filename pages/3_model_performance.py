import streamlit as st
import pandas as pd

st.title("📊 Model Performance")

st.subheader("Diagnosis Model Comparison")

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

    "Precision":[
        0.991429,
        0.988571,
        0.989971,
        0.987143,
        0.966527
    ],

    "Recall":[
        1.000000,
        0.997118,
        0.995677,
        0.995677,
        0.998559
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


st.subheader("Best Model")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Accuracy",
        "99.4%"
    )

with col2:
    st.metric(
        "F1 Score",
        "99.57%"
    )

with col3:
    st.metric(
        "ROC AUC",
        "99.94%"
    )


    st.subheader("Severity Model Performance")

st.write("""
Random Forest Multi-Class Classifier
""")

severity_results = pd.DataFrame({

    "Metric":[
        "Accuracy",
        "Weighted Precision",
        "Weighted Recall",
        "Weighted F1"
    ],

    "Score":[
        0.93,
        0.94,
        0.93,
        0.93
    ]
})

st.dataframe(
    severity_results,
    use_container_width=True
)


st.subheader("Severity Classification Report")

report = pd.DataFrame({

    "Class":[
        "Moderate",
        "Severe",
        "Uncomplicated"
    ],

    "Precision":[
        1.00,
        1.00,
        0.88
    ],

    "Recall":[
        0.83,
        1.00,
        1.00
    ],

    "F1":[
        0.91,
        1.00,
        0.94
    ]
})

st.dataframe(
    report,
    use_container_width=True
)


st.subheader("Key Findings")

st.success("""
Random Forest achieved the highest performance
for malaria diagnosis with 99.4% accuracy and
99.57% F1-score.
""")

st.info("""
The severity model achieved 93% accuracy and
successfully identified severe malaria cases
with 100% precision and recall.
""")
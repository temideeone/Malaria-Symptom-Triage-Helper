# Malaria Symptom Triage Helper

## Live Demo

🌐 Streamlit App:
https://malaria-symptom-triage-apper-jc4mgtdy2qfj5cfz3ty4pm.streamlit.app/


## Overview

The Malaria Symptom Triage Helper is a Machine Learning-powered healthcare decision support system designed to predict malaria diagnosis and assess disease severity based on patient symptoms, clinical measurements, and risk factors.

The application helps healthcare workers perform early triage and supports decision-making through predictive analytics and explainable AI techniques.

---

## Problem Statement

Malaria remains a major public health challenge, especially in Sub-Saharan Africa.

Early diagnosis and severity assessment are essential for improving patient outcomes and reducing mortality.

This project leverages Machine Learning to:

- Predict malaria diagnosis
- Assess malaria severity
- Provide triage recommendations
- Explain model decisions

---

## Dataset

Dataset Size:

- 5,000 patient records

Features:

- Demographics
- Symptoms
- Laboratory measurements
- Risk factors
- Treatment outcomes

Target Variables:

### Diagnosis

- Malaria
- No Malaria

### Severity

- Uncomplicated
- Moderate
- Severe

---

## Project Workflow

1. Data Collection
2. Exploratory Data Analysis
3. Data Preprocessing
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Hyperparameter Tuning
8. Explainable AI
9. Deployment

---

## Models Evaluated

| Model | Accuracy |
|---------|---------|
| Logistic Regression | 99.0% |
| Decision Tree | 99.0% |
| Random Forest | 99.4% |
| KNN | 97.5% |
| SVM | 98.8% |

---

## Best Model

Random Forest Classifier

Performance:

- Accuracy: 99.4%
- Precision: 99.1%
- Recall: 100%
- F1 Score: 99.57%
- ROC-AUC: 99.94%

---

## Severity Model Results

Random Forest Multi-Class Classifier

Performance:

- Accuracy: 93%
- Weighted Precision: 94%
- Weighted Recall: 93%
- Weighted F1 Score: 93%

---

## Explainable AI

Feature importance analysis identified the following major predictors:

### Diagnosis Drivers

- Bilirubin
- Fever
- Chills/Rigors
- Night Sweats
- Hemoglobin

### Severity Drivers

- Age
- Creatinine
- Lactate
- Hemoglobin
- Bilirubin

SHAP analysis was used to improve transparency and interpretability.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- SHAP
- Matplotlib
- Streamlit
- GitHub

---

## Project Structure

```
malaria-symptom-triage-helper/

├── notebooks/
├── src/
├── pages/
├── models/
├── reports/
├── tests/
├── app.py
├── requirements.txt
└── README.md
```

---

## Streamlit Application

Features:

- Patient Triage
- Diagnosis Prediction
- Severity Assessment
- Model Performance Dashboard
- Explainability Dashboard

---

## Ethical Considerations

This application is intended for educational and decision-support purposes only.

It should not replace professional medical diagnosis, treatment, or clinical judgment.

---

## Author

### Temidayo Samuel Abodunrin

AI / Machine Learning Engineer

GitHub:
https://github.com/temideeone

LinkedIn:
https://www.linkedin.com/in/temidayo-abodunrin-689143199

Email:
dayosamuel54@gmail.com

---


## Application Screenshots

### Home Page

![Home](home_page.png)

### Patient Triage

![Triage](patient_triage.png)

### Model Performance

![Performance](model_performance.png)

### Explainability

![Explainability](model_explainability.png)

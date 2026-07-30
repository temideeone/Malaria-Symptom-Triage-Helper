# MALARIA SYMPTOM TRIAGE HELPER

## A Machine Learning-Based Decision Support System for Malaria Diagnosis and Severity Assessment

### Capstone Project Report

Prepared By:

Temidayo Samuel Abodunrin

AI / Machine Learning Engineering

2026


## Abstract

Malaria remains one of the leading causes of morbidity and mortality in many developing countries, particularly in Sub-Saharan Africa. Early diagnosis and severity assessment are critical for improving patient outcomes and reducing mortality rates.

This project presents the development of a Machine Learning-based Malaria Symptom Triage Helper designed to predict malaria diagnosis and assess disease severity using patient symptoms, demographic information, clinical measurements, and risk factors.

A dataset containing 5,000 patient records was analyzed and processed through a complete machine learning pipeline including exploratory data analysis, preprocessing, feature engineering, model training, evaluation, hyperparameter tuning, and explainability analysis.

Multiple machine learning algorithms including Logistic Regression, Decision Tree, Random Forest, K-Nearest Neighbors, and Support Vector Machines were evaluated. Random Forest achieved the highest performance with an accuracy of 99.4%, F1-score of 99.57%, and ROC-AUC of 99.94% for malaria diagnosis.

A separate severity classification model achieved 93% accuracy in distinguishing uncomplicated, moderate, and severe malaria cases.

The final solution was deployed as an interactive Streamlit web application capable of providing diagnosis predictions, severity assessments, and triage recommendations.

Keywords: Malaria, Machine Learning, Healthcare Analytics, Classification, Explainable AI, Streamlit.


# Introduction

Malaria is a life-threatening disease caused by parasites transmitted through the bites of infected mosquitoes. According to global health reports, malaria continues to affect millions of individuals annually and remains a major public health challenge.

Early diagnosis and appropriate treatment are essential for preventing severe complications and reducing mortality. However, healthcare systems in many endemic regions face challenges including limited resources, shortages of trained personnel, and delayed diagnosis.

Machine Learning provides an opportunity to support healthcare professionals through predictive analytics capable of identifying disease patterns from patient data.

This project aims to develop an intelligent decision-support system capable of predicting malaria diagnosis and assessing disease severity using machine learning techniques.


# Problem Statement

Malaria diagnosis often relies on laboratory tests and clinical expertise. Delays in diagnosis or incorrect severity assessment can lead to severe complications and increased mortality.

Healthcare providers require tools that can assist in early identification of malaria cases and prioritize patients requiring urgent intervention.

This project seeks to address this challenge by developing a machine learning system capable of:

1. Predicting malaria diagnosis.
2. Assessing malaria severity.
3. Providing triage recommendations.
4. Supporting healthcare decision-making.


# Objectives

## General Objective

To develop a machine learning-based malaria triage system capable of assisting healthcare workers in diagnosis and severity assessment.

## Specific Objectives

- Analyze malaria patient data.
- Perform exploratory data analysis.
- Build and compare multiple machine learning models.
- Select the best-performing model.
- Explain model decisions using Explainable AI.
- Deploy the solution through a Streamlit application.


# Dataset Description

The dataset contains 5,000 patient records and 37 features.

The features include:

- Demographic information
- Symptoms
- Laboratory measurements
- Risk factors
- Treatment outcomes

Target variables include:

## Diagnosis

- Malaria
- No Malaria

## Severity

- Uncomplicated
- Moderate
- Severe

Dataset Distribution:

- Malaria: 1,528 (30.56%)
- No Malaria: 3,472 (69.44%)

Severity Distribution:

- Uncomplicated: 796
- Moderate: 650
- Severe: 82



# Exploratory Data Analysis

Exploratory analysis revealed several important patterns.

## Symptom Analysis

Among malaria-positive patients:

- Fever: 91.10%
- Fatigue/Malaise: 84.69%
- Chills/Rigors: 78.60%
- Headache: 68.65%
- Night Sweats: 65.97%

These symptoms appeared significantly more frequently among malaria cases than non-malaria cases.

## Laboratory Findings

Patients diagnosed with malaria exhibited:

- Lower hemoglobin levels
- Lower platelet counts
- Higher bilirubin levels
- Higher parasitemia levels

These findings align with known clinical characteristics of malaria.



# Machine Learning Methodology

The machine was trained using some machine learning methods to prevent data leakage and obtain best result and here are the series of method used after cleaning the data and ensured no duplicated data was enterd.


Preprocessing
Encoding
Train/Test Split
Feature Engineering
Model Training
Hyperparameter Tuning



#  Model Results

we used five diffrent models to train in other to compare and select the model with best performance knowing that we are dealing with clinical issue where by any little error can be fatal so here are the result from the five trained models:

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|---------|---------|---------|---------|---------|---------|
| Random Forest | 0.994 | 0.991429 | 1.000000 | 0.995696 | 0.999423 |
| Logistic Regression | 0.990 | 0.988571 | 0.997118 | 0.992826 | 0.998262 |
| Decision Tree | 0.990 | 0.989971 | 0.995677 | 0.992816 | 0.986401 |
| SVM | 0.988 | 0.987143 | 0.995677 | 0.991392 | 0.998022 |
| KNN | 0.975 | 0.966527 | 0.998559 | 0.982282 | 0.989996 |


**Best Performing Model:** Random Forest

- Accuracy: 99.4%
- Precision: 99.14%
- Recall: 100%
- F1 Score: 99.57%
- ROC-AUC: 99.94%

The Random Forest classifier achieved the highest overall performance across all evaluation metrics and was therefore selected as the final diagnosis model.


# Explainability

To improve transparency and trust in the machine learning system, feature importance analysis and SHAP (SHapley Additive exPlanations) techniques were used to identify the factors that most influenced model predictions.

### Diagnosis Drivers

The diagnosis model identified the following features as the strongest predictors of malaria:

**Bilirubin** – Elevated bilirubin levels were strongly associated with malaria infection and were the most important predictor.

**Chills/Rigors** – Patients experiencing chills and rigors were significantly more likely to have malaria.

**Fever** – Fever is one of the most common symptoms of malaria and played a major role in prediction.

**Night Sweats** – Frequent among malaria-positive patients and contributed significantly to classification.

**Hemoglobin** – Lower hemoglobin levels were associated with malaria due to the destruction of red blood cells by the parasite.

These findings are consistent with known clinical characteristics of malaria, increasing confidence in the model's predictions.

### Severity Drivers

The severity model identified the following features as the most influential in determining whether a malaria case was uncomplicated, moderate, or severe:

**Age** – Younger and older patients were more likely to experience severe outcomes.

**Creatinine** – Elevated creatinine levels may indicate kidney dysfunction, a potential complication of severe malaria.

**Lactate** – High lactate levels can indicate poor oxygen delivery and severe disease progression.

**Hemoglobin** – Low hemoglobin levels suggest anemia, which is commonly associated with severe malaria.

**Bilirubin** – Increased bilirubin levels may indicate liver involvement and worsening disease severity.

The explainability analysis demonstrates that the model relies on clinically meaningful factors rather than random patterns, making the predictions more interpretable and trustworthy.



# Deployment


The final machine learning solution was deployed as an interactive web application using Streamlit and managed through GitHub.

### **Streamlit**

Streamlit was used to develop a user-friendly web interface that allows healthcare workers and users to interact with the machine learning models without requiring programming knowledge. The application provides real-time predictions and displays diagnosis results, severity assessments, confidence scores, and recommendations.

### **GitHub**

GitHub was used for version control, project management, and code storage. All project files, notebooks, source code, trained models, and documentation were maintained in a centralized repository to ensure reproducibility and collaboration.

### **Interactive Triage Interface**

The application includes an interactive patient triage page where users can enter:

-Demographic information
-Malaria symptoms
-Clinical measurements
-Risk factors

After submitting the information, the system analyzes the data and generates predictions instantly.

### **Prediction Workflow**

The prediction workflow follows these steps:

-The user enters patient information through the Streamlit interface.
-The data is passed to the trained Random Forest diagnosis model.
-The diagnosis model predicts whether the patient has malaria.
-If malaria is detected, the severity model is executed.
-The severity model classifies the case as Uncomplicated, Moderate, or Severe.
-The system generates a recommendation based on the predicted severity level.
-The results are displayed to the user through the Streamlit dashboard.

This deployment demonstrates how machine learning can be integrated into a practical healthcare decision-support application capable of assisting with malaria screening and triage.


# Conclusion

This project successfully developed a machine learning-based malaria triage system capable of predicting malaria diagnosis and assessing disease severity.

Random Forest achieved outstanding performance with 99.4% diagnostic accuracy while the severity model achieved 93% accuracy.

The final application demonstrates the potential of machine learning to support healthcare decision-making and improve patient triage processes.


# Recommendations

Future improvements may include:

- Integration with real hospital data.
- Real-time patient monitoring.
- Deep learning approaches.
- Mobile application deployment.
- Electronic Health Record integration.
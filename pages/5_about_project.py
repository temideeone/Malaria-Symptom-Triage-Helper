import streamlit as st

st.title("About Project")

st.header("Dataset")

st.write("""
Records: 5,000

Features: 37

Target:
- Malaria
- No Malaria
""")

st.header("Methodology")

st.markdown("""
1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Explainability
8. Deployment
""")

st.header("Technology Stack")

st.markdown("""
- Python
- Pandas
- NumPy
- Scikit-Learn
- SHAP
- Streamlit
- GitHub
""")
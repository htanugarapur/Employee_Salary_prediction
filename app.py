import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("best_salarymodel.pkl")

# Encoding maps (used during training)
education_map = {
    "10th": 6, "11th": 7, "12th": 8, "HS-grad": 9, "Some-college": 10,
    "Assoc-voc": 11, "Assoc-acdm": 12, "Bachelors": 13,
    "Masters": 14, "Prof-school": 15, "Doctorate": 16
}

occupation_map = {
    "Tech-support": 0, "Craft-repair": 1, "Other-service": 2, "Sales": 3,
    "Exec-managerial": 4, "Prof-specialty": 5, "Handlers-cleaners": 6,
    "Machine-op-inspct": 7, "Adm-clerical": 8, "Farming-fishing": 9,
    "Transport-moving": 10, "Priv-house-serv": 11, "Protective-serv": 12,
    "Armed-Forces": 13
}

workclass_map = {
    "Private": 0, "Self-emp-not-inc": 1, "Self-emp-inc": 2, "Federal-gov": 3,
    "Local-gov": 4, "State-gov": 5
}

marital_map = {
    "Never-married": 0, "Married-civ-spouse": 1, "Divorced": 2,
    "Married-spouse-absent": 3, "Separated": 4, "Widowed": 5, "Married-AF-spouse": 6
}

relationship_map = {
    "Wife": 0, "Own-child": 1, "Husband": 2, "Not-in-family": 3,
    "Other-relative": 4, "Unmarried": 5
}

race_map = {
    "White": 0, "Asian-Pac-Islander": 1, "Amer-Indian-Eskimo": 2,
    "Other": 3, "Black": 4
}

gender_map = {"Male": 0, "Female": 1}

native_country_map = {
    "United-States": 0, "Mexico": 1, "Philippines": 2, "Germany": 3,
    "Canada": 4, "India": 5, "England": 6, "Cuba": 7, "China": 8, "South": 9
}

# Streamlit UI
st.title("Employee Salary Prediction App")

age = st.slider("Age", 18, 90, 30)
workclass_str = st.selectbox("Workclass", list(workclass_map.keys()))
marital_str = st.selectbox("Marital Status", list(marital_map.keys()))
occupation_str = st.selectbox("Occupation", list(occupation_map.keys()))
relationship_str = st.selectbox("Relationship", list(relationship_map.keys()))
race_str = st.selectbox("Race", list(race_map.keys()))
gender_str = st.selectbox("Gender", list(gender_map.keys()))
hours_per_week = st.slider("Hours per Week", 1, 100, 40)
native_country_str = st.selectbox("Native Country", list(native_country_map.keys()))
education_str = st.selectbox("Education", list(education_map.keys()))

# Encode selected strings to integers
workclass = workclass_map[workclass_str]
marital_status = marital_map[marital_str]
occupation = occupation_map[occupation_str]
relationship = relationship_map[relationship_str]
race = race_map[race_str]
gender = gender_map[gender_str]
native_country = native_country_map[native_country_str]
education = education_map[education_str]

# Prepare input DataFrame
input_df = pd.DataFrame([[
    age, workclass, marital_status, occupation,
    relationship, race, gender, hours_per_week,
    native_country, education
]], columns=[
    "age", "workclass", "marital-status", "occupation",
    "relationship", "race", "gender", "hours-per-week",
    "native-country", "education"
])

# Predict
if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Income Class: {prediction}")
# python -m streamlit run app.py
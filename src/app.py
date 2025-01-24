import streamlit as st
from pickle import load

with open("best_model.pkl", "rb") as f:
    model = load(f)

st.title("Medical Insurance Cost - Linear Regression")

age = st.slider("Age", min_value = 0.0, max_value = 99.0, step = 1.0)
sex = st.selectbox("Sex", options=["Female", "Male"])
sex = 1 if sex == "Male" else 0
bmi = st.slider("BMI", min_value=15.0, max_value=50.0, step=0.1)
children = st.slider("How many childrens", min_value = 1.0, max_value = 5.0, step = 1.0)
smoker = st.selectbox("Smoker", options=["No", "Yes"])
smoker = 1 if smoker == "No" else 0
region = st.selectbox("Region", options=["southwest", "southeast", "northwest", "northeast"])
region = ["southwest", "southeast", "northwest", "northeast"].index(region)


if st.button("Predict"):
    data = [[age, sex, bmi, children, smoker, region]]
    data_a_predecir = [[age, sex, bmi, children, smoker, region]]
    prediction = model.predict(data_a_predecir)[0]
    st.write("Prediction", prediction)
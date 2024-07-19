import streamlit as st
from src.pipeline.prediction_pipeline import Features, Prediction

country_list = ['France', 'Spain', 'Germany']
gender_list = ["Male", "Female"]
hascrcard_list = ["yes", "no"]
isactivemember_list = ["yes", "no"]

st.header("Churn Prediction")

creditscore = st.number_input("please enter credit score", value=0)
age = st.number_input("please enter age", value=0, max_value=100)
tenure = st.number_input("please enter tenure", value=0)
balance = st.number_input("please enter balance", value=0)
estimatedsalary = st.number_input("please enter salary", value=0)


hascrcard = st.selectbox("does user has credit card", hascrcard_list)
country = st.selectbox("please select country", country_list)
gender = st.selectbox("please select gender", gender_list)
isactivemember = st.selectbox("please select member activity", isactivemember_list)
ok = st.button("predict")

if ok:

    f = Features(creditscore, country, gender, age,tenure, balance, hascrcard,isactivemember, estimatedsalary)
    data = f.to_dataframe()
    p = Prediction()
    output = p.initiate_prediction(data)
    if output == 0:
        st.write("exits")
    else:
        st.write("stay")

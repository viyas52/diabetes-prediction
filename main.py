import streamlit as st
import pickle
import numpy as np

import xgboost as xgb
model = pickle.load(open('C:/Users/karth/Desktop/New folder/datathon/diap.sav', 'rb'))
st.set_page_config(page_title="my predict", page_icon=":tada: ", layout="wide")
st.subheader("Hi :wave:")
st.title("A diabetes predictor program")
st.write("Input the values to determine")

Gender = ['Female',  'Male',  'Other']
SH = ['never', 'No Info', 'current', 'former', 'ever', 'not current']
HT = ['Yes', 'No']
HD = ['Yes', 'No']

col1, col2, col3 = st.columns (3)
with col1:
    gender = st.selectbox('Enter your Gender', Gender)
    if gender == "Female":
        gen = 0
    elif gender == 'Male':
        gen = 1
    else:
        gen = 2
with col2:
    heart_disease = st.selectbox('If you have heart disease', HD)
    if heart_disease == "Yes":
        heart = 1
    else:
        heart = 0
with col3:
    HbA1c_level = st.text_input( 'Enter your hemoglobin level')
with col1:
    age = st.text_input( 'Enter your Age')
with col2:
    smoking_history = st.selectbox('Your Smoking history', SH)
    if smoking_history == "never":
        smoke = 4
    elif smoking_history == 'No Info':
        smoke = 0
    elif smoking_history == 'current':
        smoke = 1
    elif smoking_history == 'former':
        smoke = 3
    elif smoking_history == 'ever':
        smoke = 2
    else:
        smoke = 5
with col3:
    blood_glucose_level = st.text_input("Enter your glucose level")
with col1:
    hypertension = st.selectbox('If you have hypertension', HT)
    if hypertension == "Yes":
        hyper = 1
    else:
        hyper = 0
with col2:
    bmi = st.text_input('Enter your BMI')


#code for Prediction
result =''
# creating a button for Prediction
if st.button('Diabetes Test Result'):
    feat_list = np.array([[gen, age, hyper, heart, smoke, bmi, HbA1c_level, blood_glucose_level]], dtype=object)
    ans = model.predict(feat_list)
    if (ans[0]==1):
        result = "The person is Diabetic"
    else:
        result = "The person is Not Diabetic"
st.success(result)
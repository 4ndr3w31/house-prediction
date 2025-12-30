import streamlit as st
import joblib 
import numpy as np

model = joblib.load("model.pkl")

st.title("House Price Prediction")

st.divider()

st.write("This app uses machine learning for predict house price.")

st.divider()

bedrooms = st.number_input("Number of Bedrooms", min_value = 0, max_value = 100, value = 0)
bathrooms = st.number_input("Number of Bathrooms", min_value = 0, max_value = 100, value = 0)
livingarea = st.number_input("Living Area",min_value = 0, value = 2000)
condition = st.number_input("Condition", min_value = 0, value = 31)
numberofschools = st.number_input("Number of school nearby",min_value = 0, value =0)
distancefromairport = st.number_input("Distance from the airport",min_value=0, value = 0)

st.divider()

X = [[bedrooms,bathrooms,livingarea,condition,numberofschools,distancefromairport]]

predictbutton = st.button("Predict")

if predictbutton:

    X_array = np.array(X)

    prediction = model.predict(X_array)

    formatted_price = f"{prediction[0]:,.2f}"

    st.markdown(f"### 🏡 Predicted Price: **₹ {formatted_price}**")


else:
    st.write("Please click the predict button")
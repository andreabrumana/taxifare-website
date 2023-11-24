import streamlit as st
import requests
import pandas as pd
import numpy as np

st.title("Taxi Fares in New York City :taxi:")
st.markdown(
    """
            This website predicts the taxi fares in NYC based on pickup and dropoff positions and number of passengers.
            The model has been trained on New York City Taxi Fare Prediction available on [Kaggle](https://www.kaggle.com/c/new-york-city-taxi-fare-prediction).
            The model is a NN model.
            """
)

st.markdown(
    """
    In order to make predictions, the model needs data!
    Please insert yours and our **fantastic** model will predict the fare you are going to pay :smile:
    """
)

pickup_datetime = st.text_input(
    "Date and Time of the ride (US/Eastern tmz)",
    value="2012-10-06 12:10:20",
)
pickup_longitude = st.number_input("pickup longitude", value=-73.9798156)
pickup_latitude = st.number_input("pickup latitude", value=40.7614327)
dropoff_longitude = st.number_input("dropoff longitude", value=-73.8803331)
dropoff_latitude = st.number_input("dropoff latitude", value=40.6513111)
passenger_count = st.slider("Number of passengers", value=2, min_value=1, max_value=10)

params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count,
}

url = "https://taxifare-ne4yelgixa-uc.a.run.app/predict"


## Create a sample DataFrame with latitude and longitude values
data_map = pd.DataFrame(
    {
        "latitude": [pickup_latitude, dropoff_latitude],
        "longitude": [pickup_longitude, dropoff_longitude],
        "status": ["#fc031c", "#0317fc"],
    }
)


st.markdown("*Map with the location (in red pick, in Blue dropoff)*")
## Create a map with the data
st.map(data_map, color="status", size=20)

if st.button("Predict Fare", help="Click the button to have your predicted price"):
    response = requests.get(url, params=params).json()
    fare = float("{:.2f}".format(response["fare_amount"]))
    st.markdown(
        f"""
                ## ${fare}
                ### GIVE ME YOUR MONEY :moneybag:
                """
    )

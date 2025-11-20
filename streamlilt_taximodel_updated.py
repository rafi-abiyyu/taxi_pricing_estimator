import streamlit as st
import pandas as pd
import pickle

data = "taxi_pricing_model_for_streamlit.pkl"
with open(data, "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Taxi Fare Prediction", page_icon="🚕")

st.title("🚕 Taxi Fare Prediction App")
st.write("Predict taxi fares based on trip details.")

st.subheader("Enter Trip Details")

# ============================
# User Inputs
# ============================
trip_distance = st.number_input(
    "Trip Distance (km)",
    min_value=0.1,
    step=0.1,
    format="%.2f"
)

passenger_count = st.selectbox(
    "Passenger Count",
    [1, 2, 3, 4, 5]
)

time_of_day = st.selectbox(
    "Time of Day",
    ["Morning", "Afternoon", "Evening", "Night"]
)

day_of_week = st.selectbox(
    "Day of Week",
    ["Weekday", "Weekend"]
)

weather = st.selectbox(
    "Weather",
    ["Clear", "Rain", "Snow"]
)

input_df = pd.DataFrame({
    "trip_distance_km": [trip_distance],
    "passenger_count": [passenger_count],
    "time_of_day": [time_of_day],
    "day_of_week": [day_of_week],
    "weather": [weather]
})

if st.button("Predict Fare"):

    # First predict (not shown yet)
    predicted_fare = model.predict(input_df)[0]

    # Reject inputs beyond reliable model range
    if predicted_fare > 160:
        st.error(
            f" Oops — looks like your destination is  out of reach. "
        )
        st.stop()

    # If valid → continue normally
    MAPE = 0.30  # your model's error level

    lower_bound = predicted_fare * (1 - MAPE)
    upper_bound = predicted_fare * (1 + MAPE)

    st.success(f"Estimated Fare: **${predicted_fare:.2f}**")

    st.info(
        f"Likely Fare Range: **${lower_bound:.2f} - ${upper_bound:.2f}**\n\n"
        f"This range reflects the model’s average error on test data (~30% MAPE). "
        f"Real fares may vary due to route selection, traffic conditions, and other external factors."
    )

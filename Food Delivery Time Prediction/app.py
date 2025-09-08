import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns


model = joblib.load("./delivery_time_model.pkl")
df = pd.read_excel("Food Delivery Time Prediction Case Study.xlsx", sheet_name="Sheet1")


df = df.dropna()
df = df[df["Delivery_person_Age"] > 15]


def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat/2)**2 + np.cos(lat1)*np.cos(lat2)*np.sin(dlon/2)**2
    c = 2*np.arcsin(np.sqrt(a))
    return R * c

df["distance_km"] = df.apply(lambda row: haversine(
    row["Restaurant_latitude"], row["Restaurant_longitude"],
    row["Delivery_location_latitude"], row["Delivery_location_longitude"]), axis=1)


st.set_page_config(page_title="Delivery Time Prediction", layout="wide")
st.title("🚚 Quick Commerce Delivery Time Prediction Dashboard")

# Tabs for Navigation
tab1, tab2 = st.tabs(["🔮 Predict Delivery Time", "📊 Dashboard Insights"])


with tab1:
    st.subheader("Enter Order Details")

 
    distance = st.slider("📏 Distance (km)", 0.5, 20.0, 5.0)
    prep_time = st.slider("⏱ Prep Time (mins)", 5, 60, 20)
    age = st.slider("👤 Delivery Person Age", 18, 60, 30)
    rating = st.slider("⭐ Delivery Person Rating", 1.0, 5.0, 4.5, 0.1)
    order_type = st.selectbox("🛒 Type of Order", ["Snack", "Drinks", "Buffet", "Meal"])
    vehicle_type = st.selectbox("🚲 Vehicle Type", ["motorcycle", "scooter"])


    order_map = {"Snack":2, "Drinks":0, "Buffet":1, "Meal":3}
    vehicle_map = {"motorcycle":1, "scooter":0}

    row = {
        "Delivery_person_Age": age,
        "Delivery_person_Ratings": rating,
        "Restaurant_latitude": 0, 
        "Restaurant_longitude": 0,
        "Delivery_location_latitude": 0,
        "Delivery_location_longitude": 0,
        "Type_of_order": order_map[order_type],
        "Type_of_vehicle": vehicle_map[vehicle_type],
        "distance_km": distance
    }

    features = pd.DataFrame([row])

    if st.button("🔮 Predict"):
        prediction = model.predict(features)[0]
        st.success(f"Estimated Delivery Time: **{prediction:.1f} minutes**")


with tab2:
    st.subheader("📊 Data Insights")

    col1, col2 = st.columns(2)

    with col1:
        avg_by_vehicle = df.groupby("Type_of_vehicle")["Time_taken(min)"].mean()
        fig, ax = plt.subplots()
        avg_by_vehicle.plot(kind="bar", ax=ax, color="teal")
        ax.set_title("Avg Delivery Time by Vehicle Type")
        st.pyplot(fig)

    with col2:
        avg_by_order = df.groupby("Type_of_order")["Time_taken(min)"].mean()
        fig, ax = plt.subplots()
        avg_by_order.plot(kind="bar", ax=ax, color="orange")
        ax.set_title("Avg Delivery Time by Order Type")
        st.pyplot(fig)

    st.subheader("📏 Delivery Time vs Distance")
    fig, ax = plt.subplots()
    sns.scatterplot(x="distance_km", y="Time_taken(min)", data=df.sample(1000), alpha=0.5, ax=ax)
    ax.set_title("Distance vs Delivery Time")
    st.pyplot(fig)

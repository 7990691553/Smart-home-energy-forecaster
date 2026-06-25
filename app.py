import streamlit as st
import pickle
import pandas as pd

# 1. Load the trained model
with open('energy_model.pkl', 'rb') as f:
    model = pickle.load(f)

# 2. Set up the web page title
st.title("🏡 Smart Home Energy Consumption Forecaster")
st.write("Adjust the environmental factors below to predict the home's energy usage in real-time.")

# 3. Create User Input Controls
st.subheader("📊 Current Environmental Parameters")

temperature = st.slider("Outdoor Temperature (°C)", min_value=-10, max_value=40, value=22)
humidity = st.slider("Outdoor Humidity (%)", min_value=10, max_value=100, value=50)

hour = st.slider("Time of Day (Hour)", min_value=0, max_value=23, value=12)
day = st.selectbox("Day of the Week", 
                     options=[0, 1, 2, 3, 4, 5, 6], 
                     format_func=lambda x: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][x])

# 4. Prediction Button
if st.button("Predict Energy Usage"):
    # Notice how we use 'T_out' and 'RH_out' here to match the dataset!
    input_data = pd.DataFrame([[hour, day, temperature, humidity]], 
                              columns=['hour', 'day_of_week', 'T_out', 'RH_out'])
    
    # Make the prediction
    prediction = model.predict(input_data)[0]
    
    # Display the result (The dataset measures in Wh, so we divide by 1000 for kW)
    kw_prediction = prediction / 1000
    st.success(f"🔮 Predicted Energy Consumption: **{kw_prediction:.2f} kW**")
    
    st.info("💡 Tip: Try changing the hour to evening times (18-21) to see how the forecast adjusts dynamically!")
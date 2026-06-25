# 🏡 Smart Home Energy Consumption Forecaster

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📌 Project Overview
As global energy grids transition toward renewable sources, predicting precise power consumption at the residential level is critical for grid stability and load balancing. 

This project is an end-to-end Machine Learning application that forecasts residential energy demand based on real-time meteorological data and temporal features. It demonstrates a complete Data Science pipeline—from feature engineering raw time-series data to deploying a trained predictive model via an interactive web dashboard.

## 🧠 Machine Learning Architecture
The core predictive engine is built using a **Random Forest Regressor**. 

* **Feature Engineering:** Extracted cyclical temporal features (Hour of Day, Day of Week) from raw timestamps to capture human behavioral routines.
* **Environmental Inputs:** Integrated external meteorological variables (Outdoor Temperature `T_out` and Humidity `RH_out`) which significantly influence HVAC (Heating, Ventilation, and Air Conditioning) loads.
* **Model Training:** Utilized an ensemble learning method (Random Forest) via Scikit-Learn to capture complex, non-linear relationships between weather patterns and human power consumption.

## 🛠️ Technology Stack
* **Data Processing:** `pandas`, `numpy`
* **Machine Learning:** `scikit-learn`
* **Model Serialization:** `pickle`
* **Frontend UI / Deployment:** `streamlit`

---

## 🚀 Quickstart Guide

To replicate the environment and launch the interactive dashboard on your local machine, run the following commands in your terminal:

```bash
# Clone the repository and navigate into it
git clone [https://github.com/YOUR_USERNAME/smart-home-energy-forecaster.git](https://github.com/YOUR_USERNAME/smart-home-energy-forecaster.git)
cd smart-home-energy-forecaster

# Create and activate the virtual environment (use `.\venv\Scripts\activate` on Windows)
python -m venv venv
source venv/bin/activate

# Install required dependencies
pip install pandas numpy scikit-learn streamlit

# Launch the Streamlit application
streamlit run app.py

(Note: A pre-trained model energy_model.pkl is included. To train from scratch, run python train_model.py before starting the app).

📁 Repository Structure

📦 smart-home-energy-forecaster
 ┣ 📜 app.py               # Streamlit frontend and prediction logic
 ┣ 📜 train_model.py       # Data processing and ML training script
 ┣ 📜 energy_model.pkl     # Serialized Random Forest model
 ┣ 📜 .gitignore           # Git ignore configurations
 ┗ 📜 README.md            # Project documentation

 🔮 Future Scope
Integration of real-time API weather forecasting.

Cost-analysis module based on dynamic regional electricity pricing.

Migration of the deployment pipeline to Docker and AWS/GCP for global scaling.
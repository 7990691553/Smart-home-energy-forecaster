import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# 1. Load the dataset
df = pd.read_csv('energy_data.csv')

# 2. Feature Engineering: Extract numbers from the 'date' column
df['date'] = pd.to_datetime(df['date'])
df['hour'] = df['date'].dt.hour
df['day_of_week'] = df['date'].dt.dayofweek

# 3. Define Inputs (X) and Target Output (y)
# We use 'T_out' (Outdoor Temp) and 'RH_out' (Outdoor Humidity)
X = df[['hour', 'day_of_week', 'T_out', 'RH_out']]
y = df['Appliances'] # This is the energy consumption column

# 4. Split data into Training (80%) and Testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Initialize and Train the Model
print("Training the Random Forest model... This might take 10-30 seconds.")
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6. Save the trained model
with open('energy_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved successfully as 'energy_model.pkl'!")
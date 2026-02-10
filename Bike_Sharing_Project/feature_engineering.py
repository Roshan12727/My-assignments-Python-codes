import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder, MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create images directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Load cleaned data
try:
    df = pd.read_csv('cleaned_bike_data.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: cleaned_bike_data.csv not found. Run EDA first.")
    exit()

print(f"Initial shape: {df.shape}")

# --- 1. Feature Engineering ---

# A. Categorical Encoding
# Check unique values
print("\nUnique values in 'season':", df['season'].unique())
print("Unique values in 'weathersit':", df['weathersit'].unique())

# Ordinal/Label Mappings (if needed) or One-Hot
# If 'season' is string, we might want to map it to numbers or OHE. 
# Problem statement mentions: "Handle categorical variables through techniques like one-hot encoding"

# Let's use One-Hot Encoding for 'season' and 'weathersit'
# We will use pd.get_dummies for simplicity and readability
df = pd.get_dummies(df, columns=['season', 'weathersit'], prefix=['season', 'weather'], drop_first=True)
print("Applied One-Hot Encoding. New columns:", df.columns[df.columns.str.startswith('season_') | df.columns.str.startswith('weather_')])

# B. Cyclic Encoding for Time Variables (hr, mnth, weekday)
# This enables models to understand that hour 23 is close to hour 0
def encode_cyclic(df, col, max_val):
    df[col + '_sin'] = np.sin(2 * np.pi * df[col] / max_val)
    df[col + '_cos'] = np.cos(2 * np.pi * df[col] / max_val)
    return df

df = encode_cyclic(df, 'hr', 24)
df = encode_cyclic(df, 'mnth', 12)
df = encode_cyclic(df, 'weekday', 7)

print("Applied Cyclic Encoding for hr, mnth, weekday.")

# C. Handling 'dteday'
# We have already extracted yr, mnth, weekday, season. 
# 'dteday' itself is not needed for the model directly, but 'day' might be useful?
# Usually day of month (1-31) implies pay-day effects etc.
df['dteday'] = pd.to_datetime(df['dteday'])
df['day'] = df['dteday'].dt.day
# Cyclic encode day?
df = encode_cyclic(df, 'day', 31)

# Drop original 'dteday' and 'instant' as they are not predictive features
drop_cols = ['dteday', 'instant']
df.drop(columns=drop_cols, inplace=True, errors='ignore')

# D. Scaling Numerical Features
# We scale features like temp, atemp, hum, windspeed
# We do NOT scale target variables (cnt, casual, registered)
scale_cols = ['temp', 'atemp', 'hum', 'windspeed']
scaler = MinMaxScaler() # Normalizing to 0-1 as indicated in problem ("Normalized temperature", etc)
# Note: The original dataset says they are normalized, but let's ensure it or re-scale if we imputed.
# Since we imputed, values might be slightly off structure, so good to re-ensure.
df[scale_cols] = scaler.fit_transform(df[scale_cols])

print("Scaled feature columns.")

# --- 2. Correlation Analysis on New Features ---
plt.figure(figsize=(20, 15))
sns.heatmap(df.corr(), annot=False, cmap='coolwarm')
plt.title('Correlation Matrix (Processed Features)')
plt.tight_layout()
plt.savefig('images/correlation_matrix_processed.png')
print("Saved features correlation matrix.")

# --- 3. Save Processed Data ---
df.to_csv('processed_bike_data.csv', index=False)
print("\nSaved processed dataset to 'processed_bike_data.csv'")
print(f"Final shape: {df.shape}")
print("Final columns:", df.columns.tolist())

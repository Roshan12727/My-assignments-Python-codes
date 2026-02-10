import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os
from sklearn.model_selection import train_test_split

if not os.path.exists('images'):
    os.makedirs('images')

# Load the cleaned and processed data
df_clean = pd.read_csv('cleaned_bike_data.csv')
df_proc = pd.read_csv('processed_bike_data.csv')
model = joblib.load('models/best_random_forest.joblib')

# --- 1. Rental Distribution ---
plt.figure(figsize=(10, 6))
sns.histplot(df_clean['cnt'], kde=True, color='purple')
plt.title('Distribution of Total Bike Rentals')
plt.xlabel('Rental Count')
plt.savefig('images/dist_cnt.png')

# --- 2. Hourly Demand ---
plt.figure(figsize=(12, 6))
sns.lineplot(x='hr', y='cnt', data=df_clean, ci=None, marker='o')
plt.title('Average Hourly Demand Pattern')
plt.xlabel('Hour of Day')
plt.ylabel('Average Count')
plt.savefig('images/hourly_trend.png')

# --- 3. Seasonal Demand ---
plt.figure(figsize=(10, 6))
sns.barplot(x='season', y='cnt', data=df_clean, palette='viridis')
plt.title('Rental Counts by Season')
plt.savefig('images/seasonal_demand.png')

# --- 4. Weather Situation Impact ---
plt.figure(figsize=(10, 6))
sns.boxplot(x='weathersit', y='cnt', data=df_clean)
plt.title('Impact of Weather Status on Rentals')
plt.savefig('images/weather_impact.png')

# --- 5. Temperature Influence ---
plt.figure(figsize=(10, 6))
sns.scatterplot(x='temp', y='cnt', data=df_clean, alpha=0.3, color='orange')
plt.title('Normalized Temperature vs Rental Count')
plt.savefig('images/temp_vs_count.png')

# --- 6. Working Day vs Holiday ---
plt.figure(figsize=(10, 6))
sns.barplot(x='workingday', y='cnt', hue='holiday', data=df_clean)
plt.title('Rentals: Working Day vs Holiday comparison')
plt.savefig('images/workingday_holiday.png')

# --- 7. Residual Plot (Actual vs Predicted) ---
target = 'cnt'
X = df_proc.drop(columns=['casual', 'registered', 'cnt'], errors='ignore')
y = df_proc[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
y_pred = model.predict(X_test)

plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5, color='teal')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.title('Actual vs Predicted Count')
plt.xlabel('Actual Count')
plt.ylabel('Predicted Count')
plt.savefig('images/actual_vs_predicted.png')

# --- 8. Feature Importance (Rich version) ---
importances = model.feature_importances_
feature_names = X.columns
feature_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
feature_df = feature_df.sort_values(by='Importance', ascending=False)
plt.figure(figsize=(10, 10))
sns.barplot(x='Importance', y='Feature', data=feature_df.head(20), palette='magma')
plt.title('Top 20 Drivers of Bike Demand')
plt.savefig('images/top_drivers.png')

print("Rich visualizations generated for PPT.")

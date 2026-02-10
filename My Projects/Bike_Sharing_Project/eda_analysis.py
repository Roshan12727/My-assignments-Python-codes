import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create images directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Load the dataset
try:
    df = pd.read_csv('Dataset.csv', encoding='latin1') # Try latin1 if utf-8 fails, otherwise default
    print("Dataset loaded successfully.")
except Exception as e:
    print(f"Error loading dataset: {e}")
    exit()

# 1. Understand the structure
print("\n--- Project Info ---")
print(df.info())

print("\n--- First 5 Rows ---")
print(df.head())

print("\n--- Statistical Summary ---")
print(df.describe())

# 2. Check for missing values
print("\n--- Missing Values ---")
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])

# 3. Check for duplicates
print("\n--- Duplicates ---")
duplicates = df.duplicated().sum()
print(f"Number of duplicate records: {duplicates}")

# 4. Outlier Detection (visualizing numerical columns)
numerical_cols = ['temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'cnt']
plt.figure(figsize=(15, 10))
for i, col in enumerate(numerical_cols, 1):
    plt.subplot(3, 3, i)
    sns.boxplot(y=df[col])
    plt.title(f'Boxplot of {col}')

plt.tight_layout()
plt.savefig('images/outliers_boxplot.png')
print("\nOutlier boxplots saved to images/outliers_boxplot.png")

# 5. Check unique values in categorical columns to identify any anomalies
categorical_cols = ['season', 'mnth', 'hr', 'holiday', 'weekday', 'workingday', 'weathersit']
print("\n--- Unique Values in Categorical Columns ---")
for col in categorical_cols:
    print(f"\n{col}: {df[col].unique()}")


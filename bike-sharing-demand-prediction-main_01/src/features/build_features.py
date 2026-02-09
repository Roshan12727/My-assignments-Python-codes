def build_features(df):
    # Generate new features from existing ones to improve model performance

    # Example feature engineering
    df['hour'] = df['datetime'].dt.hour
    df['day'] = df['datetime'].dt.day
    df['month'] = df['datetime'].dt.month
    df['year'] = df['datetime'].dt.year
    df['is_weekend'] = df['day'].apply(lambda x: 1 if x in [5, 6] else 0)
    
    # One-hot encoding for categorical variables
    df = pd.get_dummies(df, columns=['season', 'weather'], drop_first=True)

    # Scaling numerical features
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    df[['temp', 'humidity', 'windspeed']] = scaler.fit_transform(df[['temp', 'humidity', 'windspeed']])

    return df

# Note: Ensure to import necessary libraries at the beginning of the script
import pandas as pd

# This file is intentionally left blank.
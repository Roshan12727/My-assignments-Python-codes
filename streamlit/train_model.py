"""
Diabetes Prediction Model Training Script
This script trains a Logistic Regression model on the diabetes dataset
and saves the model and scaler for use in the Streamlit app.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score
import joblib

def load_and_prepare_data(filepath='diabetes.csv'):
    """Load and prepare the diabetes dataset"""
    print("Loading dataset...")
    df = pd.read_csv(filepath)
    
    print(f"Dataset shape: {df.shape}")
    print(f"\nDataset info:")
    print(df.info())
    print(f"\nFirst few rows:")
    print(df.head())
    
    # Check for missing values
    print(f"\nMissing values:\n{df.isnull().sum()}")
    
    # Replace zero values with NaN for specific columns (medical impossibilities)
    zero_columns = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    for col in zero_columns:
        df[col] = df[col].replace(0, np.nan)
    
    # Fill missing values with median
    df.fillna(df.median(), inplace=True)
    
    print(f"\nAfter handling missing values:")
    print(df.isnull().sum())
    
    return df

def train_model(df):
    """Train the logistic regression model"""
    print("\n" + "="*50)
    print("Training Logistic Regression Model")
    print("="*50)
    
    # Separate features and target
    X = df.drop('Outcome', axis=1)
    y = df['Outcome']
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"\nTraining set size: {X_train.shape[0]}")
    print(f"Test set size: {X_test.shape[0]}")
    
    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train the model
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test_scaled)
    y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]
    
    # Evaluate the model
    print("\n" + "="*50)
    print("Model Evaluation")
    print("="*50)
    
    accuracy = accuracy_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_pred_proba)
    
    print(f"\nAccuracy: {accuracy:.4f}")
    print(f"ROC AUC Score: {roc_auc:.4f}")
    
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=['Non-Diabetic', 'Diabetic']))
    
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
    # Feature importance
    print("\nFeature Importance (Coefficients):")
    feature_importance = pd.DataFrame({
        'Feature': X.columns,
        'Coefficient': model.coef_[0]
    }).sort_values('Coefficient', ascending=False)
    print(feature_importance)
    
    return model, scaler

def save_model_and_scaler(model, scaler):
    """Save the trained model and scaler"""
    print("\n" + "="*50)
    print("Saving Model and Scaler")
    print("="*50)
    
    joblib.dump(model, 'logistic_regression_model.joblib')
    joblib.dump(scaler, 'scaler.joblib')
    
    print("\n[OK] Model saved as 'logistic_regression_model.joblib'")
    print("[OK] Scaler saved as 'scaler.joblib'")

def main():
    """Main execution function"""
    print("="*50)
    print("DIABETES PREDICTION MODEL TRAINING")
    print("="*50)
    
    # Load and prepare data
    df = load_and_prepare_data()
    
    # Train model
    model, scaler = train_model(df)
    
    # Save model and scaler
    save_model_and_scaler(model, scaler)
    
    print("\n" + "="*50)
    print("Training Complete!")
    print("="*50)
    print("\nYou can now run the Streamlit app with:")
    print("streamlit run streamlit_app.py")

if __name__ == "__main__":
    main()

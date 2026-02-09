import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

def load_data(file_path):
    return pd.read_csv(file_path)

def train_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def save_model(model, file_path):
    joblib.dump(model, file_path)

def main():
    # Load the dataset
    data = load_data('../data/processed/bike_sharing_data.csv')
    
    # Split the data into features and target variable
    X = data.drop('count', axis=1)
    y = data['count']
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model
    model = train_model(X_train, y_train)
    
    # Save the trained model
    save_model(model, '../models/checkpoints/bike_sharing_model.pkl')
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')

if __name__ == '__main__':
    main()
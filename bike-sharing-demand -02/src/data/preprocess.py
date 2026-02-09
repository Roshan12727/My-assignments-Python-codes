import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    # Drop duplicates
    data = data.drop_duplicates()
    
    # Handle missing values
    imputer = SimpleImputer(strategy='mean')
    data[['column1', 'column2']] = imputer.fit_transform(data[['column1', 'column2']])
    
    return data

def detect_outliers(data):
    # Example of outlier detection using IQR
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    filtered_data = data[~((data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))).any(axis=1)]
    
    return filtered_data

def scale_features(data):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data[['feature1', 'feature2']])
    data[['feature1', 'feature2']] = scaled_data
    
    return data

def preprocess_data(file_path):
    data = load_data(file_path)
    data = clean_data(data)
    data = detect_outliers(data)
    data = scale_features(data)
    
    return data
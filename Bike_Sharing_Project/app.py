import joblib
import os

# Load model
model = joblib.load('best_random_forest.joblib')

# File access using os.path.join
csv_file_path = os.path.join('data', 'your_data_file.csv')
# Replace your_data_file.csv with the actual filename.

import os

# Define paths
model_path = 'best_random_forest.joblib'

# Ensure proper CSV path handling
csv_path = os.path.join(os.path.dirname(__file__), 'processed_bike_data.csv')

# Load your model here and any other processing needed

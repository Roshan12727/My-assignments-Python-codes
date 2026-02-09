import pandas as pd
import os

def create_dataset(raw_data_path, processed_data_path):
    if not os.path.exists(raw_data_path):
        raise FileNotFoundError(f"Raw data not found at {raw_data_path}")

    # Load raw data
    raw_data = pd.read_csv(raw_data_path)

    # Perform any necessary cleaning and processing
    # For example, handling missing values, converting data types, etc.
    processed_data = raw_data.dropna()  # Simple example of dropping missing values

    # Save the processed dataset
    processed_data.to_csv(processed_data_path, index=False)
    print(f"Processed data saved to {processed_data_path}")

if __name__ == "__main__":
    raw_data_path = '../data/raw/bike_sharing_data.csv'  # Update with actual raw data file
    processed_data_path = '../data/processed/bike_sharing_processed.csv'
    create_dataset(raw_data_path, processed_data_path)
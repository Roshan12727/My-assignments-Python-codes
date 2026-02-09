#!/bin/bash

# Activate the conda environment
source activate bike-sharing-env

# Run the data preprocessing
python src/data/preprocess.py

# Run feature engineering
python src/features/build_features.py

# Train the model
python src/models/train.py

# Save the trained model
python src/models/hyperparameter_search.py

echo "Training completed successfully!"
#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Start the prediction service
python src/deployment/api.py
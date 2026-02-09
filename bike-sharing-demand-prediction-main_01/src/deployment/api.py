from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Model loading with error handling
MODEL_PATH = os.getenv('MODEL_PATH', 'models/bike_sharing_model.pkl')
model = None

try:
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)
        logger.info(f"Model loaded successfully from {MODEL_PATH}")
    else:
        logger.warning(f"Model file not found at {MODEL_PATH}. Using mock predictions.")
except Exception as e:
    logger.error(f"Error loading model: {str(e)}")

@app.route('/', methods=['GET'])
def home():
    """Home endpoint with API information"""
    return jsonify({
        'message': 'Bike Sharing Demand Prediction API',
        'version': '1.0',
        'endpoints': {
            '/health': 'Health check endpoint',
            '/predict': 'POST - Make predictions'
        }
    })

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None
    }), 200

@app.route('/predict', methods=['POST'])
def predict():
    """Make predictions based on input features"""
    try:
        data = request.get_json(force=True)
        
        if 'features' not in data:
            return jsonify({'error': 'Missing "features" in request'}), 400
        
        features = np.array(data['features']).reshape(1, -1)
        
        if model is not None:
            prediction = model.predict(features)
            return jsonify({
                'prediction': float(prediction[0]),
                'status': 'success'
            })
        else:
            # Mock prediction when model is not available
            mock_prediction = np.random.randint(50, 500)
            return jsonify({
                'prediction': float(mock_prediction),
                'status': 'mock',
                'message': 'Using mock prediction - model not loaded'
            })
    
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        return jsonify({
            'error': str(e),
            'status': 'failed'
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
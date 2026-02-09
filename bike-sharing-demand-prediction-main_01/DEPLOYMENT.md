# Docker Deployment Guide

## 🚀 Quick Start

### Prerequisites
- Docker installed ([Download Docker](https://www.docker.com/get-started))
- Docker Compose installed (included with Docker Desktop)

### Option 1: Using Docker Compose (Recommended)

```bash
# Navigate to project directory
cd bike-sharing-demand-prediction

# Build and run the container
docker-compose up --build

# Run in detached mode (background)
docker-compose up -d

# Stop the container
docker-compose down
```

### Option 2: Using Docker directly

```bash
# Build the image
docker build -t bike-sharing-api .

# Run the container
docker run -p 5000:5000 bike-sharing-api

# Run with environment variables
docker run -p 5000:5000 -e MODEL_PATH=models/your_model.pkl bike-sharing-api
```

---

## 📋 API Endpoints

### Health Check
```bash
curl http://localhost:5000/health
```

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

### Home
```bash
curl http://localhost:5000/
```

### Make Prediction
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [1, 2, 3, 4, 5, 6, 7, 8]}'
```

**Response (with model):**
```json
{
  "prediction": 245.8,
  "status": "success"
}
```

**Response (without model - mock):**
```json
{
  "prediction": 342.0,
  "status": "mock",
  "message": "Using mock prediction - model not loaded"
}
```

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file from the template:
```bash
cp .env.example .env
```

Available variables:
- `MODEL_PATH` - Path to your trained model file (default: `models/bike_sharing_model.pkl`)
- `FLASK_ENV` - Flask environment (default: `production`)
- `WORKERS` - Number of gunicorn workers (default: `4`)
- `PORT` - Port to run the API (default: `5000`)

### Adding Your Trained Model

1. **Train your model** and save it:
```python
import joblib
from sklearn.ensemble import RandomForestRegressor

# Train your model
model = RandomForestRegressor()
# ... training code ...

# Save the model
joblib.dump(model, 'models/bike_sharing_model.pkl')
```

2. **Place the model** in the `models/` directory

3. **Rebuild the container**:
```bash
docker-compose up --build
```

---

## 🧪 Testing the API

### Test with Python
```python
import requests
import json

# Test health
response = requests.get('http://localhost:5000/health')
print(response.json())

# Test prediction
data = {
    'features': [12, 1, 1, 0, 1, 2, 0, 15.0, 16.0, 80, 0]
}
response = requests.post(
    'http://localhost:5000/predict',
    json=data
)
print(response.json())
```

### Test with cURL
```bash
# Health check
curl http://localhost:5000/health

# Prediction
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [12, 1, 1, 0, 1, 2, 0, 15.0, 16.0, 80, 0]}'
```

---

## 📦 Docker Commands Reference

### View running containers
```bash
docker ps
```

### View logs
```bash
# Using docker-compose
docker-compose logs -f

# Using docker
docker logs -f <container-id>
```

### Stop containers
```bash
# Using docker-compose
docker-compose down

# Using docker
docker stop <container-id>
```

### Remove containers and images
```bash
# Remove containers
docker-compose down --volumes

# Remove images
docker rmi bike-sharing-api
```

### Execute commands in container
```bash
# Using docker-compose
docker-compose exec bike-sharing-api bash

# Using docker
docker exec -it <container-id> bash
```

---

## 🐛 Troubleshooting

### Port already in use
If port 5000 is already in use, change it in `docker-compose.yml`:
```yaml
ports:
  - "8080:5000"  # Use port 8080 instead
```

### Model not loading
- Check that your model file exists in the `models/` directory
- Verify the `MODEL_PATH` environment variable is correct
- Check logs: `docker-compose logs -f`

### Permission denied errors
Make sure the models directory has proper permissions:
```bash
chmod -R 755 models/
```

### Container won't start
View detailed logs:
```bash
docker-compose logs
```

Common issues:
- Missing dependencies in `requirements.txt`
- Port conflicts
- Syntax errors in code

---

## 🌐 Production Deployment

### Deploy to Cloud Platforms

#### Docker Hub
```bash
# Tag the image
docker tag bike-sharing-api username/bike-sharing-api:v1.0

# Push to Docker Hub
docker push username/bike-sharing-api:v1.0
```

#### AWS ECS / Azure Container Instances / Google Cloud Run
- Build and push image to respective container registry
- Configure environment variables in cloud console
- Set up health checks using `/health` endpoint
- Configure auto-scaling based on CPU/memory usage

### Security Recommendations
- ✅ Already using non-root user in container
- ✅ Environment variables for configuration
- ✅ Health checks configured
- 🔒 Add SSL/TLS for HTTPS in production
- 🔒 Implement API authentication (API keys, JWT)
- 🔒 Use secrets management for sensitive data

---

## 📊 Performance Tuning

### Adjust Worker Count
In `Dockerfile`, modify the gunicorn workers:
```dockerfile
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "8", ...]
```

Recommended: `(2 * CPU cores) + 1`

### Resource Limits
Add resource limits in `docker-compose.yml`:
```yaml
services:
  bike-sharing-api:
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 2G
```

---

## 📝 Notes

- The API works with or without a trained model (uses mock predictions as fallback)
- Model can be updated by replacing the file in `models/` directory and restarting
- Gunicorn is configured with 4 workers and 120-second timeout
- Health checks run every 30 seconds
- CORS is enabled for all origins (configure as needed for production)

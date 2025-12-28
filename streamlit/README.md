# Diabetes Prediction App

A machine learning web application that predicts the likelihood of diabetes based on patient health metrics using a Logistic Regression model.

## 🚀 Features

- Interactive web interface built with Streamlit
- Real-time diabetes risk prediction
- Trained on the Pima Indians Diabetes Database
- Easy-to-use sliders for patient data input
- Visual probability display

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## 🛠️ Installation & Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Train the Model

Before running the app, you need to train the model and generate the required files:

```bash
python train_model.py
```

This will:
- Load and preprocess the diabetes dataset
- Train a Logistic Regression model
- Save the model as `logistic_regression_model.joblib`
- Save the scaler as `scaler.joblib`
- Display model performance metrics

### 3. Run the Streamlit App Locally

```bash
streamlit run streamlit_app.py
```

The app will open in your default web browser at `http://localhost:8501`

## 📊 Dataset Features

The model uses the following patient health metrics:

- **Pregnancies**: Number of times pregnant
- **Glucose**: Plasma glucose concentration (mg/dL)
- **Blood Pressure**: Diastolic blood pressure (mmHg)
- **Skin Thickness**: Triceps skin fold thickness (mm)
- **Insulin**: 2-Hour serum insulin (mu U/ml)
- **BMI**: Body mass index (weight in kg/(height in m)^2)
- **Diabetes Pedigree Function**: Diabetes pedigree function score
- **Age**: Age in years

## 🌐 Server Deployment

### Option 1: Streamlit Community Cloud (Free)

1. Push your code to a GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click "New app"
5. Select your repository, branch, and `streamlit_app.py`
6. Click "Deploy"

**Important**: Make sure to run `train_model.py` locally first and commit the generated `.joblib` files to your repository.

### Option 2: Heroku

1. Create a `Procfile`:
```
web: sh setup.sh && streamlit run streamlit_app.py
```

2. Create `setup.sh`:
```bash
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

3. Deploy to Heroku:
```bash
heroku login
heroku create your-app-name
git push heroku main
```

### Option 3: Docker Deployment

1. Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python train_model.py

EXPOSE 8501

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

2. Build and run:
```bash
docker build -t diabetes-prediction-app .
docker run -p 8501:8501 diabetes-prediction-app
```

### Option 4: AWS EC2 / VPS

1. SSH into your server
2. Clone the repository
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Train the model:
```bash
python train_model.py
```
5. Run with nohup for persistent execution:
```bash
nohup streamlit run streamlit_app.py --server.port=8501 --server.address=0.0.0.0 &
```

## 📁 Project Structure

```
diabetes-prediction-app/
├── streamlit_app.py              # Main Streamlit application
├── train_model.py                # Model training script
├── diabetes.csv                  # Dataset
├── requirements.txt              # Python dependencies
├── README.md                     # This file
├── logistic_regression_model.joblib  # Trained model (generated)
└── scaler.joblib                 # Feature scaler (generated)
```

## 🔍 Model Performance

The Logistic Regression model achieves:
- Accuracy: ~77-78%
- ROC AUC Score: ~0.82-0.84

(Exact metrics will be displayed when you run `train_model.py`)

## ⚠️ Disclaimer

This application is for educational and demonstration purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.

## 📝 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements.

## 📧 Support

For issues or questions, please open an issue in the repository.

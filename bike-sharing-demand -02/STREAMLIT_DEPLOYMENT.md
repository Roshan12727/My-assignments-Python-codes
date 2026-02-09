# Streamlit Deployment Guide

## 🚀 Quick Start (Local)

### 1. Install Dependencies
```bash
cd "E:\new vsc\bike-sharing-demand-prediction"
pip install -r requirements.txt
```

### 2. Run the App
```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

---

## ☁️ Deploy to Streamlit Cloud (Free!)

### Prerequisites
- GitHub account
- Your code pushed to a GitHub repository

### Step-by-Step Deployment

#### 1. Push Your Code to GitHub
```bash
cd "E:\new vsc\bike-sharing-demand-prediction"
git init
git add .
git commit -m "Initial commit - Bike Sharing Prediction App"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/bike-sharing-prediction.git
git push -u origin main
```

#### 2. Deploy on Streamlit Cloud

1. **Go to** [share.streamlit.io](https://share.streamlit.io)
2. **Sign in** with your GitHub account
3. **Click** "New app"
4. **Select** your repository: `bike-sharing-prediction`
5. **Set** main file path: `app.py`
6. **Click** "Deploy!"

That's it! Your app will be live in a few minutes at:
`https://YOUR_USERNAME-bike-sharing-prediction.streamlit.app`

---

## 🌐 Alternative Deployment Options

### Deploy to Heroku

1. **Create** `Procfile`:
```bash
web: streamlit run app.py --server.port=$PORT
```

2. **Deploy**:
```bash
heroku create bike-sharing-app
git push heroku main
```

### Deploy with Docker

Use the existing Dockerfile and add:
```dockerfile
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

## 📊 App Features

### 🔮 Prediction Tab
- Interactive sliders for all input features
- Real-time demand predictions
- Visual metrics and insights
- Estimated revenue and capacity usage

### 📈 Analytics Tab
- Hourly demand patterns
- Weather impact analysis
- Seasonal distribution charts
- Interactive Plotly visualizations

### ℹ️ Information Tab
- App documentation
- Feature descriptions
- Technology stack
- Deployment information

---

## 🔧 Configuration

### Custom Theme
Edit `.streamlit/config.toml` to change colors and appearance:
```toml
[theme]
primaryColor="#FF4B4B"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
```

### Add Your Trained Model

1. **Train and save your model**:
```python
import joblib
model = your_trained_model
joblib.dump(model, 'models/bike_sharing_model.pkl')
```

2. **App will automatically use it** - no code changes needed!

---

## 🐛 Troubleshooting

### App won't start locally
```bash
# Make sure all dependencies are installed
pip install -r requirements.txt --upgrade

# Check Streamlit version
streamlit --version
```

### Port already in use
```bash
# Use a different port
streamlit run app.py --server.port=8502
```

### Model not loading
- Check that `models/bike_sharing_model.pkl` exists
- App works with mock predictions if model is missing
- Check file permissions

---

## 📝 Streamlit Cloud Settings

### Secrets Management
For API keys or sensitive data, use Streamlit secrets:

1. In Streamlit Cloud dashboard, go to **Settings** → **Secrets**
2. Add your secrets in TOML format:
```toml
[model]
path = "models/bike_sharing_model.pkl"
```

3. Access in code:
```python
import streamlit as st
model_path = st.secrets["model"]["path"]
```

### Resource Limits
**Free tier includes:**
- 1 GB RAM
- 1 CPU
- Unlimited public apps
- Community support

**For production apps**, consider Streamlit for Teams.

---

## 🎨 Customization Ideas

### Add More Features
- Upload CSV for batch predictions
- Download predictions as Excel
- User authentication
- Database integration
- Email notifications

### Enhance Visualizations
- Map view of bike stations
- Real-time usage dashboard
- Prediction accuracy metrics
- A/B testing different models

---

## 📚 Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Streamlit Gallery](https://streamlit.io/gallery)
- [Plotly Charts](https://plotly.com/python/)
- [Deployment Guide](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app)

---

## ✅ Deployment Checklist

- [ ] Code pushed to GitHub
- [ ] requirements.txt includes all dependencies
- [ ] app.py is in the root directory
- [ ] .streamlit/config.toml configured (optional)
- [ ] Streamlit Cloud account created
- [ ] App deployed and tested
- [ ] Share the URL with users!

---

## 🎉 You're Ready!

Your Streamlit app is production-ready and can be deployed in minutes. Choose Streamlit Cloud for the easiest deployment experience!

**Local URL**: http://localhost:8501  
**Cloud URL**: https://YOUR_USERNAME-bike-sharing-prediction.streamlit.app

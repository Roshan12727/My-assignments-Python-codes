# Deploying to Streamlit Cloud

To deploy your Bike Sharing Demand Prediction app, follow these 3 steps:

### 1. Upload to GitHub
1. Create a new **Public** repository on your GitHub (e.g., `bike-sharing-prediction`).
2. Upload the following essential files from your desktop folder:
   - `app.py` (The main app)
   - `requirements.txt` (The list of libraries)
   - `processed_bike_data.csv` (Used for column matching)
   - `models/best_random_forest.joblib` (The trained brain of the app)

### 2. Connect to Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io).
2. Sign in with your GitHub account.
3. Click **"New app"**.
4. Select your repository: `bike-sharing-prediction`.
5. Branch: `main` (or `master`).
6. Main file path: `app.py`.

### 3. Launch
1. Click **"Deploy!"**.
2. Your app will be live at a URL like `https://bike-sharing-prediction.streamlit.app`.

---
**Note:** I have already created the `requirements.txt` file in your folder to make this process seamless.

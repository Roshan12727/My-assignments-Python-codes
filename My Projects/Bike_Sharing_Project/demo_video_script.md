# Demo Video Script: Bike-Sharing Demand Prediction

## Introduction (0:00 - 1:00)
- "Hello, my name is [Your Name], and today I will be presenting my project on Bike-sharing Rental Demand Prediction."
- "The goal is to ensure a stable supply of rental bikes in urban cities by predicting demand using weather and time factors."

## Step 1: Exploratory Data Analysis (1:00 - 3:00)
- *Show the code in `eda_analysis_v2.py`*
- "We started by loading the dataset and checking for missing values. We found hidden '?' symbols in columns like temperature and humidity."
- "I replaced these with medians to keep the data robust."
- "We also fixed the date formats and validated that total rentals always match the sum of casual and registered users."

## Step 2: Data Visualization (3:00 - 4:30)
- *Show some plots in the `images/` folder*
- "Here you can see the hourly trend. Demand peaks exactly at commuter rush hours: 8 AM and 5-6 PM."
- "Temperature shows a clear positive correlation; as it gets warmer, more people rent bikes."

## Step 3: Feature Engineering (4:30 - 6:30)
- *Show the code in `feature_engineering_v2.py`*
- "Standard models don't understand that hour 23 is next to hour 0. So, I applied **Cyclic Encoding** using Sine and Cosine transformations."
- "We also used **One-Hot Encoding** for Categorical features like Season and Weather to avoid implying any mathematical order between them."
- "Finally, we scaled all features using Min-Max scaling."

## Step 4: Model Building & Tuning (6:30 - 8:30)
- *Show `model_building.py` and `hyperparameter_tuning.py*
- "I evaluated three high-performance algorithms: Decision Tree, Random Forest, and Gradient Boosting."
- "**Why Random Forest?** It was our clear winner with an R-squared of 0.94. Unlike a single Decision Tree, which often overfits the data, Random Forest uses 'Bagging'—an ensemble technique that averages multiple trees to reduce variance and improve stability. This makes it highly robust to the outliers we see during peak traffic hours."
- "**Why not the others?** The **Decision Tree** hit a baseline of 88% but struggled with high variance; it were too 'greedy' and learned the training noise. **Gradient Boosting** also reached 88% but had the highest average error (MAE 42), likely because it was too sensitive to the high variability in our hourly spikes."
- "I then used Randomized Search CV to optimize the Random Forest, fine-tuning parameters like tree depth and the number of estimators to ensure maximum reliability for real-world deployment."

## Step 5: Web App Deployment (8:30 - 10:00)
- *Show the running Streamlit App in the browser*
- "Finally, I deployed the model using Streamlit. Users can adjust weather conditions like temperature and humidity on the left side."
- "When we click 'Predict', the model instantly calculates the expected rental demand."
- "This tool helps city planners and bike-share companies prepare for peak demand in real-time."

## Conclusion
- "Thank you for watching!"

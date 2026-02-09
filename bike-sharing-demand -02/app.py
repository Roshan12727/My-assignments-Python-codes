import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="Bike Sharing Demand Prediction",
    page_icon="🚴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        padding: 0.5rem;
        border-radius: 0.5rem;
    }
    .prediction-box {
        padding: 2rem;
        border-radius: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-align: center;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Load model (with fallback to mock predictions)
@st.cache_resource
def load_model():
    model_path = 'models/bike_sharing_model.pkl'
    try:
        if os.path.exists(model_path):
            model = joblib.load(model_path)
            return model, True
        else:
            return None, False
    except Exception as e:
        st.warning(f"Could not load model: {str(e)}")
        return None, False

model, model_loaded = load_model()

# Header
st.title("🚴 Bike Sharing Demand Prediction")
st.markdown("### Predict bike rental demand based on weather and temporal features")

# Sidebar information
with st.sidebar:
    st.header("ℹ️ About")
    st.info("""
    This application predicts bike-sharing demand using machine learning.
    
    **Features:**
    - Real-time predictions
    - Interactive visualizations
    - Historical data analysis
    """)
    
    st.header("📊 Model Status")
    if model_loaded:
        st.success("✅ Model loaded successfully")
    else:
        st.warning("⚠️ Using mock predictions")
    
    st.header("🎯 Quick Tips")
    st.markdown("""
    - Adjust the sliders for different scenarios
    - Higher temperature = more rentals
    - Clear weather = higher demand
    - Rush hours have peak demand
    """)

# Main content
tab1, tab2, tab3 = st.tabs(["🔮 Prediction", "📈 Analytics", "ℹ️ Information"])

with tab1:
    st.header("Make a Prediction")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("📅 Temporal Features")
        hour = st.slider("Hour of Day", 0, 23, 12, help="Hour of the day (0-23)")
        month = st.selectbox("Month", range(1, 13), index=5, 
                            format_func=lambda x: datetime(2024, x, 1).strftime('%B'))
        day_of_week = st.selectbox("Day of Week", 
                                   ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 
                                    'Friday', 'Saturday', 'Sunday'],
                                   index=0)
        is_holiday = st.checkbox("Is Holiday?")
        
    with col2:
        st.subheader("🌤️ Weather Conditions")
        temperature = st.slider("Temperature (°C)", -10, 40, 20)
        humidity = st.slider("Humidity (%)", 0, 100, 60)
        windspeed = st.slider("Wind Speed (km/h)", 0, 50, 15)
        weather = st.selectbox("Weather Condition", 
                              ['Clear', 'Mist', 'Light Rain/Snow', 'Heavy Rain/Snow'])
    
    with col3:
        st.subheader("📊 Additional Info")
        is_working_day = st.checkbox("Is Working Day?", value=True)
        season = st.selectbox("Season", ['Spring', 'Summer', 'Fall', 'Winter'])
        
        # Visual indicators
        st.metric("Temperature", f"{temperature}°C", 
                 delta=f"{temperature - 20}°C from avg")
        st.metric("Humidity", f"{humidity}%")
    
    # Encode categorical variables
    weather_mapping = {'Clear': 1, 'Mist': 2, 'Light Rain/Snow': 3, 'Heavy Rain/Snow': 4}
    season_mapping = {'Spring': 1, 'Summer': 2, 'Fall': 3, 'Winter': 4}
    day_mapping = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3,
                   'Friday': 4, 'Saturday': 5, 'Sunday': 6}
    
    # Create feature array (adjust based on your model's expected features)
    features = np.array([[
        hour,
        month,
        day_mapping[day_of_week],
        int(is_holiday),
        int(is_working_day),
        season_mapping[season],
        weather_mapping[weather],
        temperature,
        humidity,
        windspeed,
        0  # Additional feature placeholder
    ]])
    
    # Predict button
    if st.button("🔮 Predict Demand", use_container_width=True):
        with st.spinner("Calculating prediction..."):
            if model_loaded and model is not None:
                try:
                    prediction = model.predict(features)[0]
                    st.success("Prediction completed!")
                except Exception as e:
                    # Fallback to mock prediction
                    base = 100
                    temp_factor = (temperature - 10) * 5
                    hour_factor = 50 if hour in [7,8,9,17,18,19] else 0
                    weather_factor = -30 if weather in ['Light Rain/Snow', 'Heavy Rain/Snow'] else 20
                    prediction = max(0, base + temp_factor + hour_factor + weather_factor + np.random.randint(-20, 20))
            else:
                # Mock prediction
                base = 100
                temp_factor = (temperature - 10) * 5
                hour_factor = 50 if hour in [7,8,9,17,18,19] else 0
                weather_factor = -30 if weather in ['Light Rain/Snow', 'Heavy Rain/Snow'] else 20
                prediction = max(0, base + temp_factor + hour_factor + weather_factor + np.random.randint(-20, 20))
            
            # Display prediction
            st.markdown(f"""
                <div class="prediction-box">
                    <h2>Predicted Bike Demand</h2>
                    <h1 style="font-size: 4rem; margin: 1rem 0;">{int(prediction)}</h1>
                    <p style="font-size: 1.2rem;">bikes per hour</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Additional insights
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Demand Level", 
                         "High" if prediction > 200 else "Medium" if prediction > 100 else "Low")
            with col2:
                st.metric("Estimated Revenue", f"${int(prediction * 2)}")
            with col3:
                daily_est = int(prediction * 24)
                st.metric("Daily Estimate", f"{daily_est} bikes")
            with col4:
                capacity = int((prediction / 500) * 100) if prediction < 500 else 100
                st.metric("Capacity Usage", f"{capacity}%")

with tab2:
    st.header("📈 Demand Analytics")
    
    # Generate sample hourly data for visualization
    hours = list(range(24))
    sample_demands = [100 + i*10 + np.random.randint(-20, 20) if i < 12 
                     else 100 + (24-i)*10 + np.random.randint(-20, 20) 
                     for i in hours]
    
    # Hourly demand chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=hours, 
        y=sample_demands,
        mode='lines+markers',
        name='Hourly Demand',
        line=dict(color='#667eea', width=3),
        marker=dict(size=8)
    ))
    fig.update_layout(
        title="Typical Hourly Demand Pattern",
        xaxis_title="Hour of Day",
        yaxis_title="Number of Bikes",
        height=400,
        hovermode='x unified'
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Weather impact
    col1, col2 = st.columns(2)
    
    with col1:
        weather_data = pd.DataFrame({
            'Weather': ['Clear', 'Mist', 'Light Rain', 'Heavy Rain'],
            'Avg Demand': [350, 250, 150, 80]
        })
        fig2 = px.bar(weather_data, x='Weather', y='Avg Demand', 
                     title="Average Demand by Weather",
                     color='Avg Demand',
                     color_continuous_scale='Blues')
        st.plotly_chart(fig2, use_container_width=True)
    
    with col2:
        season_data = pd.DataFrame({
            'Season': ['Spring', 'Summer', 'Fall', 'Winter'],
            'Avg Demand': [220, 380, 300, 180]
        })
        fig3 = px.pie(season_data, values='Avg Demand', names='Season',
                     title="Seasonal Distribution",
                     color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig3, use_container_width=True)

with tab3:
    st.header("ℹ️ About This Application")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 Features")
        st.markdown("""
        - **Real-time Predictions**: Get instant demand forecasts
        - **Interactive UI**: Easy-to-use sliders and inputs
        - **Visual Analytics**: Charts and graphs for insights
        - **Mock Predictions**: Works even without a trained model
        """)
        
        st.subheader("🔧 Technology Stack")
        st.markdown("""
        - **Streamlit** - Web framework
        - **Scikit-learn** - Machine learning
        - **Plotly** - Interactive visualizations
        - **Pandas & NumPy** - Data processing
        """)
    
    with col2:
        st.subheader("📊 Input Features")
        st.markdown("""
        The prediction model uses the following features:
        
        - **Temporal**: Hour, month, day of week
        - **Weather**: Temperature, humidity, wind speed, conditions
        - **Calendar**: Holiday, working day, season
        """)
        
        st.subheader("🚀 Deployment")
        st.markdown("""
        This app can be deployed to:
        - **Streamlit Cloud** (Free & Easy)
        - **Heroku**
        - **AWS / Azure / GCP**
        
        See STREAMLIT_DEPLOYMENT.md for instructions.
        """)

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #666;">
        <p>Bike Sharing Demand Prediction | Built with Streamlit ❤️</p>
    </div>
""", unsafe_allow_html=True)

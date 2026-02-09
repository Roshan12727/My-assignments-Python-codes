import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_rentals_over_time(data):
    plt.figure(figsize=(12, 6))
    data['datetime'] = pd.to_datetime(data['datetime'])
    rentals_per_hour = data.groupby(data['datetime'].dt.hour)['count'].sum()
    sns.lineplot(x=rentals_per_hour.index, y=rentals_per_hour.values)
    plt.title('Bike Rentals Over Time')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Rentals')
    plt.xticks(range(24))
    plt.grid()
    plt.show()

def plot_rentals_by_season(data):
    plt.figure(figsize=(12, 6))
    data['season'] = data['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
    rentals_by_season = data.groupby('season')['count'].sum()
    sns.barplot(x=rentals_by_season.index, y=rentals_by_season.values)
    plt.title('Bike Rentals by Season')
    plt.xlabel('Season')
    plt.ylabel('Number of Rentals')
    plt.grid()
    plt.show()

def plot_rentals_by_weather(data):
    plt.figure(figsize=(12, 6))
    rentals_by_weather = data.groupby('weather')['count'].sum()
    sns.barplot(x=rentals_by_weather.index, y=rentals_by_weather.values)
    plt.title('Bike Rentals by Weather Condition')
    plt.xlabel('Weather Condition')
    plt.ylabel('Number of Rentals')
    plt.grid()
    plt.show()

def plot_correlation_matrix(data):
    plt.figure(figsize=(12, 10))
    correlation = data.corr()
    sns.heatmap(correlation, annot=True, fmt=".2f", cmap='coolwarm', square=True)
    plt.title('Correlation Matrix')
    plt.show()
"""
Get 7 days of weather using weather api
"""

import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os

#calculate dates
today = datetime.now()
week_ago_date = today -timedelta(days=7)

#format date for api as YYYY-MM-DD

start_date = week_ago_date.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

#Get city weather
longitude = 67.00
latitude = 24.86

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
response = requests.get(url)
data = response.json()

print(data)

daily_data = data["daily"]

df = pd.DataFrame({
    "date": daily_data["time"],
    "max_temp": daily_data["temperature_2m_max"],
    "min_temp": daily_data["temperature_2m_min"]
})

df["date"] = pd.to_datetime(df["date"])


plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('karachi Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('weather_chart.png')
plt.show()

if not os.path.exists("data"):
    os.makedirs("data")

df.to_csv('data/paris_weather.csv', index=False)
print("Data saved to data/paris_weather.csv")
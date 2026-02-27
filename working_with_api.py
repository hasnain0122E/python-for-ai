"""
API: application programming interface is like a 
waiter at a restaurant. You tell it what you want, 
and it brings you the data. But APIs do more than 
just fetch information. They re the bridges that 
connect your code to other systems
"""

"""
How it works:
1. You send a request to the API’s URL with parameters (like coordinates)
2. The API processes your request and finds the data
3. You receive JSON data back with the information
4. You extract the specific parts you need
"""

import requests

longitude = 67.00
latitude = 24.86

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

response = requests.get(url) 
data = response.json()

data["current"]["temperature_2m"]

print(f"tempareture in karachi is: {data["current"]["temperature_2m"]}C")


###Now working with api and function both

def get_weather(longitude, latitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
    response = requests.get(url)
    data = response.json()
    return data["current"]["temperature_2m"]

karachi_temp = get_weather(longitude=67.00, latitude=24.86)

print(f"karachi temperature: {karachi_temp}°C")
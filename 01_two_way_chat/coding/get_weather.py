# filename: get_weather.py
import requests

def get_weather(city):
    api_key = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Using metric to get temperature in Celsius
    }
    response = requests.get(base_url, params=params)
    return response.json()

cities = ['Mumbai', 'Delhi', 'Bengaluru', 'Kolkata']
weather_data = {}

for city in cities:
    weather_data[city] = get_weather(city)

for city, data in weather_data.items():
    if data.get('main'):
        print(f"Weather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Condition: {data['weather'][0]['description']}\n")
    else:
        print(f"Could not retrieve weather for {city}. Error: {data.get('message')}
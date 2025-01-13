# filename: scrape_weather_updated.py
import requests
from bs4 import BeautifulSoup

def get_weather(city):
    url = f'https://www.weather-forecast.com/locations/{city}/forecasts/latest'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Try to find the forecast using two different classes
    weather_section = soup.find('span', class_='b-forecast__table-value')
    if not weather_section:
        weather_section = soup.find('span', class_='temp')
    
    if weather_section:
        return weather_section.text.strip()
    return None

cities = ['Mumbai', 'Delhi', 'Bengaluru', 'Kolkata']
weather_data = {}

for city in cities:
    weather_data[city] = get_weather(city)

for city, temp in weather_data.items():
    if temp:
        print(f"Weather in {city}: {temp}")
    else:
        print(f"Could not retrieve weather for {city}.")
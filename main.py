import requests
import json

def input_city_name():
    city_name = input("Please enter the name of the city you'd like to know the weather of: ")
    return city_name

def show_weather_info(data):
    print(f"Here is the weather information for the city {city_name}: ")
    print(f"Temperatue: {data["temperature"]}")
    print(f"Description: {data["description"]}")
    print(f"Humidity: {data["humidity"]}")
    print(f"Wind: {data["wind"]}")
    
def fetch_api_info(city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=2c826facbf92103fc989b8b9c5e9f19f&units=metric&lang=es"
    #url1 = "https://weather.com/es-US/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"There was an issue trying to access to the weather information: {e}")
        return None
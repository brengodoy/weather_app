import requests
from typing import Dict

def input_city_name() -> str:
    while True:
        city_name = input("Please enter the name of the city you'd like to know the weather of: ")
        if any(cn.isdigit() for cn in city_name):
            print("Numbers are not a valid input.")
        else:
            break
    return city_name

def parse_weather_data(data: Dict[str,any]) -> Dict[str,any]:
    return {
		'city': data['name'],
		'temp': data['main']['temp'],
		'description': data['weather'][0]['description'],
		'humidity': data['main']['humidity'],
		'wind': data['wind']['speed']
	}

def show_weather_info(weather_info: Dict[str,any]) -> None:
    print(f"Here is the weather information for {weather_info['city']}: ")
    print(f"Temperatue: {weather_info['temp']}")
    print(f"Description: {weather_info['description']}")
    print(f"Humidity: {weather_info['humidity']}")
    print(f"Wind: {weather_info['wind']}")
    
def fetch_api_info(city_name: str):
    api_key = "2c826facbf92103fc989b8b9c5e9f19f"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=es"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data.get("cod") != 200:
            print(f"Error de API: {data.get('message', 'Error desconocido')}")
            return
        return data
    except requests.exceptions.RequestException as e:
        print(f"There was an issue trying to access to the weather information: {e}")
        return None
    
def main():
    city_name = input_city_name()
    data = fetch_api_info(city_name)
    if data:
        weather_info = parse_weather_data(data)
        show_weather_info(weather_info)
        
if __name__ == "__main__":
    main()
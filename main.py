import requests
import os

class WeatherAPIError(Exception):
    """Custom exception for API errors."""
    pass

def input_city_name() -> str:
    """Ask user for city name. This function will keep asking until a valid
    answer is given. The answer is valid if it does not contain any numbers.
    """
    while True:
        city_name = input("Please enter the name of the city you'd like to know the weather of: ")
        if any(cn.isdigit() for cn in city_name):
            print("Numbers are not a valid input.")
        else:
            break
    return city_name

def parse_weather_data(data: dict[str,any]) -> dict[str,any]:
    """Takes the data from the weather API and transforms it into a 
    dictionary with the most relevant information.
    """
    return {
		'city': data['name'],
		'temp': data['main']['temp'],
		'description': data['weather'][0]['description'],
		'humidity': data['main']['humidity'],
		'wind': data['wind']['speed']
	}

def show_weather_info(weather_info: dict[str,any]) -> None:
    """
    Displays the weather information for a given city.

    Args:
        weather_info (Dict[str, any]): A dictionary containing weather data including
                                       'city', 'temp', 'description', 'humidity', and 'wind'.

    Returns:
        None
    """
    print(f"Here is the weather information for {weather_info['city']}: ")
    print(f"Temperature: {weather_info['temp']}")
    print(f"Description: {weather_info['description']}")
    print(f"Humidity: {weather_info['humidity']}")
    print(f"Wind: {weather_info['wind']}")
    
def fetch_api_info(city_name: str):
    """
    Fetches weather information for a given city from the OpenWeatherMap API.

    Args:
        city_name (str): The name of the city for which to fetch weather data.

    Returns:
        dict: A dictionary containing weather data if the request is successful.

    Raises:
        WeatherAPIError: If the API key is missing, if there is an API error, 
                         or if there is a network error.
    """
    if not isinstance(city_name, str) or not city_name.strip():
        raise WeatherAPIError("City name must be a non-empty string.")
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise WeatherAPIError("API key is missing.")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang=es"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data.get("cod") != 200:
            raise WeatherAPIError(f"API error: {data.get('message', 'Unknown error')}")
        return data
    except requests.exceptions.RequestException as e:
        raise WeatherAPIError(f"Network error: {e}")
    
def main():
    """
    Main entry point for the script. The script does the following:
    
    1. Asks the user for the name of the city they want to know the weather of.
    2. Fetches the weather information for the given city from the 
       OpenWeatherMap API.
    3. Parses the weather data into a dictionary with the most relevant
       information.
    4. Shows the weather information to the user.
    
    If there is an error during any of these steps, the error is caught and
    shown to the user.
    """
    try:
        city_name = input_city_name()
        data = fetch_api_info(city_name)
        weather_info = parse_weather_data(data)
        show_weather_info(weather_info)
    except WeatherAPIError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
if __name__ == "__main__":
    main()
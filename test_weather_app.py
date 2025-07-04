from main import fetch_api_info,WeatherAPIError
import pytest

def test_weather_for_existing_city():
	assert fetch_api_info("New York")['cod'] == 200
 
def test_weather_for_nonexistent_city():
    pytest.raises(WeatherAPIError,fetch_api_info,"Nonexistent City")
 
def test_weather_for_empty_city():
    pytest.raises(WeatherAPIError,fetch_api_info,"")
     
def test_weather_for_null_city():
    pytest.raises(WeatherAPIError,fetch_api_info,None)
 
def test_weather_for_integer_city():
	pytest.raises(WeatherAPIError,fetch_api_info,123)
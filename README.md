# Weather App 🌦️

A simple Python app that fetches the weather of a city using the OpenWeatherMap API.  
It asks the user for the city name, retrieves the weather info, and displays it in the terminal.

## 📂 Project Structure

- `main.py`: The main script.
- `test_weather_app.py`: Unit tests using `pytest`.
- `requirements.txt`: Project dependencies.
- `README.md`: Project documentation.

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/brengodoy/weather_app.git
cd weather-app
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Set your OpenWeatherMap API key:

```bash
export OPENWEATHER_API_KEY=your_api_key_here  # On Windows: set OPENWEATHER_API_KEY=your_api_key_here
```

5. Run the application:

```bash
python main.py
```

## 🧪 Running the Tests

Tests are written using pytest.

To run the tests:

```bash
pytest
```

## 📋 Features
- ✅ Validates that the entered city name does not contain numbers.

- ✅ Fetches weather information from the OpenWeatherMap API.

- ✅ Displays temperature, description, humidity, and wind speed.

- ✅ Handles custom errors using WeatherAPIError.

- ✅ Includes unit tests for various edge cases.

## 💡 Technologies Used

- Python
- requests
- pytest

## ✨ Author
Created with lots of love by @brengodoy 💖
If you like it, please give it a star! ⭐

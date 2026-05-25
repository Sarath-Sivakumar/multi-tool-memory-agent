from datetime import datetime


def get_weather(city: str):

    weather_data = {
        "chennai": "Sunny, 34°C",
        "bangalore": "Rainy, 22°C",
        "mumbai": "Cloudy, 29°C"
    }

    return weather_data.get(
        city.lower(),
        f"No weather data for {city}"
    )


def get_current_time():

    return datetime.now().strftime("%I:%M %p")


def calculate(expression: str):

    try:
        return str(eval(expression))
    except:
        return "Invalid expression"
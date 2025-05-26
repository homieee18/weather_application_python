from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="Haryana"):
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
    weather_data = requests.get(request_url).json()
    return weather_data


if __name__ == "__main__":
    print('\n*** Get current weather conditions ***\n')
    city = input("Enter your city name: ")
    #check if string is empty or not
    if not bool(city.strip()):
        city = "Haryana"

    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)

import requests
from api_key import api_key


def print_Weather_information():
    url = 'https://api.openweathermap.org/data/2.5/weather'

    weather_params = {
        "lat":31.046051,
        "lon":34.851612,
        "appid":api_key
    }

    response = requests.get(url,params=weather_params)
    data = response.json()
    print("\n*********************************")
    print('The current weather :', data['weather'][0]['main'] ,',' ,data['weather'][0]['description'] )
    print("*********************************\n")


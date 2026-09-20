import requests


def get_city_location(city):

    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1,
        "language": "fa",
        "format": "json",
        "countryCode": "IR"
    }

    response = requests.get(url, params=params)

    data = response.json()

    if "results" not in data:
        return None

    result = data["results"][0]

    latitude = result["latitude"]
    longitude = result["longitude"]
    city_name = result["name"]

    return city_name, latitude, longitude


def get_weather(city):

    location = get_city_location(city)

    if location is None:
        return None

    city_name, latitude, longitude = location

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
        "timezone": "Asia/Tehran"
    }

    response = requests.get(url, params=params)

    data = response.json()

    temperature = data["current"]["temperature_2m"]
    wind_speed = data["current"]["wind_speed_10m"]

    return city_name, temperature, wind_speed


if __name__ == "__main__":
    city = input("Enter your city:")
    result =get_weather(city)
    print('Result:',result)

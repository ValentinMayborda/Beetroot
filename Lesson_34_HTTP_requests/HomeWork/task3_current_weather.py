import requests
import json

API_KEY = "d872599ac4b098037d26b92a22f5f09f"

def get_current_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        print(f"Getting current weather for {city}...")
        response = requests.get(url, params=params, timeout=10)
        #print(f"Response status code: {response.status_code}")
        #print(response.text)

        response.raise_for_status()
        data = response.json()

        city = data['name']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']

        print(f"\nWeather in {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Feels like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind: {wind} m/s")


    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error occurred: {e}")
    except requests.exceptions.Timeout as e:
        print(f"Request timed out: {e}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except IOError as e:
        print(f"I/O error occurred: {e}")
    return []

if __name__ == "__main__":
    get_current_weather("Kyiv")
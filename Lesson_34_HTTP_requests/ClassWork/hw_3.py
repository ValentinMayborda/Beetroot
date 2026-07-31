import requests
import json

API_KEY = ""

def get_filtered_forecast(city, temp_threshold, output_file='forecast.json'):
    url = f"https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        print(f"Getting forecast for {city}...")
        response = requests.get(url, params=params, timeout=10)
        print(f"Response status code: {response.status_code}")
        response.raise_for_status()
        data = response.json()

        # TODO: Check if the 'list' key exists in the response
        # filtered_forecast = [
        #     entry for entry in data['list']
        #     if entry['main']['temp'] > temp_threshold
        # ]
        return data

        # if not filtered_forecast:
        #     print("No forecast entries found with temperature above the threshold.")
        #     return []
        # with open(output_file, 'w') as f:
        #     json.dump(filtered_forecast, f, indent=4)
        # print(f"Forecast saved to {output_file}")
        # return filtered_forecast
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
    get_filtered_forecast("Lviv", 20)
import requests
import json

def get_weather_forecast():

    url = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=59.4370&lon=24.7536"
    
    headers = {
        'User-Agent': 'WeatherApp/1.0 github.com/trondemynde/weatherApp1.0'
    }
    
    try:
        # HTTP GET request
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            
            timeseries = data['properties']['timeseries']
            
            for entry in timeseries:
                time = entry['time']
                temp = entry['data']['instant']['details']['air_temperature']
                print(f"{time} {temp}C")
        else:
            print(f"Error: Received status code {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
    except KeyError as e:
        print(f"Error accessing data: {e}")

get_weather_forecast()
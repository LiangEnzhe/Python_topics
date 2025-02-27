import requests
import json

city = input("What city, choices are Beijing, Astana, Ankara, San Mateo: ").upper()
match city:
    case "BEIJING":
        latitude, longitude = 39.9075, 116.3972
    case "ASTANA":
        latitude, longitude = 51.3648, 67.2679
    case "ANKARA":
        latitude, longitude = 39.9199, 32.8543
    case "SAN MATEO":
        latitude, longitude = 37.563, -122.3255

response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m") 

if response.status_code == 200:
    data = response.json() 
    print(data["hourly"]["temperature_2m"][0])
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

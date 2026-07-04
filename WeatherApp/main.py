import requests
import json
import pyttsx3

city = input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=24aeeb87e99a47f7b5270522260307&q={city}"

r = requests.get(url)
print(r.json())

wdic = json.loads(r.text)
current = wdic['current']

# Extract available weather data
temp_c = current['temp_c']
condition = current['condition']['text']
humidity = current['humidity']
wind_kph = current['wind_kph']
feels_like = current['feelslike_c']
visibility = current['vis_km']
pressure = current['pressure_mb']

# Build concise message with all info
message = f"In {city}: {temp_c}°C, feels like {feels_like}°C, {condition}. Humidity {humidity}%, wind {wind_kph} km/h, visibility {visibility} km, pressure {pressure} mb."

print(message)

# Use RoboSpeaker to read the message
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 150)
engine.say(message)
engine.runAndWait()

#Example of requesting JSON data.
#In this example, we are going to request the data from weather API.
#we are going to use free weather API from weatherapi.com

import requests

city = input("Enter the city name to get the current weather: ")
url = "http://api.weatherapi.com/v1/current.json?key=dc0723efd0334eb29ea214132261001&q=" + city + "&aqi=no"
response = requests.get(url)

json = response.json()

print("City Name:", json.get("location").get("name"))
print("The Current Temperature in", json.get("location").get("name"), " is",json.get("current").get("temp_c"), "°C", "and it is", json.get("current").get("condition").get("text"), "today.", sep=" ")
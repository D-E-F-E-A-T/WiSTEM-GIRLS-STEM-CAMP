import requests
import math

def get_condition(city):
    url = "https://api.openweathermap.org/data/2.5/weather?q="
    key = "&APPID=3c12cca1f1ba8a664ef15e1c19ade2ce"
    
    query = url + city + key
    response = requests.get(query)
    main = response.json()["weather"][0]["main"]
    description = response.json()["weather"][0]["description"]
    temp = response.json()["main"]["temp"]
    temp_c = (temp - 273.15) 
    temp_c = math.floor(temp_c)
    
    return ("Current weather for " + city + ": " + main + ", " +  description + ", " + str(temp_c) + " degree celsius")
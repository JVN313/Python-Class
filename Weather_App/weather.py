import requests
api_key  = "9592393e8425b8bc86c480303b0cb94f"
city = input("What City?: ").capitalize()
url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"
request = requests.get(url)
json = request.json()
#print(json)
json_write = open("weather.json","w")
json_write.write(str(json))
weather_temps= json.get("main")
weather_feel = weather_temps.get("feels_like")
weather = json.get("weather")
weather_description = weather[0].get("description")
print(weather_description)
print(weather_feel)
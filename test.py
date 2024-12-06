import requests
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY ="tôi sẽ nhập api của tôi sau"
CITY ="Nha Trang"
def kelvin_to_celcius(kelvin):
    celsius = kelvin - 273.15
    return celsius
url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()
temp_kelvin = response['main']['temp']
temp_celcius = kelvin_to_celcius(temp_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
print(f"Nhiệt độ ở {CITY}: {temp_celcius: .2f} °C")
print(f"Độ ẩm ở {CITY}: {humidity}%")
print(f"Tốc độ gió ở {CITY}: {wind_speed}m/s")

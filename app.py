import requests


city = input('Enter a valid city: ')
city_format = city.lower()
city_format = city.replace(' ', '+')
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=e9926d9cabaa85df3a3592b64a40691b&units=imperial'.format(city_format)

request = requests.get(url)

data = request.json()

print(request)

print(data)

print(url)

print('*~*~*~*~*~*~*~*')
# variable storage
temp = int(data['main']['temp'])
wind_speed = data['wind']['speed']
wind_dir = data['wind']['deg']
humidity = data['main']['humidity']
high = int(data['main']['temp_max'])
low = int(data['main']['temp_min'])
latitude = data['coord']['lat']
longitude = data['coord']['lon']


def wind_direction_convert(degree):
    """Takes in the variable wind_dir and converts the numeric value to its corresponding cardinal direction IN PROGRESS"""
    if degree >= 340.001 or degree <= 20:
        wind_direction = 'North'
    elif degree >= 20.001 and degree <= 40:
        wind_direction = 'North/Northeast'
    elif degree >= 40.001 and degree <= 60:
        wind_direction = 'Northeast'
    elif degree >= 60.001 and degree <= 80:
        wind_direction = 'East/Northeast'
    else:
        wind_direction = 'North/Northwest'
    return wind_direction


print('*~*~*~' + city + '~*~*~*')
print('The current temperature is: ' + str(temp) + ' Fahrenheit')
print('The local high is: ' + str(high) + ' Fahrenheit')
print('The local low is: ' + str(low) + ' Fahrenheit')
print('The wind speed is: ' + str(wind_speed) + ' mph')
print('The wind direction is: ' + wind_direction_convert(wind_dir))
print('The humidity is: ' + str(humidity) + '%')
print('The locational coordinates for %s are: (%.2f, %.2f)' % (city, latitude, longitude))

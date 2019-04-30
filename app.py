import requests


city = input('Enter a valid city: ')
city_format = city.lower()
city_format = city.replace(' ', '+')
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=e9926d9cabaa85df3a3592b64a40691b&units=imperial'.format(city_format)

request = requests.get(url)

request_string = str(requests.get(url))

# Converts the request value into a base 3 digit error code for error handling
error = int(request_string[-5:-2])
# print(error)
if error == 404:
    print("You didn't enter a valid city name!")
    quit()

data = request.json()

print(request)
# print(data)
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
    """Takes in the variable wind_dir and converts the numeric value to its corresponding cardinal direction"""
    if degree >= 337.501 or degree <= 22.5:
        wind_direction = 'North'
    elif degree >= 22.501 and degree <= 65.5:
        wind_direction = 'Northeast'
    elif degree >= 65.501 and degree <= 112.5:
        wind_direction = 'East'
    elif degree >= 112.501 and degree <= 157.5:
        wind_direction = 'Southeast'
    elif degree >= 157.501 and degree <= 202.5:
        wind_direction = 'South'
    elif degree >= 202.501 and degree <= 247.5:
        wind_direction = 'Southwest'
    elif degree >= 247.501 and degree <= 292.5:
        wind_direction = 'West'
    else:
        wind_direction = 'Northwest'
    return wind_direction


print('*~*~*~' + city + '~*~*~*')
print('The current temperature is: ' + str(temp) + ' Fahrenheit')
print('The local high is: ' + str(high) + ' Fahrenheit')
print('The local low is: ' + str(low) + ' Fahrenheit')
print('The wind speed is: ' + str(wind_speed) + ' mph')
print('The wind direction is: ' + wind_direction_convert(wind_dir))
print('The humidity is: ' + str(humidity) + '%')
print('The locational coordinates for %s are: (%.2f, %.2f)' % (city, latitude, longitude))

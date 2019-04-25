import requests


city = input('Enter a valid city: ')
city = city.lower()
city = city.replace(' ', '+')
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=e9926d9cabaa85df3a3592b64a40691b&units=imperial'.format(city)

request = requests.get(url)

data = request.json()

# print(request)
#
# print(data)
#
print(url)

print('*~*~*~*~*~*~*~*')
# variable storage
temp = data['main']['temp']
wind_speed = data['wind']['speed']

print('The temperature in ' + city + ' is: ' + str(temp) + ' Farenheit')
print('The windspeed is: ' + str(wind_speed) + ' mph')

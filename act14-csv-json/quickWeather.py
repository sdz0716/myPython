#! python3
# quickWeather.py - prints the weather for a location from the command line

import json
import requests
import pprint
# import sys

# location = ' '.join(sys.argv[1:])
res = requests.get('http://api.openweathermap.org/data/2.5/weather?id=1792947&APPID=d952091b0b7436dd4ca5fa9f72547bf0')

weatherData = json.loads(res.text)
# w = weatherData['list']
print(pprint.pformat(weatherData))

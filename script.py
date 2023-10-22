import pprint
import requests
from matplotlib import pyplot as plt
from datetime import datetime

API_URL = 'https://weather-api-node-wisc.herokuapp.com/weather/'
city = 'seattle' # feel free to enter your own city here!
r = requests.get(API_URL + city)
response = r.json()
print(response)

import requests
import sys
from flask import Flask
from flask_bootstrap import Bootstrap

# FLASK TO BOOTSTRAP
def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app

# apiKey = '2b8741e06538e78e887ffe56f1715616'
apiKey = '8ef257c3d948ead6db20e66823605d71'
userInput = 'Pittsburgh' # input("Enter a city: ")
print(userInput)

weatherData = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={userInput}&units=imperial&APPID={apiKey}")
status = weatherData.status_code
if status == 200:
    print("Successful API access!")
else:
    print("Could not access API.")

# print(weatherData.json())

if weatherData.json()['cod'] == '404':
    print("No City Found")
    sys.exit()

# CONDITION
conditions = {2:'Thunderstorm', 3:'Drizzle', 5:'Rain', 6:'Snow', 7:'Atmosphere', 800:'Clear', 8:'Clouds'}
cond = weatherData.json()['weather'][0]['id']
condition = "Today's conditions:"
if cond == 800:
    num = 800
else:
    num = int(str(cond)[0])
print(condition, conditions[num])
temp = weatherData.json()['main']['temp']

# TEMPERATURE
if temp < 30:
    msg = "It's " + str(int(temp)) + " degrees Farenheit. That's cold!"
elif temp < 50:
    msg = "It's " + str(int(temp)) + " degrees Farenheit. That's chilly!"
elif temp < 70:
    msg = "It's " + str(int(temp)) + " degrees Farenheit. That's moderate!"
elif temp < 90:
    msg = "It's " + str(int(temp)) + " degrees Farenheit. That's hot!"
elif temp >= 90:
    msg = "It's " + str(int(temp)) + " degrees Farenheit. That's scorching!"
print(msg)

# OUTFITS
# 1: <30
# 2: 30-50
# 3: 50-70
# 4: 70-90
# 5: >90
tops = {}

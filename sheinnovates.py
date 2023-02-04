import requests
import sys
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

def get_outfit(city, occasion):
    # apiKey = '8ef257c3d948ead6db20e66823605d71'
    apiKey = '2b8741e06538e78e887ffe56f1715616'
    # userInput = 'Pittsburgh' # input("Enter a city: ")
    # print(userInput)

    weatherData = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={apiKey}")
    status = weatherData.status_code
    if status == 200:
        print("Successful API access!")
    else:
        print("Could not access API.")

    # print(weatherData.json())

    if weatherData.json()['cod'] == '404':
        print("No City Found")
        return ("Invalid City", None)

    # CONDITION
    conditions = {2:'Thunderstorm', 3:'Drizzle', 5:'Rain', 6:'Snow', 7:'Atmosphere', 800:'Clear', 8:'Clouds'}
    cond = weatherData.json()['weather'][0]['id']
    condition = "Today's conditions:"
    if cond == 800:
        num = 800
    else:
        num = int(str(cond)[0])
    weather_type = conditions[num]
    print(condition, weather_type)

    # TEMPERATURE
    temp = weatherData.json()['main']['temp']
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
    return (str(int(temp)) + "F", weather_type) # and outfit

###################################################
###################################################
###################################################

# FLASK TO HTML
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/city', methods=['GET','POST'])
def find_city():
    if request.method == 'POST':
        city = request.form.get('city')
        occasion = request.form.get('occasion')
        print("City:", city)
        temperature, conditions = get_outfit(city, occasion) # and outfit
        # return "This is the city: " + city
        if temperature == "Invalid City":
            return render_template('display.html', city = temperature, temp = "", cond = "") # outfit = "Cannot choose outfit"
        return render_template('display.html', city = city, temp = temperature, cond = conditions) # outfit = outfit

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


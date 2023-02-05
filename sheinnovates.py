import requests
import sys
import random
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

def get_outfit(city, option):
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
        return ("Invalid City", None, None)

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
    casTops = {'cold':{1: "thermal top", 2:"sweater",},
        'chilly':{3:'long sleeve top'},
        'moderate':{4:'half sleeve top',},
        'hot':{5:'half sleeve top',6:'tank top',},
        'scorching':{7:'half sleeve top',8:'tank top',}}

    fancyTops = {'cold':{1:"sweater", 2:'turtleneck'},
            
        'chilly':{1:'sweater', 2:'blouse',},

        'moderate':{1:'blouse'},

        'hot':{1:'half sleeve blouse', 2:'dressy tank top',},

        'scorching':{1:'half sleeve blouse', 2:'dressy tank top',}}

    profTop = {'cold':{1:"sweater", 2:'turtleneck'}, 
            
        'chilly':{1:'sweater', 2:'blouse', 3:'button-up top'},

        'moderate':{1:'blouse', 2:'button-up top'},

        'hot':{1:'half sleeve blouse', 2:'dressy tank top',},

        'scorching':{1:'half sleeve blouse', 2:'dressy tank top',}}

    athTops = {'cold':{6:'sweatshirt',},
        
        'chilly':{6:'sweatshirt', 7:'long sleeve compression',},

        'moderate':{1:'blouse', 7:'long sleeve compression', 9:'atheltic short sleeve',},

        'hot':{1:'half sleeve blouse', 2:'dressy tank top', 9:'atheltic short sleeve', 10:'athletic tank top'},

        'scorching':{9:'atheltic short sleeve',10:'athletic tank top', 11:"honestly, it's hot enough, just wear a sports bra!"}}

# BOTTOMS BOTTOMS BOTTOMS BOTTOMS BOTTOMS 

    casBottoms = {'cold':{1:'jeans ', 2:'courdory pants',},
            
        'chilly':{8:'jeans', 2:'courdory pants'},

        'moderate':{1:'jeans', 2:' jean shorts',},

        'hot':{1:'jean shorts', 4:'flowy shorts',},

        'scorching':{1:'jean shorts',4:'flowy shorts',}}

    fancyBottoms = {'cold':{1:'leather pants', 2:'maxi skirt',},
                
        'chilly':{8:'leather pants'},

        'moderate':{1:'maxi skirt', 2:'tailored pants', 3:'leather pants'},

        'hot':{1:'mini skirt', 4:'tailored pants',},

        'scorching':{1:'mini skirt',4:'tailored shorts',}}

    athBottoms = {'cold':{1:'windproof pants', 2:'fleece lined leggings',},

        'chilly':{8:'sweatpants', 1:'lounge pants', 2:'leggings', 3:'yoga pants'},

        'moderate':{8:'sweatpants', 1:'lounge pants', 2:'leggings', 3:'yoga pants', 4:'sweatshorts'},

        'hot':{1:'sweatshorts',4:'atheltic shorts'},

        'scorching':{1:'atheltic shorts'}}

    profBottoms = {'cold':{1:'dress pants', 2:'plaid trousers', 3:'chinos', 4:'slacks'},
        'chilly':{1:'dress pants', 2:'plaid trousers', 3:'chinos', 4:'slacks'},
        'moderate':{1:'dress pants', 2:'plaid trousers', 3:'chinos', 4:'slacks'},
        'hot':{1:'dress pants', 2:'plaid trousers', 3:'chinos', 4:'slacks'},
        'scorching':{1:'dress pants', 2:'plaid trousers', 3:'chinos', 4:'slacks'}}

# OUTERWEAR OUTERWEAR OUTERWEAR

    casOut = {'cold':{1:'winter puffer', 2:'sherpa jacket'},
            'chilly':{8:'winter puffer'},
            'moderate':{1:'jean jacket', 2:'cardigan'},
            'hot':{1:'no outerwear needed!'},
            'scorching':{1:'no outerwear needed!'}}


    fancyOut = {'cold':{1:'trench coat', 2:'fur overcoat',},
            'chilly':{8:'sherpa lined coat', 3:'trench coat'},
            'moderate':{1:'leather jacket',},
            'hot':{1:'no outerwear needed!'},
            'scorching':{1:'no outerwear needed!'}}


    athOut = {'cold':{1:'winter puffer'},
            'chilly':{8:'winter puffer'},
            'moderate':{1:'windbreaker',},
            'hot':{1:'no outerwear needed!'},
            'scorching':{1:'no outerwear needed!'}}


    profOut = {'cold':{1:'trench coat', 2:'fur overcoat',},
            'chilly':{8:'sherpa lined coat', 2:'trench coat'},
            'moderate':{1:'blazer',},
            'hot':{1:'no outerwear needed!'},
            'scorching':{1:'no outerwear needed!'}}

    # SHOES SHOES SHOES SHOES SHOES SHOES 

    casShoes = {'cold':{1:'combat boots ', 2:'white sneakers',3:'hightop sneakers', 4:'uggs'},
            'chilly':{8:'combat boots', 2:'white sneakers', 3:'hightop sneakers', 4:'uggs'},
            'moderate':{1:'white sneakers',2:'hightop sneakers', 3:'sandals'},
            'hot':{1:'white sneakers',2:'hightop sneakers', 3:'sandals', 4:'flip flops'},
            'scorching':{1:'white sneakers',2:'hightop sneakers', 3:'sandals', 4:'flip flops'}}

    fancyShoes = {'cold':{1:'knee high boots', 2:'booties',},
            'chilly':{8:'booties'},
            'moderate':{1:'booties',2:'heels'},
            'hot':{1:'heels',4:'flats',2:'wedge sandals'},
            'scorching':{1:'heels',4:'flats',2:'wedge sandals'}}

    athShoes = {'cold':{1:'running shoes',2:'white sneakers'}, 3:'waterproof boots',
            'chilly':{1:'running shoes',2:'white sneakers'},
            'moderate':{1:'running shoes',2:'white sneakers'},
            'hot':{1:'running shoes',2:'white sneakers'},
            'scorching':{1:'running shoes',2:'white sneakers'}}

    # ACC ACC ACC ACC  ACC  ACC

    casAcc = {'cold':{1:'beanie', 2:'mittens'},
            'chilly':{8:'beanie', 9:'baseball cap'},
            'moderate':{1:'baseball cap',2:'tote bag'},
            'hot':{1:'baseball cap', 2:'tote bag', 3:'sunglasses'},
            'scorching':{1:'baseball cap', 2:'tote bag', 3:'sunglasses'}}

    fancyAcc = {'cold':{1:'scarf', 2:'leather gloves', 3:'earmuffs'},
            'chilly':{8:'scarf'},
            'moderate':{1:'purse',},
            'hot':{1:'purse',4:'watch',},
            'scorching':{1:'purse',4:'watch',}}

    athAcc = {'cold':{1:'beanie', 2:'earmuffs', 3:'thermal socks'},
            'chilly':{8:'beanie', 9:'baseball cap'},
            'moderate':{1:'belt bag',},
            'hot':{1:'belt bag'},
            'scorching':{1:'belt bag'}}

    # option = (input('''Select Style Option:
    # 1) Casual 
    # 2) Athletic / Leisure 
    # 3) Professional
    # 4) Fancy
    # 5) Quit 
    # Type your choice: '''))
    random_value = "" 
    random_value2 = "" 
    random_value3 = "" 
    random_value4 = "" 
    random_value5 = "" 

    if option == "Casual":
        print("You chose Casual. Generating outfit...")
        if temp < 30:
            first_lvl_key = 'cold'
            random_top = random.choice(list(casTops[first_lvl_key].keys()))
            random_value = casTops[first_lvl_key][random_top]
            randB = random.choice(list(casBottoms[first_lvl_key].keys()))
            random_value2 = casBottoms[first_lvl_key][randB]
            randS = random.choice(list(casShoes[first_lvl_key].keys()))
            random_value3 = casShoes[first_lvl_key][randS]
            randA = random.choice(list(casAcc[first_lvl_key].keys()))
            random_value4 = casAcc[first_lvl_key][randA]
            randO = random.choice(list(casOut[first_lvl_key].keys()))
            random_value5 = casOut[first_lvl_key][randO]
            print(f'Outit: {random_value} + {random_value2} + {random_value3} + {random_value4} + {random_value5}')
            
            
        elif temp < 50:
            first_lvl_key = 'chilly'
            random_top = random.choice(list(casTops[first_lvl_key].keys()))
            random_value = casTops[first_lvl_key][random_top]
            randB = random.choice(list(casBottoms[first_lvl_key].keys()))
            random_value2 = casBottoms[first_lvl_key][randB]
            randS = random.choice(list(casShoes[first_lvl_key].keys()))
            random_value3 = casShoes[first_lvl_key][randS]
            randA = random.choice(list(casAcc[first_lvl_key].keys()))
            random_value4 = casAcc[first_lvl_key][randA]
            randO = random.choice(list(casOut[first_lvl_key].keys()))
            random_value5 = casOut[first_lvl_key][randO]
            print(f'Outit: {random_value} + {random_value2} + {random_value3} + {random_value4} + {random_value5}')

        elif temp < 70:
            first_lvl_key = 'moderate'
            random_top = random.choice(list(casTops[first_lvl_key].keys()))
            random_value = casTops[first_lvl_key][random_top]
            randB = random.choice(list(casBottoms[first_lvl_key].keys()))
            random_value2 = casBottoms[first_lvl_key][randB]
            randS = random.choice(list(casShoes[first_lvl_key].keys()))
            random_value3 = casShoes[first_lvl_key][randS]
            randA = random.choice(list(casAcc[first_lvl_key].keys()))
            random_value4 = casAcc[first_lvl_key][randA]
            randO = random.choice(list(casOut[first_lvl_key].keys()))
            random_value5 = casOut[first_lvl_key][randO]
            print(f'Outit: {random_value} + {random_value2} + {random_value3} + {random_value4} + {random_value5}')

        elif temp < 90:
            first_lvl_key = 'hot'
            random_top = random.choice(list(casTops[first_lvl_key].keys()))
            random_value = casTops[first_lvl_key][random_top]
            randB = random.choice(list(casBottoms[first_lvl_key].keys()))
            random_value2 = casBottoms[first_lvl_key][randB]
            randS = random.choice(list(casShoes[first_lvl_key].keys()))
            random_value3 = casShoes[first_lvl_key][randS]
            randA = random.choice(list(casAcc[first_lvl_key].keys()))
            random_value4 = casAcc[first_lvl_key][randA]
            randO = random.choice(list(casOut[first_lvl_key].keys()))
            random_value5 = casOut[first_lvl_key][randO]
            print(f'Outit: {random_value} + {random_value2} + {random_value3} + {random_value4} + {random_value5}')

        elif temp >= 90:
            first_lvl_key = 'scorching'
            random_top = random.choice(list(casTops[first_lvl_key].keys()))
            random_value = casTops[first_lvl_key][random_top]
            randB = random.choice(list(casBottoms[first_lvl_key].keys()))
            random_value2 = casBottoms[first_lvl_key][randB]
            randS = random.choice(list(casShoes[first_lvl_key].keys()))
            random_value3 = casShoes[first_lvl_key][randS]
            randA = random.choice(list(casAcc[first_lvl_key].keys()))
            random_value4 = casAcc[first_lvl_key][randA]
            randO = random.choice(list(casOut[first_lvl_key].keys()))
            random_value5 = casOut[first_lvl_key][randO]
            print(f'Outit: {random_value} + {random_value2} + {random_value3} + {random_value4} + {random_value5}')

    elif option == "Athletic/Leisure":
        if temp < 30:
            first_lvl_key = 'chilly'
            random_top = random.choice(list(athTops[first_lvl_key].keys()))
            random_value = athTops[first_lvl_key][random_top]
            randB = random.choice(list(athBottoms[first_lvl_key].keys()))
            random_value2 = athBottoms[first_lvl_key][randB]
            randS = random.choice(list(athShoes[first_lvl_key].keys()))
            random_value3 = athShoes[first_lvl_key][randS]
            randA = random.choice(list(athAcc[first_lvl_key].keys()))
            random_value4 = athAcc[first_lvl_key][randA]
            randO = random.choice(list(athOut[first_lvl_key].keys()))
            random_value5 = athOut[first_lvl_key][randO]
            print(f'Outit: {random_value} + {random_value2} + {random_value3} + {random_value4} + {random_value5}')

        elif temp < 50:
            first_lvl_key = 'chilly'
            random_top = random.choice(list(athTops[first_lvl_key].keys()))
            random_value = athTops[first_lvl_key][random_top]
            randB = random.choice(list(athBottoms[first_lvl_key].keys()))
            random_value2 = athBottoms[first_lvl_key][randB]
            randS = random.choice(list(athShoes[first_lvl_key].keys()))
            random_value3 = athShoes[first_lvl_key][randS]
            randA = random.choice(list(athAcc[first_lvl_key].keys()))
            random_value4 = athAcc[first_lvl_key][randA]
            randO = random.choice(list(athOut[first_lvl_key].keys()))
            random_value5 = athOut[first_lvl_key][randO]
            print(f'Outit: {random_value} + {random_value2} + {random_value3} + {random_value4} + {random_value5}')

        elif temp < 70:
            first_lvl_key = 'moderate'
            random_top = random.choice(list(athTops[first_lvl_key].keys()))
            random_value = athTops[first_lvl_key][random_top]
            randB = random.choice(list(athBottoms[first_lvl_key].keys()))
            random_value2 = athBottoms[first_lvl_key][randB]
            randS = random.choice(list(athShoes[first_lvl_key].keys()))
            random_value3 = athShoes[first_lvl_key][randS]
            randA = random.choice(list(athAcc[first_lvl_key].keys()))
            random_value4 = athAcc[first_lvl_key][randA]
            randO = random.choice(list(athOut[first_lvl_key].keys()))
            random_value5 = athOut[first_lvl_key][randO]
            print(f'Outit: {random_value} + {random_value2} + {random_value3} + {random_value4} + {random_value5}')

        elif temp < 90:
            first_lvl_key = 'hot'
            random_top = random.choice(list(athTops[first_lvl_key].keys()))
            random_value = athTops[first_lvl_key][random_top]
            randB = random.choice(list(athBottoms[first_lvl_key].keys()))
            random_value2 = athBottoms[first_lvl_key][randB]
            randS = random.choice(list(athShoes[first_lvl_key].keys()))
            random_value3 = athShoes[first_lvl_key][randS]
            randA = random.choice(list(athAcc[first_lvl_key].keys()))
            random_value4 = athAcc[first_lvl_key][randA]
            randO = random.choice(list(athOut[first_lvl_key].keys()))
            random_value5 = athOut[first_lvl_key][randO]
            print(f'Outit: {random_value} + {random_value2} + {random_value3} + {random_value4} + {random_value5}')

        elif temp >= 90:
            first_lvl_key = 'scorching'
            random_top = random.choice(list(athTops[first_lvl_key].keys()))
            random_value = athTops[first_lvl_key][random_top]
            randB = random.choice(list(athBottoms[first_lvl_key].keys()))
            random_value2 = athBottoms[first_lvl_key][randB]
            randS = random.choice(list(athShoes[first_lvl_key].keys()))
            random_value3 = athShoes[first_lvl_key][randS]
            randA = random.choice(list(athAcc[first_lvl_key].keys()))
            random_value4 = athAcc[first_lvl_key][randA]
            randO = random.choice(list(athOut[first_lvl_key].keys()))
            random_value5 = athOut[first_lvl_key][randO]
            print(f'Outit: {random_value} + {random_value2} + {random_value3} + {random_value4} + {random_value5}')

    elif option == "Professional":
        print("You chose Professional. Generating outfit...")
        if temp < 30:
            first_lvl_key = 'chilly'
            random_top = random.choice(list(profTop[first_lvl_key].keys()))
            random_value = profTop[first_lvl_key][random_top]
            randB = random.choice(list(profBottoms[first_lvl_key].keys()))
            random_value2 = profBottoms[first_lvl_key][randB]
            randS = random.choice(list(fancyShoes[first_lvl_key].keys()))
            random_value3 = fancyShoes[first_lvl_key][randS]
            randA = random.choice(list(fancyAcc[first_lvl_key].keys()))
            random_value4 = fancyAcc[first_lvl_key][randA]
            randO = random.choice(list(profOut[first_lvl_key].keys()))
            random_value5 = profOut[first_lvl_key][randO]
            print(f'Outit: {random_value} + {random_value2} + {random_value3} + {random_value4} + {random_value5}')

        elif temp < 50:
            first_lvl_key = 'chilly'
            random_top = random.choice(list(profTop[first_lvl_key].keys()))
            random_value = profTop[first_lvl_key][random_top]
            randB = random.choice(list(profBottoms[first_lvl_key].keys()))
            random_value2 = profBottoms[first_lvl_key][randB]
            randS = random.choice(list(fancyShoes[first_lvl_key].keys()))
            random_value3 = fancyShoes[first_lvl_key][randS]
            randA = random.choice(list(fancyAcc[first_lvl_key].keys()))
            random_value4 = fancyAcc[first_lvl_key][randA]
            randO = random.choice(list(profOut[first_lvl_key].keys()))
            random_value5 = profOut[first_lvl_key][randO]
            print(f'Outit: {random_value} + {random_value2} + {random_value3} + {random_value4} + {random_value5}')
        elif temp < 70:
            first_lvl_key = 'moderate'
            random_top = random.choice(list(profTop[first_lvl_key].keys()))
            random_value = profTop[first_lvl_key][random_top]
            randB = random.choice(list(profBottoms[first_lvl_key].keys()))
            random_value2 = profBottoms[first_lvl_key][randB]
            randS = random.choice(list(fancyShoes[first_lvl_key].keys()))
            random_value3 = fancyShoes[first_lvl_key][randS]
            randA = random.choice(list(fancyAcc[first_lvl_key].keys()))
            random_value4 = fancyAcc[first_lvl_key][randA]
            randO = random.choice(list(profOut[first_lvl_key].keys()))
            random_value5 = profOut[first_lvl_key][randO]
            print(f'Outit: {random_value} + {random_value2} + {random_value3} + {random_value4} + {random_value5}')

        elif temp < 90:
            first_lvl_key = 'hot'
            random_top = random.choice(list(profTop[first_lvl_key].keys()))
            random_value = profTop[first_lvl_key][random_top]
            randB = random.choice(list(profBottoms[first_lvl_key].keys()))
            random_value2 = profBottoms[first_lvl_key][randB]
            randS = random.choice(list(fancyShoes[first_lvl_key].keys()))
            random_value3 = fancyShoes[first_lvl_key][randS]
            randA = random.choice(list(fancyAcc[first_lvl_key].keys()))
            random_value4 = fancyAcc[first_lvl_key][randA]
            randO = random.choice(list(profOut[first_lvl_key].keys()))
            random_value5 = profOut[first_lvl_key][randO]
            print(f'Outit: {random_value} + {random_value2} + {random_value3} + {random_value4} + {random_value5}')

        elif temp >= 90:
            first_lvl_key = 'scorching'
            random_top = random.choice(list(profTop[first_lvl_key].keys()))
            random_value = profTop[first_lvl_key][random_top]
            randB = random.choice(list(profBottoms[first_lvl_key].keys()))
            random_value2 = profBottoms[first_lvl_key][randB]
            randS = random.choice(list(fancyShoes[first_lvl_key].keys()))
            random_value3 = fancyShoes[first_lvl_key][randS]
            randA = random.choice(list(fancyAcc[first_lvl_key].keys()))
            random_value4 = fancyAcc[first_lvl_key][randA]
            randO = random.choice(list(profOut[first_lvl_key].keys()))
            random_value5 = profOut[first_lvl_key][randO]
            print(f'Outit: {random_value} + {random_value2} + {random_value3} + {random_value4} + {random_value5}')

    elif option =="Fancy":
        print("You chose Fancy. Generating outfit...")
        if temp < 30:
            first_lvl_key = 'chilly'
            random_top = random.choice(list(fancyTops[first_lvl_key].keys()))
            random_value = fancyTops[first_lvl_key][random_top]
            randB = random.choice(list(fancyBottoms[first_lvl_key].keys()))
            random_value2 = fancyBottoms[first_lvl_key][randB]
            randS = random.choice(list(fancyShoes[first_lvl_key].keys()))
            random_value3 = fancyShoes[first_lvl_key][randS]
            randA = random.choice(list(fancyAcc[first_lvl_key].keys()))
            random_value4 = fancyAcc[first_lvl_key][randA]
            randO = random.choice(list(fancyOut[first_lvl_key].keys()))
            random_value5 = fancyOut[first_lvl_key][randO]
            print(f'Outit: {random_value} + {random_value2} + {random_value3} + {random_value4} + {random_value5}')

        elif temp < 50:
            first_lvl_key = 'chilly'
            random_top = random.choice(list(fancyTops[first_lvl_key].keys()))
            random_value = fancyTops[first_lvl_key][random_top]
            randB = random.choice(list(fancyBottoms[first_lvl_key].keys()))
            random_value2 = fancyBottoms[first_lvl_key][randB]
            randS = random.choice(list(fancyShoes[first_lvl_key].keys()))
            random_value3 = fancyShoes[first_lvl_key][randS]
            randA = random.choice(list(fancyAcc[first_lvl_key].keys()))
            random_value4 = fancyAcc[first_lvl_key][randA]
            randO = random.choice(list(fancyOut[first_lvl_key].keys()))
            random_value5 = fancyOut[first_lvl_key][randO]
            print(f'Outit: {random_value} + {random_value2} + {random_value3} + {random_value4} + {random_value5}')

        elif temp < 70:
            first_lvl_key = 'moderate'
            random_top = random.choice(list(fancyTops[first_lvl_key].keys()))
            random_value = fancyTops[first_lvl_key][random_top]
            randB = random.choice(list(fancyBottoms[first_lvl_key].keys()))
            random_value2 = fancyBottoms[first_lvl_key][randB]
            randS = random.choice(list(fancyShoes[first_lvl_key].keys()))
            random_value3 = fancyShoes[first_lvl_key][randS]
            randA = random.choice(list(fancyAcc[first_lvl_key].keys()))
            random_value4 = fancyAcc[first_lvl_key][randA]
            randO = random.choice(list(fancyOut[first_lvl_key].keys()))
            random_value5 = fancyOut[first_lvl_key][randO]
            print(f'Outit: {random_value} + {random_value2} + {random_value3} + {random_value4} + {random_value5}')

        elif temp < 90:
            first_lvl_key = 'hot'
            random_top = random.choice(list(fancyTops[first_lvl_key].keys()))
            random_value = fancyTops[first_lvl_key][random_top]
            randB = random.choice(list(fancyBottoms[first_lvl_key].keys()))
            random_value2 = fancyBottoms[first_lvl_key][randB]
            randS = random.choice(list(fancyShoes[first_lvl_key].keys()))
            random_value3 = fancyShoes[first_lvl_key][randS]
            randA = random.choice(list(fancyAcc[first_lvl_key].keys()))
            random_value4 = fancyAcc[first_lvl_key][randA]
            randO = random.choice(list(fancyOut[first_lvl_key].keys()))
            random_value5 = fancyOut[first_lvl_key][randO]
            print(f'Outit: {random_value} + {random_value2} + {random_value3} + {random_value4} + {random_value5}')

        elif temp >= 90:
            first_lvl_key = 'scorching'
            random_top = random.choice(list(fancyTops[first_lvl_key].keys()))
            random_value = fancyTops[first_lvl_key][random_top]
            randB = random.choice(list(fancyBottoms[first_lvl_key].keys()))
            random_value2 = fancyBottoms[first_lvl_key][randB]
            randS = random.choice(list(fancyShoes[first_lvl_key].keys()))
            random_value3 = fancyShoes[first_lvl_key][randS]
            randA = random.choice(list(fancyAcc[first_lvl_key].keys()))
            random_value4 = fancyAcc[first_lvl_key][randA]
            randO = random.choice(list(fancyOut[first_lvl_key].keys()))
            random_value5 = fancyOut[first_lvl_key][randO]
            print(f'Outit: {random_value} + {random_value2} + {random_value3} + {random_value4} + {random_value5}')
    
    outfit = random_value.capitalize() + " + " + random_value2.capitalize() + " + " + random_value3.capitalize() + " + " + random_value4.capitalize() + " + " + random_value5.capitalize()
 
###################################################
###################################################

    return (str(int(temp)) + "F", weather_type, outfit) 

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
        temperature, conditions, outfit = get_outfit(city, occasion) # and outfit
        # return "This is the city: " + city
        if temperature == "Invalid City":
            return render_template('display.html', city = temperature, temp = "", cond = "", outfit = "Cannot choose outfit")
        return render_template('display.html', city = city.title(), temp = temperature, cond = conditions, outfit = outfit)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


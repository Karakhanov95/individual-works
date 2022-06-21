countries = {
    'Uzbekistan':{
        'capital':'Tashkent',
        'area':448978,
        'population':35_300_000,
        'currency':'Uzbek so\'m'
        },
    
    'Russia':{
        'capital':'Moscow',
        'area':17098246,
        'population':145_478_097,
        'currency':'Russian rubl'
        },
    
    'USA':{
        'capital':'Washington',
        'area':9631418,
        'population':331_893_745,
        'currency':'American dollar'
        },
    
    'UAE':{
        'capital':'Abu-Dhabi',
        'area':83600,
        'population':9_282_410,
        'currency':'UAE dirham'
        }
    }

print('We have information about those countries in below: ')
for country in countries:
    print(country)

country_0 = input('Which country do you want to know about:>>>>>\n')
if country_0 in countries:
    info = countries[country_0]
    print(f"\n{country_0}'s capital is {info['capital']} "
          f"\n Area: {info['area']} kv.km"
          f"\n Population: {info['population']} "
          f"\n Currency: {info['currency']} ")

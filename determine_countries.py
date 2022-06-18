countries_0 = {
    'USA':'Washignton',
    'Russia':'Moscow',
    'Uzbekistan':'Tashkent',
    'Tajikistan':'Dushanbe',
    'Canada':'Ottawa',
    'Germany':'Berlin',
    'Japan':'Tokyo',
    'Iran':'Tehran',
    'UAE':'Abu-Dhabi'
    }

ask_q = input('Please choose any country: ')
country = countries_0.get(ask_q)
if country == None:
    print('We don\'t have any information about this country')
else:
    print(f"Capital of {ask_q} is {country}")
player_0 = {
    'name':'Cristiano Ronaldo',
    'born':1985,
    'born_c':"Funchal, Madeira, Portugal",
    'c_team':'Manchester United',
    'p_teams':['Sporting CP','Manchester United', 'Real Madrid', 'Juventus']
    }

player_1 = {
    'name':'Lionel Andrés Messi',
    'born':1987,
    'born_c':'Rosario, Santa Fe, Argentina',
    'c_team':'Paris Saint-Germain',
    'p_teams':['Barcelona C', 'Barcelona B', 'Barcelona']
    }

player_2 = {
    'name':'Karim Mostafa Benzema',
    'born':1987,
    'born_c':'Lyon, France',
    'c_team':'Real Madrid',
    'p_teams':['Lyon B', 'Lyon',]
    }

athletes = [player_0, player_1, player_2]

for player in athletes:
    name = player['name']
    born = player['born']
    born_c = player['born_c']
    c_team = player['c_team']
    p_teams = player['p_teams']
    print(f"Athlet name is {name.title()}, he was born {born} in {born_c.title()}. Current playing team is {c_team}.\nHe played in: ")
    for teams in p_teams:
        print(teams)
ingredients = ['carrot', 'cabbage', 'apple', 'pear', 'potato', 'sugar', 'banana',
               'cherry', 'peach', 'orange']
basket = []
for n in range(5):
    basket.append(input(f'Choose {n+1}-ingredient in basket: '))
for ingredient in basket:
    if ingredient in ingredients:
        print(f'Available {ingredient} in  market')
    else:
        print(f"Unavailable {ingredient} in  market")
menu = {
    'Steak':50,
    'Soup':10,
    'Fried Chicken':20,
    'Pasta with cheese':19,
    'Fried Fish':22,
    'Spagetti':24,
    'Snacks':14,
    'Pizza':32,
    'Sandwich':17
    }
print('Please choose 3 different dishes')

orders = []

for n in range(3):
    orders.append(input(f"Please choose {n+1}-food: "))

for order in orders:
    if order in menu:
        print(f"For {order.title()} cost {menu[order]}$")
    else:
        print(f'Sorry we don\'t have {order}')

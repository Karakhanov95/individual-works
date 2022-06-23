print('Orders from market')
ordered = []
n = 1
while True:
    quest = f"Your {n}-order: "
    orders = input(quest)
    ordered.append(orders)
    repeated = input("Do you want anything else ? (yes/no)")
    n += 1
    if repeated != 'yes':
        break
    
print('Your orders: ')
for ordered_0 in ordered:
    print(ordered_0)
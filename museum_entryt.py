print("Information about Museum entry prices")
ques_1 = 'Please your age: '
while True:
    ask_q = input(ques_1)
    if ask_q == 'exit' or ask_q == 'quit':
        break
    age = int(ask_q)
    
    if age<7:
        price = 15
    elif 7<=age<18:
        price = 20
    elif 18<=age<65:
        price = 30
    else:
        price = 0
    
    if price == 0:
        print('Enrty price for you free')
    else:
        print(f"Entry price for you {price}$ ")

print('Thank you !')
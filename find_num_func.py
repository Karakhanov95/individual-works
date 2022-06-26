import random
def find_num(x=10):
    r_num = random.randint(1, x)
    print(f"Can you find the number I thought of froma 1 to {x} ?")
    predicts = 0
    while True:
        predicts += 1
        predicted = int(input(">>>>>> "))
        if predicted < r_num:
            print("False, the number I thought was bigger than that. Try again: ")
        elif predicted > r_num:
            print("False, the number I thought was smaller than that. Try again: ")
        else:
            break
    print(f"Congratulations you found with {predicts} guesses")
    return predicts

def find_num_pc(x=10):
    input(f"Think of a number from 1 to {x} and press any button.I will find: ")
    below = 1
    above = 10
    predicts = 0
    while True:
        predicts += 1
        if below != above:
            r_num_0 = random.randint(below, above)
        else:
            r_num_0 = below
        
        answers = input(f"you thought of the number {r_num_0}: (t),"
                        f"the number I thought was bigger than that (+), or samller (-): ")
        if answers == '-':
            above = r_num_0 - 1
        elif answers == '+':
            below = r_num_0 + 1
        else:
            break
    print(f"I found with {predicts} guesses")
    return predicts

def play(x=10):
    again = True
    while again:
        predicts_uesers = find_num(x)
        predicts_pc = find_num_pc(x)
        if predicts_uesers > predicts_pc:
            print(f"I won with {predicts_pc} guesses")
        elif predicts_uesers < predicts_pc:
            print(f"You won with {predicts_uesers} guesses")
        else:
            print("Draw !")
        again = int(input(f"Do you want to play again ? Yes(1)/No(0): "))
            
        

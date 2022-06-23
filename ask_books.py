#Your favorite book
question = 'What is your favorite bookd '
question += "(type 'exit' to stop !): "
ask_q = ''
while ask_q != 'exit':
    ask_q = input(question)
    if ask_q != 'exit':
        print(ask_q)
print('The program stopped')
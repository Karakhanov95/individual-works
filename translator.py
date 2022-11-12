from translate import Translator
ques = "What do you want to translate?: "
translator = Translator(from_lang='english', to_lang="uzbek")
while True:
    ask = input(ques)
    if ask == "exit":
        break
    else:    
        translation = translator.translate(ask)
        print(translation)
    
print("Dastur tugadi")
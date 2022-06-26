def private_info(name, surname, b_year, b_place, email='', m_number=''):
    """This function will collect all
    information from user and
    will return"""
    person0 = {
        'name':name,
        'surname':surname,
        'b_year':b_year,
        'b_place':b_place,
        'email':email,
        'm_number':m_number
        }
    return person0

print("We'll collect private infromation from users")
user1 = []
while True:
    print('\nPlease fill the form in below: ', end='')
    name = input("Your name: ")
    surname = input('Your surname: ')
    b_year = input('When was you born: ')
    b_place = input("Place of born: ")
    email = input("Your email adress: ")
    m_number = input("Your mobile number: ")
    
    user1.append(private_info(name, surname, b_year, b_place, email, m_number))
    answer = input("Would you like to add more infromation ?(yes/no): ")
    if answer == 'no':
        break
print("\nYour private information: ")
for users in user1:
    if users['email'] or users['m_number']:
        email = users['email']
        m_number = users['m_number']
    else:
        email = 'Unknown email'
        m_number = 'Unknown number'
    print(f"Name: {users['name'].title()} \nSurname: {users['surname'].title()}"
          f"\nYear of birth: {users['b_year']} \nPlace of birth: {users['b_place'].title()}"
          f"\nEmail adress: {email} \nMobile number: {m_number}")
    
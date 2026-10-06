#name = input('Enter your full name: ')
#phone_num = input('Enter your phone number: ')


#result = len(name)
#result = name.find('u')
#result = name.rfind('s')
#name = name.capitalize()
#name = name.upper()
#name = name.isalpha()
#name = name.lower()
#name = name.isdigit()


#result = phone_num.count('0')
#result = phone_num.replace('-',' ')


#print(result)





username = input('Enter a username for your account: ')


if len(username) > 12:
    print('U can\'t Enter more than 12 characters')

elif not username.find(' ') == -1:
    print('Username can\'t contain any spaces')

elif not username.isalpha():
    print('username can\'t contain any numebrs')
    

else:
    print('Your Good To Go')
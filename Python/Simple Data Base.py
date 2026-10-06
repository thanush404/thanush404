import time,os

def database():

    print(f'Here You Go: {data}')

def repeat():
    again = input(f'Do You Wanna Store Something Again (y/n): ').lower()
    os.system('cls')
    if again == 'n':
        print('Thanks For Using Our Data Base')

    elif again == 'y':
        inputagain()

    else:
        print('You Entered A Wrong Comand,\nPlease Re-Enter The Corect one!')
        
    again = input(f'Do You Wanna Store Something Again (y/n): ').lower()
    os.system('cls')
    if again == 'n':
        print('Thanks For Using Our Data Base')

    elif again == 'y':
        inputagain()


def inputagain():
    data = input('what do u want to save to the data base: ')
    os.system('cls')
    print('We\'ll Keep Your Data Safe')
    print('---😊------😊-----😊---')
    time.sleep(2)
    os.system('cls')
    
        
while True:
        
    data = input('what do u want to save to the data base (exit) To EXIT: ').capitalize()
    if data == 'Exit':
        print('Good Bye!')
        break
    os.system('cls')
    print('We\'ll Keep Your Data Safe')
    print('---😊------😊-----😊---')
    time.sleep(1)
    os.system('cls')

                

    savedinfo = input('Do U Wanna Take Your Data Back\nOr change The Data That U Entered (change) or (dback): ').lower()
    os.system('cls')
    if savedinfo == 'change':
        inputagain()
        repeat()

    elif savedinfo == 'dback':
        print(f'Here\'s Your Data: {data}')
        time.sleep(3)
        os.system('cls')
        break

    else:
        print('You Entered Wrong Command\nPlease Re-Enter The Correct One!')
        time.sleep(2)
        os.system('cls')

        savedinfo = input('Do U Wanna Take Your Data Back\nOr change The Data That U Entered (change) or (dback): ').lower()
        os.system('cls')

        if savedinfo == 'change':
            inputagain()
            time.sleep(2)
            os.system('cls')
            break    

        

        elif savedinfo == 'dback':
            print(f'Here\'s Your Data: {data}')
            time.sleep(3)
            os.system('cls')
        

    again = input(f'Do You Wanna Store Something Again (y/n): ').lower()
    os.system('cls')
    if again == 'n':
        print('Thanks For Using Our Data Base')

    elif again == 'y':
        inputagain()

    else:
        print('You Entered A Wrong Comand,\nPlease Re-Enter The Corect one!')
        
    again = input(f'Do You Wanna Store Something Again (y/n): ').lower()
    os.system('cls')
    if again == 'n':
        print('Thanks For Using Our Data Base')
        break

    elif again == 'y':
        inputagain()
        break
    
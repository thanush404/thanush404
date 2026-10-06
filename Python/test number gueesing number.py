import random 

print('Wellcome to Number Guessing Game')
while True:
        try:

            num_range = int(input('Guess a Number Between 1-?: '))
        except ValueError:
            print('That\'s not a valid number')

        print(f'You Choose 1-{num_range}')
        
        number = random.randint(1,num_range)
        attempts = 0

        while True:
                try:
                   guess = int(input('Your Guess: '))
                except ValueError:
                      print(f'{guess} is not a valid number')
                guess = int(guess)    
                attempts =+ 1

                if guess > num_range:
                      print(f'Your guess is out of range , please try again')
                elif guess > number:
                      print('Too High ⬆, Guess again')
                elif guess < number:
                      print('Too Low ⬇ , Guess Again') 
                else:
                      print(f'✔ Congrats You Won!. The Answer Is = {number} You Gessed It In {attempts} Attempts')
                      break

        replay = input('Do You Wanna Play Again? (y/n): ').lower()   
        if replay != 'y':
              print('Thanks For Playing Good Bye👋')
              break


                  
            




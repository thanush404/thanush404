import random 

print('Wellcome to Number Guessing Game')
while True:
        try:

            num_range = int(input('Enter a Number Between 1-?: '))
        except ValueError:
            print('That\'s not a valid number')
            continue

        print(f'You Choose 1-{num_range}')
        
        number = random.randint(1,num_range)
        attempts = 0

        while True:
                try:
                   guess = int(input('Your Guess: '))
                except ValueError:
                      print(f'{guess} is not a valid number')
                      continue
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
              print('Thanks For Playing')
              break
        
rps_game = input('Do You Wanna Play The NEXT GAME, IT CAN BE A SUPRISE! (y/n): ').lower()
if rps_game != 'y':
      print('Ohh My Bad You Missed The Suprise , I Guess That\'s Fine Then See You Later!')


#----------------------------------------------------------
#----------------------------------------------------------
#----------------------------------------------------------
#-----------THE NEXT GAME--------THE NEXT GAME-------------
#----------------------------------------------------------
#----------------------------------------------------------
#-----------THE NEXT GAME--------THE NEXT GAME-------------
#----------------------------------------------------------
#----------------------------------------------------------
#----------------------------------------------------------


else:
      options = ('rock','paper','scissor')


print('-----------------------------------')
print('       ROCK,PAPER,SCISSOR          ')
print('-----------------------------------')
print('                                   ')
        
while True:
        
    round = 0
    score = 0
             
    while round < 5:

        


        computer = random.choice(options)
        player = str(input('Select One Between__Rock / Paper / Scissor: '))
        
      

        print(f"Player : {player}")
        print(f'Computer : {computer}')

        if computer == player:
            print('It\'s a Tie!')
            score +=1

        elif player == 'paper' and computer == 'rock':
            print('You Win')
            score +=1
        
        elif player == 'rock' and computer == 'scissor':
            print('You Win')
            score +=1 
 
        elif player == 'scissors' and computer == 'paper':
            print('You Win')
            score +=1

        else:
            print('You lose')
         
        round +=1
        print(f'score : {score}')
        print(f'round : {round}/5\n')

    print('                                   ')
    print('-----------------------------------')
    print('------------Game Over! GG----------')
    print('-----------------------------------')
    print('                                   ')

    print(f'Final Score: {score}')

    replay = input('If You Wanna Play Again Then Click (y/n): ').lower()
    if replay != 'y':
        print('Thanks For Playing!')

        break
 
calculater = input('DO YOU WANNA CHECK OUT OUR NEW CALCULATER TOO! (y/n): ').lower()
if calculater != 'y':
    print('Ok Then Have A Nice Day Sir')
else:
 

#----------------------------------------------------------
#----------------------------------------------------------
#----------------------------------------------------------
#-----------THE NEXT GAME--------THE NEXT GAME-------------
#----------------------------------------------------------
#----------------------------------------------------------
#-----------THE NEXT GAME--------THE NEXT GAME-------------
#----------------------------------------------------------
#----------------------------------------------------------
#----------------------------------------------------------


 i: int = 0


def adition (a,b):
    return a + b 
def substraction (a,b):
    return a - b
def multiplication (a,b):
    return a * b
def division (a,b):
     if (b == 0):
        return 'Error: Division by zero is not allowed'
     else:
          return a/b 
      
while 1 < 5:
          
     Disision  : list[str] = ['1. Addition','2. Subtraction','3. Multiplication','4. Division']
     for name in Disision:
         print(f'{name}')
                
     choice = input('Enter the Number (1-4): ')
     num1 = float(input('Enter the first Number: '))
     num2 = float(input('Enter the second Number: '))

     if (choice == '1'):
                print(adition(num1,num2))
                        
     elif (choice == '2'):
            print(substraction(num1,num2))
     elif (choice == '3'):
            print(multiplication(num1,num2))
     elif(choice == '4'):
                print(division(num1,num2))
     else:
                print("invalid input")
                
                i += 1
                



import random
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
        player = str(input('Select One Between: Rock / Paper / Scissor: '))
        
      

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

    print('-------------')
    print('Game Over! GG')
    print('-------------')
    print('             ')

    print(f'Final Score: {score}')

    replay = input('If You Wanna Play Again Then Click (y/n): ').lower()
    if replay != 'y':
        print('Thanks For Playing!')

        break


            


        

    
import random
lowest_number = 1
highest_number = 100
answer = random.randint(lowest_number , highest_number)
guesses = 0
is_running = True

print('Welcome to python number guessing game')
print(f'Select a number between{lowest_number} and {highest_number}')

while is_running:

    guess = input('Enter your guess: ')

    if guess.isdigit():
        guess=int(guess)
        guesses += 1

        if guess < lowest_number or guess > highest_number:
            print('That number is out of range')
            print(f'plese select a number betweem {lowest_number} and {highest_number}')
        elif guess < answer:
            print('It\' too low')
        elif guess > answer:
            print('It\'s too hight')
        else:
            print(f'CORECT ANSWER WAS {answer}')
            print(f'Number Of Guesses You Took Is {guesses} ')
            is_running = False



    else:
         print('Invalid Guess ')
         print(f'Please select a Number between {lowest_number} and {highest_number}')


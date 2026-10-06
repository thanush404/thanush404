questions = (('Which animal lay the largest egg')
             ,('How many letters in alphabet')
             ,('How many days in a week')
             ,('When is the crismas')
             ,('Which animal is the biggest in size'))

options = (('A. Chicken','B. Pasbara','C. Parrot','D. Kiwi')
           ,('A. 27','B. 24','C. 28','D. 29')
           ,('A. 8','B. 6','C. 5','D. 7')
           ,('A. April : 19','B. August : 24','C. Desember : 27','D. November : 29')
           ,('A. Blue Whail','B. Shark','C. Dolphine','D. Eliphant'))

answers =('B','A','D','C','A')
guesses = []
score = 0
question_num = 0

for question in questions:
    print('--------------------------------')
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input('Enter (A,B,C,D): ').upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
        
    else:
        print('INCORRECT!')
        print(f'{answers[question_num]} Is The CORRECT Answer!')
        
    question_num += 1

print(f'The Answers Are: ',end='')
for answer in answers:
    print(answer,end=' ')
print()

print(f'Your Guesses Are: ',end='') 
for guess in guesses:
    print(guess,end=' ') 
print()  

score = int(score / len(questions) * 100)
print(f'Your Score Is: {score}%\nGood Luck!')
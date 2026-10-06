while True:


        import time

        my_time = int(input('Enter the time you wanna count: '))

        for countdown in range(my_time,0,-1):

            seconds = countdown % 60
            minutes = int (countdown / 60) % 60
            hours = int(countdown / 3600)

            print(f'{hours :02}:{minutes :02}:{seconds :02}', end='\r')

            time.sleep(1)



        print("Time's UP!")

        again = input('DO YOU WANNA PLAY AGAIN? (Y/N): ').lower()

        if again != 'y':
              print(f'Have a nice day!')
              break
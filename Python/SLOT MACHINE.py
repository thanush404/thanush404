import time,random

def spin_row():
    symbols = ['🍒' , '🍉' , '🍍' , '🔔' , '⭐']
    return[random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("**************")
    print(' | '.join(row))
    print("**************")

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[1] == '🍒':
            return bet * 3
        elif row[1] == '🍉':
            return bet * 4
        elif row[1] == '🍍':
            return bet * 5
        elif row[1] == '🔔':
            return bet * 10
        elif row[1] == '⭐':
            return bet * 20
    return 0

def main():

    balance = 100

    print("*************************")
    print("Welcome to Python Slots ")
    print("Symbols: 🍒 🍉 🍍 🔔 ⭐")
    print("*************************")

    while balance > 0:

        print(f'Current Balance ${balance}')

        bet = input('Enter a amount to bet! $: ')
        

        if not bet.isdigit():
            print('Please Enter a valid Number to bet!')
            continue
        
        bet = int(bet)

        if bet > balance:
            print('Insufficient Funds!')
            continue
        if bet < 0:
            print('The bet must be grater that $0')
            continue

        

        row = spin_row()
        print('spinning..\n')
        time.sleep(1)
        print_row(row)
        
        balance -= bet

        payout = get_payout(row , bet)

        if payout > 0:
            print(f'You Won ${payout}')
        else:
            print('sorry you lost this round!')    

        balance += payout   

        play_again = input('Do you wanna play again(Y/N)').upper()
        if play_again != 'Y':
            print('Thanks for playing, Have a nice day!')
            break

if __name__ == '__main__':
    main()
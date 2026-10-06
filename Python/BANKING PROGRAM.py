import os,time

def show_balance(balance):
    print(f'Your Balance Is ${balance :.2f}')

def deposit():
    amount = float(input('Enter a amount to deposit $: '))

    if amount < 0:
        print('That\'s Not A Valid Amount!')
        return 0
    else:
        return amount
    
def withdraw(balance):
    amount = float(input('Enter A Amount To Withdraw $: '))
    if amount > balance:
        print('Insufficient Funds!')
        return 0
    elif amount < 0:
        print('The Amount Must Be Grater Than $0')
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print('**********************')
        print(' Banking Program! ')
        print('**********************\n')
        print('**********************')
        print('1. Show Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. EXIT!')
        print('**********************')
        choice = input(f'Enter Your Choice (1-4): ')

        if choice == '1':
            print('**********************')
            show_balance(balance)
            time.sleep(2)
            os.system('cls')

        elif choice == '2':
            print('**********************')
            balance += deposit()
            print("Your Money Has Being Successfuly Deposited!")
            time.sleep(2)
            os.system('cls')

        elif choice == '3':
            print('**********************')
            balance -= withdraw(balance)
            print('Your Money Has Being Successfuly Withdrawn!')
            time.sleep(2)
            os.system('cls')

        elif choice == '4':
            is_running = False 
        else:
            print('**********************')
            print('That\'s Not A Valid Choice!')
            time.sleep(2)
            os.system('cls')

    print('Thank You, Have A nice day!')       

if __name__ == '__main__':
    main()  

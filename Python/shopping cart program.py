foods = []
prices = []
total = 0

menu = '\nHotDog ,\nCake ,\nHameBurger ,\nSubmarine'
print(f'Menu :\n {menu}')

while True:
    food = input('Enter The Food You Wanna Buy (q to quit): ').capitalize()
    if food.lower() == 'q':
        break
    
    else:
        price = float(input(f'Enter The Price Of The {food}:$ '))
        foods.append(food)
        prices.append(price)

print('-------Your--Cart-------')

for food in foods:
    print(f'Items U brought: {food}',end =' ')

for price in prices:
 total = total + price

print(f'\nYour Total Is ${total}')





    

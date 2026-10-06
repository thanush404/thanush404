weight = float(input('Enter Your Weight: '))
unit = input('Enther The Unit (Kg/Lbs)').lower()

if unit == 'kg':
    weight = weight * 2.205
    unit = 'Lbs.'
    print(f'Your weight is : {round(weight ,2)} {unit}')


elif unit == 'lbs':
    weight = weight / 2.205
    unit = 'Kg.'
    print(f'Your weight is :{round(weight , 2)} {unit}')   

else:
    print(f'{unit} Is Not Valid, Enter A Valid Number')


 

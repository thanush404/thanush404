temp = float(input('Enter the temperature: '))
unit  = input('Enter the Unit Fahrenhiet or celcius (C/F): ')

if unit == 'c': 
    temp = round((9 * temp)/ 5 + 32 , 2)
    print(f'The Temperature In Fahrenhiet Is: {temp}°F')

elif unit == 'f':
    temp = round((temp - 32) * 5 / 9 , 2)  
    print(f'The Temperature In Celcius Is: {temp}°C') 

    
else:
    print(f'The {unit} Is An Invalid Unit Of Mesurment')
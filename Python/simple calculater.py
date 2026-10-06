i: int = 0


def adition (a,b):
                return a + b 
def substraction (a,b):
                return a - b
def multiplication (a,b):
                return a * b
def division (a,b):
     if (b == 0):
        return 'Error:Division by zero is not allowed'
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
#name: str = 'Binodi'
#age: int = 15

#print(f'Name: {name}, Age: {age}')





#def add (a: float, b: float ) ->float:
    #print(f'Adding: {a} + {b}')
    #return a + b

#print(add (a=10 , b=15))
#print(add (a=15, b=30))



#def greet(name=str,greeting=str) -> None:
    
    #print(f'{name}, {greeting}')
#greet(name='Binodi' , greeting='ciao')





#def greet(name = str, greeting:str = 'Hii') -> None:
  #print(f'{name}, {greeting}')

#greet(name='Binodi' , greeting='ciao')
#greet('james')
#greet('Thanush')








#for i in range(3): 
  #  print('Hello')
  
  

#names: list[str] = ['Thanush','Isath','Thidesh']
#for name in names:
    #print(f'Hello ,{name}')
   # print('Gammak')
   
  
  
  
  
  
  
#while True:  
  #print('Hello World :)')
  
  
    
#i: int = 0

#while i < 5:


 
 
  #  i += 1
  
  
  
  
  
  
  
#a: int = 3
#b: int = 2
 
#print(a > b)
#print(a <= b) 
#print(a == b)
#print(a != b)





#while True:
   #  user_input: str = input('hii')
 
   #  if user_input == 'hello':
   #    print('Bot: Hello baby..!')
   #  elif user_input == 'bye':
   #    print('Bot:Good Bye my little pooky..')  
   #  elif user_input == 'hii':
   #    print('Hey sweety Mommy is here wanna come over sweet heart')  
   #  elif user_input == 'how are you?':
    #   print('Bot: I am good, how about you baby are u tired hm..?')
   #  else:
    #   print('Sorry I am still learning baby, i am so sorry my pooky umma..')

    
    
    
     
    
 
 
 
 
#a, b = 10 , 'fifteen'
  
#try: 
  #   print(a + b)
#except TypeError as e:
#   print('please enter a number in the form of an integer or a float!')
    

  # print(' to continuing with the program...')
  
  
  
  
  
  
  
  
  

#import math  
#import math as m
#from math import sqrt 
#from math import sqrt, tan
 
#print(math.sqrt(3))
#print(m.sqrt(4))
#print(sqrt(5))
#print(tan(2))








   
   
   
bot_name:str ='Bob'
print(f'hello i\'m {bot_name}: how can i help you today?')

while True:
    user_input: str = input ('you: ').lower()
   
    if user_input in ['hello','hi','yo']:
        print(f'{bot_name}:Hey how is your day going and how can i help you')
    elif user_input in['how are you','whats up dude']:
        print(f'{bot_name}:I\'m good how about you :)')
    elif user_input in ['bye','cya','see you']:
        print(f'{bot_name}:ok Good Bye See You Later')
        
    elif user_input in ['+', 'add']:
        print(f'{bot_name}:Sure let\'s do some addition! please enter two numbers.')
        try:
            num1:float = float(input('first number:'))
            num2:float = float(input('second number:'))
            print(f'{bot_name}:The sum is {num1 + num2 }')
        except ValueError:
            print(f'{bot_name}: Oops! That doesn\'t seems like a valid number.Try again!')
    else:
        print(f'{bot_name}: I\'m sorry, I don\'t understand that. please try again.')        
   
   
   
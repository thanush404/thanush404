fruits = {'Apple' : 125 ,
          'Pineapple' : 350,
          'Watermelon' : 450,
          'Avacado' : 160}
  

 ## print(dir(fruits))
 ## print(help(fruits))
  


 #print(fruits.get('Apple'))



#if fruits.get('Banana'):
    #print('That Fruit Is Seems Like In The Stock!')
    
#else:
    #print('That Fruit Is Out Of Stock!')


 
#fruits.update({'Berry' : 300})
#print(fruits)


#fruits.pop('Avacado')
#print(fruits)


#fruits.popitem()
#print(fruits)


#fruits.clear()
#print(fruits)


#keys = fruits.keys()
#print(keys)


#for key in fruits.keys():
 #   print(key)


#values = fruits.values()
#for value in fruits.values():
 #   print (value)



items = fruits.items()
for key ,value in fruits.items():
 print(f'{key}: {value}')

 # btw this .items() use if u need both key and value at the same time 
 
 # this .values() use if u need just the value (if u just need the key just dont do anything :)
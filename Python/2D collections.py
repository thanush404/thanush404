#fruits = ['Apple','Banana','Avacado','Pears']
#vegitables =['Carrot','Brocolli','Chili','Cabage']
#meats = ['Fish','Chicken','Turkey','Beef']

#groceries = [['Apple','Banana','Avacado','Pears'],
            # ['Carrot','Brocolli','Chili','Cabage'],
            # ['Fish','Chicken','Turkey','Beef']]

#print(groceries[1][0])

#for collection in groceries:
   # for food in collection:
       # print(food,end=' ')
   # print()

num_pad =[(1,2,3),
          (4,5,6),
          (7,8,9),-
         ('*',0,'#')]


for row in num_pad:
    for num in row:
        print(num,end=' ')
    print()
#---- EXAMPLE ----

def net_price(list_price, discount=0, tax=0.05):
   return list_price * (1 - discount) * (1 - tax)

print(net_price(500))
# print(net_price(500,0.1))
# print(net_price(500,0.1,0.3))


#---- EXERCISE ----

# import time,os

# def count(end,start=0):
#    for x in range(start,end + 1):
#       print(x,end='\r')
#      time.sleep(1)
#    print("DONE!")
#   time.sleep(3)
#    os.system('cls')
     
# count(5)
# count(10,5)

      

# ---- *ARGS Example 1 ----

# def add(*args):                    # you can use any argunment name with this * _ _
#     total = 0
#    for arg in args:
#         total += arg
#     return total

# print(add(1, 2, 3, 4))



# ---- *ARGS Example 2 ----

# def names(*args):
#     for arg in args:
#         print(arg,end=" ")

# names('Mr','Thanush','Senupa')



# ---- **KWARGS ----

def address(**kwargs):
    for key , value in kwargs.items():
        print(f'{key:8}: {value}')

address(Address='123455',
        Street='idk street',
        Country='Sri Lanka')    

# ---- EXERCISE ----

# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg,end=" ")
#     print()

#     if 'apt' in kwargs:
#        print(f'{kwargs.get('street')} {kwargs.get('apt')}')

#     else:
#         print(f'{kwargs.get('street')}')    

#     print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")





# shipping_label("Dr.", "Spongebob", "Squarepants",
#                street="123 Fake St.",
#                pobox="PO box #1001",
#                city="Detroit",
#                state="MI",
#                zip="54321")



      
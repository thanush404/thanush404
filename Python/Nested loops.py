#this is an example of nested loops


rows = int(input('Enter How  Many Rows U want: '))
colums = int(input('Enter How Many Colums U want: '))
symbles = input('Enter the symble that u wanna print: ')


for x in range(rows):
    for y in range(colums):
       print(symbles,end='')
    print()
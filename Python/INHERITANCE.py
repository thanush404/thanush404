class Animal:
    def __init__(self,name,):

        self.name = name
        self.is_alive = True

    def eat(self):
            print(f'The {self.name} is eating!')

    def sleep(self):
            print(f'The {self.name} is sleeping!')  

class Dog(Animal):
    def speak(self):
         print('WOOF!')


class Cat(Animal):
    def speak(self):
         print('MEOW!')

class Mouse(Animal):
    def speak(self):
         print('SQUEEK!')


dog = Dog('Scooby')
cat = Cat('Garfiled')
mouse = Mouse('Mikey')


# print(dog.name)
# print(dog.is_alive)
# dog.eat()
# dog.sleep()

dog.speak()
cat.speak()
mouse.speak()



class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'The {self.name} is eating!') 

    def sleep(self):
        print(f'The {self.name} is sleeping')  

class prey(Animal):
    def flee(self):
        print(f'The {self.name} is Fleeing!')    
    
class predator(Animal):
    def hunt(self):
        print(f'The {self.name} is hunting!')

class Rabbit(prey):
    pass

class Tiger(predator):
    pass

class Fish(prey,predator):
    pass
 
rabbit = Rabbit('Bunny')
tiger = Tiger('Tigress')
fish = Fish('Nemo')

fish.eat()

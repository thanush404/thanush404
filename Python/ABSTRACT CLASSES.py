from abc import ABC, abstractmethod

class Vehicle:
    
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print('You Drive Car!')

    def stop(self):
        print('You Stops Car!')

class Boat(Vehicle):
    def go(self):
        print('You Drive The Boat!')

    def stop(self):
        print('You Anchor The Boat!')   

car = Car()     
boat = Boat()


# car.go()
# car.stop()

boat.go()
boat.stop()
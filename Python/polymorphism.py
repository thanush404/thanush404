from abc import ABC,abstractmethod

class Shapes(ABC):
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shapes):

    def __init__(self,radius):

        self.radius = radius

    def area(self):
        return  3.14 * self.radius ** 2
    
class Square(Shapes):

    def __init__(self,side):

        self.side = side

    def area(self):
        return self.side ** 2
    
class Pizza(Circle):

    def __init__(self,topping,radius):

        super().__init__(radius)
        self.topping = topping

shapes = [Circle(6), Square(8), Pizza('Pepperoni',14)]

for shapes in shapes:
    print(f'{shapes.area()}cm²')


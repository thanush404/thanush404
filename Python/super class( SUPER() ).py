class Shape:
    def __init__(self,colour,is_filled):

        self.colour = colour
        self.is_filled = is_filled

    def describe(self):
        print(f'It is {self.colour} and {'FIlled!' if self.is_filled else 'not Filled!'}')


class Circle(Shape):

    def __init__(self,colour,is_filled,radius):

        super().__init__(colour,is_filled)
        self.radius = radius
    
    def describe(self):
        print(f'It is a circle with an area of {3.14 * self.radius * self.radius} cm^2')
        super().describe()

class Square(Shape):
    
    def __init__(self,colour,is_filled,width):

        super().__init__(colour,is_filled)
        self.width = width

    def describe(self):
        print(f"It is a square with an area of {self.width * self.width}cm^2")
        super().describe()


circle = Circle(colour='Red', is_filled=True, radius=7 )  
square = Square(colour='Green', is_filled=False, width=4) 

# square.describe()

circle.describe()
    
        
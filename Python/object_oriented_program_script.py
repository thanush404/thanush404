class blueprint:
    def __init__(self, model,colour,year,for_sale):
        
        self.model = model
        self.colour = colour
        self.year = year
        self.for_sale = for_sale

    def drive(self):
        print(f'Your dive a {self.colour} {self.model}')

    def stop(self):
        print(f'Stop the {self.colour} {self.model}') 

    def describe(self):
        print(f'You Drive a {self.colour} {self.model} {self.year}')   
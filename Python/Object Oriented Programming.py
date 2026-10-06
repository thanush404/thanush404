# ==============================
# ============Class=============
# ==============================


# class car:
#     def __init__(self, model,colour,year,for_sale):
        
#         self.model = model
#         self.colour = colour
#         self.year = year
#        self.for_sale = for_sale

# Car1 = car('Charger', 'black', 2026, True)

# print(Car1.model)
# print(Car1.colour)
# print(Car1.year)
# print(Car1.for_sale)



# ==============================
# ===========Methods============
# ==============================

from object_oriented_program_script import blueprint

car1 = blueprint('Charger', 'black', 2026, True)

car1.drive()
car1.stop()
car1.describe()
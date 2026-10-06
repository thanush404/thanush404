class Student:

    count = 0
    total_gpa = 0

    def __init__(self,name,gpa):

        self.name = name
        self.gpa = gpa

        Student.count += 1
        Student.total_gpa += gpa

    #INSTANCE METHOD

    def get_info(self):
        return f'{self.name} | {self.gpa}'
    
    @classmethod
    def get_count(cls):
        return f'The Total Number Of Students: {cls.count}'
    
    @classmethod
    def get_avarage_gpa(cls):

        if cls.count == 0:
            return 0 
        
        else:
            return f'Avarage GPA: {cls.total_gpa / cls.count : 2f}'
        
student1 = Student('sponge bob', 3)
student2 = Student('squidward', 3.4)
student3 = Student('Sandy', 4)
student4 = Student('Patrick', 2.6)

print(Student.get_count())
print(Student.get_avarage_gpa())

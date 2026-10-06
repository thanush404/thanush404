class Student:

    num_of_students = 0
    class_year = 2026

    def __init__(self,name,age):
        self.name = name
        self.age = age
         
        Student.num_of_students += 1

student1 = Student('SpongeBob',30) 
student2 = Student('Patrick', 35)  
student3 = Student('Sandy', 28)

print(f'My Graguating class number of students is {Student.num_of_students} and the year is {Student.class_year}')
print(student1.name)
print(student2.name)
print(student3.name)
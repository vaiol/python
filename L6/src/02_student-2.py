class Student:
    def __init__(self, name, age):
        self.name = name # instance attribute
        self.age = age
        self.mark = 0


some_student = Student('Alex', 27)
oleg_student = Student('Oleg', 21)
print(some_student.name)
print(oleg_student.name)



# print(Student.course) # помилка

# instance (object) vs class


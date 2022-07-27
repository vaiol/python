
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.mark = 0 # 0 - 100
        self.course = 'Python'

    def greeting(self):
        print("My str repr: " + self.__str__())
    
    def __str__(self):
        return f'Student. Name is {self.name}. Age is {self.age}. Study at the {self.course} and has {self.mark} mark.'

alex_student = Student('Alex', 27)
oleg_student = Student('Oleg', 21)

print(alex_student)
oleg_student.greeting()




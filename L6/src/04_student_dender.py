
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.mark = 0 # 0 - 100
        self.course = 'Python'

    def greeting(self):
        print("Hello my name is " + self.name)

    def increaseMark(self, num):
        if num <= 0:
            return
        self.mark += num
        if self.mark > 100:
            self.mark = 100
    
    def description(self):
        return f'Student. Name is {self.name}. Age is {self.age}. Study at the {self.course} and has {self.mark} mark.'

student = Student('Alex', 27)
student.greeting()
print(student.description())
# create __str__
# see if it's chanhging


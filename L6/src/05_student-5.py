
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.mark = 0 # 0 - 100
        self.course = 'Python'

    def greeting(self):
        print("Hello my name is " + self.name)

    def increase_mark(self, num):
        if num <= 0:
            return
        self.mark += num
        if self.mark > 100:
            self.mark = 100

student = Student('Alex', 27)

# private members

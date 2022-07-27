# create from dict
class Student:
    def __init__(self, person):
        self.name = person['name']
        self.age = person['age']
        self.mark = 0

    def greeting(self):
        print("Hello my name is " + self.name)

student = Student({ 'name': 'Alex', 'age': 27 })
print(student)
print(student.name)
print(type(student))

student.greeting()
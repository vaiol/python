# create from dict
class Student:
    def __init__(self, person):
        self.name = person['name']
        self.age = person['age']
        self.mark = 0

    def greeting(self):
        print("Hello my name is " + self.name)




student = Student({ 'name': 'Alex', 'age': 27 })
num = 121
print(type(student))

# student.name
student.greeting()
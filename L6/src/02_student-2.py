class Student:
    course = 'Python'
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.mark = 0


someStudent = Student('Alex', 27)
print(someStudent.name)
print(someStudent.course)
# print(Student.name) # помилка

# instance (object) vs class


# name as CapWords

class Student:
  name = 'Alex'
  age = 27
  mark = 'A'


someStudent = Student()


someStudent.name = 'Oleg'
print(someStudent.name)
anotherStudent = Student()
print(anotherStudent.name)
print(Student.name)
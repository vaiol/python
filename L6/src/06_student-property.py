
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._mark = 0 # 0 - 100
        self.course = 'Python'

    def greeting(self):
        print("Hello my name is " + self.name)

    def set_mark(self, new_mark):
        if new_mark <= 0:
            self._mark = 0
            return
        if new_mark >= 100:
            self._mark = 100
            return
        self._mark = new_mark
    
    def get_mark(self):
        return self._mark

    def del_mark(self):
        del self._mark

    mark = property(get_mark, set_mark, del_mark) 

student = Student('Alex', 27)
print(student.mark)
student.mark += 10
print(student.mark)
student.mark += 110
print(student.mark)
student.mark -= 3000
print(student.mark)

# private members

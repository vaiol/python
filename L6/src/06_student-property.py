
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._mark = 0 # 0 - 100
        self.course = 'Python'

    def greeting(self):
        print("Hello my name is " + self.name)

    def set_mark(self, new_mark):
        print('set mark', new_mark)
        if new_mark <= 0:
            self._mark = 0
            return
        if new_mark >= 100:
            self._mark = 100
            return
        self._mark = new_mark
    
    def get_mark(self):
        print('get mark')
        return self._mark

    def del_mark(self):
        print('del op')
        del self._mark

    mark = property(get_mark, set_mark, del_mark)

    def say_mark(self):
        print('My score is ' + str(self.mark))

alex_student = Student('Alex', 27)
print('before')
alex_student.mark = 110
print(alex_student.mark)
del alex_student.mark # == alex_student.del_mark()




# private members

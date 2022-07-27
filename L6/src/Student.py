from datetime import date


class Student:
    def __init__(self, first_name, last_name, birth_date, course):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self._mark = 0 # 0 - 100
        self.course = course

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

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age

    age = property(get_age)

    def __str__(self):
        return f'Student. Name is {self.first_name} {self.last_name}. Age is {self.age}. Study at the {self.course} and has {self.mark} mark.'


# student = Student('Alex', 'Stepanov', date(1995, 7, 8))
# print(student.age)
# print(student)
# student.age = 28 # помилка
# print(student.age)

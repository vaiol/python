from datetime import date


class Person:
    def __init__(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age

    age = property(get_age)

class Student(Person):
  def __init__(self, first_name, last_name, birth_date):
    super().__init__(first_name, last_name, birth_date)
    self.mark = 100

class Teacher(Person):
  def __init__(self, first_name, last_name, birth_date, subject):
    super().__init__(first_name, last_name, birth_date)
    self.subject = subject

alex_student = Student('Alex', 'Stp', date(1995, 7, 8))
print(alex_student.first_name)
print(alex_student.age)

math_teacher = Teacher('Oleg', 'Some', date(1993, 7, 8), 'Math')
print(math_teacher.first_name)
print(math_teacher.age)
from datetime import date
from Student import Student
from Course import Course

python_сourse = Course('Python', date(2022, 7, 11), date(2022, 8, 4))

alex_student = Student('Alex', 'Stepanov', date(1995, 7, 8), python_сourse)
# tom_student = Student('Tom', 'Hanks', date(1956, 7, 9), python_сourse)

print(alex_student.course)

# composition
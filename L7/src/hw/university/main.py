from datetime import date, datetime, timedelta
from university import Course, Mentor, Teacher, Student

some_course = Course('Python', datetime.now(), datetime.now() + timedelta(days = 30))

alex_student = Student('Alex', 'Stp', date(1995, 7, 8))

bred_teacher = Teacher('Bred', 'Cmp', date(1974, 6, 25), 2000, some_course)

koli_mentor = Mentor('Koli', 'Key', date(1987, 3, 13), 1200, [some_course])

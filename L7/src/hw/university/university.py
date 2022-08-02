"""Модуль який обʼєднує в собі класи
які допомогають управляти університетом: курсами, студентами і вчителями.

Деякі з цих класів частково реалізовані.
Потрібно пройти по всіх класах, зрозуміти логуку і завершити реалізацію певних методів.
Для тестування можна використовувати інший файл main.py, в данному файлі тестування не робимо.
Потрібно реалізувати всі методи які позначені TODO.
Також потрібно додати до кожно класу метод  def __str__(self):
"""

from datetime import date, datetime
from abc import abstractclassmethod


class Person:
    """Клас Person який означає просто людину і обʼєднує в собі базові атрибути."""

    def __init__(self, first_name: str, last_name: str, birth_date: date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def get_age(self):
        """Метод який розрахову і повертає поточний вік людини в залежності від дати народження."""

        today = date.today()
        age = today.year - self.birth_date.year - (
            (today.month, today.day) <
            (self.birth_date.month, self.birth_date.day))
        return age

    age = property(get_age)

class Course:
    """Клас курсу в університеті. Обʼєднує логіку яка стосується по курсу."""
    def __init__(self, name: str, start_date: datetime, end_date: datetime):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date

    def is_active(self) -> bool:
        """Повертає True або False в залежності від тогу чи курс активний чи ні.
        Активний курс це той який проходить в данний момент тобто start_date < NOW < end_date.
        TODO розробити!
        """

    def __str__(self):
        return f'{self.name} course. Start: {self.start_date}. Finish: {self.end_date}'



class UniversityEmployee(Person):
    """Клас UniversityEmployee який відповідає за працівника університету.
    Наслідується від класу Person.
    Відрізняється від класу Person тим що додано новий атрибут salry
    який відповідає за зарплату працівника (за місяць).
    """

    def __init__(self, first_name: str, last_name: str, birth_date: date,
                 salary: int):
        super().__init__(first_name, last_name, birth_date)
        self.monthly_salary = salary

    def get_yearly_salary(self):
        """Метод який повертає річну зарплату працівника.
        Розраховувати річну зарплату потрібно за місячною ЗП (атрибут monthly_salary).
        TODO розробити!
        """

    @abstractclassmethod
    def answer_question(self, course: Course, question: str) -> bool:
        """Метод який викликається коли студент задає питання по навчанню.
        Якщо працівник може відповісти на питання метод повертає True,
        якщо ж працівник не може відповісти метод повертає False.
        По замовчуванню працівник університету не може відповісти на будь які питання,
        тому метод призначений для перепризначення у класах наслідниках.
        """


class Teacher(UniversityEmployee):
    """Клас Teacher який відповідає за вчителя університету.
    Наслідується від класу UniversityEmployee.
    Відрізняється тим що зберігає інформацію про курс на якому викладає вчитель.
    (атрибут course)
    Вчитель може викладати тільки на одному курсу одночасно.
    Курс на якому вчитель викладає можна замінити за допомогою метода change_course.
    Можна додавати додаткові атрибути для внутрішньої логіки.
    """

    def __init__(self, first_name: str, last_name: str, birth_date: date,
                 salary: int, course: Course):
        super().__init__(first_name, last_name, birth_date, salary)
        self.course = course

    def answer_question(self, course: Course, question: str) -> bool:
        """Метод який викликається коли студент задає питання по навчанню.
        Якщо працівник може відповісти на питання метод повертає True,
        якщо ж працівник не може відповісти метод повертає False.

        Вчитель є дуже розумним, тому може відповісти на будь яке запитання (в незалежності від того що було передано в аргументі question).
        Але вчитель не може відповісти на запитання яке не стосується того курсу який він проводить в данний момент (атрибут course).
        Також вчитель принципово не відповідає на запитання по курсу який не є активним.
        Тобто якщо у вчителя курс який він проводить закічився (not is_active()) то вчитель не відповідє на запитання.

        TODO розробити!
        """

    def change_course(self, course: Course) -> bool:
        """Метод який призначений для того щоб призначати викладачу новий курс.
        Курс може бути призначений тільки якщо новий курс активний, тобто розпочався і не закінчився (див. метод Course.is_active).
        Якщо курс був успішно оновлений метод повертає True, в іншому випадку False.
        TODO розробити!
        """


class Mentor(UniversityEmployee):
    """Клас Mentor який відповідає за ментора університету.
    Наслідується від класу UniversityEmployee.
        
    Ментор може менторити на декількох курсах одночасно.
    (атрибут courses)
    Курси на яких ментор працює можна замінити за допомогою метода change_courses.
    Можна додавати додаткові атрибути для внутрішньої логіки.
    """

    def __init__(self, first_name: str, last_name: str, birth_date: date,
                 salary: int, courses: list[Course]):
        super().__init__(first_name, last_name, birth_date, salary)
        self.courses = courses

    def answer_question(self, course: Course, question: str) -> bool:
        """Метод який викликається коли студент задає питання по навчанню.
        Якщо працівник може відповісти на питання метод повертає True,
        якщо ж працівник не може відповісти метод повертає False.

        Ментор є також дуже розумним і може відповідати на всі запитання.
        Але ментор дуже зайнятий, він може менторити на декількох курсах,
        тому відповідає не на кожне запитання.

        Ментор може відповідати на всі питання якщо він менторить тільки на одному активному курсі (Course.is_active()),
        але якщо курсів більше то ментор відповідає на кожне N заняття, де N кількість активних курсів у ментора.

        Тобто, якщо ментор має 2 активних курси, то ментор буде відповідати на кожне друге запитання.
        Тобто, якщо ментор має 3 активних курси, то ментор буде відповідати на кожне третє запитання.
        
        Ментор як і вчитель ніколи не відповідає на питання по курсах на яких він не менторить (атрибут courses) і на курсах
        які вже не є активними.

        У ментора гарна памʼять, він запамʼятовує відповіді на запитання, і може відповідати на запитання, на які вже відповідав без черги.
        Питання не унікальні для курсу, тобто для порівняння запитань достатньо використовувати аргумент question.

        Наприклад:
        len(mentor.courses) -> 2 # менторить на 2ух курсах
        mentor.answer_question(some_course, 'Яка домашка?') -> True # на перше питання відповіли
        mentor.answer_question(some_course, 'Чи можу я здати пізніше?') -> False # на друге питання НЕ відповіли
        mentor.answer_question(some_course, 'Чи можу я здати пізніше?') -> True # теж саме питання, але вже знайшли час відповісти
        mentor.answer_question(some_course, 'Яка оцінка?') -> False # не вистачило часу відповісти на це питання

        mentor.answer_question(expired_course, 'Чи можу я здати пізніше?') -> False 
        # питання на яке відповідали, і є час відповісти, але питання стосується курсу який вже закінчився

        mentor.answer_question(some_course, 'Що було на уроці?') -> True 
        # так як на минуле питання ми не відповідали, на наступне питання є можливість відповісти


        mentor.answer_question(some_course, 'Що було на уроці?') -> True 
        # не дивлячись на те що ми дуже зайняті, але маємо змогу відповісти на питання, на яке вже відповідали.

        mentor.answer_question(some_course, 'Як мені виконати ДЗ?') -> False 
        # знову зайняті, False

        mentor.answer_question(some_other_course, 'Як мені виконати ДЗ?') -> True 
        # те саме питання по іншому курсу, знайшли час відповісти в цей раз

        mentor.answer_question(some_course, 'Як мені виконати ДЗ?') -> True 
        # те саме питання по першому курсу, можемо відповідати на це питання поза чергою

        TODO розробити!
        """

    def change_courses(self, courses: list[Course]) -> bool:
        """Метод який призначений для того щоб призначати ментори нові курси.
        Курс може бути призначений тільки якщо новий курс активний, тобто розпочався і не закінчився (див. метод Course.is_active).
        Якщо всі курси були успішно призначені метод повертає True, в іншому випадку False.
        Метод повінстю перезаписує атрибут курсів, тобто ми втрачаємо попередні курсі.
        Якщо хоча б один курс не був активним у списку, залишаємо старі курси.
        TODO розробити!
        """



class Student(Person):
    """Клас Student який відповідає за студента університету.
    Наслідується від класу Person.
    Можна додавати додаткові атрибути для внутрішньої логіки.
    """
    
    def add_mark(self, mark: int):
        """Метод який використовується вчителем коли той ставить оцінку стунденту.
        Оцінка не залежить від предмету. Потрібно зберігати всі оцінки які коли небудь були додані.
        Мінімальна оцінка: 1
        Максимальна оцінка: 12
        Для зберігання оцінок можна використовувати довільну структуру данних.
        TODO розробити!
        """
    
    def get_all_marks(self) -> list[int]:
        """Метод який використовується вчителем коли той ставить оцінку стунденту.
        Оцінка не залежить від предмету. Потрібно зберігати всі оцінки які коли неьудь були додані.
        TODO розробити!
        """
    
    def get_avarage_mark(self) -> float:
        """Метод який повертає середню оцінку студенту по всіх наданих студенту оцінках.
        Наприклад, студент має наступні оцінки [2, 10, 3]
        якшо викликати функцію то результат повинен бути 5,
        (2+10+3)/3=5
        TODO розробити!
        """

    def get_average_by_last_n_marks(self, n: int) -> float:
        """Метод який повертає середню оцінку за певною кількістю останніх оцінок.
        Наприклад, студент має наступні оцінки: [2, 10, 3, 6, 8, 7], 
        якшо викликати функцію з аргументом n=2 то результат повинен бути 6,
        тому що 2 останні оцінки: 2 і 10 - (2+10)/2=6
        Якщо число n<=0 - повертаємо 0.
        Перевірку n на число робити не потрібно, програма може повертати стандартну помилку виконання.
        TODO розробити!
        """
    
    def get_average_from_date(self, from_date: datetime) -> float:
        """Метод який повертає середню оцінку за певний період (від певної дати).
        Для того щоб реалізувати цей метод потрібно хберігати інформацію про те коли певна оцінка була додана.
        Наприклад, студент має наступні оцінки: [
            (2, datetime(2022, 7, 28)),
            (10, datetime(2022, 7, 27)),
            (3, datetime(2022, 7, 26)),
            (6, datetime(2022, 7, 25)),
            (8, datetime(2022, 7, 24)),
            (7, datetime(2022, 7, 23))], 
        якшо викликати функцію з аргументом from_date=datetime(2022, 7, 27) то результат повинен бути 6, 
        тому що в заданий період входять тільки 2 останні оцінки: 2 і 10 - (2+10)/2=6
        TODO розробити!
        """

    

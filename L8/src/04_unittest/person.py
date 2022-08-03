from datetime import date

class Person:
    """Клас Person який обʼєднує в собі базові атрибути кожній людині."""

    def __init__(self, first_name: str, last_name: str, birth_date: date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def get_age(self):
        """Метод який розрахову і повертає поточний вік людини в залежності від дати народження."""

        today = date.today()
        age = (
            today.year
            - self.birth_date.year
            - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        )
        return age

    age = property(get_age)

    def ask(self, question: str) -> bool:
        if question == 'do you love coffee?':
            return True
        if question.lower() == 'do you know programming?':
            raise Exception('NO NO NO NO!!!')
        return False

    def __str__(self):
        return f"Person {self.first_name} {self.last_name}, {self.age} years old."



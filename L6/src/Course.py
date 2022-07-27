class Course:
    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f'{self.name} course. Start: {self.start_date}. Finish: {self.end_date}'


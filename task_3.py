class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return (' '.join([self.name, self.surname]))
    def get_total_income(self):
        return self._income['wage']+self._income['bonus']

Worker_1 = Position('Иван', 'Иванов', 'Junior Data Scientist', {'wage': 50000, 'bonus': 30000})

print(Worker_1.name)
print(Worker_1.surname)
print(Worker_1.position)
print(Worker_1.get_full_name())
print(Worker_1.get_total_income())

Worker_2 = Position('Петр', 'Петров', 'Senior Data Scientist', {'wage': 100000, 'bonus': 50000})

print(Worker_2.name)
print(Worker_2.surname)
print(Worker_2.position)
print(Worker_2.get_full_name())
print(Worker_2.get_total_income())
import re
class Worker:
    def __init__(self, position='Должность', surname='Фамилия', name="Имя", wage=0, bonus=0):
        self.position = position
        self.surname = surname
        self.name = name
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self):
        super().__init__()
        self.position = input("Введите должность сотрудника ")
        self.get_full_name()
        self.get_total_income()

    def get_full_name(self):
        self.surname = input("Введите фамилию сотрудника ")
        self.name = input("Введите имя сотрудника ")

    def get_total_income(self):
        self._income["wage"] = int(input("Введите оклад сотрудника "))
        self._income["bonus"] = int(input("Введите премию сотрудника "))


men = Position()
print(vars(men))

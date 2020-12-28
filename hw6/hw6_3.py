"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self._income = {'Оклад': 0, 'Бонус': 0}

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_income(self):
        return sum(self._income.values())


class Position(Worker):
    def __init__(self, position_name, name, surname, payroll, bonus):
        self.position_name = position_name
        super().__init__(name, surname)
        self._income['Оклад'] = payroll
        self._income['Бонус'] = bonus

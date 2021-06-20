#3. Реализовать базовый класс Worker (работник).
#определить атрибуты: name, surname, position (должность), income (доход);
#последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus};
#создать класс Position (должность) на базе класса Worker;
#в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии
# (get_total_income);
#проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить
# значения атрибутов, вызвать методы экземпляров.


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit_worker": wage, "bonus_worker": bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{sum(self._income.values())}'

engineer = Position('Roman', 'Nevskiy', 'Engineer', 100000, 25000)
print(engineer.get_full_name())
print(f'Total income: {engineer.get_total_income()}')

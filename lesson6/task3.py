# Урок 6
# Задание 3

'''
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).

Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например,
{"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        return full_name

    def get_total_income(self):
        total_income = self._income.get('wage') + self._income.get('bonus')
        return total_income

u_name = input('Введите имя сотрудника: ')
u_surname = input('Введите фамилию сотрудника: ')
u_position = input('Введите должность сотрудника: ')
u_wage = int(input('Введите оклад сотрудника: '))
u_bonus = int(input('Введите бонусную премию сотрудника: '))

user = Position(u_name, u_surname, u_position, u_wage, u_bonus)

print('-------Данные о сотруднике-------')
print('Имя и Фамилия: ', user.get_full_name())
print('Занимаемая должность: ', user.position)
print('Доход сотрудника с учетом премии: ', user.get_total_income())
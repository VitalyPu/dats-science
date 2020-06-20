# Урок 4
# Задание 1
'''
Реализовать скрипт, в котором должна быть предусмотрена  функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
 Для выполнения расчета для конкретных значений необходимо  запускать скрипт с параметрами.
'''

from sys import argv

script_name, hours, rate, award = argv

def cnt_employee_salary(hours, rate, award):
    try:
        hours = float(hours)
        rate = int(rate)
        award = int(award)

        print(f'Вы ввели следующие параметры: Часов: {hours}, ставка: {rate} руб., премия: {award} руб.')
        print(f'Общая зарплата составила:  {int(hours * rate + award)} руб.')
    except ValueError:
        return print('Ошибка, попробуйте запустить скрипт заново')

cnt_employee_salary(hours, rate, award)

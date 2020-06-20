# Урок 3
# Задание 2
'''
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''

def person(name, surname, year, city, email, tel):
     return_str = name + ', ' + surname + ', '  + year + ', '  + city + ', '  + email + ', '  + tel
     return return_str

print('Итоговая информация по персоне:', person(year='1989', surname='Pudovkin', name='Vitaly', tel='8(925)22-99-249', email='vitaly@pudovkin.com', city='Moscow'))
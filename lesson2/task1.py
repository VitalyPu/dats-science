# Урок 1
# Задание 1
"""
Задание:
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
"""

my_list = [42, True, 3.14, 'Песик', None, 'Котик', 666, 6, 17234.234]
list_cnt = 0
while list_cnt < len(my_list):
    print(f'{list_cnt}-ый элемент списка "{my_list[list_cnt]}" имеет тип:', type(my_list[list_cnt]))
    list_cnt +=1
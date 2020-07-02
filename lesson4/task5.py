# Урок 4
# Задание 5
'''
Задание:
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.

Подсказка: использовать функцию reduce().
'''

from functools import reduce

def multiply_func(el1, el2):
    return el1 * el2

range_list = [el for el in range(99, 1001) if (el % 2 == 0)]
multiplied_list = reduce(multiply_func, [el for el in range(99, 1001) if (el % 2) == 0])
print('Список четных значений от 100 до 1000: ', range_list)
print('Результат перемножения всех элементов списка выше: ', multiplied_list)


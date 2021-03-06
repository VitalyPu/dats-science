# Урок 4
# Задание 4
'''
Задание:
Представлен список чисел.
Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.

Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
'''
from itertools import count

sorce_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print('Исходный список: ', sorce_list)

new_list = [ el for el in sorce_list if (sorce_list.count(el) < 2) ]
print('Получившийся список: ', new_list)

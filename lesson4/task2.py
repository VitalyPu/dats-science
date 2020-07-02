# Урок 4
# Задание 2
'''
Задание:
Представлен список чисел.
Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

Подсказка:
элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.

Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

'''
# В подсказке ошибка.
# 0ой список указан неверно: Написано -> [12, 44, 4, 10, 78, 123], должно быть [300, 12, 44, 4, 10, 78, 123]

sorce_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print('Изначальный список: ', sorce_list)

new_list = [ el for i, el in enumerate(sorce_list, 0) if (sorce_list[i-1] < sorce_list[i]) ]
print('Получившийся список: ', new_list)



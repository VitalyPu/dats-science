# Урок 1
# Задание 2
"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()
"""

# Комментарии: ***
# Для завершения ввода нужно ввести str "Exit"
# Мог сделать с "Введите длину списка", но как-то скучно.
# То ли дело бесконечный цикл.

my_list = []
print('Caution: Для завершения ввода списка нужно ввести "Exit"')
print('==========') # Визуально понятнее
while True:
    list_el = input('Введите элемент списка: ',)
    if (list_el == 'Exit'):
        break
    else:
        my_list.append(list_el)
print('Cписок получился такой: ', my_list)
print('Теперь перемешаем соседние индексы') # Визуально понятнее
cnt = 0
for list_el in range(int(len(my_list)/2)):
    # Второе решение, подсмотрел в интернете
    my_list[cnt], my_list[cnt+1] = my_list[cnt+1], my_list[cnt]
    cnt += 2

    """
    # Свое первое решение, не такое красивое
    dummy = my_list[cnt]
    my_list[cnt] = my_list[cnt + 1]
    my_list[cnt + 1] = dummy
    cnt += 2
    """
print(my_list)
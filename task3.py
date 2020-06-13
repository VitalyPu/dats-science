# Урок 1
# Задание 3
"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

cnt = 5
seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}

while cnt != 0:
    month_num = int(input('Введите номер месяца, который хотите получить (1-12): '))
    if (month_num > 12) or (month_num < 1):
        print(f'Вы ввели неправильное значение, осталось {cnt} попыток')
        cnt -= 1
    else:
        if (month_num == 1) or (month_num == 12) or (month_num == 2):
            print(f'Dict: Номера месяца {month_num} соответствует: {seasons_dict.get(1)}')
            print(f'List: Номера месяца {month_num} соответствует: {seasons_list[0]}')

        elif (month_num == 3) or (month_num == 4) or (month_num) == 5:
            print(f'Dict: Номера месяца {month_num} соответствует: {seasons_dict.get(2)}')
            print(f'List: Номера месяца {month_num} соответствует: {seasons_list[1]}')

        elif (month_num == 6) or (month_num == 7) or (month_num == 8):
            print(f'Dict: Номера месяца {month_num} соответствует: {seasons_dict.get(3)}')
            print(f'List: Номера месяца {month_num} соответствует: {seasons_list[2]}')

        elif (month_num == 9) or (month_num == 10) or (month_num == 11):
            print(f'Dict: Номера месяца {month_num} соответствует: {seasons_dict.get(4)}')
            print(f'List: Номера месяца {month_num} соответствует: {seasons_list[3]}')
        break

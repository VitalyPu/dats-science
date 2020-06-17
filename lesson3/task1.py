# Урок 3
# Задание 1

'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

def divider (a,b):
    return a/b

while True:
    try:
        Num_a = int(input('Введите число A в выражении A/B: '))
        Num_b = int(input('Введите чиало B в выражении A/B: '))
        print('Результат деления A/B: ', round(divider(Num_a, Num_b), 3))

    except ZeroDivisionError:
        print('Нельзя делить на ноль! Ата-та! Повтори-ка ввод')
    except ValueError:
        print('Ошибка, повтори еще раз, дружок.')
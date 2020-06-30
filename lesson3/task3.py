# Урок 3
# Задание 3
'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''

def my_func(arg1 , arg2, arg3):
    '''
    # Сперва решил через if-ы, но получилось большое и громостское решение, решил сделать поменьше

    if arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    elif arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    else:
        return arg2 + arg3
    '''
    min_arg = min(arg1, arg2, arg3)
    return arg1+arg2+arg3-min_arg


arg1 = int(input('Введите первый аргумент: '))
arg2 = int(input('Введите второй аргумент: '))
arg3 = int(input('Введите третий аргумент: '))

print('Сумма двух максимальных аргументов из трех равна:', my_func(arg1, arg2, arg3))
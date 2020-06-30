# Урок 3
# Задание 6

'''
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
'''

# Комментарий
# Можно вводить и не только латинские буквы, но и русские

def int_func(word):
    return word.title()

words = []
result_list = []

words = input("Напишите предложение из маленьких латинских букв через пробел: ").split()
print('Итоговое предложение с заглавными буквами:', end='')

for el in words:
    result_list.append(int_func(el))
for i in range(len(result_list)):
    print('', result_list[i], end='') # ключ end подсмотрел в интернете для Python 3.0
# Урок 5
# Задание 1
'''
Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

new_file = open('task1_file.txt', 'w+')
one_line_text = str('')

while True:
    text = str(input('Введите текст, который запишется в файл: '))
    if not text: # Подсмотрел в интернете. Если пустая строка, то мы выпадем из списка
        break
    one_line_text += text + '\n' # чтобы текст сохранялся построчно

new_file.writelines(one_line_text)

# new_file.seek(0) # Для отладки
# print('Итоговый текст: \n', new_file.read()) # Для отладки
new_file.close()
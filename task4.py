# Урок 1
# Задание 4
"""
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

my_string = input("Введите строку :", )
my_string_spaces=my_string.count(' ') + 1

my_word = my_string.split()
word_num = 1

for char in range(my_string_spaces):
    if len(str(my_word)) <= 10:
        print(f"{word_num} {my_word[char]}")
        word_num += 1
    else:
        print(f"{word_num} {my_word [char] [0:10]}")
        word_num +=1

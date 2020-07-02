# Урок 5
# Задание 4
'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

# translate_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
print_file = []

with open('task4_file1.txt', 'r') as my_file:

    for el in my_file:
        el = el.split(' ')
        # print(el) # Отладка

        if el[0] == 'One':
            print_file.append('Один' + ' - ' + el[2]) # print_file.append('Два' + str(el[1]) + str(el[2])) выводит вЂ” - вот такую ерунду в файл и в консоль, поэтому просто заменил дефисом
        elif el[0] == 'Two':
            print_file.append('Два' + ' - ' + el[2])
        elif el[0] == 'Three':
            print_file.append('Три' + ' - ' + el[2])
        elif el[0] == 'Four':
            print_file.append('Четыре' + ' - ' + el[2])
        else:
            break
    print(print_file) # Отладка

with open('task4_file2.txt', 'w') as my_file:
    my_file.writelines(print_file)
